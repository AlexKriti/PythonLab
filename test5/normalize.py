def normalize(values: list[float | None]) -> list[float]:
    """
    Normalize numeric values to range [0, 1].
    Ignores None values.

    Raises:
        ValueError: if no valid numbers or all numbers equal.
    """
    nums = [v for v in values if v is not None]

    if not nums:
        raise ValueError("No valid numbers to normalize")

    min_v = min(nums)
    max_v = max(nums)

    if min_v == max_v:
        raise ValueError("All numbers are equal")

    result = []
    for v in values:
        if v is None:
            result.append(None)
        else:
            result.append((v - min_v) / (max_v - min_v))

    return result
