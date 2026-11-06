# 🎓 Python Office Hub

A BCA project that brings **7 small Python projects** together in one clean, animated dashboard built with **Streamlit**. It has a light/dark theme, a dotted background, a sidebar menu, and saves your data in simple CSV files.

---

## ✨ Features

| Module | What it does |
|--------|--------------|
| 🏠 **Dashboard** | Summary of everything saved: student count, average attendance, pending tasks, results generated, and charts |
| 📝 **Student Marks** | Enter marks for 5 subjects and get total, percentage, grade and Pass/Fail result. Results are saved and can be downloaded as CSV |
| 📊 **Performance Analysis** | Upload a student CSV (or use sample data), clean it (remove duplicates, fill missing values), and find top performers |
| 🏡 **House Price Prediction** | Linear Regression model that predicts house price from lot area, bedrooms, house age and garage area. Shows MAE, MSE and R² score |
| 📷 **Face Recognition** | Take a photo with the webcam, detect faces using OpenCV (Haar Cascade), and mark attendance |
| ✅ **Task List** | Add tasks with priority (Low / Medium / High), mark them done, and clear completed tasks |
| 🧮 **Calculator** | Simple arithmetic: `+ - * / % **` with divide-by-zero handling |
| 🎓 **Student Management** | Add or remove student records, track attendance, and download a report |

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit**: web interface
- **Pandas / NumPy**: data handling
- **scikit-learn**: Linear Regression and evaluation metrics
- **OpenCV + Pillow**: face detection

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**

   ```bash
   pip install streamlit pandas numpy scikit-learn opencv-python pillow
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

   The app opens in your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
.
├── app.py              # Complete application (UI + all 7 modules)
├── data/               # Created automatically on first run
│   ├── students.csv    # Student Management records
│   ├── todos.csv       # Task List data
│   └── marks.csv       # Saved Student Marks results
└── README.md
```

---

## 📖 How to Use (Step by Step)

### General steps

1. Run `streamlit run app.py` and open the app in your browser.
2. Pick a page from the sidebar menu.
3. Fill in the form or upload a CSV file.
4. Your records are saved automatically in the `data/` folder.
5. Use the download buttons to export reports as CSV.

### 📝 Student Marks

1. Open **Student Marks** from the sidebar.
2. Enter the student name, roll number and course.
3. Enter marks (out of 100) for Python, Data Science, Machine Learning, Math and English.
4. Click **Generate result**.
5. See the total, percentage, grade and Pass/Fail result.
6. Scroll down to view all saved results, or click **Download results (CSV)**.

### 📊 Performance Analysis

1. Open **Performance Analysis**.
2. Upload a student CSV file, or skip this step to use the sample data.
3. Check the raw data, then the cleaned data (duplicates removed, missing values filled with the column average).
4. View the class average, highest average and number of top performers (average of 75 or more).
5. See the bar chart and the Top 5 students table.
6. Click **Download report (CSV)** to save the result.

### 🏡 House Price Prediction

1. Open **House Price Prediction**.
2. Upload a house CSV, or skip this step to use generated sample data.
3. Check the model accuracy: MAE, MSE and R² score.
4. In **Predict a new house**, enter the lot area, bedrooms, house age and garage area.
5. The predicted price appears instantly.
6. Compare actual and predicted prices in the scatter chart.

### 📷 Face Recognition

1. Open **Face Recognition**.
2. Type the registered user name.
3. Allow camera access in your browser and click **Take a photo**.
4. The app draws a box around each detected face.
5. If a face is found, attendance is marked and you can click **Download attendance (CSV)**.
6. If no face is found, try again with better light, facing the camera.

### ✅ Task List

1. Open **Task List**.
2. Type a task, choose the priority (Low / Medium / High) and click **Add task**.
3. To finish a task, pick it from the pending list and click **Mark done**.
4. Click **Clear completed tasks** to remove all finished tasks.

### 🧮 Calculator

1. Open **Calculator**.
2. Enter the first number and the second number.
3. Choose an operation: `+`, `-`, `*`, `/`, `%` or `**`.
4. The result is shown immediately.

### 🎓 Student Management

1. Open **Student Management**.
2. Enter the roll number, name and course.
3. Set the attendance with the slider and choose the status (Active / Inactive / Completed).
4. Click **Add student**. Duplicate roll numbers are not allowed.
5. View the totals and the student table.
6. To delete a record, pick the roll number and click **Remove**.
7. Click **Download report (CSV)** to export all students.

### 🏠 Dashboard

1. Open **Dashboard** to see a summary of all saved data.
2. It shows total students, average attendance, pending tasks and results generated.
3. It also shows a chart of students by status and the latest 5 results.

### CSV formats for uploads

**Performance Analysis**: needs a `name` column and at least one of `math`, `english`, `hindi`, `science`.

**House Price Prediction**: needs these columns:

```
LotArea, Bedrooms, HouseAge, GarageArea, SalePrice
```

If you do not upload a file, both pages use built-in sample data so you can try them right away.

---

## 📊 Grading Scale (Student Marks)

| Percentage | Grade |
|-----------|-------|
| 90 and above | A+ |
| 80 – 89 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| 50 – 59 | D |
| Below 50 | Fail |

---

## ⚠️ Notes

- The **Face Recognition** page currently **detects** faces and marks attendance for the name you type. It does not identify *who* the person is.
- The webcam page needs camera permission in your browser.
- The house price model is trained on generated sample data unless you upload your own CSV.

---

## 🚀 Future Improvements

- Real face recognition (matching faces to registered users)
- Login system for students and teachers
- Database support (SQLite) instead of CSV files
- More charts and analytics

---

## 👨‍💻 Author

**<Your Name>**
BCA Student
GitHub: [@your-username](https://github.com/your-username)

---

## 📄 License

This project is made for educational purposes. You can add a license of your choice (for example, MIT).
