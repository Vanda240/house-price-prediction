# House Price Prediction

## Project Overview
This project predicts house prices using machine learning based on features such as area, bedrooms, bathrooms, stories, parking, air conditioning, and furnishing status.

The goal of this project is to build a complete end-to-end machine learning pipeline, including:
- data loading
- data preprocessing
- exploratory data analysis
- model training
- model evaluation
- model saving
- Streamlit app deployment

## Problem Statement
The objective is to predict the price of a house using available house features.

This is a regression problem because the target variable `price` is a continuous numeric value.

## Dataset
The dataset contains 545 rows and 13 columns.

### Features
- area
- bedrooms
- bathrooms
- stories
- mainroad
- guestroom
- basement
- hotwaterheating
- airconditioning
- parking
- prefarea
- furnishingstatus

### Target
- price

## Data Preprocessing
The following preprocessing steps were performed:
- checked missing values
- analyzed numeric and categorical columns
- converted yes/no columns into 1/0
- one-hot encoded furnishing status
- split data into training and testing sets

## Exploratory Data Analysis
EDA included:
- summary statistics
- correlation heatmap
- price distribution
- feature relationship analysis

Main findings:
- area showed the strongest correlation with price
- bathrooms also had a strong impact
- stories, parking, and bedrooms had moderate influence

## Models Used
The following models were trained and compared:
- Linear Regression
- Random Forest Regressor
- Tuned Random Forest Regressor

## Model Performance

| Model | MAE | RMSE | R2 |
|------|------:|------:|------:|
| Linear Regression | 970043 | 1324507 | 0.6529 |
| Random Forest | 1022560 | 1401497 | 0.6114 |
| Tuned Random Forest | 1051638 | 1423691 | 0.5990 |

## Best Model
Linear Regression performed best on this dataset with:
- lowest MAE
- lowest RMSE
- highest R2 score

## Feature Importance
Random Forest feature importance showed that the most important features were:
- area
- bathrooms
- airconditioning
- parking
- stories

## Files in Project
- `app.py` - Streamlit application
- `best_house_price_model.pkl` - saved trained model
- `model_features.pkl` - saved feature column list
- `requirements.txt` - dependencies
- `README.md` - project documentation
- `data/raw/Housing.csv` - dataset
- `data/raw/Untitled.ipynb` - notebook file

## How to Run
Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

## Conclusion
This project demonstrates a complete machine learning workflow for predicting house prices.
Among the tested models, Linear Regression performed best for this dataset.
The results show that area and bathrooms are among the strongest predictors of house price.

## Author
Vandana Pathania
