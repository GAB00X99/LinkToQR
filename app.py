from flask import Flask, render_template, request
import qrcode
import validators

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']

    if not validators.url(url):
        return render_template('error.html', message='URL inválida')

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('static/qr_code.png')
    return render_template('result.html')

if __name__ == '__main__':
    app.run()
