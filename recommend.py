import pandas as pd
import warnings


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Books:
    def __init__(self, dataframe):
        self.books = [
            Book(row["Title"], row["Author"]) for _, row in dataframe.iterrows()
        ]


warnings.filterwarnings("ignore")


books = pd.read_csv("books-2.csv")
ratings = pd.read_csv("ratings.csv")
book_tags = pd.read_csv("book_tags.csv")
tags = pd.read_csv("tags.csv")

books["original_publication_year"] = (
    books["original_publication_year"]
    .fillna(-1)
    .apply(lambda x: int(x) if x != -1 else -1)
)
ratings_rmv_duplicates = ratings.drop_duplicates()
unwanted_users = ratings_rmv_duplicates.groupby("user_id")["user_id"].count()
unwanted_users = unwanted_users[unwanted_users < 3]
unwanted_ratings = ratings_rmv_duplicates[
    ratings_rmv_duplicates.user_id.isin(unwanted_users.index)
]
new_ratings = ratings_rmv_duplicates.drop(unwanted_ratings.index)
new_ratings["title"] = books.set_index("id").title.loc[new_ratings.book_id].values
v = books["ratings_count"]
m = books["ratings_count"].quantile(0.95)
R = books["average_rating"]
C = books["average_rating"].mean()
W = (R * v + C * m) / (v + m)
books["weighted_rating"] = W
qualified = books.sort_values("weighted_rating", ascending=False).head(250)
genres = [
    "Art",
    "Biography",
    "Business",
    "Chick Lit",
    "Children's",
    "Christian",
    "Classics",
    "Comics",
    "Contemporary",
    "Cookbooks",
    "Crime",
    "Ebooks",
    "Fantasy",
    "Fiction",
    "Gay and Lesbian",
    "Graphic Novels",
    "Historical Fiction",
    "History",
    "Horror",
    "Humor and Comedy",
    "Manga",
    "Memoir",
    "Music",
    "Mystery",
    "Nonfiction",
    "Paranormal",
    "Philosophy",
    "Poetry",
    "Psychology",
    "Religion",
    "Romance",
    "Science",
    "Science Fiction",
    "Self Help",
    "Suspense",
    "Spirituality",
    "Sports",
    "Thriller",
    "Travel",
    "Young Adult",
]
genres = list(map(str.lower, genres))
available_genres = tags.loc[tags.tag_name.str.lower().isin(genres)]
available_genres_books = book_tags[book_tags.tag_id.isin(available_genres.tag_id)]
available_genres_books["genre"] = available_genres.tag_name.loc[
    available_genres_books.tag_id
].values
cols = ["title", "authors", "weighted_rating", "image_url"]


def recommend(quantity, genre, percentile=0.85):
    df = available_genres_books[available_genres_books["genre"] == genre.lower()]
    qualified1 = books.set_index("book_id").loc[df.goodreads_book_id]

    v2 = qualified1["ratings_count"]
    m2 = qualified1["ratings_count"].quantile(percentile)
    R2 = qualified1["average_rating"]
    C2 = qualified1["average_rating"].mean()
    qualified1["weighted_rating"] = (R2 * v2 + C2 * m2) / (v2 + m2)
    qualified1.sort_values("weighted_rating", ascending=False, inplace=True)

    # Randomly select books from the top 75
    qualified1 = qualified1.head(75)
    qualified1 = qualified1.sample(frac=1).reset_index(drop=True)
    python_list = qualified1[cols].head(quantity).values.tolist()
    for book in python_list:
        title_words = book[0].split(" ")
        amazon_link = "https://www.amazon.com/s?k=" + "+".join(title_words)
        book.append(amazon_link)

    return python_list
