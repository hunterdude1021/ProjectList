#mostly here for me to learn how to use customtkinter

import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Todo List")
        self.geometry("400x400")

        self.task_entry = customtkinter.CTkEntry(self, placeholder_text="Enter a task")
        self.task_entry.pack(pady=10)

        self.add_button = customtkinter.CTkButton(self, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        self.task_textbox = customtkinter.CTkTextbox(self)
        self.task_textbox.pack(pady=10, fill="both", expand=True)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_textbox.insert(customtkinter.END, task)
            self.task_entry.delete(0, customtkinter.END)


app = app()
app.mainloop()
