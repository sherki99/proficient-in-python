"""
Tutorial: Demonstrating List, Tuple, and Dictionary usage in Python
This script includes examples of creating and working with lists, tuples, and dictionaries. 
It also defines a function that utilizes these data types.
"""

from typing import Dict, List, Tuple


# Example: Creating and working with a List
def create_list() -> List[str]:
    """
    Creates a list of strings and returns it.

    Returns:
        List[str]: A list containing example strings.
    """
    fruits = ["apple", "banana", "cherry"]
    return fruits


# Example: Creating and working with a Tuple
def create_tuple() -> Tuple[int, int, int]:
    """
    Creates a tuple of integers and returns it.

    Returns:
        Tuple[int, int, int]: A tuple containing three integers.
    """
    numbers = (1, 2, 3)
    return numbers


# Example: Creating and working with a Dictionary
def create_dict() -> Dict[str, int]:
    """
    Creates a dictionary mapping strings to integers and returns it.

    Returns:
        Dict[str, int]: A dictionary where keys are strings and values are integers.
    """
    age_dict = {"Alice": 25, "Bob": 30, "Charlie": 35}
    return age_dict


# Combining the data types in a function
def summarize_data() -> Dict[str, List[str]]:
    """
    Combines a list, tuple, and dictionary into a summary dictionary.

    Returns:
        Dict[str, List[str]]: A dictionary summarizing the data types.
    """
    fruits = create_list()
    numbers = create_tuple()
    ages = create_dict()

    summary = {
        "Fruits": fruits,
        "Numbers": [str(num) for num in numbers],  # Convert tuple to list of strings
        "Age Keys": list(ages.keys()),  # Extract keys from dictionary
    }
    return summary


# Running the tutorial
if __name__ == "__main__":
    print("List Example:", create_list())
    print("Tuple Example:", create_tuple())
    print("Dictionary Example:", create_dict())
    print("Summary Data:", summarize_data())
