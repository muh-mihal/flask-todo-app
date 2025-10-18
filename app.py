import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for

# Create the Flask app instance
app = Flask(__name__)

# Define the path for the database in the instance folder
DATABASE = os.path.join(app.instance_path, 'tasks.db')

def get_db_connection():
    """Creates a connection to the SQLite database."""
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass  # Already exists
    
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database and creates the 'tasks' table if it doesn't exist."""
    conn = get_db_connection()
    with app.open_resource('schema.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

# --- One-Time Database Initialization ---
# This function will run before the first request to the app
@app.before_request
def before_request():
    if not os.path.exists(DATABASE):
        init_db()

# --- Routes ---

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles viewing the main page and adding new tasks to the database."""
    conn = get_db_connection()
    if request.method == 'POST':
        task_content = request.form['content']
        conn.execute('INSERT INTO tasks (content, completed) VALUES (?, ?)',
                     (task_content, False))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    tasks_from_db = conn.execute('SELECT * FROM tasks ORDER BY id').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks_from_db)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    """Deletes a task from the database."""
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle(task_id):
    """Toggles the completion status of a task."""
    conn = get_db_connection()
    task = conn.execute('SELECT completed FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if task:
        new_status = not task['completed']
        conn.execute('UPDATE tasks SET completed = ? WHERE id = ?',
                     (new_status, task_id))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    """Handles editing a task."""
    conn = get_db_connection()
    if request.method == 'POST':
        new_content = request.form['content']
        conn.execute('UPDATE tasks SET content = ? WHERE id = ?',
                     (new_content, task_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    task_to_edit = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    return render_template('edit.html', task=task_to_edit)


# --- Main Execution (for local development) ---
if __name__ == '__main__':
    app.run(debug=True)
