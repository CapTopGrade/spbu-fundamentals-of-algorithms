from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""

    # Sort points by x-coordinate
    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))

    # Initialize stack with first two points
    stack = [sorted_points[0], sorted_points[1]]

    # Iterate over remaining points
    for p in sorted_points[2:]:
        # Remove points from top of stack until slope is non-positive
        while len(stack) > 1 and (p[1] - stack[-1][1]) * (stack[-1][0] - stack[-2][0]) <= (
                stack[-1][1] - stack[-2][1]) * (p[0] - stack[-1][0]):
            stack.pop()

        # Add current point to stack
        stack.append(p)

    # Return clockwise order of points in stack
    return np.array(stack + stack[-2::-1])


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"practicum_5/homework/points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
