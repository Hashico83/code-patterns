
import sys
from src.coordinator import CoordinatorAgent

def display_intro():
    print("\n=== Multi-Agent Critique System ===")
    print("Provide a paragraph and select personas for critique.")
    print("Available personas: grammar_expert, technical_reviewer, creative_coach")
    print("Type 'done' when finished selecting personas.\n")

def get_user_input():
    paragraph = input("Enter the paragraph to critique:\n> ")
    print("\nSelect personas (type one at a time):")
    personas = []
    while True:
        persona = input("> ")
        if persona.lower() == "done":
            break
        personas.append(persona)
    return paragraph, personas

def main():
    display_intro()
    paragraph, personas = get_user_input()

    if not paragraph.strip() or not personas:
        print("Error: Paragraph and at least one persona are required.")
        sys.exit(1)

    model_choice = input("\nChoose model (chatgpt/gemini): ").strip().lower()
    if model_choice not in ["chatgpt", "gemini"]:
        print("Invalid model choice. Defaulting to chatgpt.")
        model_choice = "chatgpt"

    print("\nProcessing critique...\n")
    coordinator = CoordinatorAgent(model=model_choice)
    result = coordinator.process(paragraph, personas)

    print("\n=== FORMATTED OUTPUT ===\n")
    print(result["formatted"])

    print("\n=== RAW OUTPUT ===\n")
    print(result["raw"])

if __name__ == "__main__":
    main()
