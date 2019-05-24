#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request,redirect,abort,render_template
from flask import make_response,url_for

app = Flask(__name__)
# @app.route('/')
# def index():
#     user_agent = request.headers.get("user-Agent")
#     return '<p>your broswer is %s</p>'%user_agent
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>hello %s!</h1>'%name
# # @app.route('/')
# # def index():
# #     return '<h1>Bad Request</h1>',400
# # @app.route('/')
# # def index():
# #     response = make_response('<h1>This is document a cookie</h1>')
# #     response.set_cookie('answer','4422')
# #     return response
# #
# # @app.route('/')
# # def index():
# #     return redirect("http://www.baidu.com")
# # @app.route('/')
# # def index():
# #     return redirect('http://www.baidu.com')

# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not  user:
#         abort(404)
#     return '<h1>hello %s</h1>'%id

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login')
def login():pass

@app.route('/user/<uaername>')
def profile(uaername):pass

if __name__ == '__main__':
    app.run(debug=True)























