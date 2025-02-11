import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def visualizacion_1(dataframe:pd.DataFrame):
    
    fig, axes = plt.subplots(1,1,figsize= (12,9))
    sns.boxplot(x = "Brand", y= "Price", data = dataframe, ax = axes )
    plt.title("Distribución de precios por marca")
    plt.xlabel("Marca")
    plt.ylabel("Precio")
    plt.xticks(rotation = 45)
    return fig