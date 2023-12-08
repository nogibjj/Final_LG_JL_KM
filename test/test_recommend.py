import unittest
import sys
sys.path.append("..") 
from mylib.recommend import recommend

class TestBookRecommendation(unittest.TestCase):
    def setUp(self):
        # Set up any variables you need for your tests
        self.test_genre = "Cookbooks"
        self.test_quantity = 5
        self.expected_columns = [
            "title",
            "authors",
            "weighted_rating",
            "image_url",
            "amazon_link",
        ]

    def test_recommend_output_format(self):
        # Test if the output format is correct
        result = recommend(self.test_quantity, self.test_genre)
        self.assertIsInstance(result, list)
        for book in result:
            self.assertIsInstance(book, list)
            self.assertEqual(len(book), len(self.expected_columns))

    def test_recommend_with_different_genre(self):
        # Test the function with different genres
        genres = ["Fiction", "Mystery", "Science-Fiction"]
        for genre in genres:
            result = recommend(self.test_quantity, genre)
            self.assertIsInstance(result, list)
            for book in result:
                self.assertIsInstance(book, list)
                self.assertEqual(len(book), len(self.expected_columns))

    def test_recommend_with_invalid_genre(self):
        # Test the function with an invalid genre
        result = recommend(self.test_quantity, "InvalidGenre")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_recommend_with_different_percentile(self):
        # Test the function with different percentiles
        percentiles = [0.75, 0.85, 0.95]
        for percentile in percentiles:
            result = recommend(self.test_quantity, self.test_genre, percentile)
            self.assertIsInstance(result, list)
            for book in result:
                self.assertIsInstance(book, list)
                self.assertEqual(len(book), len(self.expected_columns))


# This allows the test to be run from the command line
if __name__ == "__main__":
    unittest.main()

print(recommend(2, 'art'))