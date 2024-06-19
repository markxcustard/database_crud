# Films CRUD API

This project is a basic CRUD (Create, Read, Update, Delete) API for managing films using SQLAlchemy with SQLite. It includes Python scripts for adding, updating, deleting, and retrieving film records. The project also includes unit tests to ensure the functionality of the API.

## Project Structure

Films/
├── add_item.py
├── delete_item.py
├── get_all_items.py
├── get_item_by_id.py
├── items.db
├── models.py
├── seed_data.py
├── test_crud_operations.py
├── test_items.db
├── update_item.py
└── .gitignore


## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd Films
    ```

2. **Create and activate a virtual environment (optional but recommended)**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install sqlalchemy pytest
    ```

4. **Initialize the database with seed data**:

    ```bash
    python3 seed_data.py
    ```

## Usage

### Adding an Item

To add a new film:

```bash
python3 add_item.py "Movie Name" "Movie Description"
Updating an Item
To update an existing film:

python3 update_item.py <id> "Updated Movie Name" "Updated Movie Description"
Example:

python3 update_item.py 1 "Updated Movie Name" "Updated Movie Description"
Deleting an Item
To delete an existing film:

python3 delete_item.py <id>
Example:


python3 delete_item.py <id>
Retrieving All Items
To retrieve all films:


python3 get_all_items.py
Retrieving an Item by ID
To retrieve a film by its ID:

python3 get_item_by_id.py <id>
Example:

python3 get_item_by_id.py 1
Running Tests
To run the unit tests:

pytest test_crud_operations.py
.gitignore
The .gitignore file is set up to ignore the SQLite database files and the __pycache__ directory:

# Ignore the SQLite database files
Films/items.db
Films/test_items.db

# Ignore the __pycache__ directory
__pycache__/
Films/__pycache__/
