from models import Item, Session

def get_item_by_id(item_id):
    if not isinstance(item_id, int):
        raise ValueError("Item ID must be an integer")
    session = Session()
    item = session.get(Item, item_id)
    if item:
        print(f"ID: {item.id}, Name: {item.name}, Description: {item.description}")
    else:
        print(f"No item found with ID: {item_id}")
    session.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python get_item_by_id.py <id>")
    else:
        try:
            item_id = int(sys.argv[1])
            get_item_by_id(item_id)
        except ValueError as e:
            print(e)
