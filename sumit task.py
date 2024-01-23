import tkinter as tk
from tkinter import simpledialog


class Application(tk.Tk):
    def __init__(self, master=None):
        """
        Initialize the TODO Application.

        Parameters:
            master (tk.Tk): The master Tkinter window.
        """
        tk.Tk.__init__(self, master)
        self.title("TODO Application")
        self.geometry("800x450")
        self.resizable(False, False)
        self.createWidgets()

    def createWidgets(self):
        """
        Create and configure widgets for the TODO Application.
        """
        self.tasks = []

        # Title Label
        title_label = tk.Label(self, text="To-Do Task List", font=("Helvetica", 24))
        title_label.pack(pady=10)

        # Scrollable List of Tasks
        self.tasks_listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=70, height=15)
        self.tasks_listbox.pack(pady=10)

        # Add sample tasks
        self.add_task_to_list("Complete homework")
        self.add_task_to_list("Buy groceries")
        self.add_task_to_list("Exercise")

        # Add/Edit/Delete/Complete Buttons for Tasks
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Add New Task", command=self.add_task)
        add_button.pack(side=tk.LEFT)

        edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task)
        edit_button.pack(side=tk.LEFT)

        delete_button = tk.Button(
            button_frame, text="Delete Task", command=self.delete_task
        )
        delete_button.pack(side=tk.LEFT)

        complete_button = tk.Button(
            button_frame, text="Complete Task", command=self.complete_task
        )
        complete_button.pack(side=tk.LEFT)

    def add_task(self):
        """
        Prompt user for a new task description and add it to the task list.
        """
        description = simpledialog.askstring("Add New Task", "Enter task description:")
        if description:
            self.add_task_to_list(description)

    def add_task_to_list(self, description):
        """
        Add a task to the task list.

        Parameters:
            description (str): The description of the task.
        """
        task_info = {"description": description, "complete": False}
        self.tasks.append(task_info)
        self.tasks_listbox.insert(tk.END, self.format_task_for_display(task_info))

    def edit_task(self):
        """
        Edit the description of the selected task in the task list.
        """
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            selected_task_info = self.tasks[selected_task_index[0]]
            new_description = simpledialog.askstring(
                "Edit Task",
                "Enter new task description:",
                initialvalue=selected_task_info["description"],
            )
            if new_description:
                selected_task_info["description"] = new_description
                self.update_task_display()

    def delete_task(self):
        """
        Delete the selected task from the task list.
        """
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.tasks_listbox.delete(selected_task_index)

    def complete_task(self):
        """
        Toggle the completion status of the selected task in the task list.
        """
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            selected_task_info = self.tasks[selected_task_index[0]]
            selected_task_info["complete"] = not selected_task_info["complete"]
            self.update_task_display()

    def update_task_display(self):
        """
        Update the display of tasks in the listbox.
        """
        self.tasks_listbox.delete(0, tk.END)
        for task_info in self.tasks:
            self.tasks_listbox.insert(tk.END, self.format_task_for_display(task_info))

    def format_task_for_display(self, task_info):
        """
        Format a task for display in the listbox.

        Parameters:
            task_info (dict): The dictionary representing a task.

        Returns:
            str: The formatted task string.
        """
        return (
            f"{'[X]' if task_info['complete'] else '[  ]'} {task_info['description']}"
        )


if __name__ == "__main__":
    app = Application()
    app.mainloop()
