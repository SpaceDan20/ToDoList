# create class 'task_manager' that handles tasks
class TaskManager:
    def __init__(self) -> None:
        self.task_list = {}

    # create function to add tasks
    def add_task(self):
        task_confirmed = False
        while not task_confirmed:
            task_name = input("\nName your task: ")
            task_description = input("Describe the task: ")
            confirmation = input(
                f"\nTask: {task_name}\nDescription: {task_description}\n\nIs this correct? 'yes' or 'no': "
            )
            if confirmation.lower() == "yes":
                task_confirmed = True
        self.task_list[task_name] = task_description
        print(f"\nYour task, '{task_name}', is set.\n")

    # create function to view tasks
    def view_tasks(self):
        print("\nHere's a list of your tasks:")
        print("---------------------------")
        for task, description in self.task_list.items():
            print(f"Task: {task}\nDescription: {description}")
            print("---------------------------")

    def confirm_task(task, description):
        return input(
            f"Task: {task}\nDescription: {description}\n\nIs this correct? 'yes' or 'no': "
        )

    # create function to edit/cancel tasks
    def edit_task(self):
        self.view_tasks()

        # loops through to make sure user is editing the right task
        edit_confirmed = False
        while not edit_confirmed:
            task_to_edit = input("\nWhich task do you want to edit? ")
            if task_to_edit in self.task_list.keys():
                task_description = self.task_list[task_to_edit]
                print("This is the task you are looking to edit:\n")
                edit_confirmation = TaskManager.confirm_task(
                    task_to_edit, task_description
                )
                if edit_confirmation.lower() == "yes":
                    edit_confirmed = True

        # loops through to make sure task is edited properly
        edit_complete_confirmation = False
        while not edit_complete_confirmation:
            what_to_edit = input(
                "\nWhat do you want to edit?\n'name'\n'description'\n'delete'\n'cancel'\n\n"
            ).lower()

            # lets the user change the name of a task by creating a new k:v pair with previous description as value
            # deletes the previous k:v pair from task_list dictionary
            if what_to_edit == "name":
                new_task_name = input("What do you want the new task name to be?\n")
                og_description = self.task_list[task_to_edit]
                self.task_list[new_task_name] = og_description
                del self.task_list[task_to_edit]

            # lets the user change description of specified task
            if what_to_edit == "description":
                new_task_description = input(
                    "What do you want the new description to be?\n"
                )
                self.task_list[task_to_edit] = new_task_description

            # lets the user delete the specified task
            if what_to_edit == "delete":
                del self.task_list[task_to_edit]
                print("\nTask successfully deleted.\n")
                edit_complete_confirmation = True

        self.view_tasks()


# create function to complete tasks

# create function to list tasks
# create tree to list all tasks vs to-do tasks vs completed tasks


print("Welcome to the To-Do List Creator Application.")

task_manager = TaskManager()
application_open = True

while application_open:
    user_choice = input(
        """Please select from the following options:\n
        'add'
        'edit'
        'complete'
        'quit'\n\n"""
    )

    if user_choice == "add":
        task_manager.add_task()

    if user_choice == "edit":
        task_manager.edit_task()

    if user_choice == "quit":
        application_open = False
