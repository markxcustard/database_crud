from models import Base, Item, Session

def seed_data():
    session = Session()
    # Drop all tables and recreate them
    Base.metadata.drop_all(session.get_bind())
    Base.metadata.create_all(session.get_bind())

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

    session.bulk_save_objects(items)
    session.commit()
    session.close()

if __name__ == '__main__':
    seed_data()
