from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient
import os

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    
    print(f"Searching the web for: {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")

    #result = agent.invoke({"messages":[HumanMessage(content="What is the weather in Tokyo?")]})
    result = agent.invoke({"messages":[HumanMessage(content="search for 3 job listings for an ai engineer using langchain in the bay area on linkedin and list their details")]})

    print(result)


if __name__ == "__main__":
    main()
