import os
from datetime import datetime, timezone

import httpx
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Repository to monitor
REPO_NAME = "streak_keeper"


class GitHubService:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
        }

    def verify_token(self):
        response = httpx.get(
            f"{self.BASE_URL}/user",
            headers=self.headers,
        )

        if response.status_code == 200:
            data = response.json()
            print("✅ GitHub Authentication Successful")
            print(f"Logged in as: {data['login']}")
            return True

        print("❌ Authentication Failed")
        print(response.text)
        return False
        
    def has_commit_today(self):
        today_start = datetime.now(timezone.utc).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

        print("\n🔍 Checking today's commits...\n")

        response = httpx.get(
            f"{self.BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}/commits",
            headers=self.headers,
            params={
                # "author": GITHUB_USERNAME,
                "since": today_start.isoformat(),
            },
        )

        if response.status_code != 200:
            print("❌ Failed to fetch commits")
            print(response.text)
            return False

        commits = response.json()

        if not commits:
            print(f"❌ No commits found today in '{REPO_NAME}'.")
            return False

        print(f"✅ {len(commits)} commit(s) found today in '{REPO_NAME}'\n")

        for i, commit in enumerate(commits, start=1):
            message = commit["commit"]["message"]
            sha = commit["sha"][:7]
            date = commit["commit"]["author"]["date"]

            print(f"{i}. {message}")
            print(f"   SHA : {sha}")
            print(f"   Time: {date}\n")

        return True



if __name__ == "__main__":
    github = GitHubService()

    if github.verify_token():
        github.has_commit_today()