# -*- coding: utf-8 -*-

from flask import Flask
from Module.OAuth.InstagramOAuth import *

app = Flask(__name__)

print app


@app.route('/')
def index():
    return 'Welcome to iflyshadow.com.'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/instagram/microfollow/oauth/', methods=['GET'])
def oauth():
    oauth_flow = InstagramOAuth()
    return oauth_flow.exchange_for_access_token()


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.run(debug=True)