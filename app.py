from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

def fetch_student_by_id(unique_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ids WHERE unique_id = ?', (unique_id,))
    student = cursor.fetchone()
    conn.close()
    return student

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_id', methods=['POST'])
def check_id():
    unique_id = request.form.get('unique_id')
    student = fetch_student_by_id(unique_id)

    if student:
        return jsonify({
            "status": "exists",
            "unique_id": student[0],
            "name": student[1],
            "course": student[2],
            "branch": student[3],
            "batch": student[4],
            "college": student[5],
            "image_path": student[6]
        })
    else:
        return jsonify({"status": "not_found", "message": "ID not found."})

if __name__ == '__main__':
    app.run(debug=True)
