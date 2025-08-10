
# 📊 IT Audit Evaluation System

An interactive **Streamlit** dashboard to evaluate IT processes using weighted audit criteria.
It loads evaluation questions and their weights from an Excel file, collects auditor scores, calculates a weighted composite score (CGPA), and assigns a final grade.

---

## 🚀 Features

* **Weighted Evaluation** – Each question has a specific weight for fair scoring.
* **Multiple Auditors** – Supports scoring from multiple evaluators.
* **Interactive Inputs** – Enter scores (0–4) for each question via an intuitive UI.
* **Automated Calculations** – Computes weighted scores, total score, CGPA, and grade.
* **Grading Scale** – Converts CGPA into grades from `A++` to `D`.

---

## 📂 Project Structure

```
project/
│-- sample_weights.xlsx    # Example evaluation questions & weights
│-- app.py                 # Streamlit app code
│-- README.md              # Project documentation
```

---

## 🛠️ Steps to Run

### 1️⃣ Install Dependencies

```bash
pip install streamlit pandas openpyxl
```

### 2️⃣ Prepare Your Excel File

* Must contain two columns:

  * **Question** – The evaluation question text.
  * **Weightage** – Numerical weight assigned to the question.
* Example file: `sample_weights.xlsx`

### 3️⃣ Run the App

```bash
streamlit run app.py
```

### 4️⃣ Use the Dashboard

* Upload your `.xlsx` file.
* Enter the number of auditors.
* Input scores for each question.
* Click **Calculate Evaluation Results** to view:

  * Weighted score per question
  * Total weighted score
  * CGPA
  * Final Grade

---

## 📌 Data Format

The Excel file should have:

| Question                                | Weightage |
| --------------------------------------- | --------- |
| Is the backup process documented?       | 2         |
| Are system logs regularly reviewed?     | 3         |
| Is multi-factor authentication enabled? | 4         |

---

## 🌐 Live App

https://audit-evaluation-system.streamlit.app/
