from multiprocessing import Process
import json
import requests
import sys
import time

def spin():
    while 1:
        for cursor in '|/-\\':
            sys.stdout.write(cursor)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')

def thread(question_id, choice):
  while 1:
    identifier = requests.post('https://www.menti.com/core/identifier').json()['identifier']
    headers = {'x-identifier': identifier}
    data = {"question": question_id, "question_type": "choices", "vote": choice}
    vote = requests.post('https://www.menti.com/core/vote', json = data, headers = headers)

if __name__ == '__main__':
  code = str(input("enter menti code: "))
  menti_data = requests.get('https://www.menti.com/core/objects/vote_ids/'+code)
  question_id = menti_data.json()['pace']['active']

  print("\nlive results: https://www.mentimeter.com/s/" + menti_data.json()['series_id'] + "/" + menti_data.json()['questions'][0]['admin_key'] + "\n")

  print(menti_data.json()['questions'][0]['question'])
  question_choices = menti_data.json()['questions'][0]['choices']
  for i in range(len(question_choices)):
    print("id: " + str(question_choices[i]['id']) + " -> " + question_choices[i]['label'])

  choice = str(input("\nenter choice id: "))
  threads = int(input("enter number of threads: "))

  Process(target=spin).start()
  for x in range(threads):
      Process(target=thread,args=(question_id, choice)).start()