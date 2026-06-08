# Interactive To-Do List App

A beautiful, interactive to-do list web application built with Python Flask and SQLite. Organize your tasks by date categories (Today, Tomorrow, Upcoming) with a clean, modern interface.

## Features

✨ **Clean, Modern UI** - Beautiful gradient design with smooth animations
📅 **Smart Task Organization** - Automatically categorizes tasks as Today, Tomorrow, or Upcoming
✅ **Task Management** - Add, complete, edit, and delete tasks
📝 **Descriptions** - Add detailed descriptions to your tasks
🎯 **Due Dates** - Set due dates for tasks
💾 **Persistent Storage** - All tasks are saved to SQLite database
📱 **Responsive Design** - Works on desktop and mobile devices

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd /workspaces/TO-DO-LIST
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. **Start the Flask server:**
   ```bash
   python main.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Start creating tasks!** 🚀

## How to Use

### Adding a Task
1. Enter the task title in the input field
2. (Optional) Select a due date
3. (Optional) Add a description in the text area
4. Click the **+** button or press Enter

### Completing a Task
- Click the checkbox next to any task to mark it as complete
- Completed tasks move to the "Completed" section

### Deleting a Task
- Click the **🗑️** icon on any task to delete it
- You'll be prompted to confirm the deletion

### Editing a Task
- Click the **✏️** icon to edit task details

## File Structure

```
TO-DO-LIST/
├── main.py                 # Flask application and API routes
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/
│   └── index.html         # Main HTML template
└── static/
    └── style.css          # Styling and animations
```

## Database Schema

The app uses SQLite with a simple tasks table:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT DEFAULT 'today',
    completed INTEGER DEFAULT 0,
    due_date TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## API Endpoints

- **GET /api/tasks** - Retrieve all tasks grouped by category
- **POST /api/tasks** - Create a new task
- **PUT /api/tasks/<id>** - Update an existing task
- **DELETE /api/tasks/<id>** - Delete a task

## Customization

### Change the Port
Edit `main.py` and modify the port number:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Change 5000 to desired port
```

### Modify the Theme
Edit `static/style.css` to change colors:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, change the port in `main.py` or kill the process using that port.

### Database Issues
If you encounter database errors, delete the `tasks.db` file and restart the app to recreate the database.

### Flask Not Found
Make sure you've installed the requirements:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- 🔐 User authentication and accounts
- 🏷️ Task tags and categories
- 📊 Task statistics and productivity charts
- 🔔 Task notifications and reminders
- 🌙 Dark mode theme
- 📤 Export/Import tasks
- 🔄 Task recurrence

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.

---

Happy task management! 🎉