class Regression:

    def __init__(self, data_preparation_object):
        self.data_preparation_object = data_preparation_object
        self.model = LinearRegression()

        self.model.fit(data_preparation_object.x_train, data_preparation_object.y_train)

        y_train_predicted = self.model.predict(data_preparation_object.x_train)
        mean_train_absolute_error = np.mean(np.abs(y_train_predicted - data_preparation_object.y_train))
        print(f"sur le jeu de train : {mean_train_absolute_error=:.2f}")

        y_test_predicted = self.model.predict(data_preparation_object.x_test)
        mean_test_absolute_error = np.mean(np.abs(y_test_predicted - data_preparation_object.y_test))
        print(f"sur le jeu de test : {mean_test_absolute_error=:.2f}")

        self.show_model_predictions(y_train_predicted, y_test_predicted)

    def show_model_predictions(self, y_train_predicted, y_test_predicted):


        plt.figure(figsize=(15, 6))

        plt.plot(self.data_preparation_object.dataset_df["Years"].iloc[ : int(len(data_preparation_object.dataset_df)*0.75)], self.data_preparation_object.y_train, "bo:", label = "time series data")# vérité terrain
        plt.plot(self.data_preparation_object.dataset_df["Years"].iloc[ : int(len(data_preparation_object.dataset_df)*0.75)], y_train_predicted,"b", label = "fitted addititve model") # prediction

        plt.plot(self.data_preparation_object.dataset_df["Years"].iloc[int(len(data_preparation_object.dataset_df)*0.75) : ], self.data_preparation_object.y_test, "ro:", label = "True Future Data") # verité terrain
        plt.plot(self.data_preparation_object.dataset_df["Years"].iloc[int(len(data_preparation_object.dataset_df)*0.75) : ], y_test_predicted, "r", label = "Forecasted addititve Model Data")# prediction

        ci = 1.96 * np.std(y_test_predicted)/np.sqrt(len(self.data_preparation_object.dataset_df["Years"].iloc[int(len(data_preparation_object.dataset_df)*0.75) : ]))
        plt.fill_between(self.data_preparation_object.dataset_df["Years"].iloc[int(len(data_preparation_object.dataset_df)*0.75) : ], (y_test_predicted-ci), (y_test_predicted+ci), color='grey', alpha=.1)

        font1 = {'family':'serif','size':20}
        font2 = {'family':'serif','size':15}

        plt.title("Ventes de maillots de bain", fontdict = font1)
        plt.xlabel("Années", fontdict = font2)
        plt.ylabel("Ventes", fontdict = font2)
        plt.legend()

        plt.show()
