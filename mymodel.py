import pandas as pd
import pickle


# charger les donnees

USAhousing = pd.read_csv('USA_Housing.csv')

# features and target

X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

# Train Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# Model creation

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, y_train)

# Saving model to disk
pickle.dump(lm, open('mymodel.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('mymodel.pkl', 'rb'))
print(model.predict([[200, 900, 600, 3, 4]]))
