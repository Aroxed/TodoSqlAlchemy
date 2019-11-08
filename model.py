from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TodoList(Base):
    """
    The ORM implementation of to-do lists including attributes declaration and model specific functions
    """
    __tablename__ = 'todo_list'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        """
        String representation of objects (eg., "print(obj)")
        :return: string
        """
        return f'List: {self.name}'

    def get_items(self):
        """
        It collects the current list's items
        :return: string representation of the list items
        """
        item_name_list = [item.txt for item in self.items]
        return ', '.join(item_name_list)

    def get_done_items(self):
        """
        It collects the current list's items having done=True
        :return: string representation of the list items
        """
        item_name_list = [item.txt for item in self.items if item.done]
        return ', '.join(item_name_list)


class TodoItem(Base):
    """
    The ORM implementation of to-do lists items including attributes declaration and foreign key declaration
    """
    __tablename__ = 'todo_item'

    id = Column(Integer, primary_key=True)
    txt = Column(String)
    done = Column(Boolean)
    list_id = Column(Integer, ForeignKey('todo_list.id'))
    todo_list = relationship(TodoList, backref="items")

    def __repr__(self):
        """
        String representation of objects (eg., "print(obj)")
        :return: string
        """
        return f'Item: {self.txt}'
