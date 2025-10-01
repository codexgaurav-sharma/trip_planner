import os 
from utils.place_info_search import TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

class PlaceSearchTool:
    def __init__(self):
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()
        
    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        
        @tool
        def search_attractions(place: str) -> str:
            """Search attractions of a place"""
            try:
                attraction_result = self.tavily_search.search_place_attraction(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by Tavily: {attraction_result}"
                
            except Exception as e:
                return f"Cann't find the details due to this error:- {e}"
            
            
        @tool
        def search_restaurants(place: str) -> str:
            """Search restaurants of a place"""
            try:
                restaurant_result = self.tavily_search.search_place_restaurant(place)
                if restaurant_result:
                    return f"Following are the restaurants of {place} as suggested by Tavily: {restaurant_result}"
            except Exception as e:
                return f"Cann't find the details due to this error:- {e}"
            
        @tool
        def search_activities(place: str) -> str:
            """Search activities of a place"""
            try:
                activity_result = self.tavily_search.search_place_activity(place)
                if activity_result:
                    return f"Following are the activities of {place} as suggested by Tavily: {activity_result}"
            except Exception as e:
                return f"Cann't find the details due to this error:- {e}"
            
        @tool
        def search_transportation(place: str) -> str:
            """Search transportation of a place"""
            try:
                transport_result = self.tavily_search.search_place_transportation(place)
                if transport_result:
                    return f"Following are the transportation options of {place} as suggested by Tavily: {transport_result}"
            except Exception as e:
                return f"Cann't find the details due to this error:- {e}"   
            
        
        return [search_attractions, search_restaurants, search_activities, search_transportation]