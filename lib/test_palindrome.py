import pytest
from palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    "input_str, expected_outputs",
    [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
        ("racecar", ["racecar"]),
        ("", [""]),
        ("forgeeksskeegfor", ["geeksskeeg"]),
    ],
)
def test_longest_palindromic_substring_valid(input_str, expected_outputs):
    """Test normal, edge, and various input sizes using parameterized tests."""
    result = longest_palindromic_substring(input_str)
    assert result in expected_outputs


def test_invalid_input_type():
    """Failure case: Ensure the function handles invalid data types gracefully or raises an error."""
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)
