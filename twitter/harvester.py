import logging.config
import os
import ssl
import time
import tweepy

from listener import StreamListener
from requests.exceptions import Timeout, ConnectionError
from urllib3.exceptions import ReadTimeoutError

logger = logging.getLogger(__name__)


class Harvester:
    """A wrapper class for the StreamListener class."""

    def __init__(self):
        pass

    def harvest(self, keywords):
        while True:
            try:
                self._listen(keywords)
            except (tweepy.RateLimitError, Timeout, ssl.SSLError, ReadTimeoutError, ConnectionError, tweepy.TweepError) as e:
                logger.error(f"Error {e} waiting ~1 min to continue")
                time.sleep(int(os.environ["ERROR_WAIT_TIME"]))

    @staticmethod
    def _listen(keywords):
        listener = StreamListener(keywords)
        auth = listener.authorize(os.environ["CONSUMER_KEY"],
                                  os.environ["CONSUMER_SECRET"],
                                  os.environ["ACCESS_KEY"],
                                  os.environ["ACCESS_SECRET"])
        streamingAPI = tweepy.streaming.Stream(auth, listener)
        streamingAPI.filter(track=keywords)
