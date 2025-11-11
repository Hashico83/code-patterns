
import yaml
import os
from typing import Dict
from src.models.llm import LLMClient

class CritiqueAgent:
    def __init__(self, model: str = "chatgpt"):
        """
        Initialize the Critique Agent with the chosen LLM model.
        """
        self.llm_client = LLMClient(model=model)

    def load_persona(self, persona_name: str) -> str:
        """
        Load persona description from YAML file.
        """
        persona_path = os.path.join("config", "personas", f"{persona_name}.yaml")
        if not os.path.exists(persona_path):
            raise FileNotFoundError(f"Persona file not found: {persona_path}")

        with open(persona_path, "r") as file:
            data = yaml.safe_load(file)
        return data.get("description", "")

    def build_initial_prompt(self, persona_description: str, paragraph: str) -> str:
        """
        Build the initial critique prompt with structured output requirement.
        """
        return (
            f"You are {persona_description}.\n"
            f"Critique the following text thoroughly:\n\"{paragraph}\"\n\n"
            "Return your critique in this structured format:\n"
            "Strengths:\n- [List strengths]\n\n"
            "Weaknesses:\n- [List weaknesses]\n\n"
            "Suggestions for Improvement:\n- [List actionable suggestions]"
        )

    def build_refinement_prompt(self, draft_critique: str) -> str:
        """
        Build the refinement prompt to improve the initial critique.
        """
        return (
            f"Here is your initial critique:\n\"{draft_critique}\"\n\n"
            "Now, review and improve your critique:\n"
            "- Make it more structured and organized.\n"
            "- Add actionable suggestions where missing.\n"
            "- Ensure clarity and depth.\n"
            "Keep the same format:\n"
            "Strengths:\n- ...\nWeaknesses:\n- ...\nSuggestions for Improvement:\n- ..."
        )

    def critique(self, persona_name: str, paragraph: str) -> Dict[str, str]:
        """
        Perform critique using self-prompting (draft + refinement).
        Returns a dictionary with persona and final critique.
        """
        persona_description = self.load_persona(persona_name)

        # Stage 1: Initial critique
        initial_prompt = self.build_initial_prompt(persona_description, paragraph)
        draft_critique = self.llm_client.call(initial_prompt)

        # Stage 2: Refinement
        refinement_prompt = self.build_refinement_prompt(draft_critique)
        final_critique = self.llm_client.call(refinement_prompt)

        return {
            "persona": persona_name,
            "critique": final_critique.strip()
        }
