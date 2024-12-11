import pandas as pd

print(pd.__version__)

df = pd.read_csv("02_CBA9_flowpath5_sample1_Tscan_heating_9T_probe1mA.txt", sep='\t')
print(df.filter(items=[' _amp ']))
