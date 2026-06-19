import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Student Grade System",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4F46E5;
}

.subtitle {
    text-align: center;
    color: #6B7280;
    margin-bottom: 30px;
}

.grade-card {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
}

.student-card {
    background-color: #F9FAFB;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #4F46E5;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🎓 Student Grade System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Calculate student grades instantly</div>',
    unsafe_allow_html=True
)

# Student Information
st.markdown("### Student Information")

student_name = st.text_input(
    "Enter Student Name",
    placeholder="Type student name here..."
)

marks = st.slider(
    "Select Marks",
    min_value=0,
    max_value=100,
    value=75
)

# Grade Calculation Function
def calculate_grade(marks):
    if marks >= 90:
        return "A", "#22C55E", "Excellent Performance 🌟"
    elif marks >= 80:
        return "B", "#3B82F6", "Very Good 👍"
    elif marks >= 70:
        return "C", "#F59E0B", "Good Work 😊"
    elif marks >= 60:
        return "D", "#EF4444", "Needs Improvement 📚"
    else:
        return "F", "#7F1D1D", "Failed ❌"

# Button
if st.button("Calculate Grade", use_container_width=True):

    if not student_name.strip():
        st.error("Please enter the student name.")
    else:

        grade, color, remark = calculate_grade(marks)

        st.success("Grade calculated successfully!")

        # Student Details Card
        st.markdown(
            f"""
            <div class="student-card">
                <h4>👨‍🎓 Student: {student_name}</h4>
                <h4>📝 Marks: {marks}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Progress Bar
        st.progress(marks / 100)

        # Grade Card
        st.markdown(
            f"""
            <div class="grade-card" style="background-color:{color};">
                Grade: {grade}<br>
                <span style="font-size:18px;">{remark}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
