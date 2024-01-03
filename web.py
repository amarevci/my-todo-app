import streamlit as st
import functions

todos = functions.get_todos()  # get the todos from our todos.txt

def add_todo():
    todo = st.session_state["new_todo"] + "\n" # get the newly added todo, like the event in GUI
    todos.append(todo)
    functions.write_todos(todos)


# order of these matters, will show in the order written
st.title("My ToDo App")  # create a web app for us to view
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # create checkboxes for each todo, add key to put in session state
    if checkbox:
        todos.pop(index)  # remove completed todo
        functions.write_todos(todos)  # rewrite updated todos
        del st.session_state[todo]  # remove the completed to do from the session state too
        st.experimental_rerun()  # to rerun the code

st.text_input(label="Enter a todo", label_visibility='hidden', placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

# print("Hello")
# st.session_state
