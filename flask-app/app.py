from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/qr_scanner')
def qr_scanner():
    return render_template('qr_scanner.html')

@app.route('/barcode_scanner')
def barcode_scanner():
    return render_template('barcode_scanner.html')

@app.route('/display_data', methods=['POST'])
def display_data():
    qr_data = request.form.get('qr_data')
    # Process the QR/Barcode data here
    return f'Detected data: {qr_data}'

if __name__ == '__main__':
    app.run(debug=True)
