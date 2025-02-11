import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
def importe_datos():
    df = pd.read_csv('https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv')
    df.describe()
    return df, df.describe