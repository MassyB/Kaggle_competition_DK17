
# Kaggle_competition_DK17
jupyter notebook containing different strategies explored for the kaggle competition  https://www.kaggle.com/c/data-marketing

# To launch the notebook
**`jupyter notebook Kaggle_Competition_Marketing.ipynb`**

# Content
* **1. Data Cleaning and Encoding** to see how we cleaned the NaN values and encoded the categorical features.
* **2. Pipelines** for prototyping different strategies in each step of the classification process.
* **2.1.4.C. Gradient Boosting Classifier** is the classifier we used to produce the prediction. its parameters are tuned using a grid search.
* **3. Test With Kaggle** to save the prediction of the **`gboost`** pipeline in a csv file.

To reproduce the result: execute the cells from **"1. Data Cleaning and Encoding"** to **"2.1. Classifiers"**. Execute **"C. Gradient Boosting**"" to train the gboost pipeline and the cells under **"3. Test with Kaggle"** to get the csv file.
