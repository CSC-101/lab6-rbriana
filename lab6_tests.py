import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_sorting_books(self):
        books = [data.Book(["Author A"], "Zebra"), data.Book(["Author B"], "Apple")
                 , data.Book(["Author C"], "Mango")]
        lab6.selection_sort_book(books)
        self.assertEqual(books[0].title, "Zebra")
        self.assertEqual(books[1].title, "Apple")
        self.assertEqual(books[2].title, "Mango")

    def test_empty_list_book(self):
        books = []
        lab6.selection_sort_book(books)
        self.assertEqual(books, [])


    # Part 2
    def test_swap_case(self):
        self.assertEqual(lab6.swap_case("Hello World"), "hELLO wORLD")
        self.assertEqual(lab6.swap_case("PyThOn123"), "pYtHoN123")
        self.assertEqual(lab6.swap_case(""), "")

    # Part 3
    def test_str_translate(self):
        self.assertEqual(lab6.str_translate("abcdcba", "a", "x"), 'xbcdcbx')

    def test_str_translate2(self):
        self.assertEqual(lab6.str_translate("mango", "a", "a"), 'mango')

    # Part 4

    def test_histogram(self):
        self.assertEqual(lab6.histogram("hello world hello"), {"hello":2,"world":1})
        self.assertEqual(lab6.histogram("one two three two one one"), {"one":3, "two":2, "three":1})
        self.assertEqual(lab6.histogram(""), {})



if __name__ == '__main__':
    unittest.main()
