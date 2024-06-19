from models import Item, Session

def get_all_items():
    session = Session()
    items = session.query(Item).all()
    for item in items:
        print(f"ID: {item.id}, Name: {item.name}, Description: {item.description}")
    session.close()

if __name__ == '__main__':
    get_all_items()
