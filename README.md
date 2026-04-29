# Song-Popularity-Predictor
A full-stack Python project that predicts song popularity using tempo, energy, and danceability with Flask backend and Streamlit dashboard.
# 🎵 Song Popularity Prediction System

## 📌 Overview

This project predicts the popularity of a song based on its audio features such as **Tempo, Energy, and Danceability**.
It is a full-stack application built using a Python backend and an interactive frontend dashboard.

---

## 🚀 Features

* 🎯 Predict song popularity (Hit / Average / Low)
* 📊 Real-time popularity score (0–1)
* 📈 Interactive graphs (Feature Contribution & Trend)
* 🎛 User-friendly dashboard using Streamlit
* 🔗 Backend API integration using Flask

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Flask
* **Visualization:** Plotly
* **Data Handling:** Pandas
* **Language:** Python

---

## 🧠 Model Description

The prediction is based on a simple feature-weighted formula:

Score = (0.3 × Tempo/200) + (0.4 × Energy) + (0.3 × Danceability)

###  Output Categories:

* 🔥 Hit Song → Score > 0.6
* 👍 Average Song → 0.4 – 0.6
* 👎 Low Popularity → Score < 0.4

---

## ⚙️ Project Structure

```
Song-Popularity-Predictor/
│── app.py
│── model.py
│── frontend.py
│── requirements.txt
│── README.md
│── song prediction dataset.csv
│── OUTPUT
```

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️ Run Backend (Flask)

```
python app.py
```

###  Run Frontend (Streamlit)

```
streamlit run frontend.py
```

---



## System Workflow

1. User inputs song features (Tempo, Energy, Danceability)
2. Streamlit sends data to Flask API
3. Flask processes data using model logic
4. Prediction + score returned to frontend
5. Results displayed with graphs

---

##  Output Example

* Prediction: 👍 Average Song
* Score: 0.52

---

##  Future Scope

* Use real Spotify dataset
* Train ML model (Linear Regression / Random Forest)
* Add more audio features
* Deploy application online

---

##  Author

Ayush Yogesh Rathod

---

## Internship

Naviotech Solution Pvt. Ltd

---
