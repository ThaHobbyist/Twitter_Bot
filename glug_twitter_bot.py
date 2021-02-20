import tweepy
import time

CONSUMER_KEY = 'fOiZ2Q4TjDyOCy4OIeIIkScSN'
CONSUMER_SECRET = 'RXPG2Tls7NsbSUHCa5vNeCnFSVubJhZrRMeu3HQGydkgcRppjE'
ACCESS_KEY = '1334045938877272064-LqLSrlIOOsobFBEFamBddPzAaEP0Gk'
ACCESS_SECRET = 'VrfpxqdEglSQX4P8soCTjnV62ZN9fKpnKJmD7r2BRqJcE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'history.txt'
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

def reply_to_comment():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mention = api.mentions_timeline( tweet_mode = 'extended')

    for m in reversed(mention):
        tweet_id = m.id
        last_seen_id = retrieve_last_seen_id(FILE_NAME)
        
        print(m.full_text)
        for tweet in tweepy.Cursor(api.search, q='to:' + m.user.screen_name,since_id = last_seen_id, reselt_type = 'recent', timeout=999999).items(1000):
            try:
                if not hasattr(tweet, 'in_reply_to_status_id_str'):
                    continue
                if (tweet.in_reply_to_status_id_str == str(tweet_id)) and ('bot' in tweet.text.lower()) :
                    last_seen_id = tweet.id
                    store_last_seen_id(last_seen_id, FILE_NAME)
                    print(tweet.text)
                    print(tweet.id)
                    api.update_status('@' + tweet.user.screen_name + ' Yes I am a bot...', tweet.id)
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

while True:
    reply_to_comment()
    time.sleep(60)
