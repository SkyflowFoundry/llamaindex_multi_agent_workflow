from llama_index.llms.openai import OpenAI
from llama_index.core.prompts import PromptTemplate


class LLMAgent:
    def __init__(self, model_name: str = "gpt-4"):
        self.llm = OpenAI(model=model_name)

    def process_text(self, text: str) -> str:
        print(text)
        prompt = PromptTemplate(template=text)
        response = self.llm.predict(prompt)
        return response
