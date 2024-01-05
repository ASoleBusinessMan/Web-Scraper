from flask import Flask, render_template, request, send_from_directory
from scraper import scrape_website, save_as_pdf

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        text = scrape_website(url)
        if text:
            filename = f"{url.replace('https://', '').replace('http://', '')}.pdf"
            save_as_pdf(text, filename)
            return render_template('index.html', download_link=filename)
        else:
            return render_template('index.html', download_link=None)
    return render_template('index.html', download_link=None)


@app.route('/static/<filename>')
def download_file(filename):
    return send_from_directory('static', filename)


if __name__ == '__main__':
    app.run(debug=True)

