from DataPreparation import DataPreparationObject
from Additif import Additif

csv_path = (r"C:\Users\Belbo\Desktop\HETIC ANNEE 2023_2024\SEMESTRE 1\Mathématique et statistique + python\Modèle additif\vente_maillots_de_bain.csv")
DataPreparation = DataPreparationObject(csv_path)
Additif = Additif(DataPreparation)
