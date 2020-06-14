import os
import ssl
import time
import tweepy

from listener import StreamListener
from requests.exceptions import Timeout, ConnectionError
from urllib3.exceptions import ReadTimeoutError


class Harvester:
    """A wrapper class for the StreamListener class."""
    def __init__(self, logging):
        self.logging = logging
    
    def harvest(self, keywords):
        while True:
            try:
                self._listen(keywords)
            except (tweepy.RateLimitError, Timeout, ssl.SSLError, ReadTimeoutError, ConnectionError, tweepy.TweepError) as e:
                self.logging.info(f"Error {e} waiting ~1 min to continue")
                time.sleep(int(os.environ["ERROR_WAIT_TIME"]))

    def _listen(self, keywords):
        listener = StreamListener(keywords, logging=self.logging)
        auth = listener.authorize(os.environ["CONSUMER_KEY"],
                                  os.environ["CONSUMER_SECRET"],
                                  os.environ["ACCESS_KEY"],
                                  os.environ["ACCESS_SECRET"])
        streamingAPI = tweepy.streaming.Stream(auth, listener)
        streamingAPI.filter(track=keywords)
