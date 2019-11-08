from container import Container
from model import TodoList, TodoItem

container = Container()
container.delete_all()
todo_list_object1 = TodoList(name="Work for today")
todo_item_object1 = TodoItem(txt="Wash the car", done=False, todo_list=todo_list_object1)
todo_item_object2 = TodoItem(txt="Write a letter", done=True, todo_list=todo_list_object1)

todo_list_object2 = TodoList(name="Work for tomorrow")
todo_item_object3 = TodoItem(txt="Clean the room", done=False, todo_list=todo_list_object2)
todo_item_object4 = TodoItem(txt="Go swimming", done=True, todo_list=todo_list_object2)

container.save_all([todo_list_object1, todo_list_object2,
                    todo_item_object1, todo_item_object2, todo_item_object3, todo_item_object4])

print("All list with items:")
print(container.get_all_lists_with_items())

print("\nAll list with done items:")
print(container.get_all_lists_with_done_items())
