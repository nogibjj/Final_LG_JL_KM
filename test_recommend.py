import unittest
import pandas as pd
from recommend import recommend


class TestBookRecommendation(unittest.TestCase):
    def setUp(self):
        self.columns_expected = [
            "id",
            "best_book_id",
            "work_id",
            "books_count",
            "isbn",
            "isbn13",
            "authors",
            "original_publication_year",
            "original_title",
            "title",
            "language_code",
            "average_rating",
            "ratings_count",
            "work_ratings_count",
            "work_text_reviews_count",
            "ratings_1",
            "ratings_2",
            "ratings_3",
            "ratings_4",
            "ratings_5",
            "image_url",
            "small_image_url",
            "weighted_rating",
        ]
        self.test_genre = "Cookbooks"

    def test_recommend_output_format(self):
        # Test if the output format is correct
        result = recommend(self.test_genre)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.columns), self.columns_expected)
    def test_recommend_with_different_genre(self):
        # Test the function with different genres
        genres = ["Fiction", "Mystery", "Science Fiction"]
        for genre in genres:
            result = recommend(genre)
            self.assertIsInstance(result, pd.DataFrame)
            self.assertListEqual(list(result.columns), self.columns_expected)

    def test_recommend_with_invalid_genre(self):
        # Test the function with an invalid genre
        result = recommend("InvalidGenre")
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)

    def test_recommend_with_different_percentile(self):
        # Test the function with different percentiles
        percentiles = [0.75, 0.85, 0.95]
        for percentile in percentiles:
            result = recommend(self.test_genre, percentile)
            self.assertIsInstance(result, pd.DataFrame)
            self.assertListEqual(list(result.columns), self.columns_expected)


# This allows the test to be run from the command line
if __name__ == "__main__":
    unittest.main()