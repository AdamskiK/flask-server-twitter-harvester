import datetime
import json
import logging

logger = logging.getLogger(__name__)


class Result:
    """A simple class for creating an
    insert object in the database."""

    def __init__(self, tweet_id, tweet, tweet_url, user, source, created_at):
        logger.info('Preparing object for: {}'.format(tweet_id))
        self.result = {
            'tweet_id': tweet_id,
            'tweet': tweet,
            'tweet_url': tweet_url,
            'user': user,
            'source': source,
            'created_at': created_at
        }

    def convert_dict_to_json_string(self):
        return json.dumps(self.result, default=self._convert_datetime)

    @staticmethod
    def _convert_datetime(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()
