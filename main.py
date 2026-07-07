from github.github_service import GitHubService
from leetcode.activity import LeetCodeActivity
from leetcode.daily_problem import DailyProblemService
from ai.solver import AISolver
from ai.parser import extract_code
def print_banner():
    print("=" * 50)
    print("               STREAKFORGE")
    print("=" * 50)


def main():

    print_banner()

    github = GitHubService()

    if not github.verify_token():
        return

    print()

    github_status = github.has_commit_today()

    print()

    leetcode = LeetCodeActivity()

    leetcode_status = leetcode.has_solved_today()

    print("\n==============================")

    print(f"GitHub   : {'✅' if github_status else '❌'}")
    print(f"LeetCode : {'✅' if leetcode_status else '❌'}")

    print("==============================")
    daily = DailyProblemService()
    problem = daily.fetch_daily_problem()
    print("\nToday's Daily Challenge")
    print("=" * 40)
    print(f"Title      : {problem['title']}")
    print(f"Difficulty : {problem['difficulty']}")
    print(f"Slug       : {problem['slug']}")
    print(f"Tags       : {', '.join(problem['tags'])}")
    print(f"Content    : {problem['content'][:200]}...")  # Print first 200 chars of content
    solver = AISolver()
    solution = solver.solve(problem)
    print(solution)
    

print("=" * 40)


if __name__ == "__main__":
    main()