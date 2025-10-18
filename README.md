# Flask To-Do List Web Application

A responsive and beautifully designed To-Do List web application built with Python and Flask. This project allows users to create, edit, delete, and mark tasks as complete, with all data saved permanently in an SQLite database.

## Features

*   **Create Tasks**: Easily add new tasks through a simple input form.
*   **Edit Tasks**: Click on the edit icon that appears on hover to modify existing tasks.
*   **Complete Tasks**: Mark tasks as complete using a satisfying checkbox. Completed tasks are visually distinguished.
*   **Delete Tasks**: Remove tasks you no longer need.
*   **Persistent Storage**: Tasks are saved in an SQLite database, so they are not lost when the server restarts.
*   **Responsive Design**: A clean, modern UI that works beautifully on both desktop and mobile browsers, built with custom CSS.

## Technologies Used

*   **Backend**: Python, Flask
*   **Database**: SQLite
*   **Frontend**: HTML, CSS

## Local Setup and Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```
    git clone https://github.com/muh-mihal/flask-todo-app.git
    cd flask-todo-app
    ```

2.  **Create and activate a virtual environment:**
    ```
    # For Windows
    python -m venv venv
    venv\\Scripts\\activate
    ```

3.  **Install the required dependencies:**
    ```
    pip install Flask
    ```

4.  **Run the application:**
    ```
    python app.py
    ```

5.  Open your web browser and navigate to `http://127.0.0.1:5000` to see the application in action.
