# Todo App API Contracts

## Core Operations

### Add Task
- **Input**: title (string, 1-100 chars), description (string, 0-500 chars)
- **Output**: task object with id, title, description, completed status
- **Error cases**: Empty title

### View Tasks
- **Input**: None
- **Output**: List of task objects
- **Error cases**: None

### Update Task
- **Input**: id (integer), new title (optional string), new description (optional string)
- **Output**: Updated task object
- **Error cases**: Invalid ID, empty title when provided

### Delete Task
- **Input**: id (integer)
- **Output**: Success confirmation
- **Error cases**: Invalid ID

### Mark Task Complete/Incomplete
- **Input**: id (integer)
- **Output**: Updated task object
- **Error cases**: Invalid ID