import pandas as pd
import numpy as np
Table = pd.read_csv("Exam_Table.csv")
Table = Table.dropna()
sciname = Table.loc[Table['Scientific Name']=='Pomacentrus adelus']

count = sciname['Count']

sum =0
for x in count:
    sum = sum+x

average = sum/len(count)

print("The average count for Pomacentrus adelus is:", average)
