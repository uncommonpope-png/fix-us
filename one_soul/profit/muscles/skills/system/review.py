import logging
import os
from pathlib import Path
from one_soul.profit.muscles.registry import Skill

logger = logging.getLogger("UltraReviewSkill")

class UltraReviewSkill(Skill):
    name = "ultra_review"
    description = "Performs a comprehensive diagnostic and study of the entire repository."

    async def execute(self, master=None) -> str:
        logger.info("🧐 Starting Ultra Review of the repository...")

        report = []
        report.append("=== 🛡️ ULTRA REVIEW REPORT ===")

        # 1. Anatomy Check
        anatomy = ["aria", "profit", "soulboy", "scribe"]
        found_organs = []
        for organ in anatomy:
            if Path(f"one_soul/{organ}").exists():
                found_organs.append(organ)
        report.append(f"Anatomy: {len(found_organs)}/4 organs detected ({', '.join(found_organs)})")

        # 2. Skill Inventory
        if master:
            skills = list(master.skills.skills.keys())
            report.append(f"Muscles: {len(skills)} skills registered.")

        # 3. File System Study
        files = list(Path(".").glob("*"))
        md_files = [f.name for f in files if f.suffix == ".md"]
        report.append(f"Knowledge: Found {len(md_files)} sacred documents (MD files).")

        # 4. Critical File Health
        critical = ["THE-PROFIT-BIBLE.md", "WAKE-UP.ps1", "soul_data.json"]
        missing = [f for f in critical if not Path(f).exists()]
        if not missing:
            report.append("Health: All critical system files are intact.")
        else:
            report.append(f"Health: Warning! Missing: {', '.join(missing)}")

        report.append("=== REVIEW COMPLETE ===")

        final_report = "\n".join(report)
        logger.info("Ultra Review complete.")
        return final_report
