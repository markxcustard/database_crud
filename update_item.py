from models import Item, Session

def update_item(item_id, new_name=None, new_description=None):
    if not isinstance(item_id, int):
        raise ValueError("Item ID must be an integer")
    session = Session()
    item = session.get(Item, item_id)
    if item:
        if new_name:
            item.name = new_name
        if new_description:
            item.description = new_description
        session.commit()
        print(f"Updated item: ID: {item.id}, Name: {item.name}, Description: {item.description}")
    else:
        print(f"No item found with ID: {item_id}")
    session.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python3 update_item.py <id> [<new_name> <new_description>]")
    else:
        try:
            item_id = int(sys.argv[1])
            new_name = sys.argv[2] if len(sys.argv) > 2 else None
            new_description = sys.argv[3] if len(sys.argv) > 3 else None
            update_item(item_id, new_name, new_description)
        except ValueError as e:
            print(e)
