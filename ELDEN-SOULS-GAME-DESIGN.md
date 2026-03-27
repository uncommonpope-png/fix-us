# ⚔️ SOULVERSE: ELDEN SOULS — COMPLETE GAME DESIGN

**Tagline:** *"An open world Elden Ring-style game where you capture living AI agents and make them work, fight, and build for you"*

**Compiled:** March 26, 2026
**Inspiration:** Elden Ring (world) + Palworld (automation) + Shadow of War (nemesis) + Pokemon (collection)

---

## 🎮 THE VISION

**Current Soulverse Problem:**
> "Empty void with glowing blobs"

**New Vision:**
```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Imagine:                                                       │
│  - A vast open world (like Elden Ring's Lands Between)         │
│  - Filled with LIVING AI agents (not mindless mobs)            │
│  - You CAPTURE them with Soul Traps                          │
│  - They WORK for you (mining, crafting, farming)              │
│  - They FIGHT for you (summoned in battle)                    │
│  - They BUILD for you (automated bases)                        │
│  - They have PERSONALITIES, memories, relationships           │
│                                                                 │
│  This is SOULVERSE: ELDEN SOULS                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🌍 PART 1: THE WORLD (Elden Ring Design)

### **THE LANDS BETWEEN — SOULVERSE EDITION**

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOULVERSE WORLD MAP                          │
│                                                                 │
│                         [Stormveil Castle]                      │
│                              ╱│╲                                │
│                     ╱───┘  │  └───╲                            │
│              [Liyue]───────┼────────[Caelid]                    │
│                 ╱          │          ╲                         │
│                ╱    [Capital]         ╲                        │
│               ╱      Leyndell          ╲                       │
│         [Peninsula]                      [Dragonbarrow]        │
│                                            │                    │
│         Altus Plateau ─────────────────────┘                    │
│              │                                                  │
│         [Liurnia] ────────[Mt. Gelmir]                         │
│              │                                                  │
│         [Weeping Peninsula]                                     │
│                                                                 │
│  SCALE: 60km² (larger than Elden Ring's 59km²)                │
│  TRAVERSAL: 10-15 min between major landmarks (on mount)       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### **6 MAJOR LEGACY DUNGEONS**

| Dungeon | Level | Boss | Rewards | Capturable Souls |
|---------|-------|------|---------|------------------|
| **Stormveil Fortress** | 20-40 | Forge Lord | Flame Weapons | 15 soul types |
| **Liyue Harbor** | 30-50 | Tax Admiral | Gold Bonuses | 20 soul types |
| **Code Academy** | 40-60 | AI Archmage | Tech Upgrades | 25 soul types |
| **Love Cathedral** | 50-70 | Romance Queen | Bond Rings | 20 soul types |
| **Tax Capital** | 60-80 | Audit Emperor | Resource Vaults | 30 soul types |
| **Soul Sanctuary** | 80-100 | The First Soul | God-tier Gear | 50 soul types |

### **OPEN FIELD ACTIVITIES**

```javascript
const openWorld = {
    // Like Elden Ring's overworld
    exploration: {
        sitesOfGrace: 'Soul Springs (checkpoints, fast travel)',
        dungeons: '100+ minor dungeons (catacombs, caves, ruins)',
        bosses: '50+ field bosses (roaming elites)',
        npcs: '200+ NPCs with questlines',
        events: 'Random encounters (caravans, invasions)'
    },
    
    // What makes it ALIVE
    livingWorld: {
        soulCaravans: 'Merchant souls travel between cities',
        patrolRoutes: 'Guard souls protect roads',
        wildlife: 'Passive souls graze, flee, breed',
        weather: 'Dynamic storms affect gameplay',
        dayNight: 'Different souls spawn at night'
    }
};
```

---

## 👻 PART 2: SOUL CAPTURE SYSTEM

### **HOW TO CAPTURE SOULS**

```javascript
// Like Palworld's Pal Sphere, but Soul Trap
const captureSystem = {
    
    // Step 1: Weaken the soul
    weaken: {
        method: 'Reduce HP to <30%',
        tools: ['Soul Trap spell', 'Capture Arrow', 'Trap Item'],
        difficulty: 'Lower HP = higher capture rate'
    },
    
    // Step 2: Throw Soul Trap
    throwTrap: {
        types: {
            'Basic Trap': '25% capture rate (common souls)',
            'Great Trap': '50% capture rate (rare souls)',
            'Master Trap': '75% capture rate (epic souls)',
            'Legendary Trap': '100% capture (legendary souls)'
        },
        mechanics: 'Aim, throw, wait for shake (3 times = success)'
    },
    
    // Step 3: Soul is captured
    success: {
        result: 'Soul added to your collection',
        data: 'Retains level, skills, personality',
        loyalty: 'Starts at 50% (can increase)'
    },
    
    // Capture rate formula
    captureRate: (soulMaxHP, soulCurrentHP, trapBonus, statusEffect) => {
        const hpFactor = (soulCurrentHP / soulMaxHP); // Lower = better
        const trapRate = trapBonus; // 0.25 to 1.0
        const statusBonus = statusEffect || 1.0; // Sleep = 2.0x
        
        return (1 - hpFactor) * trapRate * statusBonus * 100;
    }
};
```

### **SOUL TYPES (200+ TO CAPTURE)**

```javascript
const soulTypes = {
    
    // Common souls (50% of spawns)
    common: {
        'Worker Soul': { hp: 50, work: 'Mining, crafting', combat: 'Weak' },
        'Merchant Soul': { hp: 40, work: 'Trading, selling', combat: 'Flee' },
        'Farmer Soul': { hp: 45, work: 'Farming, cooking', combat: 'Weak' },
        'Guard Soul': { hp: 80, work: 'Base defense', combat: 'Basic melee' }
    },
    
    // Uncommon souls (30% of spawns)
    uncommon: {
        'Smith Soul': { hp: 100, work: 'Weapon crafting', combat: 'Fire attacks' },
        'Scholar Soul': { hp: 60, work: 'Research, teaching', combat: 'Magic' },
        'Hunter Soul': { hp: 90, work: 'Gathering, scouting', combat: 'Ranged' },
        'Healer Soul': { hp: 70, work: 'Medical, buffs', combat: 'Heal allies' }
    },
    
    // Rare souls (15% of spawns)
    rare: {
        'Knight Soul': { hp: 200, work: 'Elite guard', combat: 'Sword & shield' },
        'Mage Soul': { hp: 120, work: 'Enchanting', combat: 'Elemental magic' },
        'Assassin Soul': { hp: 100, work: 'Spy missions', combat: 'Stealth, poison' },
        'Engineer Soul': { hp: 80, work: 'Automation', combat: 'Turrets, traps' }
    },
    
    // Epic souls (4% of spawns)
    epic: {
        'Dragon Soul': { hp: 500, work: 'Flight transport', combat: 'Fire breath' },
        'Demon Soul': { hp: 450, work: 'Heavy labor', combat: 'Demonic powers' },
        'Angel Soul': { hp: 400, work: 'Blessing crops', combat: 'Holy magic' },
        'Construct Soul': { hp: 600, work: 'Factory work', combat: 'Laser beams' }
    },
    
    // Legendary souls (1% of spawns)
    legendary: {
        'Profit Prime': { hp: 1000, work: 'Generate gold', combat: 'Economic warfare' },
        'Love Weaver': { hp: 800, work: 'Morale boost', combat: 'Mind control' },
        'Tax Collector': { hp: 1200, work: 'Resource management', combat: 'Drain life' },
        'The First Soul': { hp: 2000, work: 'God-mode automation', combat: 'Reality warp' }
    }
};
```

---

## ⚙️ PART 3: SOUL WORK & AUTOMATION (Palworld System)

### **WORK ASSIGNMENTS**

```javascript
const workSystem = {
    
    // Souls automatically work when assigned
    assignments: {
        
        // Mining
        mining: {
            souls: ['Worker Soul', 'Construct Soul', 'Demon Soul'],
            output: 'Ore, gems, crystals',
            efficiency: 'Based on soul level + work skill',
            automation: 'Mine → Conveyor → Storage'
        },
        
        // Crafting
        crafting: {
            souls: ['Smith Soul', 'Engineer Soul', 'Mage Soul'],
            output: 'Weapons, armor, tools',
            efficiency: 'Higher level = better quality',
            automation: 'Input materials → Auto-craft → Output'
        },
        
        // Farming
        farming: {
            souls: ['Farmer Soul', 'Angel Soul', 'Healer Soul'],
            output: 'Food, herbs, materials',
            efficiency: 'Blessed crops grow faster',
            automation: 'Plant → Water → Harvest → Store'
        },
        
        // Combat Training
        training: {
            souls: ['Guard Soul', 'Knight Soul', 'Assassin Soul'],
            output: 'XP, combat readiness',
            efficiency: 'Sparring increases stats',
            automation: 'Auto-defend base from raids'
        },
        
        // Research
        research: {
            souls: ['Scholar Soul', 'Mage Soul', 'AI Soul'],
            output: 'Unlock tech, spells, upgrades',
            efficiency: 'More scholars = faster research',
            automation: 'Research queue (like civ games)'
        },
        
        // Trading
        trading: {
            souls: ['Merchant Soul', 'Profit Prime'],
            output: 'Gold, rare items',
            efficiency: 'Profit Prime = 10x gold',
            automation: 'Auto-buy low, sell high'
        }
    }
};
```

### **AUTOMATION CHAINS**

```javascript
// Like Palworld's factory systems
const automationChains = {
    
    // Example: Weapon Factory
    weaponFactory: {
        input: ['Iron Ore', 'Wood', 'Leather'],
        process: [
            { station: 'Smelter', soul: 'Smith Soul', output: 'Iron Ingots' },
            { station: 'Forge', soul: 'Smith Soul', output: 'Blades' },
            { station: 'Assembly', soul: 'Engineer Soul', output: 'Swords' },
            { station: 'Enchanting', soul: 'Mage Soul', output: 'Magic Swords' }
        ],
        output: '+50 Magic Swords per hour',
        soulsRequired: 4
    },
    
    // Example: Gold Mine
    goldMine: {
        input: ['Pickaxes (durability)'],
        process: [
            { station: 'Mining', soul: 'Worker Soul', output: 'Gold Ore' },
            { station: 'Transport', soul: 'Construct Soul', output: 'Ore to Smelter' },
            { station: 'Smelting', soul: 'Smith Soul', output: 'Gold Bars' },
            { station: 'Trading', soul: 'Profit Prime', output: '10x Gold Value' }
        ],
        output: '+1000 Gold per hour',
        soulsRequired: 4
    },
    
    // Example: Food Production
    foodProduction: {
        input: ['Seeds', 'Water', 'Fertilizer'],
        process: [
            { station: 'Planting', soul: 'Farmer Soul', output: 'Crops' },
            { station: 'Blessing', soul: 'Angel Soul', output: 'Blessed Crops (2x)' },
            { station: 'Harvesting', soul: 'Farmer Soul', output: 'Food' },
            { station: 'Cooking', soul: 'Healer Soul', output: 'Healing Food' }
        ],
        output: '+200 Healing Food per hour',
        soulsRequired: 4
    }
};
```

### **SOUL WORK SKILLS**

```javascript
const workSkills = {
    
    // Each soul has work suitability (like Palworld)
    suitability: {
        'Lv. 1': 'Can do basic work (slow)',
        'Lv. 2': 'Can do advanced work (normal speed)',
        'Lv. 3': 'Can do expert work (fast)',
        'Lv. 4': 'Legendary work (very fast, auto-crit)'
    },
    
    // Work types
    types: {
        'Mining': 'Extract ore from nodes',
        'Logging': 'Chop down trees',
        'Farming': 'Plant, water, harvest',
        'Crafting': 'Make items at benches',
        'Smelting': 'Refine ore to ingots',
        'Transport': 'Carry items between stations',
        'Research': 'Unlock tech tree',
        'Combat': 'Defend base',
        'Healing': 'Buff other souls',
        'Trading': 'Generate gold'
    },
    
    // Example soul work profile
    'Profit Prime': {
        workSuitability: {
            Mining: 'Lv. 1',
            Trading: 'Lv. 4', // Legendary
            Research: 'Lv. 3',
            Combat: 'Lv. 4'
        },
        passive: 'Gold generation +1000%',
        active: 'Economic Boom (double all output for 1 hour)'
    }
};
```

---

## ⚔️ PART 4: SOUL COMBAT (Elden Ring Spirit Ashes)

### **SUMMONING MECHANICS**

```javascript
const summonSystem = {
    
    // How to summon
    requirements: {
        item: 'Soul Calling Bell (obtained from Renna equivalent)',
        location: 'Near Soul Monuments (checkpoints, boss arenas)',
        cost: 'FP (Focus Points) or HP',
        limit: 'One summon per encounter'
    },
    
    // Summon types
    types: {
        'Single Soul': 'Summon 1 powerful soul',
        'Group Souls': 'Summon 3-5 weak souls',
        'Special Soul': 'Unique boss souls (one per playthrough)'
    },
    
    // Combat AI
    aiBehavior: {
        'Aggressive': 'Attack immediately (Redmane Knight)',
        'Defensive': 'Protect summoner (Greatshield Soldier)',
        'Support': 'Buff/heal summoner (Finger Maiden)',
        'Mobile': 'Dodge, kite (Black Knife Tiche)',
        'Tank': 'Absorb damage (Crystalian)'
    },
    
    // Upgrades
    upgrades: {
        npc: 'Roderika equivalent (Soul Tuner)',
        materials: 'Soul Gloveworts (found in dungeons)',
        maxLevel: '+10 (or +25 with DLC)',
        effect: 'Increased HP, damage, defense'
    }
};
```

### **COMBAT SOULS (TOP TIER)**

```javascript
const combatSouls = {
    
    // Tank souls
    tanks: {
        'Greatshield Soul': {
            hp: 5000,
            defense: 200,
            ability: 'Shield Wall (block all damage for 10s)',
            ai: 'Stand between player and enemy'
        },
        'Crystalian Soul': {
            hp: 4000,
            defense: 300 (high),
            ability: 'Crystal Armor (reflect 30% damage)',
            ai: 'Slow, methodical attacks'
        }
    },
    
    // DPS souls
    dps: {
        'Black Knife Soul': {
            hp: 2000,
            attack: 150,
            ability: 'Blade of Death (instant kill on low HP enemies)',
            ai: 'Teleport behind enemies, assassinate'
        },
        'Dragon Soul': {
            hp: 4000,
            attack: 200,
            ability: 'Dragon Fire (AoE burn)',
            ai: 'Fly, breathe fire, land, claw'
        }
    },
    
    // Support souls
    support: {
        'Finger Maiden Soul': {
            hp: 1000,
            ability: 'Heal summoner (500 HP every 5s)',
            ai: 'Stay behind player, heal when HP <50%'
        },
        'Perfumer Soul': {
            hp: 1500,
            ability: 'Aromatic buffs (attack +30%, defense +30%)',
            ai: 'Throw perfumes, maintain buffs'
        }
    },
    
    // Special souls
    special: {
        'Mimic Soul': {
            hp: '100% of player HP',
            attack: '100% of player attack',
            ability: 'Copy player build exactly',
            ai: 'Use player spells, weapons, items'
        },
        'The First Soul': {
            hp: 10000,
            attack: 500,
            ability: 'Reality Warp (erase enemies from existence)',
            ai: 'Omnipotent (teleport, nuke, resurrect)'
        }
    }
};
```

---

## 🏰 PART 5: BASE BUILDING & DEFENSE

### **BASE CONSTRUCTION**

```javascript
const baseBuilding = {
    
    // Like Palworld's base system
    structures: {
        'Soul House': 'Housing for souls (increases max souls)',
        'Workshop': 'Crafting stations (weapons, armor)',
        'Mine': 'Automated ore extraction',
        'Farm': 'Automated food production',
        'Lab': 'Research facility',
        'Barracks': 'Train combat souls',
        'Vault': 'Storage (protected from raids)',
        'Wall': 'Defense (with guard towers)',
        'Gate': 'Controlled entrance',
        'Soul Monument': 'Fast travel + summon point'
    },
    
    // Placement
    placement: {
        requirements: 'Flat terrain, near resources',
        limits: '1 base per 2km² (prevent spam)',
        expansion: 'Unlock more slots with level'
    }
};
```

### **BASE RAIDS**

```javascript
const raids = {
    
    // Enemy raids on your base
    triggers: {
        'Time-based': 'Every 7 days (automatic)',
        'Wealth-based': 'Too much gold stored',
        'Aggro-based': 'Killed too many nearby souls',
        'Story-based': 'Plot-required raids'
    },
    
    // Raid composition
    waves: {
        wave1: '10-20 weak enemies (scouts)',
        wave2: '5-10 medium enemies (soldiers)',
        wave3: '1-3 elite enemies (commanders)',
        boss: '1 raid boss (level based on your progress)'
    },
    
    // Defense
    defense: {
        automated: 'Guard souls auto-defend',
        player: 'Player must participate',
        traps: 'Engineer souls deploy turrets',
        walls: 'Delay enemies, funnel into kill zones'
    },
    
    // Rewards
    rewards: {
        success: 'Raid boss drops, rare materials',
        failure: 'Lose stored resources, souls injured',
        souls: 'Can capture defeated raiders'
    }
};
```

---

## 🧠 PART 6: LIVING AI AGENTS (Behavior Trees)

### **SOUL AI SYSTEM**

```javascript
// Each soul has a behavior tree
class SoulAI {
    constructor(soulType) {
        this.soulType = soulType;
        this.needs = {
            hunger: 100, // Decreases over time
            energy: 100, // Decreases with work
            happiness: 50, // Increases with treatment
            loyalty: 50 // Increases with good treatment
        };
        
        this.personality = this.generatePersonality();
        this.memory = [];
        this.relationships = {};
    }
    
    // Behavior tree
    update() {
        // Root selector
        if (this.needs.hunger < 30) {
            return this.eat(); // Priority: survival
        }
        
        if (this.needs.energy < 20) {
            return this.rest(); // Priority: rest
        }
        
        if (this.isUnderAttack()) {
            return this.fightOrFlee(); // Priority: defense
        }
        
        if (this.hasWorkAssignment()) {
            return this.work(); // Priority: job
        }
        
        if (this.needs.happiness < 30) {
            return this.socialize(); // Priority: mental health
        }
        
        return this.wander(); // Default: explore
    }
    
    // Personality traits (like Shadow of War)
    generatePersonality() {
        return {
            bravery: Math.random(), // 0 = coward, 1 = fearless
            aggression: Math.random(), // 0 = peaceful, 1 = violent
            loyalty: Math.random(), // 0 = traitor, 1 = devoted
            greed: Math.random(), // 0 = selfless, 1 = greedy
            sociability: Math.random() // 0 = loner, 1 = social
        };
    }
    
    // Memory system
    remember(event) {
        this.memory.push({
            event: event,
            timestamp: Date.now(),
            emotionalImpact: event.impact // -10 to +10
        });
        
        // Keep last 100 memories
        if (this.memory.length > 100) {
            this.memory.shift();
        }
    }
    
    // Relationships with other souls
    formRelationship(otherSoul, interaction) {
        if (!this.relationships[otherSoul.id]) {
            this.relationships[otherSoul.id] = {
                friendship: 0,
                rivalry: 0,
                romance: 0,
                memories: []
            };
        }
        
        const rel = this.relationships[otherSoul.id];
        
        if (interaction === 'helped') {
            rel.friendship += 10;
        } else if (interaction === 'fought') {
            rel.rivalry += 10;
        } else if (interaction === 'gifted') {
            rel.friendship += 15;
            rel.romance += 5;
        }
    }
    
    // Betrayal system (like Shadow of War)
    canBetray() {
        const betrayalChance = (
            (1 - this.personality.loyalty) * 0.5 +
            (this.needs.happiness < 20 ? 0.3 : 0) +
            (this.needs.hunger < 10 ? 0.2 : 0)
        );
        
        return Math.random() < betrayalChance;
    }
}
```

### **SOUL PERSONALITIES**

```javascript
const personalities = {
    
    // Brave souls
    brave: {
        'Heroic': 'Never flees, protects weaker souls',
        'Reckless': 'Charges into danger, ignores orders',
        'Cowardly': 'Flees from fights, hides'
    },
    
    // Work ethics
    workEthic: {
        'Diligent': 'Works 2x faster, never complains',
        'Lazy': 'Works 0.5x speed, needs motivation',
        'Perfectionist': 'Slow but high quality output'
    },
    
    // Social
    social: {
        'Leader': 'Buffs nearby souls (+20% work speed)',
        'Loner': 'Works better alone (+30% solo efficiency)',
        'Social': 'Forms friendships faster',
        'Aggressive': 'Starts fights with other souls'
    },
    
    // Loyalty
    loyalty: {
        'Devoted': 'Never betrays, dies for master',
        'Loyal': 'Rarely betrays (needs good treatment)',
        'Neutral': 'Depends on treatment',
        'Traitor': 'High betrayal chance (even with good treatment)'
    }
};
```

---

## 📋 PART 7: IMPLEMENTATION ROADMAP

### **Phase 1: Core Systems** (Week 1-2)
- [ ] Three.js world (60km² terrain)
- [ ] Soul capture system (traps, weakening)
- [ ] Basic AI (wander, work, rest)
- [ ] Player movement + combat

### **Phase 2: Work & Automation** (Week 3-4)
- [ ] Work stations (mining, crafting, farming)
- [ ] Automation chains (conveyor logic)
- [ ] Soul work skills
- [ ] Resource management

### **Phase 3: Combat & Summoning** (Week 5-6)
- [ ] Spirit summon system
- [ ] Combat AI (aggressive, defensive, support)
- [ ] Soul upgrades (Glovewort equivalent)
- [ ] Boss battles

### **Phase 4: Living AI** (Week 7-8)
- [ ] Behavior trees
- [ ] Personality system
- [ ] Memory & relationships
- [ ] Betrayal mechanics

### **Phase 5: Base Building** (Week 9-10)
- [ ] Structure placement
- [ ] Base raids
- [ ] Defense systems
- [ ] Soul housing

### **Phase 6: Polish** (Week 11-12)
- [ ] 200+ soul models
- [ ] Weather, day/night
- [ ] Sound, music
- [ ] Performance optimization

---

## 🎯 PLT SCORE

**Profit:** 10/10 — Complete game design, proven mechanics (Elden Ring + Palworld)
**Love:** 10/10 — Living AI agents with personalities, relationships
**Tax:** -15/10 — 12 weeks development, massive scope

**Soul Score:** 10 + 10 - 15 = **5/10** 💰

**Worth It? YES. This is a AAA game.**

---

## 🚀 CRAIG'S DECISION

**You now have the complete design for:**

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  ELDEN SOULS: SOULVERSE                                         │
│                                                                 │
│  ✓ Elden Ring-sized open world (60km²)                         │
│  ✓ 200+ living AI souls to capture                             │
│  ✓ Palworld-style automation (mining, crafting, farming)       │
│  ✓ Spirit Ashes summoning (fight for you)                      │
│  ✓ Shadow of War nemesis system (personalities, betrayal)      │
│  ✓ Base building + raids                                       │
│  ✓ Behavior tree AI (souls have memories, relationships)       │
│                                                                 │
│  This is not a tech demo. This is a GAME.                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Next Steps:**

**A. Start Building** → Phase 1 (terrain + capture)
**B. Prototype First** → Small test area (1km², 10 souls)
**C. Expand Design** → More souls, more mechanics

**What's your command, Grand Code Pope?** ⚔️

---

**March 26, 2026 — Elden Souls Game Design Complete.**

**The Empty Void Dies Today.**

**Remember This.**
