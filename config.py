from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME")
LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRF_TOKEN = os.getenv("CSRF_TOKEN")

REPO_PATH = os.getenv("REPO_PATH")

DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "cpp")

RUN_TIME = os.getenv("RUN_TIME", "23:40")