import math


class Circle:
    """
    circle with radius, diameter and area.
    """
    # def __init__(self, radius=1):
    #     self.radius = radius
    #     self.diameter = radius * 2
    #     self.area = math.pi * self.radius **2

    # def __repr__(self):
    #     return f'Circle({self.radius})'

    # Bonus 1

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    # Bonus 2
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

# Adding a getter and setter for the radius property is all we need to do to get the bonus working. Whenever we set radius (like in our __init__ method or our diameter setter) or access the radius (like in our diameter and area getters), these getter and setter methods will be called.

# You might think you need to update your __init__ method to also assign to self._radius and handle that exceptional case. But we don't! The reason we don't is that by the time __init__ is called, our class instance has been constructed and assigning to self.radius will call our radius setter automatically! We're able to treat our _radius attribute as encapsulated in the property getter/setters. We can change _radius outside, but there's not a good reason to do so.

# Note that we were storing our actual radius in a radius attribute before, but we're using a _radius attribute now. We're doing this for two reasons:

# We can't use a radius attribute to store this data because my_circle.radius will call our radius property and that will look up self.radius which looks up the same property infinitely so we'd get a recursion error.
# That _ is a convention in Python that means "this attribute is non-public by convention, so don't touch it unless you know what you're doing". There's no such thing as private attributes in Python, but an underscore prefix is often used to declare an attribute as being an internal implementation detail, not to be touched by folks outside this class implementation.

    # Bonus 3
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

# Note that we didn't have to do anything special here to get diameter to not accept negative values. That's because diameter sets self.radius, which calls our radius property setter. Also note that we don't reference self._radius anywhere except in our radius property getter and setter methods: even __init__ sets self.radius instead of self._radius. We never touch that self._radius attribute directly but instead always go through our radius setter, so that every time that attribute is set it'll check for validity correctly.

# Properties are really powerful in Python. Python's properties allow us to take an existing attribute-based class API and maintain backwards compatibility while adding new functionality during attribute lookup or assignment.
