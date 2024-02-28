from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Establishing a connection to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="username",    
  password="password",  
  database="your_database"  
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_data', methods=['POST'])
def save_data():
    if request.method == 'POST':
        # Get form data
        patient_name = request.form['patient-name']
        drug_name = request.form['drug-name']
        # Add more fields as needed

        # Create cursor
        mycursor = mydb.cursor()

        # Insert data into MySQL database
        sql = "INSERT INTO your_table_name (patient_name, drug_name) VALUES (%s, %s)"
        val = (patient_name, drug_name)
        mycursor.execute(sql, val)

        # Commit to database
        mydb.commit()

        # Close cursor and database connection
        mycursor.close()

        return "Data saved successfully"

if __name__ == '__main__':
    app.run(debug=True)
