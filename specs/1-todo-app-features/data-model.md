# Data Model: Todo App

## Task Entity

### Fields
- **id**: Integer, unique identifier for the task (auto-generated)
- **title**: String, the task title (required, max 100 characters)
- **description**: String, detailed description of the task (optional, max 500 characters)
- **completed**: Boolean, completion status of the task (default: False)

### Validation Rules
- Title must not be empty
- Title must be between 1 and 100 characters
- Description can be empty or between 1 and 500 characters
- ID must be unique within the task list
- ID is auto-generated as an incrementing integer

### State Transitions
- A task starts with `completed = False`
- A task can transition from `completed = False` to `completed = True` (mark as complete)
- A task can transition from `completed = True` to `completed = False` (mark as incomplete)