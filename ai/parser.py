def extract_code(response: str) -> str:
    """
    Removes Markdown code fences if present.
    """

    response = response.strip()

    if response.startswith("```"):
        lines = response.splitlines()

        # Remove first line (```cpp)
        lines = lines[1:]

        # Remove last line (```)
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        return "\n".join(lines).strip()

    return response