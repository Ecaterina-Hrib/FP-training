import pandas as pd
import plotly.express as px

## date preluate: https://insideairbnb.com/get-the-data/

# Citim fișierele pentru cele două orașe

df_amsterdam = pd.read_csv('data/listings_amsterdam.csv')
df_barcelona = pd.read_csv('data/listings_barcelona.csv')

print("New York data:", df_amsterdam.shape)
print("Other City data:", df_barcelona.shape)

df_barcelona['city'] = 'Barcelona'
df_amsterdam['city'] = 'Amsterdam'

df = pd.concat([df_barcelona, df_amsterdam], ignore_index=True)

pd.set_option('display.max_columns', None)
print(df.head())

# Verificăm dacă au aceleași coloane
print(df.columns)

# Verificăm prezența valorilor lipsă
print(df.isnull().sum())

# Verificăm tipurile de date
print(df.dtypes)

df.drop_duplicates(inplace=True)

df.fillna({'host_name': "Unknown"}, inplace=True)
df.fillna({'neighbourhood_group': "Unknown"}, inplace=True)
df.fillna({'price': df['price'].median()}, inplace=True)

# Calculăm prețul mediu pe tipul de cameră
room_price = df.groupby('room_type')['price'].mean().sort_values()

# Corelația între preț și numărul de recenzii
fig1 = px.scatter(df, x='number_of_reviews', y='price',
                  title='📉 Corelația între Preț și Numărul de Recenzii',
                  labels={'number_of_reviews': 'Număr Recenzii', 'price': 'Preț'},
                  color='room_type')
fig1.show()

# Top 10 locuințe cu cele mai multe recenzii (pandas-> SORTARE)
top_reviews = df[['name', 'number_of_reviews']].sort_values(by='number_of_reviews',
                                                            ascending=False).head(10)

fig2 = px.bar(top_reviews, x='name', y='number_of_reviews',
              labels={'name': 'Locuință', 'number_of_reviews': 'Număr Recenzii'},
              title="🏆 Top 10 Locuințe după Numărul de Recenzii",
              color='name')
fig2.show()

# Creăm harta folosind plotly express
fig3 = px.scatter_map(
    df,
    lat="latitude",  # Coloana cu latitudine
    lon="longitude",  # Coloana cu longitudine
    color="price",  # Vom colora punctele în funcție de preț
    size="price",
    hover_name="name",  # Date suplimentare afișate la hover
    title="🌍Locuințe Airbnb cu Prețuri",
    # zoom=10,  # Zoom-ul inițial pe hartă
)

# Afișăm graficul
fig3.show()

# harta doar pt un oras

# Filtrăm datasetul pentru Amsterdam
df_amsterdam_top = df[
    (df['city'] == 'Amsterdam') & (df['price'] > 100) & (df['number_of_reviews'] > 100)]

fig4 = px.scatter_map(
    df_amsterdam_top,
    lat="latitude",
    lon="longitude",
    color="price",
    size="price",
    hover_name="name",
    hover_data=["room_type", "neighbourhood", "price"],
    title="Locuințe 'Top' din Amsterdam"
)

fig4.show()

df_barcelona = df[(df['city'] == 'Barcelona')]
fig5 = px.density_mapbox(df_barcelona,
                         lat='latitude',
                         lon='longitude',
                         z='price',
                         range_color=[df_amsterdam['price'].min(), df_amsterdam['price'].max()],
                         title="Harta de Căldură a Prețurilor în Amsterdam",
                         mapbox_style="carto-positron",
                         opacity=0.6,
                         zoom=12)

fig5.show()
