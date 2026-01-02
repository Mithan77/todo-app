"""
Unit tests for the TodoManager functionality.
"""
import unittest
import sys
import os

# Add src directory to path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.todo_manager import TodoManager, Task


class TestTask(unittest.TestCase):
    """Test cases for the Task class."""
    
    def test_task_creation_valid(self):
        """Test creating a valid task."""
        task = Task(1, "Test Title", "Test Description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
    
    def test_task_creation_without_description(self):
        """Test creating a task without description."""
        task = Task(1, "Test Title")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "")
        self.assertFalse(task.completed)
    
    def test_task_creation_empty_title(self):
        """Test creating a task with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            Task(1, "")
    
    def test_task_creation_whitespace_title(self):
        """Test creating a task with whitespace-only title raises ValueError."""
        with self.assertRaises(ValueError):
            Task(1, "   ")
    
    def test_task_creation_long_title(self):
        """Test creating a task with title longer than 100 chars raises ValueError."""
        long_title = "A" * 101
        with self.assertRaises(ValueError):
            Task(1, long_title)
    
    def test_task_creation_long_description(self):
        """Test creating a task with description longer than 500 chars raises ValueError."""
        long_description = "A" * 501
        with self.assertRaises(ValueError):
            Task(1, "Test Title", long_description)
    
    def test_task_id_not_positive(self):
        """Test creating a task with non-positive ID raises ValueError."""
        with self.assertRaises(ValueError):
            Task(0, "Test Title")
        
        with self.assertRaises(ValueError):
            Task(-1, "Test Title")


class TestTodoManager(unittest.TestCase):
    """Test cases for the TodoManager class."""
    
    def setUp(self):
        """Set up a fresh TodoManager for each test."""
        self.manager = TodoManager()
    
    def test_add_task_valid(self):
        """Test adding a valid task."""
        task = self.manager.add_task("Test Title", "Test Description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        
        # Verify task is in the list
        tasks = self.manager.view_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, 1)
    
    def test_add_task_without_description(self):
        """Test adding a task without description."""
        task = self.manager.add_task("Test Title")
        self.assertEqual(task.title, "Test Title")
        self.assertEqual(task.description, "")
    
    def test_add_task_empty_title(self):
        """Test adding a task with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_task("")
    
    def test_add_task_whitespace_title(self):
        """Test adding a task with whitespace-only title raises ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
    
    def test_add_task_long_title(self):
        """Test adding a task with title longer than 100 chars raises ValueError."""
        long_title = "A" * 101
        with self.assertRaises(ValueError):
            self.manager.add_task(long_title)
    
    def test_add_task_long_description(self):
        """Test adding a task with description longer than 500 chars raises ValueError."""
        long_description = "A" * 501
        with self.assertRaises(ValueError):
            self.manager.add_task("Test Title", long_description)
    
    def test_view_tasks_empty(self):
        """Test viewing tasks when the list is empty."""
        tasks = self.manager.view_tasks()
        self.assertEqual(len(tasks), 0)
        self.assertEqual(tasks, [])
    
    def test_view_tasks_multiple(self):
        """Test viewing multiple tasks."""
        task1 = self.manager.add_task("Task 1", "Description 1")
        task2 = self.manager.add_task("Task 2", "Description 2")
        task3 = self.manager.add_task("Task 3", "Description 3")
        
        tasks = self.manager.view_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[1].id, 2)
        self.assertEqual(tasks[2].id, 3)
    
    def test_update_task_title(self):
        """Test updating a task's title."""
        task = self.manager.add_task("Original Title", "Original Description")
        
        updated_task = self.manager.update_task(task.id, "New Title")
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "Original Description")
        
        # Verify the change is reflected when viewing tasks
        tasks = self.manager.view_tasks()
        self.assertEqual(tasks[0].title, "New Title")
    
    def test_update_task_description(self):
        """Test updating a task's description."""
        task = self.manager.add_task("Original Title", "Original Description")
        
        updated_task = self.manager.update_task(task.id, new_description="New Description")
        self.assertEqual(updated_task.title, "Original Title")
        self.assertEqual(updated_task.description, "New Description")
        
        # Verify the change is reflected when viewing tasks
        tasks = self.manager.view_tasks()
        self.assertEqual(tasks[0].description, "New Description")
    
    def test_update_task_both_fields(self):
        """Test updating both title and description."""
        task = self.manager.add_task("Original Title", "Original Description")
        
        updated_task = self.manager.update_task(task.id, "New Title", "New Description")
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")
        
        # Verify the changes are reflected when viewing tasks
        tasks = self.manager.view_tasks()
        self.assertEqual(tasks[0].title, "New Title")
        self.assertEqual(tasks[0].description, "New Description")
    
    def test_update_task_invalid_id(self):
        """Test updating a task with invalid ID raises ValueError."""
        with self.assertRaises(ValueError):
            self.manager.update_task(999, "New Title")
    
    def test_update_task_empty_title(self):
        """Test updating a task with empty title raises ValueError."""
        task = self.manager.add_task("Original Title", "Original Description")
        
        with self.assertRaises(ValueError):
            self.manager.update_task(task.id, "")
    
    def test_update_task_long_title(self):
        """Test updating a task with title longer than 100 chars raises ValueError."""
        task = self.manager.add_task("Original Title", "Original Description")
        long_title = "A" * 101
        
        with self.assertRaises(ValueError):
            self.manager.update_task(task.id, long_title)
    
    def test_update_task_long_description(self):
        """Test updating a task with description longer than 500 chars raises ValueError."""
        task = self.manager.add_task("Original Title", "Original Description")
        long_description = "A" * 501
        
        with self.assertRaises(ValueError):
            self.manager.update_task(task.id, new_description=long_description)
    
    def test_delete_task_valid(self):
        """Test deleting a valid task."""
        task = self.manager.add_task("Test Title", "Test Description")
        initial_tasks = self.manager.view_tasks()
        self.assertEqual(len(initial_tasks), 1)
        
        result = self.manager.delete_task(task.id)
        self.assertTrue(result)
        
        final_tasks = self.manager.view_tasks()
        self.assertEqual(len(final_tasks), 0)
    
    def test_delete_task_invalid_id(self):
        """Test deleting a task with invalid ID raises ValueError."""
        with self.assertRaises(ValueError):
            self.manager.delete_task(999)
    
    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = self.manager.add_task("Test Title", "Test Description")
        self.assertFalse(task.completed)
        
        marked_task = self.manager.mark_task_complete(task.id)
        self.assertTrue(marked_task.completed)
        
        # Verify the change is reflected when viewing tasks
        tasks = self.manager.view_tasks()
        self.assertTrue(tasks[0].completed)
    
    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete after it's complete."""
        task = self.manager.add_task("Test Title", "Test Description")
        
        # First mark as complete
        self.manager.mark_task_complete(task.id)
        
        # Then mark as incomplete
        marked_task = self.manager.mark_task_complete(task.id)
        self.assertFalse(marked_task.completed)
        
        # Verify the change is reflected when viewing tasks
        tasks = self.manager.view_tasks()
        self.assertFalse(tasks[0].completed)
    
    def test_mark_task_invalid_id(self):
        """Test marking a task with invalid ID raises ValueError."""
        with self.assertRaises(ValueError):
            self.manager.mark_task_complete(999)


if __name__ == '__main__':
    unittest.main()