"""
BCA PROJECT
A BCA project: 7 small Python projects inside one dark office-style dashboard.

Run with:   streamlit run app.py
"""

import os
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Python Office Hub", page_icon="AP", layout="wide")


# ---------------------------------------------------------------
# 1. LOOK AND FEEL (light + dark mode, dotted background)
# ---------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

    /* colours for LIGHT mode */
    :root {
        --bg: #f5f8f2;  --dot: #cfdccb;  --card: #ffffff;  --border: #dbe5d6;  --soft: #e8efe4;
        --text: #22312a;  --muted: #55665a;  --accent: #587d5f;  --accent2: #7a9c78;
        --hover: #3b5e43;  --shadow: rgba(88, 125, 95, 0.12);
    }
    /* colours for DARK mode (used automatically when the device is in dark mode) */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg: #121a15;  --dot: #25342a;  --card: #1b261f;  --border: #2d3d32;  --soft: #263529;
            --text: #e8f0e9;  --muted: #a9bbac;  --accent: #4f7a58;  --accent2: #6f9a77;
            --hover: #3b5e43;  --shadow: rgba(0, 0, 0, 0.35);
        }
    }

    html, body, [class*="css"], .stApp { font-family: 'Poppins', sans-serif; }
    #MainMenu, footer, header { visibility: hidden; }

    /* light dotted background */
    .stApp {
        background-color: var(--bg);
        background-image: radial-gradient(var(--dot) 1.3px, transparent 1.3px);
        background-size: 22px 22px;
    }
    .block-container { padding-top: 1rem; max-width: 1200px; }

    /* text colours: always readable on our backgrounds */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4,
    [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li,
    [data-testid="stWidgetLabel"] p, [data-testid="stMetricValue"],
    [data-testid="stExpander"] summary p { color: var(--text); }
    [data-testid="stCaptionContainer"], div[data-testid="stMetricLabel"] p { color: var(--muted); }

    /* animations */
    @keyframes fadeUp { from {opacity: 0; transform: translateY(14px);} to {opacity: 1; transform: none;} }
    @keyframes slideIn { from {opacity: 0; transform: translateX(-24px);} to {opacity: 1; transform: none;} }
    @keyframes dropIn { from {opacity: 0; transform: translateY(-8px);} to {opacity: 1; transform: none;} }
    @keyframes popIn {
        0% {transform: scale(0) rotate(-90deg); opacity: 0;}
        70% {transform: scale(1.2) rotate(8deg); opacity: 1;}
        100% {transform: scale(1) rotate(0); opacity: 1;}
    }
    @keyframes float { 0%, 100% {transform: translateY(0);} 50% {transform: translateY(-4px);} }

    /* sidebar and its animated menu list */
    section[data-testid="stSidebar"] { background: var(--card); border-right: 1px solid var(--border); }
    section[data-testid="stSidebar"] div[role="radiogroup"] { gap: 4px; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        width: 100%; padding: 0.55rem 0.8rem; border-radius: 10px;
        animation: slideIn 0.5s ease both; transition: all 0.2s ease;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child { display: none; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(1) { animation-delay: 0.05s; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(2) { animation-delay: 0.10s; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(3) { animation-delay: 0.15s; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(4) { animation-delay: 0.20s; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(5) { animation-delay: 0.25s; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(6) { animation-delay: 0.30s; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(7) { animation-delay: 0.35s; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:nth-child(8) { animation-delay: 0.40s; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover { background: var(--soft); transform: translateX(5px); }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
        background: linear-gradient(90deg, var(--accent), var(--accent2)); box-shadow: 0 4px 12px var(--shadow);
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) * { color: #ffffff !important; }

    /* logo icon that pops open, then floats */
    .logo {
        display: inline-flex; align-items: center; justify-content: center;
        width: 40px; height: 40px; margin-right: 0.7rem; border-radius: 12px; font-size: 1.3rem;
        background: linear-gradient(135deg, var(--accent), var(--accent2));
        animation: popIn 0.8s ease both, float 3s ease-in-out 1s infinite;
    }
    .brand { display: flex; align-items: center; margin-bottom: 0.8rem; }
    .brand b, .topbar b { font-size: 1.15rem; letter-spacing: 1.5px; color: var(--text); }

    /* top bar */
    .topbar {
        display: flex; justify-content: space-between; align-items: center;
        background: var(--card); border: 1px solid var(--border); border-radius: 14px;
        padding: 0.7rem 1.1rem; margin-bottom: 1rem; box-shadow: 0 4px 14px var(--shadow);
        animation: fadeUp 0.5s ease both;
    }
    .topbar .left { display: flex; align-items: center; }
    .topbar span.date { color: var(--muted); font-size: 0.85rem; }

    /* page title with animated icon */
    .page-title { display: flex; align-items: center; gap: 0.9rem; margin: 0.6rem 0 1.2rem; animation: fadeUp 0.5s ease both; }
    .page-icon {
        width: 48px; height: 48px; border-radius: 14px; background: var(--soft); font-size: 1.5rem;
        display: flex; align-items: center; justify-content: center; animation: popIn 0.7s ease both;
    }
    .page-title h2 { margin: 0; font-size: 1.5rem; font-weight: 600; color: var(--text); }
    div.page-title p { margin: 0.1rem 0 0; color: var(--muted); }

    /* cards */
    div[data-testid="stMetric"] {
        background: var(--card); border: 1px solid var(--border); border-left: 5px solid var(--accent);
        border-radius: 12px; padding: 0.8rem 1rem; box-shadow: 0 3px 10px var(--shadow);
        animation: fadeUp 0.5s ease both; transition: transform 0.2s ease;
    }
    div[data-testid="stMetric"]:hover { transform: translateY(-4px); }
    div[data-testid="stForm"] { background: var(--card); border: 1px solid var(--border); border-radius: 14px; animation: fadeUp 0.5s ease both; }
    div[data-testid="stDataFrame"] { border: 1px solid var(--border); border-radius: 12px; animation: fadeUp 0.6s ease both; }

    /* buttons (white text on green in both modes) */
    .stButton > button, .stDownloadButton > button, div[data-testid="stForm"] button {
        background: var(--accent); border: none; border-radius: 10px; padding: 0.4rem 1.1rem;
        transition: all 0.2s ease;
    }
    .stButton > button p, .stDownloadButton > button p, div[data-testid="stForm"] button p { color: #ffffff; }
    .stButton > button:hover, .stDownloadButton > button:hover, div[data-testid="stForm"] button:hover {
        background: var(--hover); transform: translateY(-2px); box-shadow: 0 6px 14px var(--shadow);
    }

    /* lists that open with animation (expander and dropdown lists) */
    div[data-testid="stExpander"] { background: var(--card); border: 1px solid var(--border); border-radius: 12px; }
    div[data-testid="stExpander"] details[open] > div { animation: dropIn 0.35s ease both; }
    div[data-testid="stExpander"] li { animation: slideIn 0.4s ease both; }
    div[data-testid="stExpander"] li:nth-child(2) { animation-delay: 0.08s; }
    div[data-testid="stExpander"] li:nth-child(3) { animation-delay: 0.16s; }
    div[data-testid="stExpander"] li:nth-child(4) { animation-delay: 0.24s; }
    div[data-baseweb="popover"] { animation: dropIn 0.2s ease both; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------
# 2. FILES AND SMALL HELPER FUNCTIONS
# ---------------------------------------------------------------
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)

STUDENT_FILE = "students.csv"
TODO_FILE = "todos.csv"
MARKS_FILE = "marks.csv"

STUDENT_COLUMNS = ["Roll No", "Name", "Course", "Attendance", "Status"]
TODO_COLUMNS = ["Task", "Priority", "Status"]
MARKS_COLUMNS = ["Roll No", "Name", "Course", "Total", "Percentage", "Grade", "Result", "Date"]


def load_data(file_name, columns):
    """Read a CSV from the data folder. If it does not exist, return an empty table."""
    path = os.path.join(DATA_FOLDER, file_name)
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame(columns=columns)


def save_data(table, file_name):
    """Save a table to the data folder as CSV."""
    table.to_csv(os.path.join(DATA_FOLDER, file_name), index=False)


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


ICONS = {
    "Dashboard": "🏠",
    "Student Marks": "📝",
    "Performance Analysis": "📊",
    "House Price Prediction": "🏡",
    "Face Recognition": "📷",
    "Task List": "✅",
    "Calculator": "🧮",
    "Student Management": "🎓",
}


def page_title(title, text):
    icon = ICONS.get(title, "📌")
    st.markdown(
        f'<div class="page-title"><div class="page-icon">{icon}</div>'
        f'<div><h2>{title}</h2><p>{text}</p></div></div>',
        unsafe_allow_html=True,
    )


def sample_students():
    return pd.DataFrame(
        {
            "name": ["Rahul", "Anjali", "Aman", "Neha", "Riya", "Karan", "Pooja", "Sameer"],
            "math": [78, 92, 45, 88, 35, np.nan, 81, 29],
            "english": [82, 89, 51, 90, np.nan, 67, 84, 34],
            "science": [74, 95, 49, 85, 40, 58, 79, 31],
            "attendance": [88, 94, 70, 91, 62, 75, 86, 55],
        }
    )


def sample_houses():
    rng = np.random.default_rng(42)
    area = rng.integers(700, 3500, 80)
    bedrooms = rng.integers(1, 6, 80)
    age = rng.integers(0, 45, 80)
    garage = rng.integers(0, 900, 80)
    price = area * 95 + bedrooms * 18000 - age * 1300 + garage * 55 + rng.normal(0, 18000, 80)
    return pd.DataFrame(
        {
            "LotArea": area,
            "Bedrooms": bedrooms,
            "HouseAge": age,
            "GarageArea": garage,
            "SalePrice": price.round(0).astype(int),
        }
    )


# ---------------------------------------------------------------
# 3. PAGES
# ---------------------------------------------------------------
def dashboard_page():
    page_title("Dashboard", "A summary of everything saved in this workspace.")

    students = load_data(STUDENT_FILE, STUDENT_COLUMNS)
    todos = load_data(TODO_FILE, TODO_COLUMNS)
    marks = load_data(MARKS_FILE, MARKS_COLUMNS)

    total_students = len(students)
    average_attendance = students["Attendance"].mean() if total_students > 0 else 0
    pending_tasks = len(todos[todos["Status"] == "Pending"])
    results_made = len(marks)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Students", total_students)
    c2.metric("Average attendance", f"{average_attendance:.1f}%")
    c3.metric("Pending tasks", pending_tasks)
    c4.metric("Results generated", results_made)

    left, right = st.columns(2)

    with left:
        st.subheader("Students by status")
        if total_students > 0:
            st.bar_chart(students["Status"].value_counts())
        else:
            st.info("No students yet. Add some in Student Management.")

    with right:
        st.subheader("Latest results")
        if results_made > 0:
            st.dataframe(marks.tail(5), use_container_width=True, hide_index=True)
        else:
            st.info("No results yet. Create one in Student Marks.")

    st.subheader("Modules")
    modules = pd.DataFrame(
        {
            "Module": list(PAGES.keys())[1:],
            "What it does": [
                "Enter marks, get total, percentage, grade and result",
                "Clean a student dataset and find top performers",
                "Train a model that predicts house prices",
                "Detect faces from the webcam and mark attendance",
                "Keep a list of tasks with priority and status",
                "Add, subtract, multiply and divide numbers",
                "Add and manage student records with attendance",
            ],
        }
    )
    st.dataframe(modules, use_container_width=True, hide_index=True)


def marks_page():
    page_title("Student Marks", "Enter marks to calculate total, percentage, grade and result.")

    subjects = ["Python", "Data Science", "Machine Learning", "Math", "English"]

    with st.form("marks_form"):
        col1, col2, col3 = st.columns(3)
        name = col1.text_input("Student name")
        roll_no = col2.text_input("Roll number")
        course = col3.text_input("Course", "BCA")

        st.write("Marks out of 100")
        marks = {}
        columns = st.columns(len(subjects))
        for i in range(len(subjects)):
            marks[subjects[i]] = columns[i].number_input(subjects[i], 0, 100, 60)

        submitted = st.form_submit_button("Generate result")

    if submitted:
        if name.strip() == "" or roll_no.strip() == "":
            st.error("Please enter the student name and roll number.")
        else:
            total = sum(marks.values())
            percentage = total / (len(subjects) * 100) * 100
            grade = get_grade(percentage)
            result = "Fail" if grade == "Fail" else "Pass"

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total", f"{total}/{len(subjects) * 100}")
            m2.metric("Percentage", f"{percentage:.2f}%")
            m3.metric("Grade", grade)
            m4.metric("Result", result)

            new_row = pd.DataFrame(
                [[roll_no, name, course, total, round(percentage, 2), grade, result,
                  datetime.now().strftime("%Y-%m-%d %H:%M")]],
                columns=MARKS_COLUMNS,
            )
            history = pd.concat([load_data(MARKS_FILE, MARKS_COLUMNS), new_row], ignore_index=True)
            save_data(history, MARKS_FILE)
            st.success("Result saved.")

    st.subheader("Saved results")
    history = load_data(MARKS_FILE, MARKS_COLUMNS)
    if len(history) > 0:
        st.dataframe(history, use_container_width=True, hide_index=True)
        st.download_button("Download results (CSV)", history.to_csv(index=False), "marks_report.csv")
    else:
        st.info("Nothing saved yet.")


def performance_page():
    page_title("Performance Analysis", "Load a dataset, clean it, and find the top performers.")

    uploaded = st.file_uploader("Upload a student CSV (optional)", type=["csv"])
    if uploaded:
        data = pd.read_csv(uploaded)
    else:
        data = sample_students()
        st.info("No file uploaded, so a sample dataset is shown.")

    st.subheader("Raw data")
    st.dataframe(data, use_container_width=True, hide_index=True)

    # Cleaning: remove duplicates and fill empty numbers with the column average
    clean = data.drop_duplicates()
    number_columns = clean.select_dtypes(include=np.number).columns
    clean[number_columns] = clean[number_columns].fillna(clean[number_columns].mean())

    subject_columns = [c for c in clean.columns if c.lower() in ["math", "english", "hindi", "science"]]
    if len(subject_columns) == 0 or "name" not in clean.columns:
        st.warning("The CSV needs a 'name' column and at least one of: math, english, hindi, science.")
        return

    clean["average_score"] = clean[subject_columns].mean(axis=1).round(2)
    clean["level"] = np.where(clean["average_score"] >= 75, "Top performer", "Needs practice")

    st.subheader("Cleaned data")
    st.dataframe(clean, use_container_width=True, hide_index=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Class average", f"{clean['average_score'].mean():.2f}")
    c2.metric("Highest average", f"{clean['average_score'].max():.2f}")
    c3.metric("Top performers", int((clean["level"] == "Top performer").sum()))

    left, right = st.columns(2)
    with left:
        st.subheader("Average score by student")
        st.bar_chart(clean.set_index("name")["average_score"])
    with right:
        st.subheader("Top 5 students")
        top5 = clean.sort_values("average_score", ascending=False).head(5)
        st.dataframe(top5[["name", "average_score", "level"]], use_container_width=True, hide_index=True)

    st.download_button("Download report (CSV)", clean.to_csv(index=False), "performance_report.csv")


def house_page():
    page_title("House Price Prediction", "A Linear Regression model that predicts price from house details.")

    uploaded = st.file_uploader("Upload a house CSV (optional)", type=["csv"])
    if uploaded:
        data = pd.read_csv(uploaded)
    else:
        data = sample_houses()
        st.info("No file uploaded, so a generated sample dataset is used.")

    needed = ["LotArea", "Bedrooms", "HouseAge", "GarageArea", "SalePrice"]
    missing = [c for c in needed if c not in data.columns]
    if missing:
        st.warning(f"The CSV is missing these columns: {missing}")
        return

    st.dataframe(data.head(10), use_container_width=True, hide_index=True)

    # Preprocessing
    data = data[needed].drop_duplicates()
    data = data.fillna(data.mean())

    x = data[["LotArea", "Bedrooms", "HouseAge", "GarageArea"]]
    y = data["SalePrice"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)
    predicted = model.predict(x_test)

    c1, c2, c3 = st.columns(3)
    c1.metric("MAE (average error)", f"{mean_absolute_error(y_test, predicted):,.0f}")
    c2.metric("MSE", f"{mean_squared_error(y_test, predicted):,.0f}")
    c3.metric("R2 score", f"{r2_score(y_test, predicted):.2f}")

    st.subheader("Predict a new house")
    p1, p2, p3, p4 = st.columns(4)
    lot_area = p1.number_input("Lot area", value=1800)
    bedrooms = p2.number_input("Bedrooms", value=3)
    house_age = p3.number_input("House age", value=10)
    garage_area = p4.number_input("Garage area", value=350)

    new_house = pd.DataFrame(
        [[lot_area, bedrooms, house_age, garage_area]], columns=x.columns
    )
    price = model.predict(new_house)[0]
    st.success(f"Predicted price: Rs. {price:,.0f}")

    st.subheader("Actual vs predicted price")
    chart_data = pd.DataFrame({"Actual": y_test.values, "Predicted": predicted})
    st.scatter_chart(chart_data, x="Actual", y="Predicted")


def face_page():
    page_title("Face Recognition", "Take a photo, detect faces with OpenCV, and mark attendance.")

    try:
        import cv2
        from PIL import Image
    except ImportError:
        st.error("OpenCV is not installed. Run: pip install opencv-python pillow")
        return

    name = st.text_input("Registered user name", "Rahul")
    photo = st.camera_input("Take a photo")

    if photo:
        image = np.array(Image.open(photo).convert("RGB"))
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (88, 125, 95), 3)

        st.image(image, caption=f"Faces found: {len(faces)}", use_container_width=True)

        if len(faces) > 0:
            record = pd.DataFrame(
                [[name, "Present", len(faces), datetime.now().strftime("%Y-%m-%d %H:%M:%S")]],
                columns=["Name", "Status", "Faces", "Time"],
            )
            st.success(f"Attendance marked for {name}.")
            st.dataframe(record, use_container_width=True, hide_index=True)
            st.download_button("Download attendance (CSV)", record.to_csv(index=False), "face_attendance.csv")
        else:
            st.warning("No face found. Try again with better light, facing the camera.")


def todo_page():
    page_title("Task List", "Add tasks, set priority, and mark them done.")

    with st.form("todo_form", clear_on_submit=True):
        c1, c2 = st.columns([3, 1])
        task = c1.text_input("Task")
        priority = c2.selectbox("Priority", ["Low", "Medium", "High"])
        add = st.form_submit_button("Add task")

    todos = load_data(TODO_FILE, TODO_COLUMNS)

    if add and task.strip() != "":
        new_row = pd.DataFrame([[task.strip(), priority, "Pending"]], columns=TODO_COLUMNS)
        todos = pd.concat([todos, new_row], ignore_index=True)
        save_data(todos, TODO_FILE)

    if len(todos) == 0:
        st.info("No tasks yet. Add your first task above.")
        return

    st.dataframe(todos, use_container_width=True, hide_index=True)

    pending = todos[todos["Status"] == "Pending"]["Task"].tolist()
    c1, c2 = st.columns([3, 1])
    chosen = c1.selectbox("Pick a pending task", pending) if pending else None

    if chosen and c2.button("Mark done"):
        todos.loc[todos["Task"] == chosen, "Status"] = "Done"
        save_data(todos, TODO_FILE)
        st.rerun()

    if st.button("Clear completed tasks"):
        save_data(todos[todos["Status"] != "Done"], TODO_FILE)
        st.rerun()
def calculator_page():
    page_title("Calculator", "Simple arithmetic with two numbers.")
    c1, c2, c3 = st.columns(3)
    first = c1.number_input("First number", value=10.0)
    operation = c2.selectbox("Operation", ["+", "-", "*", "/", "%", "**"])
    second = c3.number_input("Second number", value=5.0)

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "**":
        result = first ** second
    elif second == 0:
        result = "Cannot divide by zero"
    elif operation == "/":
        result = first / second
    else:
        result = first % second

    st.metric("Result", result)


def student_page():
    page_title("Student Management", "Add student records, track attendance, and download a report.")

    students = load_data(STUDENT_FILE, STUDENT_COLUMNS)

    with st.form("student_form", clear_on_submit=True):
        c1, c2, c3 = st.columns(3)
        roll = c1.text_input("Roll no")
        name = c2.text_input("Name")
        course = c3.text_input("Course", "BCA")
        attendance = st.slider("Attendance %", 0, 100, 75)
        status = st.selectbox("Status", ["Active", "Inactive", "Completed"])
        add = st.form_submit_button("Add student")

    if add:
        if roll.strip() == "" or name.strip() == "":
            st.error("Roll no and name are required.")
        elif roll.strip() in students["Roll No"].astype(str).values:
            st.error("That roll number already exists.")
        else:
            new_row = pd.DataFrame([[roll.strip(), name.strip(), course, attendance, status]],
                                   columns=STUDENT_COLUMNS)
            students = pd.concat([students, new_row], ignore_index=True)
            save_data(students, STUDENT_FILE)
            st.success("Student added.")

    if len(students) == 0:
        st.info("No students yet. Add the first record above.")
        return

    c1, c2, c3 = st.columns(3)
    c1.metric("Total students", len(students))
    c2.metric("Average attendance", f"{students['Attendance'].mean():.1f}%")
    c3.metric("Active students", int((students["Status"] == "Active").sum()))

    st.dataframe(students, use_container_width=True, hide_index=True)

    c1, c2 = st.columns([3, 1])
    remove = c1.selectbox("Remove a student by roll no", students["Roll No"].tolist())
    if c2.button("Remove"):
        students = students[students["Roll No"] != remove]
        save_data(students, STUDENT_FILE)
        st.rerun()

    st.download_button("Download report (CSV)", students.to_csv(index=False), "student_report.csv")


# ---------------------------------------------------------------
# 4. NAVIGATION (page name -> function)
# ---------------------------------------------------------------
PAGES = {
    "Dashboard": dashboard_page,
    "Student Marks": marks_page,
    "Performance Analysis": performance_page,
    "House Price Prediction": house_page,
    "Face Recognition": face_page,
    "Task List": todo_page,
    "Calculator": calculator_page,
    "Student Management": student_page,
}

st.sidebar.markdown(
    '<div class="brand"><span class="logo">🎓</span><b>PROJECT</b></div>',
    unsafe_allow_html=True,
)
choice = st.sidebar.radio(
    "Go to",
    list(PAGES.keys()),
    format_func=lambda name: ICONS[name] + "  " + name,
    label_visibility="collapsed",
)

with st.sidebar.expander("How to use"):
    st.markdown(
        "- Pick a page from the menu\n"
        "- Add your data in the form\n"
        "- Records are saved in the data folder\n"
        "- Download reports as CSV"
    )

st.markdown(
    f'<div class="topbar"><div class="left"><span class="logo">🎓</span><b>PROJECT</b></div>'
    f'<span class="date">{datetime.now().strftime("%A, %d %B %Y")}</span></div>',
    unsafe_allow_html=True,
)

PAGES[choice]()
