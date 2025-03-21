# Cybersecurity-Agentic-AI
# 🔐 Cybersecurity Agentic AI Assistant
![Demo](assets/Agentic_AI.gif)
## 📌 Overview
The **Cybersecurity Agentic AI Assistant** is a powerful, AI-driven research tool designed to provide accurate and up-to-date cybersecurity insights. Built with **Streamlit**, this assistant leverages multiple AI agents and tools to fetch relevant information from trusted sources.

## ⚡ Key Features
- **Multi-Agent Architecture**: Includes specialized agents for different types of queries.
- **Web Agent**: Retrieves general cybersecurity information using DuckDuckGo search.
- **Cybersecurity Agent**: Fetches in-depth cybersecurity data using Crawl4AI tools.
- **Team Agent**: Automatically routes queries to the most suitable agent.
- **Advanced AI Models**: Uses the **Qwen-2.5-32B** model for intelligent responses.
- **User-Friendly UI**: Streamlit-based interactive interface for seamless query handling.
- **Secure API Integration**: Manages API keys via environment variables for enhanced security.

## 🚀 Installation Guide
### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### Step 2: Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Environment Configuration
Create a `.env` file in the project root and add your API keys:
```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

## 🚀 Running the Application
To launch the assistant, execute the following command:
```bash
streamlit run Entersoft.py
```

## 📂 Project Dependencies
The required dependencies are listed in `requirements.txt`:
```
agno
phidata
python-dotenv
yfinance
packaging
duckduckgo-search
fastapi
uvicorn
groq
openai
streamlit
pandas
GoogleSearch
```

## 🛠 How It Works
1. **User Input**: The user enters a cybersecurity-related query.
2. **Agent Selection**: The user chooses an agent (Web Agent, Cybersecurity Agent, or Team Agent).
3. **Processing**: The selected agent processes the query using AI-powered models and search tools.
4. **Response Generation**: The assistant presents a structured, well-formatted response.

## 🔮 Future Enhancements
- Integration of additional AI models for enhanced insights.
- Advanced data visualization capabilities.
- Expanded security-related knowledge base.
- Real-time threat intelligence monitoring.

## 🤝 Contributing
We welcome contributions! If you have feature suggestions or improvements, feel free to submit an issue or a pull request.
