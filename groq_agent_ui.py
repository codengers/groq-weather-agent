import streamlit as st
from langchain_groq import ChatGroq
from langchain.agents import Tool, initialize_agent, AgentType
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

st.set_page_config(page_title="Weather Agentic Assistant 🚀", layout="centered")

st.title("🤖 Weather Agent")
st.markdown("Type a question and let Groq LLM respond intelligently!")

user_input = st.text_input("Enter your query:", "")

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.2,
    api_key=os.environ.get("GROQ_API_KEY")
)

def add_two_numbers(text: str) -> str:
    try:
        a, b = map(int, text.split(','))
        return str(a + b)
    except:
        return "Please input two comma-separated integers like: 3,5"

def get_my_name(text: str) -> str:
    output = "I am your friendly weather agent."
    return output

def get_city_temperature(text: str) -> str:
    """Get the current temperature in a given city."""
    api_key = os.environ.get("WEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": text,
        "appid": api_key,
        "units": "metric"
        }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data.get("main"):
            temperature = data["main"]["temp"]
            data = {
                "input": "what is temperature of bangalore now?",
                "output": "The current temperature in {} is {}°C.".format(text, temperature)
            }
            return data["output"]
            #return f"The current temperature in {text} is {temperature}°C."
        else:
            return "Unable to retrieve temperature for {text}."
    except Exception as e:
        return f"An error occurred: {e}"
                
    
tools = [
    Tool(
        name="AddTwoNumbers",
        func=add_two_numbers,
        description=(
        "Use this tool add numbers. Understand the user question and answer accordingly."
        "Questions like 'what is the sum of two numbers 4, 5?' or 'what is the result of adding 2, 9?'"
        "should use this tool"

        )
    ),
    Tool(
        name="Provide my name",
        func=get_my_name,
        description=("Use this tool to answer your system or user details"
                     "Questions like this 'Who are you?' or 'What is your name?' or 'How old are you?'"
                     "should use this tool")
    ),
    Tool(
    name="CityTemperature",
    func=get_city_temperature,
    description=(
        "Use this tool to get the current temperature of a city. "
        "Provide the name of the city like 'London', 'Mumbai', or 'New York'. "
        "Questions like 'What's the temperature in Paris?' or 'How hot is it in Tokyo?' or 'what is sum of temperature of Bangalore and Chennai?' "
        "should use this tool."
    )
)
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

if user_input:
    with st.spinner("Thinking..."):
        response = agent.invoke(user_input)
        st.success(response)
