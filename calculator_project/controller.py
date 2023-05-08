"""
controller.py by Addysen Tippetts
Some functions to control the Reading Time Calculator App.
"""

# Functions
def get_reading_time(current_page = int, total_pages =int, reading_speed = float) -> str:
    """Calculates reading speed and returns results."""
    reading_time = ((total_pages-current_page)*reading_speed)/60
    results = f"You have approximately{reading_time} minutes left in your book."
    return results

# Global scope
if __name__ == "__main__":
    #test your results here.
    results = get_reading_time(100, 400, 32)
    print(results)