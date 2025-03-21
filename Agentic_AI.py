import os
import streamlit as st
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from phi.tools.crawl4ai_tools import Crawl4aiTools

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize Agents
web_agent = Agent(
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="qwen-2.5-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True,
)

cybersecurity_agent = Agent(
    name="Cybersecurity Agent",
    role="Get Cybersecurity data",
    model=Groq(id="qwen-2.5-32b"),
    tools=[Crawl4aiTools()],
    instructions="Give accurate answers",
    show_tool_calls=True,
    markdown=True,
)

# Team Agent (Routes tasks to the best agent)
agent_team = Agent(
    team=[web_agent, cybersecurity_agent],
    model=Groq(id="qwen-2.5-32b"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# 🌟 Streamlit UI Setup
st.set_page_config(page_title="Agentic AI Research", layout="wide")

# Title and description
st.title("🔍 Cyber Security Agentic AI Assistant")
st.markdown("Ask any question and let our cybersecurity agent provide answers!")

# User input field
query = st.text_input("💬 **Enter your question:**")

# Agent selection dropdown
selected_agent = st.selectbox("🤖 **Select an Agent:**", ["Web Agent", "Cybersecurity Agent", "Agent Team"])

# Submit button
if st.button("🚀 **Get Answer**"):
    if query:
        with st.spinner("🔎 Searching..."):
            # Choose the appropriate agent
            if selected_agent == "Web Agent":
                response_obj = web_agent.run(query)
            elif selected_agent == "Cybersecurity Agent":
                response_obj = cybersecurity_agent.run(query)
            else:
                response_obj = agent_team.run(query)

            # Extract only the response text
            response_text = response_obj.content if hasattr(response_obj, "content") else str(response_obj)

        # Display the extracted response
        if response_text:
            st.markdown("### 📌 **Response:**")
            st.markdown(response_text, unsafe_allow_html=True)
        else:
            st.error("❌ No response received. Please check API keys and agent setup.")
    else:
        st.warning("⚠️ Please enter a question before submitting.")

# Run the script using: `streamlit run Entersoft.py`
