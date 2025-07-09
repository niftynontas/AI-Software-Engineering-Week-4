# AI-Software-Engineering-Week-4
Predictive analytics project using the Breast Cancer Wisconsin dataset to simulate issue priority classification with a Random Forest model. Includes data preprocessing, model training, evaluation metrics, and feature importance visualization.

# Predictive Analytics: Issue Priority Classification

This project uses the Breast Cancer Wisconsin dataset to simulate a predictive analytics model for classifying issue priority (high vs low). We apply a Random Forest classifier to predict priority based on diagnostic features.

## Project Overview

- **Dataset:** Breast Cancer Wisconsin (Diagnostic) dataset from Kaggle  
- **Goal:** Predict issue priority (High = Malignant, Low = Benign)  
- **Approach:**  
  - Data preprocessing and cleaning  
  - Label encoding and train-test split  
  - Model training using Random Forest  
  - Model evaluation with accuracy, classification report, and confusion matrix  
  - Visualization of top important features  

### Prerequisites

Make sure you have the following installed:  
- Python 3.x  
- Jupyter Notebook  
- Required libraries (install via pip):

### Running the Notebook

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) and place `data.csv` in the project directory.  
2. Open `predictive_analytics_priority.ipynb` in Jupyter Notebook or Google Colab.  
3. Run all cells to see data preprocessing, model training, evaluation, and plots.

## Results

- The model achieves over 95% accuracy on the test set.  
- The classification report shows strong precision and recall for both classes.  
- Feature importance highlights key diagnostic features affecting predictions.

## Author

Created by Nontando Myoli 
