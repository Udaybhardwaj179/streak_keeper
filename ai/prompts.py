def build_prompt(problem, language):

    return f"""
You are an expert competitive programmer.

Solve the following LeetCode problem.

Title:
{problem["title"]}

Difficulty:
{problem["difficulty"]}

Problem Statement:
{problem["content"]}

Requirements:

- Language: {language}
- Use the most optimal algorithm.
- Return ONLY the code.
- No markdown.
- No explanations.
- The code must compile on LeetCode.
"""