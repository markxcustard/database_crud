from models import Item, Session

def add_item(name, description):
    if not name:
        raise ValueError("Item name cannot be empty")
    session = Session()
    existing_item = session.query(Item).filter_by(name=name).first()
    if existing_item:
        raise ValueError(f"Item with name '{name}' already exists with ID: {existing_item.id}")
    else:
        new_item = Item(name=name, description=description)
        session.add(new_item)
        session.commit()
        print(f"Added item: ID: {new_item.id}, Name: {new_item.name}, Description: {new_item.description}")
    session.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python add_item.py <name> <description>")
    else:
        name, description = sys.argv[1], sys.argv[2]
        add_item(name, description)
