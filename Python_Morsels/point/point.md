This week I'd like you to write a class representing a 3-dimensional point.

The Point class must accept 3 values on initialization (x, y, and z) and have x, y, and z attributes. It must also have a helpful string representation. Additionally, point objects should be comparable to each other (two points are equal if their coordinates are the same and not equal otherwise).

#### Example usage:

>>> p1 = Point(1, 2, 3)
>>> p1
Point(x=1, y=2, z=3)
>>> p2 = Point(1, 2, 3)
>>> p1 == p2
True
>>> p2.x = 4
>>> p1 == p2
False
>>> p2
Point(x=4, y=2, z=3)
If you finish the base exercise quickly, consider working through a bonus or two.

#### Bonus 1

For the first bonus, I'd like you to allow Point objects to be added and subtracted from each other. ✔️

>>> p1 = Point(1, 2, 3)
>>> p2 = Point(4, 5, 6)
>>> p1 + p2
Point(x=5, y=7, z=9)
>>> p3 = p2 - p1
>>> p3
Point(x=3, y=3, z=3)

#### Bonus 2

For the second bonus, I'd like you to allow Point objects to be scaled up and down by numbers. ✔️

>>> p1 = Point(1, 2, 3)
>>> p2 = p1 * 2
>>> p2
Point(x=2, y=4, z=6)

#### Bonus 3

For the third bonus, I'd like you to allow Point objects to be unpacked using multiple assignment like this ✔️:

>>> p1 = Point(1, 2, 3)
>>> x, y, z = p1
>>> (x, y, z)
(1, 2, 3)

#### Hints

Hints for when you get stuck (hover over links to see what they're about):

[Creating a class](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&feature=youtu.be&t=99)
[Customizing string representations](https://www.pythonmorsels.com/topics/string-representations/)
[Comparing equality of tuples](https://treyhunner.com/2019/03/python-deep-comparisons-and-code-readability/#Deep_equality)
[Adding class instances](https://thepythonguru.com/python-operator-overloading/)
[Allowing objects to be multiplied by numbers](http://www.openbookproject.net/thinkcs/python/english2e/ch15.html#operator-overloading)
[Handling operations with arbitrary types](https://docs.python.org/3/library/constants.html#NotImplemented)
[Multiple assignment and tuple unpacking](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/)
[Creating objects that work with multiple assignment](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/#Generators_can_help_when_making_iterables_too)

#### Tests

Automated tests for this week's exercise can be found [here](https://www.pythonmorsels.com/exercises/8a614814784b4264b5085ed9b3358ca3/tests/). You'll need to write your class in a module named point.py next to the test file. To run the tests you'll run "python test_point.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.