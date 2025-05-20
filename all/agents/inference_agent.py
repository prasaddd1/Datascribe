#from langchain_google_genai import ChatGoogleGenerativeAI
from utils.database_utils import execute_sql
from utils.prompt_utils import get_inference_prompt
import pandas as pd
import json
import streamlit as st
from groq import Groq

class InferenceAgent:
    def __init__(self, engine, schema, groq_api_key):
        self.engine = engine
        self.schema = schema
        self.client = Groq(api_key=groq_api_key)
        self.model_name = "gemma2-9b-it"
        #self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=gemini_api_key)

    def query(self, user_query):
        prompt = f"{get_inference_prompt(self.schema)}\nUser Query: {user_query}"
        sql_query = ""
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            llm_response = response.choices[0].message.content
            print(f"Raw LLM Response: {llm_response}")

            if "```sql" in llm_response and "```" in llm_response.split("```sql")[-1]:
                sql_query = llm_response.split("```sql")[-1].split("```")[0].strip()
            else:
            # If no clear SQL block, return the raw response as an error
                raise ValueError(f"Could not extract SQL query from LLM response.\nRaw Response: {llm_response}")

            print(f"Extracted SQL Query: {sql_query}")
            if not sql_query.strip().upper().startswith(("SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER")):
                raise ValueError(f"Generated output is not a valid SQL query: {sql_query}")

            # Execute the SQL query
            execute_sql(sql_query, self.engine)
            return sql_query  # Return the SQL query string for display

            print(f"Extracted SQL Query: {sql_query}")  # Debugging

        except Exception as e:
            raise Exception(f"SQL Execution Error: {e}\nQuery: {sql_query}")