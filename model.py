from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TodoList(Base):
    __tablename__ = 'todo_list'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'List: {self.name}'

    def with_items(self):
        item_name_list = [item.txt for item in self.items]
        return ', '.join(item_name_list)

    def with_done_items(self):
        item_name_list = [item.txt for item in self.items if item.done]
        return ', '.join(item_name_list)


class TodoItem(Base):
    __tablename__ = 'todo_item'

    id = Column(Integer, primary_key=True)
    txt = Column(String)
    done = Column(Boolean)
    list_id = Column(Integer, ForeignKey('todo_list.id'))
    todo_list = relationship(TodoList, backref="items")

    def __repr__(self):
        return f'Item: {self.txt}'
