import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# lib Version
print(f"numpy: {np.__version__}")
print(f"\npandas: {pd.__version__}")
print(f"matplotlib: {matplotlib.__version__}")

# Create DataFrame
print("-----------------------------------------")
data = {
    "name": ["Ali", "Sara", "Reza"],
    "age": [22, 21, 23],
    "score": [88, 2, 75],
}

df_demo = pd.DataFrame(data)
print(df_demo)

# Array AVG
print("-----------------------------------------")
arr = np.array([10, 20, 30, 40])
avg_arr = arr.mean()

# Array Type
print("-----------------------------------------")
x = np.nan
type(x)

# Missing Test
print("-----------------------------------------")
np.isnan(x)

# Pipe Chart
print("-----------------------------------------")
plt.figure(figsize=(6, 3.5))
plt.bar(df_demo["name"], df_demo["score"], color=["#7c2aed", "#2563eb", "#0d9488"])
plt.title("Student Scores")
plt.ylabel("score")
plt.xlabel("name")
plt.show()

# CSV Dataset
print("-----------------------------------------")
csv_text = """name,age,city,major,gpa,score,income
Ali,22,Tehran,AI,17.5,88,12
Sara,21,Shiraz,CS,18.2,92,15
Reza,23,Tabriz,IT,15.8,75,
Maryam,20,Tehran,AI,19.1,97,18
Hossein,,Isfahan,CS,16.4,81,10
Neda,22,Mashhad,IT,14.9,68,9
Amir,24,Tehran,CS,17.0,,14
Zahra,21,Shiraz,AI,18.8,95,16
Mehdi,23,Tabriz,IT,13.7,60,8
Fatemeh,22,Isfahan,AI,17.9,90,
Ali,22,Tehran,AI,17.5,88,12
Parisa,20,Mashhad,CS,16.8,79,11
Kian,25,Tehran,IT,,72,13
Narges,21,Tehran,CS,18.0,89,15
Omid,22,Shiraz,AI,15.2,70,9
Sina,23,Isfahan,IT,16.1,77,
Leila,20,Tabriz,AI,19.5,99,20
Babak,24,Mashhad,CS,14.2,64,7
Elham,22,Tehran,AI,17.3,85,12
Taha,,Shiraz,IT,15.5,73,10
"""

# Write Text to File
print("-----------------------------------------")
with open("student.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)

# Read CSV File
print("-----------------------------------------")
# nrows=5, usecols=["name", "gpa", "score"], index_col="name"
# Top 5 shows only - Justify cols show
df = pd.read_csv("student.csv").head()
# File path - Set a Column as Index
print(df)

# Number of rows and cols
print("-----------------------------------------")
print(df.shape)

# Seperate rows and cols
print("-----------------------------------------")
rows, cols = df.shape # or
print(df.shape[0]) # rows
print(df.shape[1]) # cols

# Number of dimension
print("-----------------------------------------")
print(df["gpa"].shape)
print(df[df["gpa"] > 18].shape)

# Display types
print("-----------------------------------------")
print(df.head(5))
print(df.tail(5))

# Random instance
print("-----------------------------------------")
df.sample(4, random_state=42) # like seed

# Get col header names
print("-----------------------------------------")
tmp = df.columns.tolist()
len(tmp)

# Col exist test
print("-----------------------------------------")
print("gpa" in df.columns)

# Rename col headers (new instance)
print("-----------------------------------------")
df.rename(columns={"gpa": "GPA"}).head(3)

# Uppercasing headers
print("-----------------------------------------")
df.columns.str.upper()

# Lowercasing headers
print("-----------------------------------------")
df.columns.str.lower()

# Types for each col
print("-----------------------------------------")
df.dtypes

# Type counting
print("-----------------------------------------")
df.dtypes.value_counts()

# Seperate by type
print("-----------------------------------------")
df.select_dtypes(include="number").head(3)
df.select_dtypes(exclude="number").head(3)

# Convert data types
print("-----------------------------------------")
df["score"].astype("float64").head(3)

# Table summary
print("-----------------------------------------")
df.info()

# Memory usage
print("-----------------------------------------")
print(df.memory_usage(deep=True).sum())

# General decriptive statistics
print("-----------------------------------------")
df.describe()

# Check for missing data (NaN)
print("-----------------------------------------")
df.isna()
df[df["age"].isna()]
df[df.isna().any(axis=1)]

# isna() opposite
print("-----------------------------------------")
df[df["income"].notna()]

# Missing percent for each cols
print("-----------------------------------------")
(df.isna().mean() * 100).round(1)

# Grouping
print("-----------------------------------------")
df.groupby("city")["income"]

# Missing data Chart
print("-----------------------------------------")
plt.figure(figsize=(7, 3.5))
missing = df.isna().sum()
missing.plot(kind="bar", color="#dc2626")
plt.title("Missing values per column")
plt.ylabel("count")
plt.xticks(rotation=0)
plt.show()

# Median calc
print("-----------------------------------------")
df["gpa"].median()

# Median vs Mean
print("-----------------------------------------")
salaries = pd.Series([10, 12, 11, 13, 500])
salaries.mean()
salaries.median()

# median with custom quantile
print("-----------------------------------------")
# df["gpa"].quantile(0.5) = df["gpa"].median()
df["gpa"].quantile([0.25, 0.5, 0.75])

# Most repeated data
print("-----------------------------------------")
df["city"].mode()[0] # [0] first mode

df["city"].value_counts() # more accurcy with count numbers

# IQR method
print("-----------------------------------------")
Q1 = df["income"].quantile(0.25)
Q3 = df["income"].quantile(0.75)
IQR = Q3 - Q1

low  = Q1 - 1.5 * IQR
high = Q3 + 1.5 * IQR
print(f"بازه‌ی نرمال: {low:.1f} تا {high:.1f}")

outliers = df[(df["income"] < low) | (df["income"] > high)]
print("تعداد پرت‌ها:", len(outliers))

plt.figure(figsize=(5, 3.5))
plt.boxplot(df["gpa"].dropna())
plt.title("GPA box plot")
plt.show()

# Unique data
print("-----------------------------------------")
df["city"].unique()

# Sort
print("-----------------------------------------")
df.sort_values(by="gpa", ascending=True, na_position="last")

# Reset indexes
print("-----------------------------------------")
df.reset_index(drop=True)

# Biggest and Smalles
print("-----------------------------------------")
df.nlargest(3, "score")[["name", "score"]]
df.nsmallest(3, "score")[["name", "score"]]

# Table filter
print("-----------------------------------------")
df.loc[0, "name"] # [row, cols]
df.loc[0:3, ["name", "major", "gpa"]]
df.loc[(df["major"] == "AI") & (df["gpa"] > 18), ["name", "gpa"]] # with condition

# existance check
print("-----------------------------------------")
df.loc[df["city"].isin(["Tabriz", "Mashhad"]), ["name", "city"]]
df.loc[:, "name":"city"].head(3)

# Copy table
print("-----------------------------------------")
tmp_table = df.copy()

# Find duplicated rows
print("-----------------------------------------")
df[df.duplicated()]
df.duplicated(subset=["name", "city"], keep="first")

# Remove duplicated rows
print("-----------------------------------------")
df.drop_duplicates(subset=None, keep="first")

# Reset index
print("-----------------------------------------")
tmp_table = tmp_table.reset_index(drop=True)

# Replace NaN fields with custom number
print("-----------------------------------------")
tmp_table.fillna(0)

# Remove cols or rows
print("-----------------------------------------")
tmp_table.drop(columns=["income"])
tmp_table.drop(index=[0, 1])

# Convert table to CSV
print("-----------------------------------------")
tmp_table.to_csv("new_student.csv", columns=["name"], index=False, encoding="utf-8-sig", sep=";")

# STORE PROJ
print("-----------------------------------------")
basket_data = {
    "Bread":  [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    "Milk":   [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    "Butter": [1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    "Cheese": [0, 1, 0, 1, 1, 0, 0, 1, 1, 1],
    "Eggs":   [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    "Cola":   [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
}

basket = pd.DataFrame(basket_data)
print(len(basket))

# Support Formula
print("-----------------------------------------")
# Support(A) = P(A) = Count(A) / N
# Support(A, B, ...) = P(Σ A[n] = B[n] ...) = Count(A, B) / N

count = basket.sum()
print(count)

support = basket.mean()
print(support)

# Support for 2 or more
print("-----------------------------------------")
two_item = (basket["Bread"] == 1) & (basket["Milk"] == 1)
print(two_item.sum()) # Number of match items per any rows
print(two_item.mean())

# Confidence & Lift Formula
print("-----------------------------------------")
# Conf(A -> B) = Support(A, B) / Support(A) = Count(A, B) / Count(A)
# Lift(A -> B) = Conf(A -> B) / Supp(B) = Supp(A, B) / Supp(A).Supp(B)
"""
if Lift > 1 --> Positive
if Lift = 1 --> No Relation
if Lift < 1 --> Negative
"""

supp_bread = basket["Bread"].mean()
supp_cheese = basket["Cheese"].mean()

supp_both = ((basket["Bread"] == 1) & (basket["Cheese"] == 1)).mean()

conf = supp_both / supp_bread
lift = conf / supp_cheese

print(f"Support(Bread, Cheese): {supp_both}")
print(f"Confidence(Bread -> Cheese): {round(conf, 2)}")
print(f"Lift(Bread -> Cheese): {round(lift, 2)}")