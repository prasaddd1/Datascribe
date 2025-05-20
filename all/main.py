import streamlit as st
import os
from agents.discovery_agent import DiscoveryAgent
from agents.inference_agent import InferenceAgent
from agents.planner_agent import PlannerAgent
from utils.database_utils import get_db_engine, extract_schema
import pandas as pd
from groq import Groq

GROQ_API_KEY = "gsk_yVFScGgXDGoKnZ6QYvsuWGdyb3FYC6jyCd78kiAC9P##########"

st.title("DataScribe: AI-Powered Schema Explorer")
st.sidebar.header("Configure Database")

db_file = st.sidebar.file_uploader("Upload SQLite Database", type=["sqlite", "db"])
if db_file:
    db_path = "uploaded_db.sqlite"
    with open(db_path, "wb") as f:
        f.write(db_file.getbuffer())

    engine = get_db_engine(db_path)
    schema = extract_schema(engine)

    discovery_agent = DiscoveryAgent(engine, GROQ_API_KEY)
    inference_agent = InferenceAgent(engine, schema, GROQ_API_KEY)
    planner_agent = PlannerAgent(GROQ_API_KEY)

    st.subheader("🛠️ Extracted Database Schema")
    discovery_agent.show_schema()

    st.subheader("🔗 Database Schema Graph")
    discovery_agent.show_graph()

    st.subheader("💬 Ask Your Database ")
    user_query = st.text_input("Enter your question:")
    if st.button("Run Agents"):
        if user_query:
            # Call the query method of the InferenceAgent
            sql_query = inference_agent.query(user_query)
            st.code(sql_query, language="sql")

            # Execute SQL Query
            try:
                df = pd.read_sql(sql_query, engine)
                st.dataframe(df)
            except Exception as e:
                st.error(f"❌ SQL Error: {e}")
          








          
