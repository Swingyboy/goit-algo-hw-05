from typing import List, Optional, Tuple


def binary_search(arr: List[float], x: float) -> Tuple[int, float]:
    left: int = 0
    right: int = len(arr) - 1
    iterations: int = 0
    upper_bound: Optional[float] = None

    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1

        # Check if x is present at mid
        if arr[mid] == x:
            return (iterations, arr[mid])

        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1

        # If x is smaller, ignore right half
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # If x is not present in the array, return the upper bound
    return (iterations, upper_bound)
