import httpx


class DailyProblemService:
    GRAPHQL_URL = "https://leetcode.com/graphql"

    def __init__(self):
        self.client = httpx.Client(timeout=30)

    def fetch_daily_problem(self):
        query = """
        query questionOfToday {
          activeDailyCodingChallengeQuestion {
            date
            userStatus

            question {
              questionId
              questionFrontendId
              title
              titleSlug
              difficulty
              content

              topicTags {
                name
                slug
              }
            }
          }
        }
        """

        response = self.client.post(
            self.GRAPHQL_URL,
            json={"query": query},
        )

        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch daily challenge: {response.text}"
            )

        data = response.json()

        challenge = data["data"]["activeDailyCodingChallengeQuestion"]

        question = challenge["question"]

        return {
            "date": challenge["date"],
            "question_id": question["questionId"],
            "frontend_id": question["questionFrontendId"],
            "title": question["title"],
            "slug": question["titleSlug"],
            "difficulty": question["difficulty"],
            "content": question["content"],
            "tags": [tag["name"] for tag in question["topicTags"]],
        }