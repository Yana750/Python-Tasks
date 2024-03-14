def calculate_mean_and_variance(numbers):
    """Calculate the mean and variance of a list of numbers.

    Parameters:
    numbers (list): A list of numbers

    Returns:
    tuple: A tuple containing the mean and variance of the numbers
    """
    # Calculate the mean
    mean = sum(numbers) / len(numbers)

    # Calculate the variance
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

    return mean, variance

# Example usage
numbers = [400633.4, 0.9, 78044, 20, 375.80, 699.1, 925, 24.4, 1152401, 25372, 23098.3, 11.5, 23895, 45.4, 736.4, 3.4, 5, 12.8, 33.1, 10456, 32.463, 253670, 1548]
mean, variance = calculate_mean_and_variance(numbers)
print(f"Белгородская область")
print(f"Mean: {mean}, Variance: {variance}")