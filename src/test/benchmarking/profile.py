import timeit


def profile_model():
    """Return a random sample from the given list based on confidence level and interval

    Takes the desired confidence level and confidence interval to derive an appropriate
    sample size for the population of id_list. Using that sample size, a random sample is
    selected. Supported confidence levels are: 50%, 68%, 90%, 95%, and 99%.

    Args:
        id_list (array): The full population comprised of all possible visitor ids
        confidence_level (float): The statistical confidence level desired for the sample
        confidence_interval (float): The statistical margin of error desired for the sample

    Returns:
        sample_list(array): A sample of visitor ids randomnly selected from the id_list
    """
    pass