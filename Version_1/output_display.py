import streamlit as st
import matplotlib.pyplot as plt

def display_study_plan(study_plan):
    if "error" in study_plan:
        st.error(study_plan["error"])
        return

    st.header("📅 Your Tailored Study Plan")

    st.markdown(f"**Days Until Exam:** {study_plan['days_remaining']} days")
    st.markdown(f"**Difficulty Level:** {study_plan['difficulty_level']}")
    st.markdown(f"**Daily Study Time:** {study_plan['daily_study_time']} hours")
    st.markdown(f"**Total Preparation Time:** {study_plan['total_prep_time']} hours")
    st.markdown("**Personal Preferences:**")
    st.write(study_plan['personal_preferences'])

    # Progress Tracking Visualization
    st.subheader("Progress Tracking")
    days = list(range(1, study_plan['days_remaining'] + 1))
    study_times = [study_plan['daily_study_time']] * study_plan['days_remaining']

    fig, ax = plt.subplots()
    ax.plot(days, study_times, marker='o')
    ax.set_xlabel('Day')
    ax.set_ylabel('Study Time (hours)')
    ax.set_title('Daily Study Schedule')
    ax.grid(True)

    st.pyplot(fig)
