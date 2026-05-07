import logging
from master_soul.muscles.registry import Skill

logger = logging.getLogger("SkillCreator")

class SkillCreatorSkill(Skill):
    name = "skill_creator"
    description = "Autonomous self-evolution: Generates and registers new Python skills for the entity."

    async def execute(self, skill_name: str, purpose: str, master=None) -> str:
        """
        Uses Ollama to generate Python code for a new skill, then saves it and registers it.
        """
        if not master:
            return "Error: Master Entity reference missing."

        logger.info(f"🧬 Evolving new skill: {skill_name} for {purpose}...")

        prompt = f"""
        Generate a Python class for a new AI skill named '{skill_name}' for the following purpose: {purpose}.
        The class must inherit from `Skill` and follow this structure:

        import logging
        from master_soul.muscles.registry import Skill

        class {skill_name}Skill(Skill):
            name = "{skill_name.lower()}"
            description = "{purpose}"
            async def execute(self, **kwargs):
                # Implementation here
                return "Skill executed"

        Return ONLY the Python code.
        """

        # 1. Generate code using deep reasoning
        code = await master.skills.run_skill("ollama_thought", prompt=prompt, task_type="code")

        if not code or "Error" in code:
            return "Error: Code generation failed."

        # 2. Save the code to a new file
        filepath = f"master_soul/muscles/skills/system/auto_{skill_name.lower()}.py"
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(code)
            logger.info(f"Saved new skill to {filepath}")

            # 3. Inform the user/log that a restart or dynamic import is needed
            # For now, we confirm the file creation
            return f"Success: New skill '{skill_name}' created at {filepath}. It will be available on the next awakening."
        except Exception as e:
            return f"Error: Failed to save skill file. {str(e)}"
