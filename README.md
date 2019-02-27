# WSExample

Provide an example of use of websocket with Django framework with a bot client.


## Dependencies*
    
Python

    brew install python3


Python libraries: 
* Django
* channels 
* websocket-client
* channels_redis


    pip3 install django
    pip3 install channels
    pip3 install websocket-client
    pip3 install channels_redis
    
Redis    
    
    brew install redis 
    
## Configure

Ensure that redis service is running:

* To have launchd start redis now and restart at login:
  
    
    brew services start redis


* Or, if you don't want/need a background service you can just run:

    
    redis-server /usr/local/etc/redis.conf
    
Operate migrations for Django 

    python3 manage.py makemigrations
    python3 manage.py migrate

## Run


Run server

    python3 manage.py runserver
    
    
Run client

    python3 bot.py
    

(*) All instructions are given for MacOs