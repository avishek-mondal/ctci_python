import typing as ty

import tlog


def main():
    maze = [
        [True, True, True, False],
        [False, True, True, False],
        [False, False, True, True],
    ]
    path = []
    failed_points = set()
    if get_path(
        maze=maze,
        row=len(maze) - 1,
        col=len(maze[0]) - 1,
        path=path,
        failed_points=failed_points,
    ):
        print(path)
    else:
        print("False")


def get_path(
    maze: ty.List[ty.List],
    row: int,
    col: int,
    path: ty.List,
    failed_points: ty.Set[ty.Tuple],
):
    if out_of_range(maze, row, col) is False or maze[row][col] is False:
        tlog.info(
            (
                f"out_of_range = {out_of_range(maze, row, col)} "
                f"and maze[row][col] = {maze[row][col]}"
            )
        )
        return False

    point = (row, col)
    if point in failed_points:
        return False

    is_at_origin = row == 0 and col == 0

    if (
        is_at_origin
        or get_path(
            maze=maze,
            row=row - 1,
            col=col,
            path=path,
            failed_points=failed_points,
        )
        or get_path(
            maze=maze,
            row=row,
            col=col - 1,
            path=path,
            failed_points=failed_points,
        )
    ):
        path.append(point)
        return True

    failed_points.add(point)
    return False


def out_of_range(maze: ty.List[ty.List], row: int, col: int):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0])
