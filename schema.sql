CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
);

