import streamlit as st
import requests

st.title("🔍 Job Recommendation System")

# Get user inputs
user_skills = st.text_area("Enter your skills (comma-separated)", "")
preferred_location = st.text_input("Enter preferred job location (optional)")
preferred_job_type = st.selectbox("Select job type (optional)", ["", "full-time", "part-time", "remote", "internship","contract"])

if st.button("Get Job Recommendations"):
    if user_skills:
        API_URL = "https://54b2-34-19-119-8.ngrok-free.app/recommend"  # Update this with your actual ngrok URL

        response = requests.post(API_URL, json={
            "skills": user_skills,
            "location": preferred_location,
            "job_type": preferred_job_type
        })

        if response.status_code == 200:
            job_recommendations = response.json()
            if job_recommendations:
                st.write("### Recommended Jobs:")
                for job in job_recommendations:
                    st.write(f"**{job['Job Title']}** at {job['Company Name']} ({job['Job Location']})")
                    st.write(f"*Required Skills:* {job['Skills Required']}")
                    st.write(f"📌 Job Type: {job.get('Job Type', 'Not Specified')}")
                    st.write("---")
            else:
                st.warning("No matching jobs found.")
        else:
            st.error("Error fetching recommendations. Please try again!")
    else:
        st.warning("Please enter at least one skill!")