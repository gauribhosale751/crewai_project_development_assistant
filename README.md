# CrewAI Multi-Agent Project Development Assistant

A Streamlit application that coordinates six CrewAI agents to generate:
1. Software requirements
2. Solution architecture and database design
3. Prototype source code
4. Test plan and code review
5. Technical documentation
6. Academic project report

## Recommended environment

Use **Python 3.12** in a virtual environment. Newer Python versions may not yet be supported by every dependency.

### Windows PowerShell

```powershell
cd crewai_project_development_assistant
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If `py -3.12` is unavailable, install Python 3.12 first.

## Configure Groq

1. Copy `.env.example` to `.env`.
2. Add your own Groq API key to `GROQ_API_KEY`.
3. Set `GROQ_MODEL` to a model ID currently enabled for your Groq account.

Never upload `.env` or share your API key. The app also allows entering the key in the sidebar.

## Run

```powershell
streamlit run app.py
```

Open the local URL printed by Streamlit, usually http://localhost:8501.

## Output

Generated files are saved under `outputs/<project>_<timestamp>/`. Use the in-app ZIP download to collect all deliverables.

## Safety

The application does **not** execute AI-generated prototype code. For Python output, it only uses `ast.parse` to check syntax, which does not run the code. Review generated code manually and test it in a disposable virtual machine or isolated container before use.

## Notes

- CrewAI tasks run sequentially, passing earlier task outputs to later agents.
- The generated prototype is a starting point, not a guarantee of production readiness.
- Check the current Groq model catalog if a model ID is unavailable.
