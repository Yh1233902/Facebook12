from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/link', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        account_link = request.form['account_link']
        last3 = account_link.strip('/')[-3:]
        base_link = account_link[:-3]
        return render_template('info.html', link=base_link, last3=last3)
    return render_template('link.html')

if __name__ == '__main__':
    app.run(debug=True)
