from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import TodoList, TodoItem


class Database:
    """
    This is the general encapsulating class having some SQLAlchemy specific features (engine and session).
    Also it hides implementation details of database functions
    """

    def __init__(self):
        """
        Initialization of SQLAlchemy engine and session
        """
        engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
        session_class = sessionmaker(bind=engine)
        self.session = session_class()

    def save_all(self, objects):
        """
        It commits objects created by outer scope
        :param objects: a list of objects to save
        """
        self.session.add_all(objects)
        self.session.commit()

    def get_all_lists_with_items(self):
        """
        It collects all list and their to-do items
        :return: a dict of lists
        """
        output = dict()
        for the_list in self.session.query(TodoList).all():
            output[the_list.name] = the_list.get_items()
        return output

    def get_all_lists_with_done_items(self):
        """
        It collects all list and their to-do items having done
        :return: a dict of lists
        """
        output = dict()
        for the_list in self.session.query(TodoList).all():
            output[the_list.name] = the_list.get_done_items()
        return output

    def delete_all(self):
        """
        It deletes all items and all lists
        """
        self.session.query(TodoItem).delete()
        self.session.query(TodoList).delete()
