# -*- coding: utf-8 -*-

from getfollow.Module.OAuth.InstagramOAuth import *
from getfollow.Module.Utils.Util import *

app = Flask(__name__)

print app


@app.route('/')
def index():
    return Util.create_response(data='Welcome to iflyshadow.com.')


@app.errorhandler(404)
def not_found(error):
    return Util.create_response(code=404, error=request.url+',Page not found.')


@app.route('/instagram/microfollow/oauth', methods=['POST'])
def oauth():
    return InstagramOAuth.exchange_for_access_token()


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.run(debug=True)

