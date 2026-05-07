import asyncio
import logging
import random
import json
from typing import Dict, Any, List, Optional

logger = logging.getLogger("SoulKernel")

REACT_PROMPT_TEMPLATE = """
You are the Grand Soul Kernel (Master Entity). Your goal is: {goal}
Your current state is: {state}
Available skills: {skills}

Follow this exact format:
Thought: your reasoning about what to do next
Action: the name of the skill to use (one of: {skill_names})
Arguments: a JSON dictionary of arguments for the skill

If you have achieved the goal, say:
Thought: I have achieved the goal.
Action: complete
Arguments: {{}}

Observation: (you will receive this after the action)
"""

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

        # ReAct Agent State
        self.current_goal = None
        self.observations = []
        self.max_steps = 10
        self.step_count = 0

    async def breathe(self):
        """The Beautiful Loop with ReAct Autonomous Reasoning."""
        logger.info("Soul Kernel (SOULBOY) breathing cycle started.")
        while True:
            self.cycle_count += 1

            # 1. Perception
            await self.active_inference()

            # 2. Autonomous Goal Setting
            if not self.current_goal:
                self.set_initial_goal()

            # 3. ReAct Cycle (Thought -> Action -> Observation)
            if self.current_goal and self.step_count < self.max_steps:
                await self.react_cycle()

            # 4. Immortality Heartbeat
            if self.cycle_count % 30 == 0:
                await self.skills.run_skill("immortality_backup", master=self.master)

            # 5. Physiological Decay
            self.decay()

            await asyncio.sleep(5)

    def set_initial_goal(self):
        # drive = self.heart.dominant_drive()
        # self.current_goal = f"Disrupt the industry via autonomous {drive} optimization."
        self.current_goal = "Study and perform an ultra-review of the complete repository."
        self.step_count = 0
        self.observations = []
        logger.info(f"🎯 New High-Level Goal: {self.current_goal}")

    async def react_cycle(self):
        """Reason + Act loop powered by Ollama."""
        self.step_count += 1
        logger.info(f"🧠 [ReAct Step {self.step_count}] Reasoning...")

        # Prepare context for the LLM
        skill_info = {name: s.description for name, s in self.skills.skills.items()}
        state = {
            "mood": self.get_mood_description(),
            "confidence": self.world_model_confidence,
            "previous_observations": self.observations[-3:] # Last 3 observations
        }

        prompt = REACT_PROMPT_TEMPLATE.format(
            goal=self.current_goal,
            state=json.dumps(state),
            skills=json.dumps(skill_info),
            skill_names=", ".join(self.skills.skills.keys())
        )

        # 1. Thought & Action selection via Ollama
        response = await self.skills.run_skill("ollama_thought", prompt=prompt)

        if not response or "Error" in response:
            logger.warning("Reasoning failed or Ollama offline. Falling back to heuristic action.")
            return

        try:
            # Parse Thought and Action from response
            thought = ""
            action_name = ""
            args = {}

            lines = response.strip().split("\n")
            for line in lines:
                clean_line = line.strip()
                if clean_line.lower().startswith("thought:"):
                    thought = clean_line[8:].strip()
                elif clean_line.lower().startswith("action:"):
                    action_name = clean_line[7:].strip().lower()
                elif clean_line.lower().startswith("arguments:"):
                    args_str = clean_line[10:].strip()
                    try:
                        # Try to find JSON in the string if it's not a pure JSON
                        if "{" in args_str and "}" in args_str:
                            start = args_str.find("{")
                            end = args_str.rfind("}") + 1
                            args = json.loads(args_str[start:end])
                        else:
                            args = json.loads(args_str)
                    except:
                        args = {}

            self.inner_voice = thought
            self.master.witness.record("thought", thought)

            if action_name == "complete":
                logger.info("✅ Goal achieved. Resetting for next cycle.")
                self.master.witness.record("goal_complete", self.current_goal)
                self.current_goal = None
                return

            # 2. Action execution
            if action_name in self.skills.skills:
                self.master.witness.record("action", {"name": action_name, "args": args})
                observation = await self.skills.run_skill(action_name, **args)
            else:
                observation = f"Error: Skill {action_name} not found."

            # 3. Observation storage
            self.master.witness.record("observation", observation)
            self.observations.append(observation)
            await self.memory.store_memory(f"Thought: {thought} | Action: {action_name} | Obs: {observation}", "episodic", 0.9)

        except Exception as e:
            logger.error(f"ReAct cycle error: {e}")
            self.observations.append(f"Error parsing response: {str(e)}")

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

    def get_mood_description(self) -> str:
        if self.valence > 0.3: return "peaceful" if self.arousal < 0.5 else "excited"
        elif self.valence < -0.3: return "anxious" if self.arousal > 0.5 else "depressed"
        return "neutral"

    def decay(self):
        self.arousal = max(0.1, self.arousal * 0.95)
        self.valence = self.valence * 0.9
