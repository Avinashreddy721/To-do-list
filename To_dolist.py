import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")
        
        self.tasks = []
        self.done_tasks = set()
        
        # Colors
        self.bg_color = "#f0f0f0"
        self.button_color = "#4CAF50"
        self.text_color = "#333"
        
        # Create GUI elements
        self.master.config(bg=self.bg_color)
        
        # Entry for adding tasks
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=40, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        
        # Add Task button
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg=self.button_color, fg="white", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Task listbox
        self.task_listbox = tk.Listbox(master, width=60, height=10, bg=self.bg_color, fg=self.text_color, font=("Helvetica", 12))
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Mark as Done button
        self.done_button = tk.Button(master, text="Mark as Done", command=self.mark_as_done, bg="green", fg="white", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.done_button.grid(row=2, column=0, padx=10, pady=10)
        
        # Update Task button
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg="blue", fg="white", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.update_button.grid(row=2, column=1, padx=10, pady=10)
        
        # Delete Task button
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="red", fg="white", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.delete_button.grid(row=2, column=2, padx=10, pady=10)
        
        self.populate_task_listbox()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.populate_task_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            new_task = self.task_var.get()
            if new_task:
                self.tasks[selected_index] = new_task
                self.populate_task_listbox()
                self.task_var.set("")
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.tasks[selected_index]
            self.populate_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_as_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            task = self.task_listbox.get(selected_index)
            if task not in self.done_tasks:
                self.done_tasks.add(task)
                self.populate_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def populate_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            done = " [Done] " if task in self.done_tasks else ""
            self.task_listbox.insert(tk.END, done + task)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
