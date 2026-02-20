import config
import sqlite3
from db import queries

def create_tables():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.tasks_table)

    conn.commit()
    conn.close()

def add_new_task(name):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.insert_task, (name,))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    return id

def get_time(id):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    time = cursor.execute(queries.get_time, (id,)).fetchone()[0]

    conn.close()
    return time

def clear_completed():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE complated = 1")
    conn.commit()
    conn.close()

def delate_task(id):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.delete_task, (id,))

    conn.commit()
    conn.close()
def get_all_tasks():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    tasks = cursor.execute(queries.read_tasks).fetchall()

    conn.close()
    return tasks


def get_tasks_by_filter(filter): 
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.read_tasks_by_complated, (filter,))
    results = cursor.fetchall()
    conn.close()

    return results 