from agents.privacy_agent import PrivacyPreservingAgent
from agents.llm_agent import LLMAgent

class MultiAgentWorkflow:
    def __init__(self):
        self.privacy_agent = PrivacyPreservingAgent()
        self.llm_agent = LLMAgent()

    def run(self, input_text: str) -> str:
        deidentified_text = self.privacy_agent.deidentify_text(input_text)
        llm_response = self.llm_agent.process_text(deidentified_text)
        return llm_response
