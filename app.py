from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("india_job_market_dataset.csv")
df.fillna({"Skills Required": ""}, inplace=True)

# Ensure text consistency
df["Job Location"] = df["Job Location"].astype(str).str.strip().str.lower()
df["Job Type"] = df["Job Type"].astype(str).str.strip().str.lower()

# Apply TF-IDF Vectorization on skills
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df["Skills Required"])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Flask app
app = Flask(__name__)

# ✅ Function for recommending jobs
def recommend_jobs_for_user(user_skills, preferred_location="", preferred_job_type="", top_n=5):
    user_skills_tfidf = tfidf.transform([user_skills])
    user_similarity_scores = cosine_similarity(user_skills_tfidf, tfidf_matrix).flatten()

    filtered_df = df.copy()
    filtered_df["Similarity_Score"] = user_similarity_scores

    # Apply location filter
    if preferred_location:
        preferred_location = preferred_location.strip().lower()
        filtered_df = filtered_df[filtered_df["Job Location"].str.contains(preferred_location, na=False)]

    # Apply job type filter
    if preferred_job_type:
        preferred_job_type = preferred_job_type.strip().lower()
        filtered_df = filtered_df[filtered_df["Job Type"].str.contains(preferred_job_type, na=False)]

    # Sort and return top recommendations
    recommended_jobs = filtered_df.sort_values(by="Similarity_Score", ascending=False).head(top_n)
    
    return recommended_jobs[["Job Title", "Company Name", "Job Location", "Skills Required", "Job Type"]]

# ✅ API Route for Job Recommendations
@app.route("/recommend", methods=["POST"])
def recommend_jobs():
    data = request.json
    user_skills = data.get("skills", "")
    preferred_location = data.get("location", "")
    preferred_job_type = data.get("job_type", "")

    recommended_jobs = recommend_jobs_for_user(user_skills, preferred_location, preferred_job_type)
    return jsonify(recommended_jobs.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(port=5000)