from github.github_service import GitHubService


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

    if github.has_commit_today():
        print("\n🎉 GitHub streak is safe!")
    else:
        print("\n⚠️ No commit today!")


if __name__ == "__main__":
    main()