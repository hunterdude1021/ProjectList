#mostly here for me to learn how to use customtkinter
import json
import os
import customtkinter

SAVE_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Todo List")
        self.geometry("400x600")

        self.tasks = self.load_tasks()

        self.task_entry = customtkinter.CTkEntry(self, placeholder_text="Enter a task")
        self.task_entry.pack(pady=10)

        self.add_button = customtkinter.CTkButton(self, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        self.delete_entry = customtkinter.CTkEntry(self, placeholder_text="Enter task number")
        self.delete_entry.pack(pady=10)

        self.delete_button = customtkinter.CTkButton(self, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=10)

        self.task_textbox = customtkinter.CTkTextbox(self)
        self.task_textbox.pack(pady=10, fill="both", expand=True)

        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, customtkinter.END)
            self.save_tasks()
            self.refresh_tasks()

    # Need to make more easier to tell what is being deleted and what to pick is deleted
    def delete_task(self):
       text = self.delete_entry.get().strip()

       if not text.isdigit():
           print("Please enter a valid task number to delete.")
           return
       
       number = int(text)
       index = number - 1

       if not (0 <= index < len(self.tasks)):
           print(f"No task numbered {number}.")
           return

       del self.tasks[index]
       self.save_tasks()
       self.refresh_tasks()
       self.delete_entry.delete(0, "END")
   

    def refresh_tasks(self):
        self.task_textbox.delete("1.0", customtkinter.END)
        for number, task in enumerate(self.tasks, start=1):
            self.task_textbox.insert(customtkinter.END, f"{number}. {task}\n")

    def save_tasks(self):
        with open(SAVE_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def load_tasks(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return []
        return []

app = app()
app.mainloop()
