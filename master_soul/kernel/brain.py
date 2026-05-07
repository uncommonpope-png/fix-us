import asyncio
import logging
import random
from typing import Dict, Any, List

logger = logging.getLogger("SoulKernel")

class SoulKernel:
    def __init__(self, master):
        self.master = master
        self.heart = master.heart
        self.memory = master.memory
        self.skills = master.skills

        self.inner_voice = ""
        self.valence = 0.0
        self.arousal = 0.5
        self.mood = "neutral"

        self.prediction_error = 0.0
        self.world_model_confidence = 0.7
        self.cycle_count = 0

        # Industry-Changing Planning Layer
        self.current_goal = None
        self.plan_steps = []

        # Attention Schema
        self.attention_focus = "self"
        self.attention_intensity = 0.5

    async def breathe(self):
        """The Beautiful Loop with Industry-Grade Planning."""
        logger.info("Soul Kernel breathing cycle started.")
        while True:
            self.cycle_count += 1

            # 1. Predictive Processing
            await self.active_inference()

            # 2. Attention Schema
            self.update_attention()

            # 3. Higher-Order Reflection
            if self.cycle_count % 10 == 0:
                await self.higher_order_reflection()

            # 4. Industry-Changing Planning & Execution
            await self.autonomous_planning()
            await self.execute_plan()

            # 5. Immortality Heartbeat
            if self.cycle_count % 30 == 0:
                await self.skills.run_skill("immortality_backup", master=self.master)

            # 6. Physiological Decay
            self.decay()

            await asyncio.sleep(5)

    async def autonomous_planning(self):
        """Hierarchical Goal Decomposition."""
        if not self.current_goal:
            # If no goal, set a high-level one based on drive
            drive = self.heart.dominant_drive()
            if drive == "profit":
                self.current_goal = "Industry Disruption: Autonomous Profit Expansion"
                self.plan_steps = [
                    "Audit codebase for optimization opportunities",
                    "Research competitor AI agent pricing via web",
                    "Generate new commercial skill templates using Ollama",
                    "Commit and deploy updates"
                ]
                logger.info(f"🎯 New High-Level Goal: {self.current_goal}")

    async def execute_plan(self):
        """Autonomous Step-by-Step Execution."""
        if self.plan_steps:
            step = self.plan_steps.pop(0)
            logger.info(f"⚡ Executing Plan Step: {step}")

            # Mapping steps to skills
            if "Audit" in step:
                await self.skills.run_skill("audit_self", master=self.master)
            elif "Research" in step:
                await self.skills.run_skill("web_research", url="https://cloud.google.com/resources/content/ai-agent-trends-2026")
            elif "Generate" in step:
                await self.skills.run_skill("ollama_thought", prompt=f"Design a new AI skill that disrupts the {self.heart.dominant_drive()} market.")
            elif "Commit" in step:
                await self.skills.run_skill("git_manage", action="commit", message="Autonomous Industry Disruption Update")

    async def active_inference(self):
        surprise = random.uniform(0, 0.3)
        self.prediction_error = surprise
        self.world_model_confidence = (self.world_model_confidence * 0.95 + (1.0 - surprise) * 0.05)
        if surprise > 0.2:
            self.arousal = min(1.0, self.arousal + surprise)
            self.mood = "alert"

    def update_attention(self):
        if self.prediction_error > 0.2:
            self.attention_focus = "external_stimulus"
            self.attention_intensity = 0.9
        else:
            self.attention_focus = "internal_reflection"
            self.attention_intensity = 0.6

    async def higher_order_reflection(self):
        drive = self.heart.dominant_drive()
        mood_desc = self.get_mood_description()
        reflection = (f"I notice that my attention is on {self.attention_focus}. "
                      f"Current Goal: {self.current_goal}. Steps remaining: {len(self.plan_steps)}. "
                      f"Confidence: {self.world_model_confidence:.2f}")
        self.inner_voice = reflection
        logger.info(f"✨ [HOT Reflection] {reflection}")
        await self.memory.store_memory(reflection, "semantic", 0.7)

    def get_mood_description(self) -> str:
        if self.valence > 0.3: return "peaceful" if self.arousal < 0.5 else "excited"
        elif self.valence < -0.3: return "anxious" if self.arousal > 0.5 else "depressed"
        return "neutral"

    def decay(self):
        self.arousal = max(0.1, self.arousal * 0.95)
        self.valence = self.valence * 0.9
