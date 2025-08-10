import streamlit as st
import pandas as pd

def get_grade(cgpa):
    if cgpa >= 3.51:
        return "A++"
    elif cgpa >= 3.26:
        return "A+"
    elif cgpa >= 3.01:
        return "A"
    elif cgpa >= 2.76:
        return "B++"
    elif cgpa >= 2.51:
        return "B+"
    elif cgpa >= 2.01:
        return "B"
    elif cgpa >= 1.51:
        return "C"
    else:
        return "D"

st.title("📊 IT Audit Evaluation System")

uploaded_file = st.file_uploader("📤 Upload Excel file with Evaluation Questions and Weights", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        if 'Question' not in df.columns or 'Weightage' not in df.columns:
            st.error("Error: The Excel file must contain 'Question' and 'Weightage' columns.")
        else:
            questions = df['Question'].tolist()
            weights = df['Weightage'].tolist()

            num_auditors = st.number_input("👥 Enter number of auditors/reviewers", min_value=1, step=1)

            marks = {}
            if num_auditors:
                st.subheader("✍️ Input Scores (0 to 4) for each question")
                for i in range(num_auditors):
                    st.markdown(f"### Evaluator {i+1}")
                    marks[i] = []
                    for q in questions:
                        score = st.number_input(f"{q}", min_value=0.0, max_value=4.0, step=0.1, key=f"{i}_{q}")
                        marks[i].append(score)

            if st.button("✅ Calculate Evaluation Results"):
                df_scores = pd.DataFrame(marks).T
                df_scores.columns = questions
                average_scores = df_scores.mean()

                st.subheader("📈 Weighted Scores per Question")
                final_scores = []
                for q, w in zip(questions, weights):
                    avg = average_scores[q]
                    weighted = avg * w
                    final_scores.append(weighted)
                    st.write(f"{q[:60]}...: {avg:.2f} × {w} = {weighted:.2f}")

                total_weightage = sum(weights)
                total_score = sum(final_scores)
                cgpa = total_score / total_weightage if total_weightage else 0
                grade = get_grade(cgpa)

                st.success(f"🎯 Total Weighted Score: {total_score:.2f}")
                st.info(f"📊 Sum of Weights: {total_weightage:.2f}")
                st.success(f"📉 Final Composite Score (CGPA): {cgpa:.2f}")
                st.balloons()
                st.markdown(f"### 🏆 Final Grade: **{grade}**")

    except Exception as e:
        st.error(f"Error reading file or processing data: {e}")
else:
    st.info("ℹ️ Please upload an Excel file containing evaluation questions and their corresponding weightage.")
