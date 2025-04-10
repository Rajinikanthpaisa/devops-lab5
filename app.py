from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        event = request.form['event']
        return f"Thanks {name}, you have registered for the {event}!"
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

