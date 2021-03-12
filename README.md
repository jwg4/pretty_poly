# pretty_poly - a package for displaying polyomino tilings

This is a Python package for displaying polyomino tilings, expressed as lists of lists of (x, y) tuples, in various ways.

## Example use
```
>>> from pretty_poly import make_ascii
>>> print(make_ascii([[(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 3), (1, 3), (2, 3), (1, 2)], [(1, 0), (2, 0), (3, 0), (2, 1)], [(3, 1), (3, 2), (2, 2)]]))
+-+-+-+-+
| |     |
+ +-+ +-+
|   | | |
+ +-+-+ +
| | |   |
+-+ +-+-+
|     |
+-+-+-+

```

## Example output
You can see some examples of images created using this package:
 - ![Colored squares PNG](https://jwg4.github.io/pretty_poly/right_12.png)
 - ![Outlines PNG](https://jwg4.github.io/pretty_poly/lines.png)
 - ![Thick outlines PNG](https://jwg4.github.io/pretty_poly/thick.png)

These files were created by the code in examples/make.py

## How to cite this code:
```
@misc{pretty_poly,
  author = {Jack Grahl},
  title = {pretty_poly - a package for displaying polyomino tilings},
  year = {2021},
  howpublished = {\url{https://github.com/jwg4/pretty_poly}},
  commit = {...}
}
```
