# C-R-U-D

get_time = """
SELECT created_at FROM tasks WHERE id = ?
"""

tasks_table = """
CREATE TABLE  IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    complated INTEGER DEFAULT 0
    )
"""
#tasks = таблици   #task = поле         
read_tasks = """       
SELECT id, task, created_at, complated FROM tasks     
"""


update_task = """
UPDATE tasks SET task = ? WHERE id = ?
"""

delete_task = """
DELETE FROM tasks WHERE id = ?
"""

insert_task = """
INSERT INTO tasks (task) VALUES (?)
"""

read_tasks_by_complated = """       
SELECT id, task, complated FROM tasks WHERE complated = ?
"""