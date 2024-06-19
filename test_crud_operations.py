import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Item, Session
from add_item import add_item
from get_item_by_id import get_item_by_id
from update_item import update_item
from delete_item import delete_item

# Define a test database URL
TEST_DATABASE_URL = "sqlite:///test_items.db"

@pytest.fixture(scope="module")
def engine():
    return create_engine(TEST_DATABASE_URL)

@pytest.fixture(scope="module")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def db_session(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    transaction = connection.begin()

    # bind an individual Session to the connection
    session = sessionmaker(bind=connection)()
    Session.configure(bind=connection)  # Ensure Session is configured with this connection

    yield session

    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function", autouse=True)
def seed_data(db_session):
    items = [
        Item(name='The Shawshank Redemption', description='Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
        Item(name='The Godfather', description='The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'),
        Item(name='The Dark Knight', description='When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.'),
        Item(name='Pulp Fiction', description='The lives of two mob hitmen, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'),
        Item(name='Forrest Gump', description='The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other historical events unfold from the perspective of an Alabama man with an IQ of 75.'),
        Item(name='Inception', description='A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.'),
        Item(name='Fight Club', description='An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.'),
        Item(name='The Matrix', description='A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.'),
        Item(name='The Lord of the Rings: The Fellowship of the Ring', description='A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.'),
        Item(name='The Empire Strikes Back', description='After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader.')
    ]

    db_session.bulk_save_objects(items)
    db_session.commit()

def test_add_item(db_session):
    new_item = Item(name="Test Movie", description="Test Description")
    db_session.add(new_item)
    db_session.commit()

    added_item = db_session.query(Item).filter_by(name="Test Movie").first()
    assert added_item is not None
    assert added_item.name == "Test Movie"
    assert added_item.description == "Test Description"

def test_add_item_with_empty_name():
    with pytest.raises(ValueError):
        add_item("", "Description with empty name")

def test_add_duplicate_item(db_session):
    with pytest.raises(ValueError):
        add_item("The Shawshank Redemption", "Duplicate item description")

def test_get_all_items(db_session):
    items = db_session.query(Item).all()
    assert len(items) > 0

def test_get_item_by_id(db_session):
    new_item = Item(name="Another Test Movie", description="Another Test Description")
    db_session.add(new_item)
    db_session.commit()

    fetched_item = db_session.get(Item, new_item.id)
    assert fetched_item is not None
    assert fetched_item.name == "Another Test Movie"

def test_get_item_by_nonexistent_id(db_session):
    nonexistent_item = db_session.get(Item, 99)
    assert nonexistent_item is None

def test_get_item_by_invalid_id():
    with pytest.raises(ValueError):
        get_item_by_id("abc")

def test_update_item(db_session):
    new_item = Item(name="Update Test Movie", description="Update Test Description")
    db_session.add(new_item)
    db_session.commit()

    new_item.name = "Updated Movie"
    new_item.description = "Updated Description"
    db_session.commit()

    updated_item = db_session.get(Item, new_item.id)
    assert updated_item.name == "Updated Movie"
    assert updated_item.description == "Updated Description"

def test_update_nonexistent_item(db_session):
    nonexistent_item = db_session.get(Item, 99)
    if nonexistent_item:
        nonexistent_item.name = "Nonexistent Update"
        db_session.commit()
    assert nonexistent_item is None

def test_update_item_invalid_id():
    with pytest.raises(ValueError):
        update_item("abc", new_name="Invalid ID Update")

def test_delete_item(db_session):
    new_item = Item(name="Delete Test Movie", description="Delete Test Description")
    db_session.add(new_item)
    db_session.commit()

    db_session.delete(new_item)
    db_session.commit()

    deleted_item = db_session.get(Item, new_item.id)
    assert deleted_item is None

def test_delete_nonexistent_item(db_session):
    nonexistent_item = db_session.get(Item, 99)
    if nonexistent_item:
        db_session.delete(nonexistent_item)
        db_session.commit()
    assert nonexistent_item is None

def test_delete_item_invalid_id():
    with pytest.raises(ValueError):
        delete_item("abc")
