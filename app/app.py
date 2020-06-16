import logging.config
import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('app')

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # stop from complaining in the console

db = SQLAlchemy(app)

ma = Marshmallow(app)


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.Integer, unique=True)
    tweet = db.Column(db.String(1000))
    tweet_url = db.Column(db.String(100))
    user = db.Column(db.String(100))
    source = db.Column(db.String(100))
    created_at = db.Column(db.String(50))

    def __init__(self, tweet_id, tweet_url, tweet, user, source, created_at):
        self.tweet_id = tweet_id
        self.tweet = tweet
        self.tweet_url = tweet_url
        self.user = user
        self.source = source
        self.created_at = created_at


class TweetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tweet_id', 'tweet', 'tweet_url', 'user', 'source', 'created_at')


tweet_schema = TweetSchema(strict=True)  # strict=True - suppress validation errors
tweets_schema = TweetSchema(many=True, strict=True)


# add single tweet to db
@app.route('/tweet', methods=['POST'])
def add_tweet():
    tweet_id = request.json['tweet_id']
    tweet = request.json['tweet']
    tweet_url = request.json['tweet_url']
    user = request.json['user']
    source = request.json['source']
    created_at = request.json['created_at']
    logger.info(f'Added new tweet id: {tweet_id}')
    new_tweet = Tweet(tweet_id, tweet, tweet_url, user, source, created_at)
    db.session.add(new_tweet)
    db.session.commit()
    return tweet_schema.jsonify(new_tweet)


# get all tweets
@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    all_tweets = Tweet.query.all()
    result = tweets_schema.dump(all_tweets)
    return jsonify(result.data)


if __name__ == '__main__':
    logger.info('Started')
    app.run(debug=True)
    logger.info('Finished')
