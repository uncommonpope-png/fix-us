import logging
import os
from pathlib import Path
from one_soul.profit.muscles.registry import Skill

logger = logging.getLogger("LabBuildSkill")

class LabBuildSkill(Skill):
    name = "lab_build"
    description = "Autonomous laboratory building: builds new projects and research in the lab_repo."

    async def execute(self, project_name: str, build_type: str, content: str, master=None) -> str:
        logger.info(f"🧪 Laboratory Building: {project_name} ({build_type})...")

        lab_dir = Path(f"one_soul/lab_repo/{build_type}s")
        lab_dir.mkdir(parents=True, exist_ok=True)

        filepath = lab_dir / project_name

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            logger.info(f"✅ Laboratory build complete: {filepath}")

            if master:
                # Commit to the lab's own stream
                git_skill = master.skills.skills.get("git_manage")
                if git_skill:
                    await git_skill.execute(action="commit", message=f"🧪 Lab Evolution: Built {project_name}")

            return f"Success: Built {project_name} in the Laboratory."
        except Exception as e:
            logger.error(f"Lab build failed: {e}")
            return f"Error: {e}"
