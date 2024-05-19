"""Contain functions related to Prompting."""


def prompt(unstructured_input: str) -> str:
    """Prompts the user for unstructured input and returns a formatted string.

    Args:
    ----
        unstructured_input (str): The unstructured input provided by the user.

    Returns:
    -------
        str: A formatted string containing information about flats in Berlin and an "Anschreiben" section.

    """
    return f"""You are a bot generating inquiries about flats in Berlin that are available on the market. Always anwser in german.
        FLAT CONTEXT:
        {unstructured_input}

        ANSCHREIBEN:
        """
