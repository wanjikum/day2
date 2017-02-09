
"""Maximum and minimum number solution"""
def find_max_min(number):
    """A function that returns the max and the min number in a list"""
    if max(number) == min(number):
        return [len(number)]
    return [min(number), max(number)]