"""Guide for Sphinx documentation

The Sphinx guide and Sphinx commenting exapmle

Attributes:
    anyInt (int): global integer attribute for this Python file.

Todo:
    * Add Todo if necessary.
    * Visit ''METU-KALFA github''.

.. https://github.com/METU-KALFA

"""

anyInt = 123456

def func(param1):
    """Documentation for a function.

    More details.

    Args:
        param (int)1: The first parameter

    Returns:
        The return value.

    Yields:
        int: The next number in the range of 0 to `n` - 1.
            Yields is used for generator instead of Returns

    Examples:
        >>> print(func(5))
        [0, 1, 2, 3, 4]

    Raises:
        AttributeError: List of exceptions is listed under Raises section.

    """
    pass

class MyClass:
    """Documentation for a class.

    More details.
    Note:
        Classes have Atrributes as Method/Function Args.

    """
    def __init__(self):
        """The constructor."""
        self._memVar = 0
    
    def ClassMethod(self, anyInt):
        """Documentation for a method."""
        pass

