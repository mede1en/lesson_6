import flet as ft
from db import main_db



def main(page: ft.Page):
    tasks_collumn = ft.Column() 


    def add_new_task(e):
        def add_to_db(name):
            id = main_db.add_new_task(name)
            print(f"добавлена новая задача: {name} ID: {id}")
            return id
                  

        def to_edit(e):
            if task_text.read_only:
                task_text.read_only = False
            else:
                task_text.read_only = True 

        if user_input.value:
            
            task_text = ft.TextField(value=user_input.value, expand=True, read_only=True)
            edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=to_edit)
            task_id = add_to_db(task_text.value)
            time = ft.TextField(value=main_db.get_time(task_id), expand=True, read_only=True)
            user_input.value = None 
            delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e, id=task_id: delete_task(id))
            task_row = ft.Row([task_text, time, delete_button, edit_button])
            tasks_collumn.controls.append(task_row)

    def add_to_db(name):
        id = main_db.add_new_task(name)
        print(f"Добавлена новая задача: {name} ID: {id}")
        return id

    def edit_db(id, new_value):
        main_db.edit_task(id, new_value)
        print("Задача успешно обновлена!")

    def delete_from_db(id):
        main_db.delate_task(id)

    def add_task(task_id, task):

        def edit(e):
            edit_db(task_id, task)
            task.read_only = True

        def delete(e):
            delete_from_db(task_id)
            load_from_db()
            page.update()

        def to_edit(e):
            if task.read_only:
                task.read_only = False
            else:
                task.read_only = True
        
        task_text = ft.TextField(
            value=task, expand=True, read_only=True, on_submit=edit
        )
        completed_text = ft.TextField(value=main_db.get_time(task_id), expand=True, read_only=True)
        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=to_edit)
        submit_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=edit)
        delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete)
        # task_id = add_to_db(user_input.value)
        task_row = ft.Row([task_text, completed_text, edit_button, submit_button, delete_button])

        return task_row

    def load_from_db():
        tasks_collumn.controls.clear()

        results = main_db.get_all_tasks()
        if results:
            for id, task, created_at, complated in results:
                result = add_task(id, task)
                tasks_collumn.controls.append(result)

    def clear_completed(e):
        main_db.clear_completed()
        load_from_db()
        page.update()

    def delete_task(id):
        main_db.delate_task(id)
        load_from_db()
        page.update()
        
    def filter_by(filter):
        tasks_collumn.controls.clear()

        results = main_db.get_tasks_by_filter(filter)
        if results:
            for id, task, created_at, complated in results:
                result = add_task(id, task)
                tasks_collumn.controls.append(result)

    user_input = ft.TextField(label="новыя задача", expand=True, on_submit=add_new_task)
    enter_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_new_task)
    clear_button = ft.IconButton(icon=ft.Icons.CLEAR, on_click=clear_completed)

    filter_buttons= ft.Row(
        [
        ft.ElevatedButton(content="Все", on_click=lambda e: load_from_db()),
        ft.ElevatedButton(content="незаконченные", on_click=lambda e: filter_by(0)),
        ft.ElevatedButton(content="В работе", on_click=lambda e: filter_by(1)),
        ],
    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
   
    main_row = ft.Row([user_input, enter_button, clear_button])
    
    page.add(main_row, filter_buttons, tasks_collumn)
    load_from_db()
    
if __name__ == "__main__":
    main_db.create_tables()
    ft.run(main)
