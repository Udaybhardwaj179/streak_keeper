import os

from dotenv import load_dotenv
from groq import Groq

from ai.prompts import build_prompt

load_dotenv()


class AISolver:

    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = os.getenv(
            "MODEL_NAME",
            "llama-3.3-70b-versatile"
        )

    def solve(self, problem, language="cpp"):

        prompt = build_prompt(problem, language)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert competitive programmer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content.strip()