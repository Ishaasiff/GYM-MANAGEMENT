from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def pageFirst():
    return render_template('website.html')

@app.route('/membership.html')
def membership():
    return render_template('membership.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
app=Flask(__name__)




