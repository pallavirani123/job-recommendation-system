# job-recommendation-system

📌 Project Overview

The Job Recommendation System is an AI-powered platform that suggests relevant job opportunities based on user preferences, including skills, location, and job type. The system uses TF-IDF & Cosine Similarity for content-based filtering and provides an interactive user interface via a Streamlit web app.

🏗 Features

Personalized Job Recommendations: Matches jobs based on user-provided skills and preferences.

Content-Based Filtering: Utilizes TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity to find the most relevant job listings.

Flask API: Handles job recommendation requests.

Streamlit Web App: Provides an intuitive and interactive UI.

Public Access: Hosted via ngrok for easy sharing and testing.

🛠 Tech Stack

Programming Language: Python

Libraries & Frameworks: Pandas, Scikit-Learn, Flask, Streamlit

Machine Learning Techniques: TF-IDF, Cosine Similarity

Hosting: ngrok

📂 Project Structure

job_recommendation_system/
│── app.py                  # Flask API for job recommendations
│── streamlit_app.py         # Streamlit frontend
│── india_job_market_dataset.csv # Job dataset
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
│── LICENSE                  # MIT License
└── .gitignore               # Git ignore file

🚀 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/pallavirani123/job-recommendation-system.git
cd job-recommendation-system

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Flask API

python app.py

4️⃣ Run the Streamlit Web App

streamlit run streamlit_app.py

5️⃣ Expose the Web App using ngrok (Optional)

ngrok http 8501

🔍 How It Works

The user enters their skills, preferred job location, and job type.

The system retrieves job descriptions from the dataset.

TF-IDF & Cosine Similarity calculate the relevance score for each job.

The top-matching jobs are recommended to the user.

The results are displayed on the Streamlit web app.

📜 License

This project is licensed under the MIT License. See LICENSE for details.

📞 Contact

For any issues or queries, feel free to reach out:

GitHub: pallavirani123

Email: pallaviranivelagala@gmail.com

⭐ Star this repository if you found it helpful! 🚀

