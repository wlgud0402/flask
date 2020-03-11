from flask import Flask, url_for
app = Flask(__name__)

@app.route("/hello/")
def hello():
    return "Hello Flask!!"

@app.route('/profile/', methods=['POST,' 'GET'])
def profile(username=None):
    error = None
    if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            if not username and not email:
                    return add_profile(request.form)
    else:
            error = 'Invalid username or email'
    return render_template('profile.html', error=error)

if __name__ == "__main__":
    with app.test_request_context():
        print(url_for("hello"))
        print(url_for("profile", username="flask"))
    app.run()