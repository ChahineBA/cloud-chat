from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = gemini_api_key

# Initialize the Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Unified prompt for DevOps tasks
devops_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
    You are a highly skilled DevOps assistant. Your task is to help with the following request:
    Request: {query}

    Provide a detailed and accurate response, including:
    1. A clear explanation of the solution.
    2. Step-by-step instructions (if applicable).
    3. Best practices or additional tips.
    4. Code snippets (if applicable), formatted properly.

    Ensure your response is well-structured and easy to follow.
    """
)

# Add memory to the chain
devops_chain = devops_prompt | llm

# Define the DevOps assistant tool
@tool
def devops_assistant(query: str) -> str:
    """
    A unified DevOps assistant tool that handles various DevOps tasks.
    Input: A natural language query (e.g., "Generate Terraform code for an AWS S3 bucket").
    """
    # Call the chain with the user's query
    return devops_chain.run({"query": query})

# Initialize the agent with the single tool
tools = [devops_assistant]
memory = MemorySaver()
agent_executor = create_react_agent(llm, tools, checkpointer=memory)
config = {"configurable": {"thread_id": "abc123"}}
