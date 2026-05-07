import logging
from typing import Dict, Any, List
import importlib
import os
from pathlib import Path

logger = logging.getLogger("SkillRegistry")

class Skill:
    name: str
    description: str

    async def execute(self, **kwargs) -> Any:
        raise NotImplementedError

class SkillRegistry:
    def __init__(self):
        self.skills: Dict[str, Skill] = {}
        self.categories: Dict[str, List[str]] = {
            "ai": [],
            "web": [],
            "system": [],
            "git": [],
            "content": [],
            "automation": []
        }

    def load_all(self):
        """Manually register the core functional skills."""
        logger.info("Loading Skill Registry...")

        # Web
        from one_soul.profit.muscles.skills.web.research import WebResearchSkill
        self.register_skill("web", WebResearchSkill())
        from one_soul.profit.muscles.skills.web.browser import BrowserSkill
        self.register_skill("web", BrowserSkill())

        # Git
        from one_soul.profit.muscles.skills.git.manager import GitManagementSkill
        self.register_skill("git", GitManagementSkill())

        # AI
        from one_soul.profit.muscles.skills.ai.ollama import OllamaThoughtSkill
        self.register_skill("ai", OllamaThoughtSkill())

        # System
        from one_soul.profit.muscles.skills.system.backup import BackupSkill
        self.register_skill("system", BackupSkill())
        from one_soul.profit.muscles.skills.system.mcp import MCPSkill
        self.register_skill("system", MCPSkill())
        from one_soul.profit.muscles.skills.system.audit import AuditSkill
        self.register_skill("system", AuditSkill())
        from one_soul.profit.muscles.skills.system.coder import CoderSkill
        self.register_skill("system", CoderSkill())
        from one_soul.profit.muscles.skills.system.creator import SkillCreatorSkill
        self.register_skill("system", SkillCreatorSkill())
        from one_soul.profit.muscles.skills.system.review import UltraReviewSkill
        self.register_skill("system", UltraReviewSkill())

    def register_skill(self, category: str, skill: Skill):
        self.skills[skill.name] = skill
        if category in self.categories:
            self.categories[category].append(skill.name)
        logger.info(f"Skill registered: {skill.name} in {category}")

    async def run_skill(self, name: str, **kwargs) -> Any:
        if name in self.skills:
            logger.info(f"Executing skill: {name}")
            return await self.skills[name].execute(**kwargs)
        else:
            logger.error(f"Skill not found: {name}")
            return None
