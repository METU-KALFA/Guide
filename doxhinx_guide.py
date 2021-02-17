"""Guide for Sphinx and Doxygen integrated documentation

This guide code has comment style like Sphinx but uses tags from Java comment conventions

Author:
    Burak Bolat

Version:
    0

Args (function) / Attributes (class or global):
    ParameterName   parameter description.
    If a second line is needed care the indentation.

Return:
    Result of the method. 

Raises:
    Exception that can occur.
    Throws / Exception can be used as synonym.

See:
    emphasize important points.
    eg. give a URL
    eg. #func(), MyClass#ClassMethod(anyInt)

@depreceted

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

