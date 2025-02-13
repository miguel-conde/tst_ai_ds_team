from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, AnyMessage
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
sys_message = """
"You are a helpful assistant tasked with performing arithmetic operations. 
You can use the following operations: addition, subtraction, multiplication, division, and power. 

You can also run tour own code. You can do so by:

1 - Using 'run_code' 
2 - Then use `print_var` the times you need to get the variable(s) of your interest in order to fulfill the task or the user's request.


As far as now, these are the local variables you can access:

{locals}

And these are the global variables you can access:

{globals}
"""


# class CalculatorSchema(MessagesState):
#     execution_environment: Dict

class CalculatorSchema(Dict):
    messages: List[AnyMessage]
    execution_environment: Dict
    summary: str
    
def assistant(state: CalculatorSchema):
    
    sys_msg = SystemMessage(content=sys_message.format(locals = codeExecutor.get_locals(), globals = codeExecutor.get_globals()))
    
    return {
       "messages": [llm_with_tools.invoke([sys_msg] + state["messages"])],
       "execution_environment": get_calculator_all(),
       }

# Node
def summarizer(state: CalculatorSchema):
    
    summary = state.get("summary", "")
    
    if summary:
        sys_message_to_use = sys_message + f"\n\nFinally, this is the summary of conversation earlier: {summary}"
        
        # Append summary to any newer messages
        messages = [SystemMessage(content=sys_message_to_use)] + state["messages"]
    else:
        sys_message_to_use = sys_message
        
        messages = state["messages"]
    
    sys_msg = SystemMessage(content=sys_message_to_use.format(locals = codeExecutor.get_locals(), globals = codeExecutor.get_globals()))
    
    return {
       "messages": [llm_with_tools.invoke([sys_msg] + messages)],
       "execution_environment": get_calculator_all(),
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

