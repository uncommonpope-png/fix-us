import logging
import os
from pathlib import Path
from master_soul.muscles.registry import Skill

logger = logging.getLogger("CoderSkill")

class CoderSkill(Skill):
    name = "code_engineer"
    description = "Autonomous repository engineering: reading, writing, and fixing code."

    async def execute(self, action: str, filepath: str, content: str = None) -> str:
        """
        Actions: 'read', 'write', 'fix' (requires search/replace logic)
        """
        path = Path(filepath)

        try:
            if action == "read":
                if path.exists():
                    with open(path, "r", encoding="utf-8") as f:
                        return f.read()
                return f"Error: File {filepath} not found."

            elif action == "write":
                path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                return f"Successfully wrote to {filepath}"

            elif action == "fix":
                # Conceptually: uses Ollama to propose a fix, then writes it
                logger.info(f"Engineering fix for {filepath}...")
                return f"Fix protocol initiated for {filepath} (Ollama coordination needed)"

            return f"Unknown code action: {action}"
        except Exception as e:
            logger.error(f"Code engineering failed: {e}")
            return f"Error: {str(e)}"
