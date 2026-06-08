from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import sqlite3
import json
import os

app = Flask(__name__)
app.config['DATABASE'] = 'tasks.db'

def init_db():
    """Initialize the database."""
    if not os.path.exists(app.config['DATABASE']):
        conn = sqlite3.connect(app.config['DATABASE'])
        c = conn.cursor()
        c.execute('''
            CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                category TEXT DEFAULT 'today',
                completed INTEGER DEFAULT 0,
                due_date TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

def get_db_connection():
    """Get a database connection."""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks grouped by category."""
    conn = get_db_connection()
    c = conn.cursor()
    
    # Get today's date
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    
    tasks = {
        'today': [],
        'tomorrow': [],
        'upcoming': [],
        'completed': []
    }
    
    c.execute('SELECT * FROM tasks WHERE completed = 0 ORDER BY due_date ASC')
    for row in c.fetchall():
        task = dict(row)
        task['created_at'] = task['created_at'][:10]
        
        if task['due_date']:
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d').date()
            if due_date == today:
                tasks['today'].append(task)
            elif due_date == tomorrow:
                tasks['tomorrow'].append(task)
            else:
                tasks['upcoming'].append(task)
        else:
            tasks['today'].append(task)
    
    # Get completed tasks
    c.execute('SELECT * FROM tasks WHERE completed = 1 ORDER BY due_date DESC LIMIT 10')
    for row in c.fetchall():
        task = dict(row)
        task['created_at'] = task['created_at'][:10]
        tasks['completed'].append(task)
    
    conn.close()
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """Add a new task."""
    data = request.json
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO tasks (title, description, due_date, category)
        VALUES (?, ?, ?, ?)
    ''', (data['title'], data.get('description', ''), data.get('due_date'), 'today'))
    
    conn.commit()
    task_id = c.lastrowid
    conn.close()
    
    return jsonify({'id': task_id, 'success': True}), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task."""
    data = request.json
    conn = get_db_connection()
    c = conn.cursor()
    
    if 'completed' in data:
        c.execute('UPDATE tasks SET completed = ? WHERE id = ?', (data['completed'], task_id))
    if 'title' in data:
        c.execute('UPDATE tasks SET title = ? WHERE id = ?', (data['title'], task_id))
    if 'description' in data:
        c.execute('UPDATE tasks SET description = ? WHERE id = ?', (data['description'], task_id))
    if 'due_date' in data:
        c.execute('UPDATE tasks SET due_date = ? WHERE id = ?', (data['due_date'], task_id))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)

