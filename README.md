# Iris Flower Species Prediction Using Machine Learning

## Overview

This project is a machine learning–based web application that predicts the species of an Iris flower using its physical measurements. The system classifies the flower into one of three species: **Setosa, Versicolor, or Virginica** based on four input features — sepal length, sepal width, petal length, and petal width.

The application uses a pre-trained machine learning model stored in a pickle file. Users provide the flower measurements through a simple web interface, and the model processes the inputs to predict the corresponding Iris species.

The project demonstrates how a trained machine learning model can be deployed as a web application, allowing users to interact with the model and obtain predictions in real time.

## Features

* Predict Iris flower species using machine learning
* Interactive web interface for entering flower measurements
* Pre-trained model for fast predictions
* Real-time prediction results
* Simple and user-friendly UI

## Technologies Used

* Python
* Streamlit
* NumPy
* Scikit-learn
* Pickle

## Project Structure

```
iris-flower-prediction
│
├── app.py
├── iris.pkl
└── README.md
```

## Installation

### Clone the Repository

```
git clone https://github.com/your-username/iris-flower-prediction.git
cd iris-flower-prediction
```

### Install Required Libraries

```
pip install streamlit numpy scikit-learn
```

### Run the Application

```
streamlit run app.py
```

## How It Works

1. The user enters flower measurements.
2. The application converts the inputs into a numerical format.
3. The trained machine learning model processes the input data.
4. The system predicts the Iris flower species.
5. The predicted result is displayed on the web interface.

## Example Input

* Sepal Length: 5.1
* Sepal Width: 3.5
* Petal Length: 1.4
* Petal Width: 0.2

Predicted Output: **Setosa**

## Author

Akshay
