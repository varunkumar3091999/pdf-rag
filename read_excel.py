import pandas as pd
import sqlite3


def read_csv(filepath):
  try: 
    df = pd.read_csv(filepath)
    print(df)
    return df
  except Exception as e:
    print(f"Error reading Excel file: {e}")
    return None

def read_excel(filepath, sheet_name=0):
  try: 
    df = pd.read_excel(filepath)
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
    df = df.dropna(how='all')  # Drop rows where all elements are NaN
    # Further custom cleaning here
    add_to_db(df, filepath)
    return df
  except Exception as e:
    print(f"Error reading Excel file: {e}")
    return None
  
def add_to_db(df, filepath):
  conn = sqlite3.connect("excel_data.db")
  df.to_sql('mytable', conn, if_exists="replace",index=False)

read_excel("./excel/car_price_dataset.xlsx")
# read_csv("./excel/car_price_dataset.csv")