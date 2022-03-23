import unittest
import typing as ty


def main():
    unittest.main()


def paint_fill(
    screen: ty.List[ty.List], r: int, c: int, new_colour: int
) -> ty.List[ty.List]:
    if screen[r][c] == new_colour:
        return
    old_colour = screen[r][c]
    flood_fill(screen, r, c, old_colour, new_colour)
    return screen


def flood_fill(
    screen: ty.List[ty.List], r: int, c: int, old_colour: int, new_colour: int
):
    if not is_in_range(screen, r, c) or screen[r][c] != old_colour:
        return

    screen[r][c] = new_colour
    dels = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in dels:
        flood_fill(
            screen=screen,
            r=r + dr,
            c=c + dc,
            old_colour=old_colour,
            new_colour=new_colour,
        )


def is_in_range(screen, r, c):
    return 0 <= r < len(screen) and 0 <= c < len(screen[0])


class Test(unittest.TestCase):
    test_cases = [
        (
            [[1, 2, 5], [2, 2, 4], [2, 8, 6]],
            1,
            1,
            3,
            [[1, 3, 5], [3, 3, 4], [3, 8, 6]],
        )
    ]
    testable_functions = [paint_fill]

    def test_paint_fill(self):
        for f in self.testable_functions:
            for [screen, r, c, new_color, expected] in self.test_cases:
                assert f(screen, r, c, new_color) == expected


if __name__ == '__main__':
    main()