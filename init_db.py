import sqlite3

def init_test_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ids (
            unique_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            branch TEXT NOT NULL,
            batch TEXT NOT NULL,
            college TEXT NOT NULL,
            image_path TEXT NOT NULL
        )
    ''')

    # Insert sample data
    test_data = [
        ('0126CD221111', 'Sandeep Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/sandi.jpg'),
        ('0126CD221124', 'Shubham Singh', 'B.Tech', 'CSE-DS', '2022-2024',' OCT', '/static/images/shubham.png'),
        ('0126CD221100', 'Rahul Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/rahul.png'),
        ('0126CD221083', 'Nishant Kushwah', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/nishant.png'),
        ('0126CD221095', 'Prince Kumar', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/prince.png'),
        ('0126CD221096', 'Prince Thakre', 'B.Tech', 'CSE-DS', '2022-2024','OCT', '/static/images/princt.png')
  
    ]

    cursor.executemany(
        'INSERT OR IGNORE INTO ids (unique_id, name, course, branch, batch, college, image_path) VALUES (?, ?, ?, ?, ?, ?, ?)',
        test_data
    )

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_test_db()
