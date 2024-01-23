import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class Additif:

    def __init__(self, DataPreparationObjet):
        self.DataPreparationObjet = DataPreparationObjet
        self.model = LinearRegression()

        self.model.fit(DataPreparationObjet.x_train, DataPreparationObjet.y_train)

        y_train_predicted = self.model.predict(DataPreparationObjet.x_train)
        mean_train_absolute_error = np.mean(np.abs(y_train_predicted - DataPreparationObjet.y_train))
        print(f"sur le jeu de train : {mean_train_absolute_error=:.2f}")

        y_test_predicted = self.model.predict(DataPreparationObjet.x_test)
        mean_test_absolute_error = np.mean(np.abs(y_test_predicted - DataPreparationObjet.y_test))
        print(f"sur le jeu de test : {mean_test_absolute_error=:.2f}")

        self.show_model_predictions(y_train_predicted, y_test_predicted)

    def show_model_predictions(self, y_train_predicted, y_test_predicted):


        plt.figure(figsize=(15, 6))

        plt.plot(self.DataPreparationObjet.dataset_df["Years"].iloc[ : int(len(self.DataPreparationObjet.dataset_df)*0.75)], self.DataPreparationObjet.y_train, "bo:", label = "time series data")# vérité terrain
        plt.plot(self.DataPreparationObjet.dataset_df["Years"].iloc[ : int(len(self.DataPreparationObjet.dataset_df)*0.75)], y_train_predicted,"b", label = "fitted addititve model") # prediction

        plt.plot(self.DataPreparationObjet.dataset_df["Years"].iloc[int(len(self.DataPreparationObjet.dataset_df)*0.75) : ], self.DataPreparationObjet.y_test, "ro:", label = "True Future Data") # verité terrain
        plt.plot(self.DataPreparationObjet.dataset_df["Years"].iloc[int(len(self.DataPreparationObjet.dataset_df)*0.75) : ], y_test_predicted, "r", label = "Forecasted addititve Model Data")# prediction

        ci = 1.96 * np.std(y_test_predicted)/np.sqrt(len(self.DataPreparationObjet.dataset_df["Years"].iloc[int(len(self.DataPreparationObjet.dataset_df)*0.75) : ]))
        plt.fill_between(self.DataPreparationObjet.dataset_df["Years"].iloc[int(len(self.DataPreparationObjet.dataset_df)*0.75) : ], (y_test_predicted-ci), (y_test_predicted+ci), color='grey', alpha=.1, label = "95 Confidence interval")

        font1 = {'family':'serif','size':20}
        font2 = {'family':'serif','size':15}

        plt.title("Ventes de maillots de bain", fontdict = font1)
        plt.xlabel("Années", fontdict = font2)
        plt.ylabel("Ventes", fontdict = font2)
        plt.legend()

        plt.show()
