tasks = []
def add_task(task_name):
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()