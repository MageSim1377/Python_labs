import pytest
from contextlib import nullcontext as does_not_raise
from src.Task import count_words, find_unique, is_palindrome, are_anagrams, mergeDicts


class TestCountWords:
    @pytest.mark.parametrize(
            "str, length, expectation",
            [
                ("Hello, world", 2, does_not_raise()),
                ("Hello, hello, world!", 3, does_not_raise()),
                ("", 0, does_not_raise()),
                (" ", 0, does_not_raise()),
                (123, 0, pytest.raises(TypeError)),
                (["Hello world"], 0, pytest.raises(TypeError)),
            ]
    )
    def test_count_words(self, str, length, expectation):
        with expectation:
            assert count_words(str) == length


class TestFindUnique:
    @pytest.mark.parametrize(
        "list, uniq, expectation",
        [
            ([1, 1, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5], does_not_raise()),
            ([1, 2, 3, 4, 5, 5, 5], [1, 2, 3, 4, 5], does_not_raise()),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], does_not_raise()),
            ([], [], does_not_raise()),
            ([1], [1], does_not_raise()),
            ([1, 2, 3, 1, 2, 1, 1, 1], [1, 2, 3], does_not_raise()),
            ("1, 2, 3, 1, 2, 1, 1, 1", [1, 2, 3], pytest.raises(TypeError)),
        ]
    )
    def test_find_unique(self, list, uniq, expectation):
        with expectation:
            assert find_unique(list) == uniq


class TestIsPalindrome:
    @pytest.mark.parametrize(
        "str, ans, expectation",
        [
            (12321, True, does_not_raise()),
            ("12321", True, does_not_raise()),
            (12345, False, does_not_raise()),
            ("12345", False, does_not_raise()),
            ({"12345"}, False, pytest.raises(TypeError)),
        ]
    )
    def test_is_palindrome(self, str, ans, expectation):
        with expectation:
            assert is_palindrome(str) == ans

class TestAreAnagrams:
    @pytest.mark.parametrize(
        "word1, word2, ans, expectation",
        [
            ("Hello", "olleh", True, does_not_raise()),
            ("aaangrm", "Anagram", True, does_not_raise()),
            ("Some", "Some", True, does_not_raise()),
            ("", "", True, does_not_raise()),
            ("OneWord", "AnotherWord", False, does_not_raise()),
            ("", "AnotherWord", False, does_not_raise()),
            ("", 123, False, pytest.raises(TypeError)),
            (323, "123", False, pytest.raises(TypeError)),
        ]
    )
    def test_is_palindrome(self, word1, word2, ans, expectation):
        with expectation:
            assert are_anagrams(word1, word2) == ans


class TestMergeDicts:
    @pytest.mark.parametrize(
        "dict1, dict2, ans, expectation",
        [
            (
                {1: "one", 2: "two", 3: "tree"},
                {4: "four", 5: "five", 6: "six"},
                {1: "one", 2: "two", 3: "tree", 4: "four", 5: "five", 6: "six"},
                does_not_raise()
            ),
            (
                {"a": 1, "b": {"c": 1, "f": 4}},
                {"d": 1, "b": {"c": 2, "e": 3}},
                {'a': 1, 'b': {'c': 2, 'f': 4, 'e': 3}, 'd': 1},
                does_not_raise()
            ),
            (
                '{"a": 1, "b": {"c": 1, "f": 4}',
                {"d": 1, "b": {"c": 2, "e": 3}},
                {'a': 1, 'b': {'c': 2, 'f': 4, 'e': 3}, 'd': 1},
                pytest.raises(TypeError)
            ),
        ]
    )
    def test_is_palindrome(self, dict1, dict2, ans, expectation):
        with expectation:
            assert mergeDicts(dict1, dict2) == ans