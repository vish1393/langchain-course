from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
import os

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set")

if not os.getenv("TAVILY_API_KEY"):
    raise ValueError("TAVILY_API_KEY is not set")

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

# ⭐ Correct: instantiate the tool
tavily_tool = TavilySearch()

tools = [tavily_tool]

agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({
        "messages": [
            HumanMessage(
                content="search for 3 job listings for an ai engineer using langchain in the bay area on linkedin and list their details"
            )
        ]
    })
    print(result)

if __name__ == "__main__":
    main()