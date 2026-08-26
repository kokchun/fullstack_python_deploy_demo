from backend.constants import DATA_DIRECTORY
import pandas as pd 

df = pd.read_csv(DATA_DIRECTORY / "Pokemon.csv")
