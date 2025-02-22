import json

file_list = "todo_list.json"

def load_task(): 
    try:
        with open(file_list, 'r') as file:  # Use 'file_list' instead of 'file_name'
            return json.load(file)
    except FileNotFoundError:  # More specific exception handling
        return {"tasks": []}

def save_task(tasks):
    try:
        with open(file_list, 'w') as file:  # Corrected 'file_name' to 'file_list'
            json.dump(tasks, file,indent=4)  # No need for return, just save the data
    except Exception as e:  # Catch general exceptions and print the error
        print(f"Error saving data: {e}")

def view_task(tasks):
    print()
    task_list=tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks found.")
    else:
        print("Task List:")
        for inx,task in enumerate(task_list):
            status = "[Completed]" if task["completed"] else "[Pending]"
            print(f"{inx+1}.{task['description']} | {status}")

def create_task(tasks):
    description=input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "completed": False})
        save_task(tasks)
        print(tasks)
    else:
        print("Task description cannot be empty.")

def mark_task_complete(tasks):
    view_task(tasks)
    try:
        task_number=int(input("Enter the task number to mark as complete: ").strip())
        if 1<=task_number<=len(tasks["tasks"]):
            tasks["tasks"][task_number-1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Invalid input. Please enter a number.")

def main():
    
    tasks = load_task()
    

    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Create a new task")
        print("3. Mark a task as complete")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
