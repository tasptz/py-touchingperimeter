# py-touchingperimeter
A naive implementation of the [touching perimeter packing algorithm](http://www.numdam.org/article/RO_2012__46_1_41_0.pdf) in python.
The `example.py` script runs a simple matplotlib animation showing the packing process.
# Algorithm
A list of rectangles representing the **free space** is maintained. For each **box**
the free space with the maximum touching perimeter (left plus bottom) is chosen
and the free space updated. The touching perimeter is calculated against previously
packed boxes and the initial free space rectangle.

![Example][example]

[example]: example.png
