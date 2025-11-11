
def format_critiques(critiques: list) -> str:
    """
    Format multiple critiques into a clean Markdown output.
    """
    output = "# Critique Summary\n\n"
    for critique in critiques:
        persona = critique.get("persona", "Unknown Persona")
        text = critique.get("critique", "")
        output += f"## Persona: {persona}\n{text}\n\n"
    return output.strip()
