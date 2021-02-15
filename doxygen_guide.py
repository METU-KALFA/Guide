"""@package doxygenGuide
The doxygen guide and doxygen commenting exapmle

Using tags makes comment readable and compatible for documentation softwares.
Java Tags may be useful for tag definitions and orders.
Here are the some Java comment tags in suggested Java order:

@author     Burak Bolat
@version    0
@param      parameterName   parameter description.
                            if a second line is needed care the indentation.

@return                     result of the method. 
@exception                  exception that can occur.
                            throws can be used as synonym.
@see                        emphasize important points.
                            eg. give a URL
                            eg. #func(), MyClass#ClassMethod(anyInt)
@depreceted

"""

def func():
    """Documentation for a function.

    More details.
    """
    pass

class MyClass:
    """Documentation for a class.

    More details.
    """
    def __init__(self):
        """The constructor."""
        self._memVar = 0
    
    def ClassMethod(self, anyInt):
        """Documentation for a method."""
        pass

