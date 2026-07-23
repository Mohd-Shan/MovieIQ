import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import os

# ---------------- Load Dataset ----------------

df = pd.read_csv("movies.csv")

# Success Column
df["success"] = (df["revenue"] > df["budget"]).astype(int)

# ---------------- Title ----------------

st.title("🎬 MovieIQ Dashboard")
st.write("Predict Movie Success using Machine Learning")

# ---------------- Sidebar Filters ----------------

genre = st.sidebar.selectbox(
    "Select Genre",
    sorted(df["genres"].dropna().unique())
)

vote = st.sidebar.slider(
    "Minimum Vote Average",
    0.0,
    10.0,
    5.0
)

# ---------------- Filter Dataset ----------------

filtered_df = df[
    (df["genres"] == genre) &
    (df["vote_average"] >= vote)
]

st.subheader("Filtered Dataset")

st.dataframe(filtered_df)

# ---------------- Scatter Plot ----------------

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    data=filtered_df,
    x="budget",
    y="revenue",
    ax=ax
)

ax.set_title("Budget vs Revenue")

st.pyplot(fig)

# ---------------- Count Plot ----------------

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    data=filtered_df,
    x="success",
    ax=ax
)

ax.set_title("Movie Success")

st.pyplot(fig)

# ---------------- Heatmap ----------------

fig, ax = plt.subplots(figsize=(8,6))

sns.heatmap(
    filtered_df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

ax.set_title("Correlation Heatmap")

st.pyplot(fig)

# ---------------- Model ----------------

st.subheader("Movie Success Prediction")

# Load trained model
if os.path.exists("model.pkl"):

    model = joblib.load("model.pkl")

    budget = st.number_input("Budget", min_value=0.0)

    popularity = st.number_input("Popularity", min_value=0.0)

    runtime = st.number_input("Runtime", min_value=0.0)

    vote_average = st.number_input(
        "Vote Average",
        min_value=0.0,
        max_value=10.0
    )

    if st.button("Predict"):

        prediction = model.predict([[
            budget,
            popularity,
            runtime,
            vote_average
        ]])

        if prediction[0] == 1:
            st.success("✅ Movie will be Successful")
        else:
            st.error("❌ Movie may not be Successful")

else:
    st.warning("model.pkl not found. Please train your model first.")