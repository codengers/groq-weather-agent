# 🌤️ Agentic AI with Groq + LangChain + Weather Tool

This project is a simple agentic AI application using [GroqCloud](https://groq.com), [LangChain](https://www.langchain.com/), and a weather tool powered by OpenWeatherMap. The agent can answer questions like:
> "What is the temperature of London?"

---

## 🚀 Features

- Built using LangChain's `AgentExecutor`
- Powered by Groq LLM via `ChatGroq`
- Includes a custom tool: `TemperatureChecker`
- Streamlit interface for interactive chat
- Supports natural language queries like:
  - "What's the temperature in Tokyo?"
  - "How hot is it in Bangalore?"
  - "Check weather in Paris"

---

## 🔧 Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourname/groq-weather-agent.git
cd groq-weather-agent

### 2. Create a Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set up environment variables. Create a .env file in the root directory:
GROQ_API_KEY=your-groq-api-key
OPENWEATHER_API_KEY=your-openweathermap-api-key

### 5. Run the application
streamlit run groq_agent_ui.py