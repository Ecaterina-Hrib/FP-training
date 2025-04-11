import pandas as pd
import plotly.express as px

# read json file
df = pd.read_json("data/News_Category_Dataset_v3.json", lines=True)


print("Dimension dataset:", df.shape)
print("\nColumns:\n", df.columns)

pd.set_option('display.max_columns', None)  # afișează toate coloanele

print("\nFirst 5 rows:\n", df.head())

# EDA: Exploratory Data Analysis

# 1. Dimensiuni + tipuri de date
print("\n📐 Dimensiuni:", df.shape)
print("\n🧪 Tipuri de date:\n", df.dtypes)

# 2. Valori lipsă
print("\n Valori lipsă:\n", df.isnull().sum())

# 3. Distribuție categorii (cate din fiecare -> top 10)
print("\nTop categorii:\n", df["category"].value_counts().head(10))

# 4. Lungime headline
df["headline_len"] = df["headline"].str.len()
print("\nStatistici lungime headline:\n", df["headline_len"].describe())

# Adaugare lungime headline
df["headline_len"] = df["headline"].str.len()


# 📊 1. Distribuția lungimii headline-urilor
fig1 = px.histogram(df, x="headline_len", nbins=30,
                    title="Distribuția lungimii headline-urilor",
                    labels={"headline_len": "Număr de caractere headline"},
                    color="headline_len")
fig1.show()

# 📊 2. Top 10 categorii
top10 = df["category"].value_counts().head(10).reset_index()
top10.columns = ["category", "count"]

fig2 = px.bar(top10, x="count", y="category", orientation="h",
              title="Top 10 categorii de știri",
              labels={"count": "Număr de articole", "category": "Categorie"},
              color="count", color_continuous_scale="viridis")
fig2.update_layout(yaxis=dict(autorange="reversed"))
fig2.show()

