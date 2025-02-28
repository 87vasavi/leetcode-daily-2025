def find_factors_basic(n):
    """
    Find all factors of a positive integer using a simple iterative approach.
    
    Args:
        n (int): A positive integer
        
    Returns:
        list: A sorted list of all factors of n
    
    Examples:
        >>> find_factors_basic(12)
        [1, 2, 3, 4, 6, 12]
        >>> find_factors_basic(13)
        [1, 13]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
        
    factors = []
    # Check all integers from 1 to n
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
            
    return factors


def find_factors_optimized(n):
    """
    Find all factors of a positive integer using an optimized approach.
    Only checks up to the square root of n.
    
    Args:
        n (int): A positive integer
        
    Returns:
        list: A sorted list of all factors of n
    
    Examples:
        >>> find_factors_optimized(12)
        [1, 2, 3, 4, 6, 12]
        >>> find_factors_optimized(13)
        [1, 13]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
        
    factors = []
    # Only need to check up to the square root of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            # Add the corresponding factor (n/i) if it's different
            if i != n // i:
                factors.append(n // i)
                
    # Return the sorted list of factors
    return sorted(factors)


def find_prime_factors(n):
    """
    Find the prime factorization of a positive integer.
    
    Args:
        n (int): A positive integer
        
    Returns:
        dict: A dictionary with prime factors as keys and their exponents as values
    
    Examples:
        >>> find_prime_factors(12)
        {2: 2, 3: 1}  # 12 = 2^2 * 3^1
        >>> find_prime_factors(60)
        {2: 2, 3: 1, 5: 1}  # 60 = 2^2 * 3^1 * 5^1
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
        
    if n == 1:
        return {}  # 1 has no prime factors
        
    prime_factors = {}
    # Check if 2 is a factor
    while n % 2 == 0:
        prime_factors[2] = prime_factors.get(2, 0) + 1
        n //= 2
        
    # Check odd numbers starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            prime_factors[i] = prime_factors.get(i, 0) + 1
            n //= i
        i += 2
        
    # If n is a prime number greater than 2
    if n > 2:
        prime_factors[n] = prime_factors.get(n, 0) + 1
        
    return prime_factors


def get_all_divisors(n, include_self=True, include_one=True):
    """
    Find all divisors (factors) of a number with options to exclude 1 and n itself.
    
    Args:
        n (int): A positive integer
        include_self (bool): Whether to include n in the returned list
        include_one (bool): Whether to include 1 in the returned list
        
    Returns:
        list: A sorted list of factors according to the specified options
    
    Examples:
        >>> get_all_divisors(12)
        [1, 2, 3, 4, 6, 12]
        >>> get_all_divisors(12, include_self=False)
        [1, 2, 3, 4, 6]
        >>> get_all_divisors(12, include_one=False)
        [2, 3, 4, 6, 12]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
        
    # Find all factors using the optimized approach
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if include_one or i != 1:
                factors.append(i)
            if i != n // i:  # Avoid duplicates for perfect squares
                if include_self or n // i != n:
                    factors.append(n // i)
                    
    return sorted(factors)


def count_factors(n):
    """
    Count the number of factors of a positive integer using prime factorization.
    
    Args:
        n (int): A positive integer
        
    Returns:
        int: The number of factors
    
    Examples:
        >>> count_factors(12)
        6  # Factors are: 1, 2, 3, 4, 6, 12
        >>> count_factors(16)
        5  # Factors are: 1, 2, 4, 8, 16
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
        
    if n == 1:
        return 1
        
    # Get prime factorization
    prime_factors = find_prime_factors(n)
    
    # For a number with prime factorization p1^a1 * p2^a2 * ... * pk^ak,
    # the number of factors is (a1+1) * (a2+1) * ... * (ak+1)
    factor_count = 1
    for exponent in prime_factors.values():
        factor_count *= (exponent + 1)
        
    return factor_count
