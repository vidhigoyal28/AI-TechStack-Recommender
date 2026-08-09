#  AI Tech Stack Recommendation System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Scikit--Learn-TF--IDF-orange?style=for-the-badge&logo=scikit-learn">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

##  Overview

The **AI Tech Stack Recommendation System** is an AI-powered web application that recommends the most suitable IT job roles based on a user's technical skills.

The application uses **TF-IDF Vectorization** and **Cosine Similarity** to compare user-entered skills with real-world IT job skill requirements and recommends the best matching career opportunities.

It also performs **Skill Gap Analysis**, suggesting which skills the user already possesses and which skills should be learned to qualify for the recommended role.

---

# Features

 AI-Based Job Recommendation

 TF-IDF Vectorization

 Cosine Similarity Matching

 Skill Gap Analysis

 Interactive Dashboard

 Match Score Visualization

 Recommended Certifications

 CSV Download

 Responsive Streamlit UI

---



#  How It Works

### Step 1

The user selects their technical skills.

Example:

```
Python
Machine Learning
TensorFlow
SQL
```

↓

### Step 2

The application converts both:

- User Skills
- Job Skills

into numerical vectors using **TF-IDF Vectorization**.

↓

### Step 3

Cosine Similarity is calculated between user skills and every job profile.

↓

### Step 4

Jobs are ranked according to similarity score.

↓

### Step 5

Top matching jobs are displayed with

- Match Score
- Required Skills
- Missing Skills
- Recommended Certifications

---

#  Recommendation Workflow

```
User Skills
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Job Ranking
      │
      ▼
Top Recommendations
      │
      ▼
Skill Gap Analysis
```

---

#  Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-Learn
- Plotly
- Streamlit

### Machine Learning

- TF-IDF Vectorizer
- Cosine Similarity

### IDE

- Visual Studio Code

### Version Control

- Git
- GitHub

---

#  Project Structure

```
AI-TechStack-Recommender/
│
├── app.py
├── recommender.py
├── utils.py
├── style.css
├── raw_skills.csv
├── requirements.txt
├── README.md
├── assets/
└── screenshots/
```

---

#  Dataset

Dataset Source:

**IT Job Roles Skills Dataset**

The dataset contains:

- Job Titles
- Skills
- Certifications

The recommendation engine compares user skills against these job profiles.

---

#  Installation

Clone the repository

```bash
git clone https://github.com/vidhigoyal28/AI-TechStack-Recommender.git
```

Go to project folder

```bash
cd AI-TechStack-Recommender
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Application

```bash
streamlit run app.py
```

---

#  Sample Output

Example Input

```
Python
Machine Learning
TensorFlow
SQL
```

Example Recommendation

```
Machine Learning Engineer

Match Score
71%

Required Skills

Python
TensorFlow
Docker

Recommended Certifications

TensorFlow Developer Certificate
AWS Certified Machine Learning Specialty
```

---

#  Future Improvements

- Company Recommendations
- Salary Prediction
- Resume Analysis
- Learning Roadmap
- Course Recommendations
- Job Market Trend Analysis
- AI Chat Assistant
- Resume Matching
- Multi-language Support

---

#  Learning Outcomes

This project helped in understanding:

- Recommendation Systems
- Natural Language Processing
- TF-IDF Vectorization
- Cosine Similarity
- Feature Engineering
- Data Preprocessing
- Interactive Dashboard Development
- Streamlit Web Applications
- Machine Learning Deployment

---



#  Author

**Vidhi Goyal**

Computer Science Engineering Student

KIET Group of Institutions

GitHub:

https://github.com/vidhigoyal28

---

