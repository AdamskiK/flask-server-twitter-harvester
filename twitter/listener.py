import os
import tweepy

from utils import Request
from result import Result


class StreamListener(tweepy.StreamListener):
    def __init__(self, keywords, logging):
        super(StreamListener, self).__init__()
        self.keywords = keywords
        self.logging = logging

    @staticmethod
    def authorize(consumer_key, consumer_secret, access_key, access_secret):
        authorize = tweepy.OAuthHandler(consumer_key, consumer_secret)
        authorize.set_access_token(access_key, access_secret)
        return authorize

    def on_status(self, status):

        try:
            tweet_object = status
            if 'extended_tweet' in tweet_object._json:
                tweet = tweet_object.extended_tweet['full_text']
            else:
                tweet = tweet_object.text

            result = Result(tweet_id=status.id,
                            tweet=tweet,
                            tweet_url="https://twitter.com/statuses/" + str(status.id),
                            user=status.author.screen_name,
                            source=status.source,
                            created_at=status.created_at
                            )

            obj = result.convert_dict_to_json_string()
            request = Request(url=os.environ['POST_API_URL'])
            request.post(data=obj)

        except Exception as e:
            self.logging.info(f"Exception: {e}")
            pass
