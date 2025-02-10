from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode
from langgraph.checkpoint.memory import MemorySaver

from typing import Dict, List, Union

from langchain_openai import ChatOpenAI

from arithmetics import add, subtract, multiply, divide, power, run_code, get_calculator_locals, get_calculator_globals, get_calculator_all, codeExecutor

tools = [add, subtract, multiply, divide, power, run_code, get_calculator_locals, get_calculator_globals, get_calculator_all]

llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)

# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing EDA.")

class CalculatorSchema(MessagesState):
    execution_environment: Dict

# class CalculatorSchema(Dict):
#     messages: List[Union[AIMessage, HumanMessage, SystemMessage]]
#     execution_environment: Dict

# Node
def assistant(state: CalculatorSchema):
   return {
       "messages": [llm_with_tools.invoke([sys_msg] + state["messages"])],
       "execution_environment": codeExecutor.get_locals(),
       }

# Graph
builder = StateGraph(MessagesState)

# Define nodes: these do the work
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Define edges: these determine how the control flow moves
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")

memory = MemorySaver()

calculator_agent = builder.compile(checkpointer=memory)

