from pydantic import BaseModel, Field
from typing import Literal, Optional, Any
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from utils.config_loader import load_config


load_dotenv()



class ConfigLoader:
    def __init__(self):
        print(f"Loading config....")
        self.config = load_config()  
        
    def __getitem__(self, key):
        return self.config[key]  
    
    
class ModelLoader(BaseModel):
    model_provider: Literal["openai"] = "openai"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)
    
    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()
        
    class Config:
        arbitrary_types_allowed = True
        
    def load_llm(self):
        """
        Load and return the llm model.
        """
        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == 'openai':
            print("Loading LLM from OpenAI.........")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            openrouter_url = os.getenv("OPENROUTER_BASE_URL")
            model_name = self.config["llm"]["openai"]["model_nmae"]
            llm = ChatOpenAI(model_name = model_name, api_key=openai_api_key, base_url=openrouter_url)
        elif self.model_provider == "groq":
            print("Loading LLM from Groq..............")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm=ChatGroq(model=model_name, api_key=groq_api_key)  
            

        return llm