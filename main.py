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
            task_row = ft.Row([task_text, time, edit_button])
            tasks_collumn.controls.append(task_row) 

    user_input = ft.TextField(label="новыя задача", expand=True, on_submit=add_new_task)
    enter_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_new_task)
    
   
    main_row = ft.Row([user_input, enter_button])

    page.add(main_row, tasks_collumn)
    
if __name__ == "__main__":
    main_db.create_tables()
    ft.run(main)
