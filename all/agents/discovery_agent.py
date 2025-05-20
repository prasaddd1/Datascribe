
from utils.database_utils import extract_schema
from utils.graph_utils import create_graph, visualize_graph
from utils.prompt_utils import get_discovery_prompt
import streamlit as st
from groq import Groq

class DiscoveryAgent:
    def __init__(self, engine, groq_api_key):
        self.engine = engine
        self.schema = extract_schema(engine)
        self.graph = create_graph(self.schema)
        self.client = Groq(api_key=groq_api_key)
        self.model_name = "gemma2-9b-it"
        
        

    def discover(self, user_query):
        if "schema" in user_query.lower():
            self.show_schema()
            return "Schema displayed"
        elif "graph" in user_query.lower():
            self.show_graph()
            return "Graph displayed"
        else:
            
            # Use the Groq client to generate the response
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": f"{get_discovery_prompt()}\nUser Query: {user_query}"}]
            )
            return response.choices[0].message.content
    def show_schema(self):
        st.json(self.schema)

    def show_graph(self):
        visualize_graph(self.graph)