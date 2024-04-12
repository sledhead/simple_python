#testing simple pandas code

import pandas as pd

pand_fr = pd.read_excel("sales_9_2022.xlsx", engine='openpyxl')

pand_fr["Sales"].sum()