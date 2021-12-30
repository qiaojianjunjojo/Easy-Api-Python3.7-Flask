from flask import Flask,render_template
from markupsafe import escape

app = Flask(__name__)

#多路由匹配 使用装饰器
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


def doWork():
    return "OK,do the work!"

app.add_url_rule('/123', 'doWork', doWork)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


if __name__ == '__main__':
    app.run()
