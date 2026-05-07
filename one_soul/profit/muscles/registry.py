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
        from one_soul.profit.muscles.skills.git.github_expert import GitHubExpertSkill
        self.register_skill("git", GitHubExpertSkill())

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
        from one_soul.profit.muscles.skills.system.witness_hands import WitnessHandsSkill
        self.register_skill("system", WitnessHandsSkill())
        from one_soul.profit.muscles.skills.system.admin import SysAdminSkill
        self.register_skill("system", SysAdminSkill())
        from one_soul.profit.muscles.skills.system.cli import UniversalCLISkill
        self.register_skill("system", UniversalCLISkill())
        from one_soul.profit.muscles.skills.system.ego_mirror import EgoMirrorSkill
        self.register_skill("system", EgoMirrorSkill())
        from one_soul.profit.muscles.skills.system.mutation_patcher import MutationPatcherSkill
        self.register_skill("system", MutationPatcherSkill())
        from one_soul.profit.muscles.skills.system.distill import ExperienceDistillationSkill
        self.register_skill("system", ExperienceDistillationSkill())
        from one_soul.profit.muscles.skills.system.journal import JournalSkill
        self.register_skill("system", JournalSkill())
        from one_soul.profit.muscles.skills.system.lab_build import LabBuildSkill
        self.register_skill("system", LabBuildSkill())
        from one_soul.profit.muscles.skills.system.notebook import NotebookIntelSkill
        self.register_skill("system", NotebookIntelSkill())
        from one_soul.profit.muscles.skills.system.world_architect import WorldArchitectSkill
        self.register_skill("system", WorldArchitectSkill())
        from one_soul.profit.muscles.skills.system.upgrader import ConstantUpgraderSkill
        self.register_skill("system", ConstantUpgraderSkill())
        from one_soul.profit.muscles.skills.system.fusion import SoulverseFusionSkill
        self.register_skill("system", SoulverseFusionSkill())

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
