# DataScribe: An AI-Powered Multi-Agent System for Natural Language Exploration of Relational Databases

## Overview

DataScribe is an innovative Artificial Intelligence (AI) powered system designed to simplify interaction with SQLite databases through a natural language interface. This project addresses the complexity of traditional SQL querying and intricate database schemas by employing a multi-agent architecture. DataScribe empowers users, regardless of their technical proficiency, to intuitively explore database structures, visualize schema, and extract information using conversational queries.

## Key Features

* **Natural Language Interface:** Interact with your SQLite databases using plain English questions, eliminating the need for SQL knowledge.
* **Multi-Agent System:**
    * **Discovery Agent:** Automatically extracts and visualizes database schemas, presenting a clear graphical representation of tables and their relationships.
    * **Planner Agent:** Leverages the high-performance Groq API to formulate efficient execution plans for complex user queries.
    * **Inference Agent:** Translates natural language questions into precise and executable SQL queries.
* **High-Performance LLM Integration:** Seamlessly integrates Large Language Models (LLMs) via the Groq API for rapid and accurate natural language understanding and SQL generation.
* **Intuitive Schema Visualization:** Generates visual graphs of database schemas, making complex structures easy to understand at a glance.
* **Automated SQL Generation & Execution:** From natural language to executed SQL, DataScribe automates the entire querying process.

## Architecture

DataScribe's architecture is built around three core intelligent agents that work synergistically:

1.  **Discovery Agent:** Responsible for inspecting the uploaded SQLite database, extracting its schema (tables, columns, primary keys, foreign keys), and generating a graphical representation for visualization.
2.  **Planner Agent:** Takes the user's natural language query and the database schema, then consults an LLM (via Groq API) to devise an optimal plan for retrieving the requested information.
3.  **Inference Agent:** Based on the user's query and the schema, this agent utilizes an LLM (via Groq API) to translate the natural language question into an executable SQL statement.

The generated SQL is then executed against the SQLite database, and the results are presented to the user.

## Technologies Used

* **Python:** The core programming language for the system.
* **Large Language Models (LLMs):** Powered by models accessible via the Groq API for natural language understanding and SQL generation.
* **Groq API:** Utilized for high-speed LLM inference, ensuring responsive interactions.
* **SQLite:** The supported database type for exploration and querying.
* **Streamlit:** For building the interactive web-based user interface.
* **SQLAlchemy:** For robust database interaction and schema inspection.
* **Pandas:** For efficient data manipulation and displaying query results.
* **NetworkX:** For creating and manipulating graph structures for schema visualization.
* **Matplotlib:** For rendering the graphical schema visualizations.

## Setup and Installation

To set up DataScribe locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/prasadingavale417/DataScribe.git](https://github.com/prasadingavale417/DataScribe.git)
    cd DataScribe
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure `requirements.txt` contains all the listed technologies: `streamlit`, `groq`, `sqlalchemy`, `pandas`, `networkx`, `matplotlib`, `python-dotenv` if using env variables, etc.)

4.  **Set up Groq API Key:**
    Obtain an API key from the [Groq Console](https://console.groq.com/).
    Create a `.env` file in the root directory of the project and add your API key:
    ```
    GROQ_API_KEY="your_groq_api_key_here"
    ```

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    (Assuming `app.py` is your main Streamlit application file.)

2.  **Upload your SQLite database:**
    Once the Streamlit application is running, it will open in your web browser. You will find an option to upload your SQLite database file (.db or .sqlite).

3.  **Interact with DataScribe:**
    After uploading the database, the Discovery Agent will automatically visualize the schema. You can then use the natural language input field to ask questions about your database (e.g., "Show me all doctors," "What are the appointments for patient ID 10?").

## Project Status

This project is currently under active development. Future enhancements will focus on expanding compatibility with other database systems, improving handling of more complex analytical queries, and refining the user experience.

## Contributing

Contributions to DataScribe are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE.md). (If you have a LICENSE.md file, otherwise specify the license directly or omit if not applicable yet).

## Contact

Prasad Ingavale
Master of Computer Application
D Y Patil International University
Email: prasadingavale417@gmail.com