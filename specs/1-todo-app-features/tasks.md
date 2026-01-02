# Tasks: Todo App Features

**Input**: Design documents from `/specs/1-todo-app-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python project with standard library dependencies
- [X] T003 [P] Configure linting and formatting tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Create basic project structure with src/ directory
- [X] T005 [P] Implement Task data model in src/todo_manager.py
- [X] T006 [P] Setup TodoManager class structure in src/todo_manager.py
- [X] T007 Create base models/entities that all stories depend on
- [X] T008 Configure error handling and validation infrastructure in src/todo_manager.py
- [X] T009 Setup environment configuration management

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: User can add a new task to their todo list, which is the foundational functionality that enables all other operations.

**Independent Test**: User can add a task with title and description, and see it in the task list.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Contract test for add_task endpoint in tests/unit/test_todo_manager.py
- [X] T011 [P] [US1] Integration test for add task user journey in tests/unit/test_todo_manager.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Create Task model in src/todo_manager.py
- [X] T013 [P] [US1] Create TodoManager model in src/todo_manager.py
- [X] T014 [US1] Implement add_task method in src/todo_manager.py (depends on T012, T013)
- [X] T015 [US1] Add validation and error handling for add_task
- [X] T016 [US1] Add logging for user story 1 operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Tasks (Priority: P1)

**Goal**: User can see all their tasks with their status, which is essential for users to track their tasks.

**Independent Test**: User can view all tasks with their ID, title, description, and completion status.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T018 [P] [US2] Contract test for view_tasks endpoint in tests/unit/test_todo_manager.py
- [X] T019 [P] [US2] Integration test for view tasks user journey in tests/unit/test_todo_manager.py

### Implementation for User Story 2

- [X] T020 [P] [US2] Create view_tasks method in src/todo_manager.py
- [X] T021 [US2] Implement view_tasks functionality in src/todo_manager.py
- [X] T022 [US2] Add validation and error handling for view_tasks
- [X] T023 [US2] Integrate with User Story 1 components (if needed)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task (Priority: P2)

**Goal**: User can modify an existing task's title or description, which allows users to refine their tasks as needed.

**Independent Test**: User can update a task's title and/or description by providing the task ID.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T024 [P] [US3] Contract test for update_task endpoint in tests/unit/test_todo_manager.py
- [X] T025 [P] [US3] Integration test for update task user journey in tests/unit/test_todo_manager.py

### Implementation for User Story 3

- [X] T026 [P] [US3] Create update_task method in src/todo_manager.py
- [X] T027 [US3] Implement update_task functionality in src/todo_manager.py
- [X] T028 [US3] Add validation and error handling for update_task

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: User can remove a task from their list, which allows users to remove completed or unwanted tasks.

**Independent Test**: User can delete a task by providing its ID.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T029 [P] [US4] Contract test for delete_task endpoint in tests/unit/test_todo_manager.py
- [X] T030 [P] [US4] Integration test for delete task user journey in tests/unit/test_todo_manager.py

### Implementation for User Story 4

- [X] T031 [P] [US4] Create delete_task method in src/todo_manager.py
- [X] T032 [US4] Implement delete_task functionality in src/todo_manager.py
- [X] T033 [US4] Add validation and error handling for delete_task

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Mark Task Complete/Incomplete (Priority: P1)

**Goal**: User can toggle the completion status of a task, which is core functionality for tracking task completion.

**Independent Test**: User can mark a task as complete or incomplete by providing its ID.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T034 [P] [US5] Contract test for mark_task_complete endpoint in tests/unit/test_todo_manager.py
- [X] T035 [P] [US5] Integration test for mark task complete user journey in tests/unit/test_todo_manager.py

### Implementation for User Story 5

- [X] T036 [P] [US5] Create mark_task_complete method in src/todo_manager.py
- [X] T037 [US5] Implement mark_task_complete functionality in src/todo_manager.py
- [X] T038 [US5] Add validation and error handling for mark_task_complete

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Console Interface Implementation

**Goal**: Implement the console-based interactive menu interface as specified in the requirements.

- [X] T039 Create main application loop in src/main.py
- [X] T040 Implement menu system with numbered options in src/main.py
- [X] T041 Connect menu options to TodoManager methods in src/main.py
- [X] T042 Add input validation and error handling for console interface
- [X] T043 Implement user prompts and messages for all operations

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] TXXX [P] Documentation updates in docs/
- [X] TXXX Code cleanup and refactoring
- [X] TXXX Performance optimization across all stories
- [X] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [X] TXXX Security hardening
- [X] TXXX Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for add_task endpoint in tests/unit/test_todo_manager.py"
Task: "Integration test for add task user journey in tests/unit/test_todo_manager.py"

# Launch all models for User Story 1 together:
Task: "Create Task model in src/todo_manager.py"
Task: "Create TodoManager model in src/todo_manager.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Team completes Setup + Foundational together
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence