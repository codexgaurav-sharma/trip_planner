from utils.flight_checker import FlightChecker
from dotenv import load_dotenv
import os
from typing import List
from langchain.tools import tool
from model.flight_model import Flight


class FlightAvailability:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("FLIGHT_API_KEY")
        self.fc = FlightChecker(api_key=self.api_key)
        self.flight_tool_list = self._setup_flights()
    
    def __iter__(self):
        """Allow iteration over the underlying tool list."""
        return iter(self.flight_tool_list)
    
    def _setup_flights(self) -> List:
            """Setup all tools for the check the flights availability tool"""     
            
            @tool
            def flight_availability_tool(flight: Flight):
                """Check the flight availabilty and return a list of available flights with affordable price"""
                
                return self.fc.check_flight_availability(flight=flight)
            
            return [flight_availability_tool]