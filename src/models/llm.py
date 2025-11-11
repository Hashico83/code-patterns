
# src/models/llm.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

class LLMClient:
    def __init__(self, model: str):
        """
        Initialize with the model type.
        Supported values: 'gemini', 'chatgpt'
        """
        self.model = model.lower()
        if self.model not in ["gemini", "chatgpt"]:
            raise ValueError("Model must be either 'gemini' or 'chatgpt'")

    def _get_api_key(self):
        """
        Validate API key based on model type.
        """
        if self.model == "gemini":
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("GOOGLE_API_KEY environment variable not set.")
            return api_key
        elif self.model == "chatgpt":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY environment variable not set.")
            return api_key

    def call_gemini(self, prompt: str) -> str:
        """
        Calls Gemini API via LangChain.
        """
        if self.model != "gemini":
            raise RuntimeError("This instance is not configured for Gemini")

        self._get_api_key()  # Validate key
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")  # or gemini-1.5-pro
        response = llm.invoke(prompt)
        return response.content

    def call_chatgpt(self, prompt: str) -> str:
        """
        Calls ChatGPT API via LangChain.
        """
        if self.model != "chatgpt":
            raise RuntimeError("This instance is not configured for ChatGPT")

        self._get_api_key()  # Validate key
        llm = ChatOpenAI(model="gpt-4o-mini")  # or gpt-4, gpt-3.5-turbo
        response = llm.invoke(prompt)
        return response.content

    # def call(self, prompt: str) -> str:
    #     """
    #     Unified call method for simplicity.
    #     """
    #     if self.model == "gemini":
    #         return self.call_gemini(prompt)
    #     elif self.model == "chatgpt":
    #         return self.call_chatgpt(prompt)
