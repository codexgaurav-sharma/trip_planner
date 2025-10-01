from utils.model_loader import ModelLoader
from propmt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather_search_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.currency_converter_tool import CurrencyConverterTool
from tools.calculator_tool import CalculatorTool



class GraphBuilder():
    def __init__(self, model_provider: str = "openai"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        self.tools = []
        self.weather_tool = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.curreny_converter_tool = CurrencyConverterTool()
        
        self.tools.extend([*self.weather_tool, *self.place_search_tools,
                          *self.calculator_tools, *self.curreny_converter_tool])
        
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        self.graph = None
        self.system_prompt = SYSTEM_PROMPT
    
    def agent_function(self, state: MessagesState):
        """Main agent Function"""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"message": [response]}
    
    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)
        
        self.graph = graph_builder.compile()
        
        return self.graph
        
    
    def __call__(self):
        return self.build_graph()