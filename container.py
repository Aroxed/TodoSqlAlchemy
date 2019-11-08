from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import TodoList, TodoItem

class Container:
    def __init__(self):
        engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")
        session_class = sessionmaker(bind=engine)
        self.session = session_class()

    def save_all(self, actions):
        self.session.add_all(actions)
        self.session.commit()

    def get_all_lists_with_items(self):
        output = dict()
        for the_list in self.session.query(TodoList).all():
            output[the_list.name] = the_list.with_items()
        return output

    def get_all_lists_with_done_items(self):
        output = dict()
        for the_list in self.session.query(TodoList).all():
            output[the_list.name] = the_list.with_done_items()
        return output

    def delete_all(self):
        self.session.query(TodoItem).delete()
        self.session.query(TodoList).delete()
