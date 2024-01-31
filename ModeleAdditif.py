from DataPreparation import DataPreparationObject
from Additif import Additif

csv_path = (r"vente_maillots_de_bain.csv(1)")
DataPreparation = DataPreparationObject(csv_path)
Additif = Additif(DataPreparation)
