# mentibot
mentibot.py is a menti.com bot / vote spammer / auto voter written in python
### how to use
download it
~~~~
curl https://raw.githubusercontent.com/yoted/mentibot/master/mentibot.py -so mentibot.py
~~~~
run it
~~~~
python mentibot.py
~~~~
and follow the on-screen instructions

around 25 threads should be sufficient for maximum votes per second (depending on your machine and connection)
### help i get an error
if you get the following error:
~~~~
Traceback (most recent call last):
  File "/Users/yoted/Desktop/mentibot.py", line 3, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
~~~~
install the requests module with pip
~~~~
pip install requests
~~~~