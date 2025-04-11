import pandas as pd
import plotly.express as px

#### Link dataset :https://www.kaggle.com/datasets/kazanova/sentiment140


df = pd.read_csv('data/sentiment140.csv', header=None,
                 names=['sentiment', 'id', 'date', 'query', 'user', 'text'], encoding='ISO-8859-1')

pd.set_option('display.max_columns', None)  # afișează toate coloanele
print("\nFirst 5 rows:\n", df.head())

# df.head()
# df.tail()

# EDA: Exploratory Data Analysis

# 1.Dimensiuni + tipuri de date
print("\n📐 Dimensiuni:", df.shape)
print("\n🧪 Tipuri de date:\n", df.dtypes)
print("\nColumns:\n", df.columns)

# 2.Valori lipsă/null
print("\n Valori lipsă:\n", df.isnull().sum())

# 3.Nnumărul de valori distincte pentru fiecare coloană
distinct_values = df.nunique()
print("\n Nr of Distinct values: \n", distinct_values)

# analiza sentiment (analiza camp calitativ)
sentiment_counts = df.sentiment.value_counts()
print(sentiment_counts)

# avem doar 2(0 si 4) -> facem o mapare sa fie mai intuitive
df.sentiment = df.sentiment.map({0: -1, 4: 1})
sentiment_counts = df.sentiment.value_counts()
print(sentiment_counts)

# analiza text
df["text_len"] = df["text"].str.len()
print("\nStatistici lungime text:\n", df["text_len"].describe())

# schimbam formatul sa fie mai citibil
pd.set_option('display.float_format', lambda x: '%.2f' % x)
print("\nStatistici lungime text:\n", df["text_len"].describe())

# Adaugă lungimea texte in df
df["text_len"] = df["text"].str.len()

# # Top 10 utilizatori pe baza frecvenței postărilor
top_users = df['user'].value_counts().head(10)

fig1 = px.bar(
    top_users,
    x=top_users.index,
    y=top_users.values,
    labels={'x': 'User', 'y': 'Number of Posts'},
    title="👥 Top 10 Users by Number of Posts",
    color=top_users.index
)
fig1.show()

# # Distributia sentimentelor

sentiment_counts = df['sentiment'].value_counts()

fig2 = px.bar(
    sentiment_counts,
    x=sentiment_counts.index,
    y=sentiment_counts.values,
    labels={'x': 'Sentiment (-1=Negativ, 1=Pozitiv)', 'y': 'Count'},
    title="💬 Distribuția Sentimentelor",
    color=sentiment_counts.index
)
fig2.show()

# # Distribuția lungimii textelor
fig3 = px.histogram(
    df,
    x='text_len',
    color='sentiment',
    nbins=50,
    title='📊 Histogramă: Lungimea textelor în funcție de sentiment',
    labels={'text_len': 'Lungimea Textului', 'sentiment': 'Sentiment'}
)
fig3.update_layout(barmode='group')
fig3.show()

### sa lucram cu timpul (date column)

df['date'] = pd.to_datetime(df['date'])
print(df['date'].head())

# Data Types dupa ce am convertit timpul
print(df.dtypes)

# coloane noi
df['hour'] = df['date'].dt.hour
df['weekday'] = df['date'].dt.day_name()

# Distribuția postărilor pe ore

fig4 = px.histogram(
    df,
    x='hour',
    color='sentiment',
    title="🕒 Distribuția postărilor pe ore",
    labels={'hour': 'Ora din zi', 'sentiment': 'Sentiment'}
)
fig4.update_layout(barmode='group')
fig4.show()

# Distribuția pe zilele săptămânii

fig5 = px.histogram(
    df,
    x='weekday',
    color='sentiment',
    category_orders={
        'weekday': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']},
    title="📅 Distribuția postărilor pe zilele săptămânii",
    labels={'weekday': 'Ziua Săptămânii', 'sentiment': 'Sentiment'},
    color_discrete_map={
        -1: 'red',  # negativ
        1: 'green'  # pozitiv
    }
)
fig5.update_layout(barmode='group')
fig5.show()



# legaturi intre 2 variabile (ex: sentiment si lungimea textului)

fig6 = px.scatter(
    df,
    x='text_len',
    y='sentiment',
    color='sentiment',
    title='Scatter Plot: Lungimea textului vs Sentiment',
    color_discrete_map={-1: 'red', 1: 'green'}
)
fig6.show()


# nr  de postari pe zi
posts_per_day = df.groupby(df['date'].dt.date).size().reset_index(name='num_posts')


fig7 = px.line(
    posts_per_day,
    x='date',
    y='num_posts',
    title='📅 Numărul de postări pe zi',
    labels={'date': 'Data', 'num_posts': 'Număr postări'}
)
fig7.show()

