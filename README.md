# 🎬 MovieIQ Dashboard

MovieIQ Dashboard is an interactive data analytics and machine learning application built with **Streamlit**. It provides insights into movie performance by analyzing factors such as **budget, revenue, popularity, ratings, runtime, and genres**. The dashboard also includes a machine learning model that predicts whether a movie is likely to be successful based on its key features.

## 🚀 Features

* 📊 Interactive Movie Dashboard using Streamlit
* 🎭 Filter movies by Genre and Vote Average
* 💰 Budget vs Revenue Scatter Plot
* 📈 Movie Success Distribution
* 🔥 Correlation Heatmap for Numerical Features
* 🤖 Machine Learning-Based Movie Success Prediction
* 📋 Interactive Data Table with Filtering
* 🎨 Clean and User-Friendly Interface

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Seaborn
* Matplotlib
* Scikit-learn
* Joblib

## 📂 Dataset Features

The dataset includes the following movie attributes:

* Budget
* Revenue
* Popularity
* Runtime
* Vote Average
* Genres
* Title

A new **Success** feature is created based on movie profitability:

* **Success = 1** → Revenue > Budget
* **Success = 0** → Revenue ≤ Budget

## 🤖 Machine Learning

The dashboard uses a trained Scikit-learn classification model to predict movie success using:

* Budget
* Popularity
* Runtime
* Vote Average

## ▶️ Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/MovieIQ-Dashboard.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
python -m streamlit run MovieIQ.py
```

## 📸 Dashboard Preview

Add screenshots of your dashboard here after uploading them to the repository.

## 📌 Future Improvements

* Deploy using Streamlit Community Cloud
* Add advanced ML models for better prediction accuracy
* Include recommendation system
* Build interactive Power BI/Tableau dashboards
* Add movie trend analysis over time

## 👨‍💻 Author

**Mohd Shan**

Aspiring Data Analyst | AI & ML Student | Python | SQL | Machine Learning | Streamlit
