def even_factors(n):
    """Return a list of odd factors of the given number n."""
    return [i for i in range(1, n + 1, 2) if n % i == 0]
