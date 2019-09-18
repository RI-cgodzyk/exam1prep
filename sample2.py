#Using pandas take in a file and calculate the name most seen and calculate the total count for each ethnicity
# upload to git and submit via link

#need pandas
import pandas as pd

names = pd.read_csv("names.csv")

most_used_name = names.mode()

grouped = names.groupby("Ethnicity")
totalgroupby = grouped.sum()

print("The most utilized name is:")
print(most_used_name)
print("The total count for each ethnicity is:")
print(totalgroupby)