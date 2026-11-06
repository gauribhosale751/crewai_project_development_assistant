
# ============================================================
# CREWAI + GROQ API COMPATIBILITY FIX
# Project: CrewAI Project Development Assistant
# ============================================================

# IMPORTANT: This must execute before creating CrewAI agents.

import crewai.llms.cache as crewai_cache

# Disable unsupported cache breakpoint injection
crewai_cache.mark_cache_breakpoint = lambda msg: msg


# ============================================================
# IMPORTS
# ============================================================

import os
import sys
import streamlit as st

from pathlib import Path
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM, Process


# ============================================================
# ENVIRONMENT CONFIGURATION
# ============================================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please configure your .env file."
    )


# ============================================================
# GROQ LLM CONFIGURATION
# ============================================================

llm = LLM(
    model="groq/openai/gpt-oss-20b",
    api_key=GROQ_API_KEY,
    temperature=0.3
)


# ============================================================
# STREAMLIT CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CrewAI Project Development Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("CrewAI Project Development Assistant")
st.caption("Multi-Agent AI System powered by CrewAI and Groq")


# ============================================================
# USER INPUT
# ============================================================

project_topic = st.text_area(
    "Enter your project topic",
    placeholder="Example: AI-based College Admission Assistant"
)

# ============================================================
# CREWAI AGENT
# ============================================================

project_analyst = Agent(
    role="Senior Project Analyst",
    goal="Analyze project requirements and provide a detailed development plan.",
    backstory=(
        "You are an experienced software project analyst "
        "with expertise in AI and software development."
    ),
    llm=llm,
    verbose=True
)


# ============================================================
# CREWAI TASK
# ============================================================

project_task = Task(
    description=(
        "Analyze the following project topic: {project_topic}. "
        "Provide project objectives, modules, technology stack, "
        "architecture, and implementation steps."
    ),
    expected_output=(
        "A structured project development plan with objectives, "
        "modules, technology stack, architecture, and implementation steps."
    ),
    agent=project_analyst
)


# ============================================================
# CREATE CREW
# ============================================================

crew = Crew(
    agents=[project_analyst],
    tasks=[project_task],
    process=Process.sequential,
    verbose=True
)


# ============================================================
# EXECUTE CREW
# ============================================================

if st.button("Generate Project Plan", type="primary"):

    if not project_topic.strip():
        st.warning("Please enter your project topic.")

    else:
        with st.spinner("AI Agent is analyzing your project..."):

            try:
                result = crew.kickoff(
                    inputs={"project_topic": project_topic}
                )

                st.success("Project plan generated successfully!")

                st.markdown("### Generated Project Plan")

                st.write(result)

            except Exception as e:
                st.error("An error occurred while executing CrewAI.")
                st.exception(e)
                
                
# ================================================================
# PROJECT CONFIGURATION
# ================================================================

BASE_DIR = Path(__file__).resolve().parent

REPORT_DIR = BASE_DIR / "generated_reports"
REPORT_DIR.mkdir(exist_ok=True)
