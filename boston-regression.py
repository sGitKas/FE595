from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# Synopsis
# The linear_regression  function perfomrs lienar regression using the data bost data set found int e below URL
# Docs : https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html
def linear_regression():
    from sklearn.datasets import load_boston

    boston = load_boston()
    names = boston["feature_names"]

    # What are the names of the features in the data ?
    print (names)

    # Lets create a pandas frame and load the data into the frame
    bos = pd.DataFrame(boston.data)
    print(bos.head())

    # Set the cols of the dataframe from the features
    bos.columns = boston.feature_names
    print(bos.head())

    bos['PRICE'] =  boston.target
    X = bos.drop('PRICE', axis =1)


    # Perform Linear regression
    lm = LinearRegression()

    lm.fit(X,bos.PRICE)

    print(lm.intercept_)
    print(lm.coef_)

# Lets List the cols and the coefficients

    print(pd.DataFrame(zip(X.columns,lm.coef_), columns = ['features', 'estimatedCoefficients']))

# Lets plot the best abd worst fitting features against the Price

    plt.scatter(bos.RM, bos.PRICE)
    plt.show()

    plt.scatter(bos.RM, bos.NOX)
    plt.show()

    print(' Best Fitting feature =  RM')
    print(' Worst Fitting feature =  NOX')

if __name__ == '__main__':
    linear_regression()

    pass