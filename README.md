# 🌍 Travel Planner Agentic Application

An AI-powered travel planning application that helps users create comprehensive travel itineraries using real-time data from various APIs.

## Features

- **Weather Information**: Get current weather and forecasts for destinations
- **Place Search**: Find attractions, restaurants, activities, and transportation options
- **Currency Conversion**: Convert between different currencies for budget planning
- **Expense Calculation**: Calculate trip costs and daily budgets
- **AI Agent**: Intelligent travel planning with LangGraph workflow

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env`:
```
OPENAI_API_KEY=your_openai_api_key
OPENROUTER_BASE_URL=your_openrouter_url (optional)
GROQ_API_KEY=your_groq_api_key (optional)
OPENWEATHERMAP_API_KEY=your_weather_api_key
EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

### Run the FastAPI backend:
```bash
uvicorn main:app --reload
```

### Run the Streamlit frontend:
```bash
streamlit run app.py
```

## API Endpoints

- `POST /query`: Submit a travel planning query

## Project Structure

- `agent/`: LangGraph workflow implementation
- `tools/`: Various tools for weather, places, currency, etc.
- `utils/`: Utility functions and API wrappers
- `config/`: Configuration files
- `propmt_library/`: System prompts for the AI agent

## Recent Bug Fixes

- Fixed typos in configuration files
- Corrected method name mismatches
- Fixed return type annotations
- Improved error handling
- Added missing imports
- Fixed markdown formatting issues