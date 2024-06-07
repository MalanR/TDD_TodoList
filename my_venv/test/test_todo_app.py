import pytest
import asyncio 
from src.todoApp import TodoApp

@pytest.mark.asyncio
async def test_create():
    app = TodoApp.new()
    result = await app.create('Task 1')
    assert result['description'] == 'Task 1'
    assert 'id' in result
    assert 'created_on' in result
    assert result['completed_on'] is None
    assert result['is_completed'] is False

@pytest.mark.asyncio
async def test_update():
    app = TodoApp.new()
    task = await app.create('Task 1')
    task_id = task['id']
    updated_task = await app.update(task_id, 'Updated Task 1')
    assert updated_task['description'] == 'Updated Task 1'
    assert updated_task['id'] == task_id

@pytest.mark.asyncio
async def test_delete():
    app = TodoApp.new()
    task = await app.create('Task 1')
    task_id = task['id']
    result = await app.delete(task_id)
    assert result is True
    assert task_id not in [task['id'] for task in app.todo_list]

@pytest.mark.asyncio
async def test_complete():
    app = TodoApp.new()
    task = await app.create('Task 1')
    task_id = task['id']
    completed_task = await app.complete(task_id)
    assert completed_task['completed_on'] is not None
    assert completed_task['is_completed'] is True

@pytest.mark.asyncio
async def test_filter_completed():
    app = TodoApp.new()
    task1 = await app.create('Task 1')
    task2 = await app.create('Task 2')
    await app.complete(task1['id'])
    completed_tasks = await app.filter('completed')
    assert len(completed_tasks) == 1
    assert completed_tasks[0]['id'] == task1['id']

@pytest.mark.asyncio
async def test_filter_todo():
    app = TodoApp.new()
    task1 = await app.create('Task 1')
    task2 = await app.create('Task 2')
    await app.complete(task1['id'])
    todo_tasks = await app.filter('todo')
    assert len(todo_tasks) == 1
    assert todo_tasks[0]['id'] == task2['id']

@pytest.mark.asyncio
async def test_filter_text_search():
    app = TodoApp.new()
    task1 = await app.create('Buy groceries')
    task2 = await app.create('Clean the house')
    task3 = await app.create('Buy milk')
    search_results = await app.filter('Buy')
    assert len(search_results) == 2
    assert task1 in search_results
    assert task3 in search_results
