import asyncio
import uuid
import datetime


# create todoapp class and intitialze self.
# This class will contain all the methods that we will be calling.
# create a static method called new to be used to call a new instance of TodoApp.
class TodoApp:
    def __init__(self):
        # create a empty array called to be used for appending the tasks
        self.todo_list = []


    @staticmethod
    def new():
        return TodoApp()


    # create a method called create, this fucntion will create a new task and append it to the todo_list
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


  # create a method called delete, this method will delete a task specified by its Id from todo_list
    async def delete(self, task_id):
        for task in self.todo_list:
            if task['id'] == task_id:
                self.todo_list.remove(task)
                print(f"Task with id {task_id} was deleted")
                return True
        # if the id is not found the if statement will not be executed
        print(f"Task with id {task_id} was not found")
        return False


  # create a method update, this method will update the description value a existing task.
    async def update(self, task_id, description):
        for task in self.todo_list:
            if task['id'] == task_id:
                task['description'] = description
                return task
        # if the id is not found the if statement will not be executed.
        print(f"Could not find task with task with id {task_id} in todo list.")
        return 


  # create a method called complete, this method will change the value of is_completed to true for the specified task.
    async def complete(self, task_id):
        for task in self.todo_list:
            if task['id'] == task_id:
                task['completed_on'] = datetime.datetime.now().strftime("%d:%M:%S")
                # update the value of is_completed to True.
                task['is_completed'] = True
                return task
        # if the id is not found the if statement will not be executed.
        print(f"Could not complete task with task with id {task_id} in todo list, ID not found.")
        return


    # create a method called filter, this mehtod will filter for todo_list completed, no completed and entered text.
    async def filter(self, criteria):
        # loop through todo_list and find the tasks where is_completed is True
        if criteria == 'completed':
            return [task for task in self.todo_list if task['is_completed']]
        # loop through todo_list and find the tasks where is_completed is False
        elif criteria == 'todo':
            return [task for task in self.todo_list if not task['is_completed']]
        else:
        # loop through todo_list and find the tasks where description is equal to or contains the asserted text.
            return [task for task in self.todo_list if criteria.lower() in task['description'].lower()]
        


# create main() that will simulate the use cases for all the methods.
async def main():
    app = TodoApp.new()
    task1 = await app.create('Task 1')
    print("Created Task:", task1)
    
    
    task2 = await app.create('Task 2')
    print("Created Task:", task2)
    
    
    updated_task = await app.update(task1['id'], 'Updated Task 1')
    print("Updated Task:", updated_task)
    
    
    delete_task = await app.delete(task2['id'])
    print("Deleted Task:", delete_task)
    
    
    await app.complete(task1['id'])
    completed_tasks = await app.filter('completed')
    print("Completed Tasks:", completed_tasks)

    
    all_tasks = app.todo_list
    print (f"ALL TASKS : \n{all_tasks}")


# run to see tasks executed in terminal.
if __name__ == "__main__":
    asyncio.run(main())
