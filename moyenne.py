def compute_average(numbers: list) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)