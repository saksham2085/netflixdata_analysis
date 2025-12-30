#step-1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#step-2: Load the dataset
df = pd.read_csv("netflix_titles.csv")
print(df.head())

#step-3: Data Cleaning - Check for missing values
df = df.dropna(subset = ['type','release_year','rating','country','duration'])

#step-4: Analyze the distribution of movies vs TV shows using bar chart
type_counts = df['type'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(type_counts.index, type_counts.values, color=['red', 'blue'])
plt.title('Count of Movies and TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

#step5: Analyze content ratings using pie chart
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Content Ratings on Netflix')
plt.tight_layout()
plt.savefig('content_ratings_distribution.png')
plt.show()

#step-6: Analyze movie durations using histogram
movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration'] = movie_df['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(10,6))
plt.hist(movie_df['duration'], bins=30, color='green', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movie_durations_distribution.png')
plt.show()

#step-7: Analyze release years using scatter plot
release_year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12,6))
plt.scatter(release_year_counts.index, release_year_counts.values, color='purple')
plt.title('released years vs number of shows')
plt.xlabel('Release Year')
plt.ylabel('Number of shows')
plt.tight_layout()
plt.savefig('release_years_vs_number_of_shows.png')
plt.show()

#step-8: Analyze top 10 countries by number of shows using horizontal bar chart
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.barh(country_counts.index, country_counts.values, color='orange')
plt.title('Top 10 Countries by Number of shows on Netflix')
plt.xlabel('Number of shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top_10_countries_by_titles.png')
plt.show()
#step-9: Compare the number of movies and TV shows released over the years using line plots
content_by_year = df.groupby('release_year')['type'].value_counts().unstack().fillna(0)
fig,axs = plt.subplots(2,1, figsize=(12,10), sharex=True)

#first subplot:movies
axs[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
axs[0].set_title('Number of Movies Released Over the Years')
axs[0].set_xlabel('Release Year')
axs[0].set_ylabel('Number of Movies')
axs[0].grid(True)
#second subplot:tv shows
axs[1].plot(content_by_year.index, content_by_year['TV Show'], color='red')
axs[1].set_title('Number of TV Shows Released Over the Years')
axs[1].set_xlabel('Release Year')
axs[1].set_ylabel('Number of TV Shows')
axs[1].grid(True)
fig.suptitle('Comparison of Movies and TV Shows Released Over the Years', fontsize=16)
plt.tight_layout()
plt.savefig('movies_tvshows_over_years.png')
plt.show()