import os
from datetime import datetime, timezone

import httpx
from dotenv import load_dotenv

load_dotenv()


LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME")
LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRF_TOKEN = os.getenv("CSRF_TOKEN")


class LeetCodeActivity:

    GRAPHQL_URL = "https://leetcode.com/graphql"

    def __init__(self):
        self.client = httpx.Client(
            headers={
                "Content-Type": "application/json",
                "Referer": "https://leetcode.com",
                "Origin": "https://leetcode.com",
                "x-csrftoken": CSRF_TOKEN,
            },
            cookies={
                "LEETCODE_SESSION": LEETCODE_SESSION,
                "csrftoken": CSRF_TOKEN,
            },
            timeout=30,
        )

    def has_solved_today(self):

        query = """
        query recentAcSubmissionList($username: String!) {
          recentAcSubmissionList(username: $username) {
            title
            titleSlug
            timestamp
          }
        }
        """

        response = self.client.post(
            self.GRAPHQL_URL,
            json={
                "query": query,
                "variables": {
                    "username": LEETCODE_USERNAME
                }
            },
        )

        if response.status_code != 200:
            print("❌ Failed to contact LeetCode")
            print(response.text)
            return False

        data = response.json()

        submissions = data["data"]["recentAcSubmissionList"]

        today = datetime.now(timezone.utc).date()

        for submission in submissions:

            submit_date = datetime.fromtimestamp(
                int(submission["timestamp"]),
                tz=timezone.utc,
            ).date()

            if submit_date == today:

                print("✅ LeetCode solved today!")
                print(f"Problem : {submission['title']}")
                print(f"Slug    : {submission['titleSlug']}")
                return True

        print("❌ No accepted submission today.")
        return False