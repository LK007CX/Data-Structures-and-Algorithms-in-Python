def binary_search(data, target, low, high):
    """Return True if targets is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False  # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of the moddle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portial right of the middle
            return binary_search(data, target, mid + 1, high)


if __name__ == "__main__":
    data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    target = 22
    result = binary_search(data, target, 0, len(data) - 1)
    print(result)