class Rectangle:
    """
    Instantiates a rectangle object
    """
    def __init__(self, width, height):
        """
        Initialises instance of class 
        """
        self.width = width
        self.height = height
        
    def __str__(self):
        """
        Returns a string of the object
        """
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        """
        Updates the objects width
        """
        self.width = width

    def set_height(self, height):
        """
        Updates the objects height
        """
        self.height = height

    def get_area(self):
        """
        Returns the area of the object
        """
        return (self.width * self.height)

    def get_perimeter(self):
        """
        Returns the perimeter of the object
        """
        return (2 * self.width  + 2 * self.height)

    def get_diagonal(self):
        """
        Returns the diagonal of the object
        """
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        """
        Returns a string that prints the object to the console
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture_string = ""
            for i in range(self.height):
                picture_string += (("*" * self.width) + "\n")
        return picture_string

    def get_amount_inside(self, shape):
        """
        Returns the number of times a passed 
        shape can fit into the object shape
        """
        return ((self.width // shape.width) * (self.height // shape.height))

class Square(Rectangle):
    """
    Instantiates a square object
    inheriting from Rectangle class
    """
    def __init__(self, side):
        """
        Initialises object variables
        """
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        """
        Returns string of object
        """
        return f"Square(side={self.side})"

    def set_width(self, side):
        """
        Sets the width of the square object
        """
        super().set_width(side)
        self.set_side(side)

    def set_height(self, side):
        """
        Sets the height of the square object
        """
        super().set_height(side)
        self.set_side(side)

    def set_side(self, side):
        """
        Sets the objects side length
        """
        self.side = side
        super().set_height(side)
        super().set_width(side)