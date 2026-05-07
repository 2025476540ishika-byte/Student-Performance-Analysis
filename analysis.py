import pandas as pd

df = pd.read_csv("students.csv")

print(df)

average_marks = df[["Math","Science","English"]].mean()

print("\nAverage Marks:")
print(average_marks)

topper = df.loc[df["Math"].idxmax()]

print("\nTopper in Math:")
print(topper["Name"])