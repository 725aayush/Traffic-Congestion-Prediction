# 🚦 Traffic Congestion Prediction System

A Machine Learning-powered web application that predicts vehicle traffic congestion based on input parameters like **junction**, **date**, and **time**. The system uses a trained **Random Forest Regressor** and provides graphical output, downloadable JSON reports, and interactive mapping using **Leaflet.js**.

---

## 📌 Key Features

- 🔢 **Predict traffic (vehicle count)** for a specific junction and date-time
- 📈 **Graphical view** of results using Chart.js / Matplotlib
- 🗺️ **Interactive map** of traffic junctions via Leaflet.js
- 📜 **History table** of recent predictions
- 🧾 **Downloadable JSON report**
- 🖥️ Responsive and modern **Bootstrap-powered UI**

---

## 📁 Project Structure


---

## 🧠 Technologies Used

| Layer        | Tools/Frameworks                                      |
|--------------|--------------------------------------------------------|
| Backend      | Python, Flask                                          |
| Machine Learning | scikit-learn (Random Forest Regressor)           |
| Frontend     | HTML, CSS, JavaScript, Bootstrap                      |
| Visualization| Chart.js, Matplotlib, Leaflet.js                      |
| Data Format  | JSON (for report downloads)                           |
| Optional DB  | SQLite (for persistent history - optional)            |

---

## ⚙️ Installation & Running Locally

Follow the steps below to get the app running on your local system:

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/725aayush/Traffic-Congestion-Prediction.git
cd Traffic-Congestion-Prediction
