
import streamlit as st
import pandas as pd
from datetime import date

# Simulated data storage (in a real-world app, use a database)
homework_data = []
post_data = []
notifications = []
results_data = []

# Function to add a new homework item
def add_homework(subject, description, due_date):
    homework_data.append({"Subject": subject, "Description": description, "Due Date": due_date})

# Function to add a new post
def add_post(title, content):
    post_data.append({"Title": title, "Content": content, "Date": date.today()})

# Function to add a notification
def add_notification(content):
    notifications.append({"Content": content, "Date": date.today()})

# Function to add a result
def add_result(student_name, subject, marks):
    results_data.append({"Student Name": student_name, "Subject": subject, "Marks": marks})

# Streamlit app
st.title("School Management Portal")

menu = ["Home", "Homework", "Posts", "Notifications", "Results", "Admin"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to the School Management Portal")
    st.write("Use the menu to navigate.")

elif choice == "Homework":
    st.subheader("Homework")
    for hw in homework_data:
        st.write(f"**Subject:** {hw['Subject']}")
        st.write(f"**Description:** {hw['Description']}")
        st.write(f"**Due Date:** {hw['Due Date']}")
        st.write("---")

elif choice == "Posts":
    st.subheader("Posts")
    for post in post_data:
        st.write(f"### {post['Title']}")
        st.write(post['Content'])
        st.write(f"_Posted on: {post['Date']}_")
        st.write("---")

elif choice == "Notifications":
    st.subheader("Notifications")
    for notification in notifications:
        st.write(f"- {notification['Content']} (Posted on: {notification['Date']})")

elif choice == "Results":
    st.subheader("Results")
    df = pd.DataFrame(results_data)
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No results available.")

elif choice == "Admin":
    st.subheader("Admin Panel")

    admin_choice = st.selectbox("Admin Actions", ["Add Homework", "Add Post", "Add Notification", "Add Result"])

    if admin_choice == "Add Homework":
        subject = st.text_input("Subject")
        description = st.text_area("Description")
        due_date = st.date_input("Due Date")
        if st.button("Add Homework"):
            add_homework(subject, description, due_date)
            st.success("Homework added successfully!")

    elif admin_choice == "Add Post":
        title = st.text_input("Title")
        content = st.text_area("Content")
        if st.button("Add Post"):
            add_post(title, content)
            st.success("Post added successfully!")

    elif admin_choice == "Add Notification":
        content = st.text_area("Notification Content")
        if st.button("Add Notification"):
            add_notification(content)
            st.success("Notification added successfully!")

    elif admin_choice == "Add Result":
        student_name = st.text_input("Student Name")
        subject = st.text_input("Subject")
        marks = st.number_input("Marks", min_value=0, max_value=100, step=1)
        if st.button("Add Result"):
            add_result(student_name, subject, marks)
            st.success("Result added successfully!")
