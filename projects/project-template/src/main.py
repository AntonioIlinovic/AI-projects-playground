"""
Main entry point for the AI project.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main():
    """Main function."""
    print("Hello from your AI project!")
    
    # Example of using environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("OpenAI API key is configured")
    else:
        print("OpenAI API key not found in environment")
        

if __name__ == "__main__":
    main()
