import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ============================
# Load Dataset
# ============================

df = pd.read_csv("raw_skills.csv", encoding="cp1252")
print(df.columns.tolist())

# Keep only useful columns
df = df[["Job Title", "Job Description", "Skills", "Certifications"]]

# Remove missing values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# ============================
# TF-IDF Vectorizer
# ============================

vectorizer = TfidfVectorizer(stop_words="english")

# Convert all job skills into vectors
tfidf_matrix = vectorizer.fit_transform(df["Skills"])

# ============================
# Recommendation Function
# ============================

def recommend_jobs(user_skills, top_n=5):
    """
    Recommends top matching IT jobs based on user skills.

    Parameters:
        user_skills (str): Comma separated skills
        top_n (int): Number of recommendations

    Returns:
        DataFrame
    """

    # Convert user skills into vector
    user_vector = vectorizer.transform([user_skills])

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    ).flatten()

    # Copy dataframe
    recommendations = df.copy()

    # Add similarity score
    recommendations["Match Score"] = similarity_scores

    # Sort descending
    recommendations = recommendations.sort_values(
        by="Match Score",
        ascending=False
    )

    # Remove duplicate job titles
    recommendations = recommendations.drop_duplicates(
        subset="Job Title"
    )
    print(recommendations.columns.tolist())

    # Return Top N
    print("Returning columns:", recommendations.columns.tolist())
    return recommendations.head(top_n)


# ============================
# Test (Runs only if executed directly)
# ============================

if __name__ == "__main__":

    print("=" * 70)
    print("AI TECH STACK RECOMMENDATION SYSTEM")
    print("=" * 70)

    skills = input("\nEnter your skills (comma separated): ")

    results = recommend_jobs(skills)

    print("\nTop Job Recommendations\n")

    for _, row in results.iterrows():

        print("=" * 80)

        print("Job Title:")
        print(row["Job Title"])

        print(f"\nMatch Score: {row['Match Score']*100:.2f}%")

        print("\nRequired Skills:")
        print(row["Skills"])

        print("\nRecommended Certifications:")
        print(row["Certifications"])

        print("=" * 80)