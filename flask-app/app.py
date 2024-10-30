#import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Set up database connection placeholders
'''
db_config = {
#    'host': 'db.pihl-zimling.dk',
    'host': '64.90.32.30',
    'user': 'scanner_dbuser',
    'password': '7LaqXLfUyGiyfR2O60VH',
    'database': 'nfe_scanner'
}

def check_code_in_db(code):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Query to check if the scanned value exists in the database
#    query = "SELECT * FROM wristbands WHERE wristband_data = '%s'"
#    cursor.execute(query, (code,))
#    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result
'''

app.config['MYSQL_HOST'] = 'db.pihl-zimling.dk'
app.config['MYSQL_USER'] = 'scanner_dbuser'
app.config['MYSQL_PASSWORD'] = '7LaqXLfUyGiyfR2O60VH'
app.config['MYSQL_DB'] = 'nfe_scanner'

mysql = MySQL(app)

def check_code_in_db(code):
#    details = request.form
#    firstName = details['fname']
#    lastName = details['lname']
    cur = mysql.connection.cursor()
#    cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
#    mysql.connection.commit()
    cur.close()
    return 'success'
#    return

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/qr_scanner')
def qr_scanner():
    return render_template('qr_scanner.html')

@app.route('/barcode_scanner')
def barcode_scanner():
    return render_template('barcode_scanner.html')

@app.route('/scanner')
def scanner():
    return render_template('scanner.html')

@app.route('/display_data', methods=['POST'])
def display_data():
    qr_data = request.form.get('qr_data')
    # Process the QR/Barcode data here
    return f'Detected data: {qr_data}'

#@app.route('/issue_wristband', methods=['POST'])
@app.route('/issue_wristband', methods=['POST', 'GET'])
def issue_wristband():
    """
    qr_data = request.form.get('qr_data')
    # Process the QR/Barcode data here
    return f'Detected data: {qr_data}'
    """

    scanned_code = request.form.get('qr_data')

    # Check if the scanned code exists in the database
    data = check_code_in_db(scanned_code)
    return f'Result: {data}'
'''
    if data:
        # If the code is found, pass additional data to the template
        return render_template('issue_wristband.html', found=True, data=data)
    else:
        # If the code is not found, return a message indicating that
        return render_template('issue_wristband.html', found=False, code=scanned_code)
'''

if __name__ == '__main__':
    app.run(debug=True)
