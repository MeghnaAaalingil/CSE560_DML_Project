from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        query = request.form['query']
        # Connect to your database and execute the query
        # For example, using SQLite:
        conn = sqlite3.connect('financial_data_analysis.db')
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)  # Now printing the fetched results
        conn.close()
        return results
    except Exception as e:
        error_message = str(e)
        return error_message

    # Check if results are empty
    if not results:
        print("No results found.")

    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
