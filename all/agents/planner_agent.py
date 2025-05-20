
from utils.prompt_utils import get_planner_prompt
from groq import Groq

class PlannerAgent:
    def __init__(self, groq_api_key):
        self.client = Groq(api_key=groq_api_key)
        self.model_name = "gemma2-9b-it"

    def create_plan(self, user_query):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": f"{get_planner_prompt()}\nUser Query: {user_query}"}]
        )
        return response.choices[0].message.content  