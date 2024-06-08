import asyncio
import uuid
import datetime


# create todoapp class and intitialze self.
class TodoApp:
    def __init__(self):
        # create a empty array called todo_lsit, this will be used for appending the tasks
        self.todo_list = []

    # create a static method called new, this will be called to create a new instance of TodoApp.
    @staticmethod
    def new():
        return TodoApp()


    # create a function called create, this fucntion will create a new task and append it to the todo_list
    async def create(self, description):
        
        # this is the structure of each task defined in a dictionary
        todo_task = {
            'id': str(uuid.uuid4()),
            'description': description,
            'created_on': datetime.datetime.now().strftime("%d:%M:%S"),
            'completed_on': None,
            'is_completed': False
        }
        # append the new task called todo_task to the todolist array.
        self.todo_list.append(todo_task)
        return todo_task


  # create a function called delete, this fucntion will delete a task from todo_list
    async def delete(self, task_id):
        # loop through todo_list.
        for task in self.todo_list:
            # find the id that was passed in.
            if task['id'] == task_id:
                # call the remove function to remove the task from todo_list
                self.todo_list.remove(task)
                return True
        # if the id is not found the if statement will not be executed
        return False


  # create a function update, this fucntion will cupdate a existing task.
    async def update(self, task_id, description):
        # loop through the todo_list
        for task in self.todo_list:
            # find the task that maches the id provided
            if task['id'] == task_id:
                # if the id exists in the todo_list we set description  to be equal to the new description
                task['description'] = description
                return task
        # if the id is not found the if statement will not be executed.
        return None


  # create a function called complete, this fucntion will change the value of is_completed to true for the specified task.
    async def complete(self, task_id):
        # loop through the todO_list
        for task in self.todo_list:
            # find the task by its id using a if statement.
            if task['id'] == task_id:
                # updating the completed_on value to the current time in a day-min-sec format.
                task['completed_on'] = datetime.datetime.now().strftime("%d:%M:%S")
                # update the value of is_completed to True.
                task['is_completed'] = True
                return task
        # if the id is not found the if statement will not be executed.
        return None


  # create a function called filter, this function will filter for todo_list completed, no completed and entered text.
    async def filter(self, criteria):
        # loop through todo_list and find the tasks where is_completed is True
        if criteria == 'completed':
            return [task for task in self.todo_list if task['is_completed']]
        # loop through todo_list and find the tasks where is_completed is False
        elif criteria == 'todo':
            return [task for task in self.todo_list if not task['is_completed']]
        else:
        # loop through todo_list and find the tasks where discription is equal to or contains the user entered text.
            return [task for task in self.todo_list if criteria.lower() in task['description'].lower()]


# create a functio called main.
async def main():
    # declare app variable to be TodoApp and calling the new method.
    app = TodoApp.new()
    # set a variable name and call the create method.
    task1 = await app.create('Task 1')
    print("Created Task:", task1)
    
    # set a variable name and call the create method.
    task2 = await app.create('Task 2')
    print("Created Task:", task2)
    
    # set a variable name and call the pdate method.
    updated_task = await app.update(task1['id'], 'Updated Task 1')
    print("Updated Task:", updated_task)
    
    # set a variable name and call the delete method.
    delete_task = await app.delete(task2['id'])
    print("Deleted Task:", delete_task)
    
    # set a variable name and call the complete method.
    await app.complete(task1['id'])
    completed_tasks = await app.filter('completed')
    print("Completed Tasks:", completed_tasks)

    # call to print the todo_list containing all the tasks.
    all_tasks = app.todo_list
    print (f"ALL TASKS : \n{all_tasks}")



if __name__ == "__main__":
    asyncio.run(main())
