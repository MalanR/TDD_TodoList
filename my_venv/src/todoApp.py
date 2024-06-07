import asyncio
import uuid
import datetime

class TodoApp:
    def __init__(self):
        self.todo_list = []

    @staticmethod
    def new():
        return TodoApp()

    async def create(self, description):
        todo_task = {
            'id': str(uuid.uuid4()),
            'description': description,
            'created_on': datetime.datetime.now().strftime("%d:%M:%S"),
            'completed_on': None,
            'is_completed': False
        }
        self.todo_list.append(todo_task)
        return todo_task

    async def delete(self, task_id):
        for task in self.todo_list:
            if task['id'] == task_id:
                self.todo_list.remove(task)
                return True
        return False

    async def update(self, task_id, description):
        for task in self.todo_list:
            if task['id'] == task_id:
                task['description'] = description
                return task
        return None

    async def complete(self, task_id):
        for task in self.todo_list:
            if task['id'] == task_id:
                task['completed_on'] = datetime.datetime.now().strftime("%d:%M:%S")
                task['is_completed'] = True
                return task
        return None

    async def filter(self, criteria):
        if criteria == 'completed':
            return [task for task in self.todo_list if task['is_completed']]
        elif criteria == 'todo':
            return [task for task in self.todo_list if not task['is_completed']]
        else:
            return [task for task in self.todo_list if criteria.lower() in task['description'].lower()]


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

    # all_tasks = await app.filter('')
    # print("All Tasks:", all_tasks)


if __name__ == "__main__":
    asyncio.run(main())
