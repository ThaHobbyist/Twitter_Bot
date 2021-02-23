import tweepy
import time
import json
from threading import *

with open('twitter_credentials.txt') as f:
    data = f.read()

js = json.loads(data)
print('this my bot')

CONSUMER_KEY = js["CONSUMER_KEY"]
CONSUMER_SECRET = js["CONSUMER_SECRET"]
ACCESS_KEY = js["ACCESS_KEY"]
ACCESS_SECRET = js["ACCESS_SECRET"]

FILE_NAME = 'last_seen_id.txt'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return 

ongoing = 123


class search(Thread):
    def run(self):
        print("started 1")
        global ongoing
        while True:
            FILE_NAME = 'last_seen_id.txt'

            f_read = open(FILE_NAME, 'r')
            last_seen_id = int(f_read.read().strip())
            f_read.close()
            
            for tweet in reversed(api.search( q='#hobbist', since_id = last_seen_id, result_type = 'recent',  timeout = 999999)):
                if ongoing != tweet.id:
                    try:
                        if tweet.user.screen_name != 'DiptangshuDey':
                            ongoing = tweet.id                       
                            f_write = open(FILE_NAME, 'w')
                            f_write.write(str(tweet.id))
                            f_write.close()

                            api.update_status('@' + tweet.user.screen_name + ' I support #hobbist from 1', tweet.id)

                            print(tweet.text)
                            print(tweet.id)

                            time.sleep(15)

                    except tweepy.RateLimitError as e:
                        print("Twitter api rate is reached: {}".format(e))
                        time.sleep(60)
                        continue
                    except tweepy.TweepError as e:
                        print("Tweepy error reached: {}".format(e))
                        break
                    except StopIteration:
                        print('bruh')
                        break
                    except Exception as e:
                        print("Failed while fetching replies: {}".format(e))
                        break
                else:
                    continue

class search2(Thread):
    def run(self):
        print("started 2")
        global ongoing
        while True:
            FILE_NAME = 'last_seen_id.txt'

            f_read = open(FILE_NAME, 'r')
            last_seen_id = int(f_read.read().strip())
            f_read.close()

            for tweet in reversed(api.search( q='#hobbist', since_id = last_seen_id, result_type = 'recent',  timeout = 999999)):
                if ongoing != tweet.id:
                    try:
                        if tweet.user.screen_name != 'DiptangshuDey':
                            ongoing = tweet.id
                            
                            f_write = open(FILE_NAME, 'w')
                            f_write.write(str(tweet.id))
                            f_write.close()

                            api.update_status('@' + tweet.user.screen_name + ' I support #hobbist from 2', tweet.id)

                            print(tweet.text)
                            print(tweet.id)

                            time.sleep(15)

                    except tweepy.RateLimitError as e:
                        print("Twitter api rate is reached: {}".format(e))
                        time.sleep(60 * 15)
                        continue
                    except tweepy.TweepError as e:
                        print("Tweepy error reached: {}".format(e))
                        time.sleep(60 * 15)
                        break
                    except StopIteration:
                        print('bruh')
                        break
                    except Exception as e:
                        print("Failed while fetching replies: {}".format(e))
                        break
                else:
                    continue


t1 = search()
t2 = search2()

t1.start()
time.sleep(5)
t2.start()