The circle should have a radius, a diameter, and an area. It should also have a nice string representation.

For example:

>>> c = Circle(5)
>>> c
Circle(5)
>>> c.radius
5
>>> c.diameter
10
>>> c.area
78.53981633974483
Additionally the radius should default to 1 if no radius is specified when you create your circle:

>>> c = Circle()
>>> c.radius
1
>>> c.diameter
2
There are three bonuses for this exercise.

#### Bonus 1

For the first bonus, make sure when the radius of your class changes that the diameter and area both change as well: ✔️

>>> c = Circle(2)
>>> c.radius = 1
>>> c.diameter
2
>>> c.area
3.141592653589793
>>> c
Circle(1)
If you get stuck on this bonus, make sure to check the hints.

#### Bonus 2

For the second bonus, make sure you can set the diameter attribute in your class and the radius will update accordingly. Also make sure also that you cannot set the area (setting area should raise an AttributeError): ✔️

>>> c = Circle(1)
>>> c.diameter = 4
>>> c.radius
2.0
>>> c.area = 45.678
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 16, in radius
AttributeError: can't set attribute

#### Bonus 3

For the third bonus, make sure your radius cannot be set to a negative number. You should raise a ValueError exception with the error message "Radius cannot be negative". ✔️

>>> c = Circle(5)
>>> c.radius = 3
>>> c.radius = -2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
This means that diameter cannot be negative either (and setting diameter to a negative number should also raise a ValueError).

#### Hints

Here are some hints you can use when you get stuck (hover over links to see what they're about):

[Computing the area of a circle](https://en.wikipedia.org/wiki/Area_of_a_circle)
[Creating a class](https://www.youtube.com/watch?v=ZDa-Z5JzLYM/)
[String representation of a class](https://www.youtube.com/watch?v=5cvM-crlDvg)
[math things](https://docs.python.org/3/library/math.html#math.pi)
[Bonus 1: Making an auto-updating attribute](https://www.youtube.com/watch?v=jCzT9XFZ5bw)
[Bonus 2: Raising exceptions](https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python)

#### Tests

Automated tests for this week's exercise can be found [here](https://www.pythonmorsels.com/exercises/ac9f7d60d95d493f9e354f18a3ea9d82/tests/). You'll need to write your class in a module named circle.py next to the test file. To run the tests you'll run "python test_circle.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.