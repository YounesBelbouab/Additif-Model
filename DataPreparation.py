import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




class DataPreparationObject:

    def __init__(self, csv_path):
        self.dataset_df = pd.read_csv(csv_path)
        self.dataset_df["Years"] = pd.to_datetime(self.dataset_df["Years"])
        #self.dataset_df["DATE"] = self.dataset_df["Years"].dt.strftime("%m/%y")
        self.dataset_df["month_name"]= self.dataset_df["Years"].dt.strftime("%B")
        number_of_rows = len(self.dataset_df)
        self.dataset_df["time"] = np.arange(0, number_of_rows, 1)
        df2 = pd.get_dummies(data = self.dataset_df["month_name"], dtype = int)
        self.dataset_df = self.dataset_df.join(df2)
        print(self.dataset_df)
        self.prepare_data()

    def prepare_data(self):
        number_of_rows = len(self.dataset_df)


        dataset_train_df = self.dataset_df.iloc[ : int(number_of_rows*0.75)]
        dataset_test_df = self.dataset_df.iloc[int(number_of_rows*0.75) : ]

        self.x_train = dataset_train_df.iloc[:,3:16].values
        self.y_train = dataset_train_df["Sales"].values

        self.x_test = dataset_test_df.iloc[:,3:16].values
        self.y_test = dataset_test_df["Sales"].values

    def show_graph(self):
        plt.figure(figsize=(15, 6))
        plt.plot(self.dataset_df["Years"], self.dataset_df["Sales"], "o:")
        plt.show()