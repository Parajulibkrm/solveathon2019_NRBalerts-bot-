import requests
import tweepy
import json
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("Consumer_api",
                           "consumer_api_token")
auth.set_access_token("Access_token",
                      "Access_token_token")

# Create API object
api = tweepy.API(auth)

while True:
    apiUrl = "Apiurl/user/"
    response = requests.get(apiUrl)
    apidatafinal = str((response.text))

    f = open("demofile.txt", "r", encoding="utf-8")
    data = f.read()
    f.close()

    if apidatafinal == data:
        print("duplicate data")
    else:
        f = open("demofile.txt", "w", encoding="utf-8")
        f.write(apidatafinal)
        apidatafinal1 = apidatafinal.split(" XX ")[0]
        apidatafinal2 = apidatafinal.split(" XX ")[1]
        apidatafinal2 = apidatafinal2.replace(" ", "")
        apidatafinal = apidatafinal1 + "\n" + apidatafinal2
        f.close()
        api.update_status(apidatafinal)
        print(apidatafinal)

    time.sleep(60)
    print("Slept and woke again")
