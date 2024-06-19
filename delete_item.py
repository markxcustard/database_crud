from models import Item, Session

def delete_item(item_id):
    if not isinstance(item_id, int):
        raise ValueError("Item ID must be an integer")
    session = Session()
    item = session.get(Item, item_id)
    if item:
        session.delete(item)
        session.commit()
        print(f"Deleted item with ID: {item.id}")
    else:
        print(f"No item found with ID: {item_id}")
    session.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python delete_item.py <id>")
    else:
        try:
            item_id = int(sys.argv[1])
            delete_item(item_id)
        except ValueError as e:
            print(e)
