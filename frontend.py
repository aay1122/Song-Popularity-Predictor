import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("🎵 Song Popularity")
    st.success("● Backend connected")

    tempo = st.slider("Tempo (BPM)", 0.0, 200.0, 120.0)
    energy = st.slider("Energy", 0.0, 1.0, 0.5)
    danceability = st.slider("Danceability", 0.0, 1.0, 0.5)

    predict_btn = st.button("⚡ Predict Popularity")

# ---------- HEADER ----------
st.markdown("## 🎵 Song Popularity Prediction")
st.caption("Feature-based Model • Music Analytics")

if predict_btn:

    data = {
        "tempo": tempo,
        "energy": energy,
        "danceability": danceability
    }

    try:
        res = requests.post("http://127.0.0.1:5000/predict", json=data)

        if res.status_code == 200:
            output = res.json()

            score = output["score"]
            prediction = output["prediction"]

            # ---------- TOP CARDS ----------
            c1, c2, c3 = st.columns(3)

            c1.metric("Prediction", prediction)
            c2.metric("Score", score)
            c3.metric("Confidence", f"{round(score*100)}%")

            # ---------- GAUGE ----------
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Popularity Score"},
                gauge={
                    'axis': {'range': [0, 1]},
                    'steps': [
                        {'range': [0, 0.3], 'color': "red"},
                        {'range': [0.3, 0.6], 'color': "orange"},
                        {'range': [0.6, 1], 'color': "green"}
                    ]
                }
            ))

            st.plotly_chart(fig, use_container_width=True)

            # ---------- BAR GRAPH ----------
            st.subheader("Feature Contribution")

            features = ["Tempo", "Energy", "Danceability"]
            values = [tempo/200, energy, danceability]

            fig_bar = go.Figure(go.Bar(
                x=features,
                y=values
            ))

            fig_bar.update_layout(template="plotly_dark")
            st.plotly_chart(fig_bar, use_container_width=True)

            # ---------- LINE GRAPH ----------
            st.subheader("Popularity Trend")

            x_vals = list(range(50, 200, 10))
            y_vals = []

            for t in x_vals:
                y = (0.3 * t/200) + (0.4 * energy) + (0.3 * danceability)
                y_vals.append(y)

            fig_line = go.Figure(go.Scatter(
                x=x_vals,
                y=y_vals,
                mode="lines+markers"
            ))

            fig_line.update_layout(template="plotly_dark")
            st.plotly_chart(fig_line, use_container_width=True)

            # ---------- TABLE ----------
            df = pd.DataFrame({
                "Feature": ["Tempo", "Energy", "Danceability"],
                "Value": [tempo, energy, danceability]
            })

            st.subheader("Input Data")
            st.dataframe(df)

            # ---------- MODEL INFO ----------
            st.subheader("Model Details")
            st.write({
                "Type": "Feature-based model",
                "Formula": "0.3*T + 0.4*E + 0.3*D"
            })

        else:
            st.error("Backend error")

    except:
        st.error("⚠️ Backend not running")