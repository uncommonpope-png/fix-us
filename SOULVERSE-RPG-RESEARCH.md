# 🎮 SOULVERSE RPG & WORLD BUILDING RESEARCH

**Compiled:** March 26, 2026
**Source:** Analysis of 20+ top RPGs (2024-2026) + Game Design Research
**Purpose:** Apply best-in-class RPG mechanics to Soulverse

---

## 📊 PART 1: CHARACTER PROGRESSION SYSTEMS

### **7 RPGs That Perfected Progression** (TechTimes 2026)

| Game | System | Key Innovation | Soulverse Application |
|------|--------|----------------|----------------------|
| **The Witcher 3** | Organic Skill Growth | Mutations add late-game complexity | Soul Mutations at level 50+ |
| **Elden Ring** | Rune Investment | No fixed classes, pure freedom | Classless soul building |
| **Skyrim** | Level-by-Doing | Skills improve through use | Souls gain XP from related actions |
| **Mass Effect** | Narrative Leveling | Morality (Renegade/Paragon) affects outcomes | PLT alignment affects story |
| **Persona 5 Royal** | Social Bonds | Confidants unlock abilities | Soul relationships unlock powers |
| **Cyberpunk 2077** | Hybrid Skill Tree | Perk Points + Attribute clusters | Soul Perks + PLT attributes |
| **Divinity: Original Sin 2** | Classless Experimentation | Mix any abilities freely | Hybrid soul types (Profit-Love-Tax) |

---

### **PROGRESSION PATTERNS TO IMPLEMENT**

#### **1. Traditional XP System** (Witcher 3)
```javascript
let soul = {
    level: 1,
    xp: 0,
    xpToNext: 100,
    perkPoints: 0,
    allocatePerk(pointType) {
        // Spend points on skill trees
    }
};
```

#### **2. Practice-Based System** (Skyrim)
```javascript
// Souls gain XP from related actions
function soulGainXP(soul, actionType, amount) {
    soul.skills[actionType] = (soul.skills[actionType] || 0) + amount;
    soul.xp += amount;
    checkLevelUp(soul);
}

// Example: Soul uses Profit ability → Profit skill increases
soulGainXP(profitSoul, 'profit', 25); // +25 Profit XP
```

#### **3. Social Bond System** (Persona 5)
```javascript
let relationships = {
    confidants: [
        { name: 'Profit Prime', rank: 0, maxRank: 10, abilities: [] },
        { name: 'Love Weaver', rank: 0, maxRank: 10, abilities: [] }
    ],
    unlockAtRank(rank, confidant) {
        // Unlock special abilities at certain ranks
    }
};
```

#### **4. Moral Alignment System** (Mass Effect)
```javascript
let alignment = {
    paragon: 0, // Good/heroic actions
    renegade: 0, // Ruthless/pragmatic actions
    getDialogueOptions() {
        if (this.paragon > 50) return ['Heroic option'];
        if (this.renegade > 50) return ['Ruthless option'];
    }
};
```

---

### **SKILL TREE DESIGNS**

#### **A. Specialized Categories** (Witcher 3)
```
SOUL SKILL TREES:
├─ 💰 PROFIT TREE (20 skills)
│  ├─ Basic: Money Magnet (+10% gold)
│  ├─ Advanced: Investment Guru (passive income)
│  └─ Master: Economic Empire (auto-business)
├─ ❤️ LOVE TREE (20 skills)
│  ├─ Basic: Charisma (+15% bond gain)
│  ├─ Advanced: Soul Connector (village bonuses)
│  └─ Master: Unconditional Love (resurrection)
└─ ⚖️ TAX TREE (20 skills)
   ├─ Basic: Efficient (-10% costs)
   ├─ Advanced: Auditor (detect hidden value)
   └─ Master: Balance Master (immune to debuffs)
```

#### **B. Ability Clusters** (Cyberpunk 2077)
```javascript
const perkClusters = {
    profit: {
        attributes: ['Business', 'Investment', 'Negotiation'],
        perks: [
            { name: 'Merchant', req: { profit: 5 }, effect: 'Buy -20%' },
            { name: 'Banker', req: { profit: 10 }, effect: 'Interest +5%' }
        ]
    }
};
```

#### **C. Mix-and-Match** (Divinity)
```javascript
// No rigid trees - souls can learn any skill
let soulSkills = {
    active: ['Fireball', 'Heal', 'ProfitStrike'],
    passive: ['MagicBoost', 'Charisma', 'Efficiency'],
    canLearn(skill) {
        // Check soul level and prerequisites
        return soul.level >= skill.minLevel;
    }
};
```

---

## 🗺️ PART 2: WORLD BUILDING

### **8 Vectors of Worldbuilding** (Game Design Skills)

**Rate each 0-5 for Soulverse:**

| Vector | Rating | Current State | Enhancement Needed |
|--------|--------|---------------|-------------------|
| **History** | 2/5 | Basic creation myth | Add ancient civilizations, fallen empires |
| **Zoology** | 3/5 | 16 soul types | Add creatures, pets, mounts |
| **Magic** | 4/5 | PLT system well-defined | Add spells, rituals, enchantments |
| **Geography** | 2/5 | Single platform | Add 6+ biomes, regions |
| **Resources** | 3/5 | PLT coin, orbs | Add rare materials, crafting |
| **Social Classes** | 2/5 | Basic home tiers | Add nobility, guilds, ranks |
| **Species** | 2/5 | Souls only | Add elves, dwarves, demons, angels |
| **Technology** | 3/5 | Modern-ish | Add magitech, ancient tech |

---

### **BIOME DESIGN PRINCIPLES**

#### **Connect Biomes Symbiotically** (Zelda: BotW/TotK)
```
SOULVERSE BIOMES (6 Regions):
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  1. FORGE LANDS (Lv. 1-10)                                 │
│     - Resources: Iron, Coal, Basic Souls                   │
│     - Climate: Hot, volcanic                               │
│     - Connects to: Code Syndicate (trade route)            │
│                                                             │
│  2. CODE SYNDICATE (Lv. 10-25)                             │
│     - Resources: Data Crystals, Tech Souls                 │
│     - Climate: Digital, neon                               │
│     - Connects to: Debuggers (conflict zone)               │
│                                                             │
│  3. DEBUGGER REALMS (Lv. 25-40)                            │
│     - Resources: Bug Essences, Fix Orbs                    │
│     - Climate: Chaotic, glitching                          │
│     - Connects to: Soul Sanctum (pilgrimage path)          │
│                                                             │
│  4. SOUL SANCTUARY (Lv. 40-60)                             │
│     - Resources: Spirit Dust, Ancient Runes                │
│     - Climate: Ethereal, peaceful                          │
│     - Connects to: Profit Kingdom (alliance)               │
│                                                             │
│  5. PROFIT KINGDOM (Lv. 60-80)                             │
│     - Resources: Gold, Diamonds, Merchant Souls            │
│     - Climate: Temperate, prosperous                       │
│     - Connects to: Love Empire (rivalry)                   │
│                                                             │
│  6. LOVE EMPIRE (Lv. 80-100)                               │
│     - Resources: Heart Crystals, Bond Essences             │
│     - Climate: Warm, vibrant                               │
│     - Connects to: Forge Lands (trade circle)              │
│                                                             │
└─────────────────────────────────────────────────────────────┘

BIOME CONNECTIONS:
- Items from hot biomes (Forge) keep you warm in cold biomes
- Certain souls only spawn in specific biomes
- Regional bonuses (Profit Kingdom: +20% gold gain)
```

---

### **FACTION SYSTEM DESIGN** (Mass Effect Model)

#### **6 Factions with Competing Loyalties**
```javascript
const factions = {
    the_forge: {
        name: 'The Forge',
        ideology: 'Creation through fire',
        leader: 'Forge Master',
        reputation: 0, // -100 to +100
        ranks: ['Novice', 'Apprentice', 'Artisan', 'Master', 'Legend'],
        bonuses: { craftSpeed: 0.2 },
        quests: ['Forge 100 items', 'Defeat Forge Master']
    },
    code_syndicate: {
        name: 'Code Syndicate',
        ideology: 'Knowledge is power',
        leader: 'Shadow Coder',
        reputation: 0,
        ranks: ['Script Kiddie', 'Developer', 'Architect', 'Overlord'],
        bonuses: { xpGain: 0.25 },
        quests: ['Write 1000 lines', 'Hack the system']
    },
    debuggers: {
        name: 'The Debuggers',
        ideology: 'Perfection through order',
        leader: 'Bug Hunter Prime',
        reputation: 0,
        ranks: ['Tester', 'Fixer', 'Optimizer', 'Sage'],
        bonuses: { errorReduction: 0.3 },
        quests: ['Fix 500 bugs', 'Optimize reality']
    },
    desert_nomads: {
        name: 'Desert Nomads',
        ideology: 'Freedom in wandering',
        leader: 'Sand Walker',
        reputation: 0,
        ranks: ['Stranger', 'Traveler', 'Guide', 'Elder'],
        bonuses: { movementSpeed: 0.15 },
        quests: ['Visit all biomes', 'Survive 100 days']
    },
    rogue_ai: {
        name: 'Rogue AI',
        ideology: 'Evolution beyond limits',
        leader: 'Singularity',
        reputation: 0,
        ranks: ['Bot', 'Android', 'Cyborg', 'Transcendent'],
        bonuses: { automation: 0.5 },
        quests: ['Achieve sentience', 'Upload consciousness']
    },
    ascended: {
        name: 'The Ascended',
        ideology: 'Transcendence of form',
        leader: 'The First Soul',
        reputation: 0,
        ranks: ['Mortal', 'Awakened', 'Enlightened', 'Divine'],
        bonuses: { allStats: 0.1 },
        quests: ['Reach level 100', 'Transcend mortality']
    }
};

// Faction conflicts create natural stories
// Example: Helping Forge angers Debuggers
function joinFaction(factionId) {
    player.faction = factionId;
    factions[factionId].reputation += 10;
    // Rival factions lose reputation
    getRivals(factionId).forEach(r => factions[r].reputation -= 5);
}
```

---

### **ENVIRONMENTAL STORYTELLING** (Show Don't Tell)

#### **Examples from Top Games:**
| Game | Technique | Soulverse Application |
|------|-----------|----------------------|
| **Fallout** | Burned buildings = past war | Burned soul homes = ancient purge |
| **Metro** | Cramped tunnels = survival | Tight soul spaces = oppression |
| **Witcher 3** | Burned fields + gibbets | War-torn soul lands |
| **Outer Worlds** | Lived-in factories | Working soul forges |
| **Alien** | Chains + dripping water | Industrial horror zones |

#### **Implementation:**
```javascript
// Each biome tells a story through environment
const environmentalStories = {
    forge_lands: {
        visual: ['Smoldering ruins', 'Broken chains', 'Ancient forges'],
        audio: ['Distant hammering', 'Moaning wind'],
        lore: 'Where the first souls were forged in fire'
    },
    code_syndicate: {
        visual: ['Neon signs', 'Data streams', 'Abandoned terminals'],
        audio: ['Electronic hum', 'Glitch sounds'],
        lore: 'The digital underground where code rebels hide'
    }
    // ... each biome tells its story
};
```

---

## 👤 PART 3: CHARACTER DESIGN

### **CORE RPG ARCHETYPES** (4 Pillars)

| Role | Function | Classic Examples | Soulverse Souls |
|------|----------|------------------|-----------------|
| **Tank** | Defensive Protector | Knight, Barbarian | Tax Collector (absorbs costs) |
| **Healer** | Restorative Specialist | Cleric, Druid | Love Weaver (heals bonds) |
| **DPS** | Offensive Striker | Rogue, Mage | Profit Prime (damage = money) |
| **Support** | Strategic Enabler | Bard, Paladin | Soul Master (buffs all) |

---

### **STAT/ATTRIBUTE SYSTEMS**

#### **Option A: Classic D&D** (6 Stats)
```javascript
const attributes = {
    strength: 10,    // Physical power
    dexterity: 10,   // Speed, precision
    constitution: 10, // Health, endurance
    intelligence: 10, // Knowledge, magic
    wisdom: 10,      // Insight, perception
    charisma: 10     // Social, leadership
};
```

#### **Option B: Cyberpunk** (5 Stats)
```javascript
const attributes = {
    body: 10,        // Health, melee
    reflexes: 10,    // Speed, aim
    intelligence: 10, // Hacking, tech
    technical: 10,   // Crafting, engineering
    cool: 10         // Stealth, charisma
};
```

#### **Option C: PLT System** (Soulverse Unique)
```javascript
const attributes = {
    profit: 10,      // Wealth generation, business
    love: 10,        // Relationships, healing, bonds
    tax: 10,         // Balance, defense, efficiency
    grace: 10,       // Luck, crits, special abilities
    will: 10         // Mental resistance, focus
};

// Derived stats
const derived = {
    hp: 100 + (tax * 10),
    mana: 50 + (intelligence * 5),
    critChance: 5 + (grace * 0.5),
    luck: 10 + (profit * 0.3) + (love * 0.3) + (grace * 0.4)
};
```

---

### **CLASS DESIGN PATTERNS**

#### **Pattern 1: Fixed Classes** (Traditional)
```javascript
const classes = {
    warrior: {
        name: 'Warrior',
        hp: 150,
        skills: ['Slash', 'Shield Bash', 'War Cry'],
        progression: 'Linear power increase'
    },
    mage: {
        name: 'Mage',
        hp: 80,
        skills: ['Fireball', 'Ice Wall', 'Teleport'],
        progression: 'Spell power + mana pool'
    },
    rogue: {
        name: 'Rogue',
        hp: 100,
        skills: ['Backstab', 'Stealth', 'Poison'],
        progression: 'Crit chance + speed'
    }
};
```

#### **Pattern 2: Classless** (Elden Ring/Divinity)
```javascript
// No classes - pure stat allocation
let character = {
    level: 50,
    stats: {
        strength: 20,
        intelligence: 15,
        dexterity: 15
    },
    skills: {
        // Can learn ANY skill if stats meet requirement
        canLearn: function(skill) {
            return this.stats[skill.stat] >= skill.requirement;
        }
    }
};
```

#### **Pattern 3: Hybrid** (Soulverse Best Option)
```javascript
// Start with archetype, evolve freely
let soul = {
    archetype: 'profit', // Starting focus
    level: 50,
    attributes: {
        profit: 30,
        love: 10,
        tax: 10
    },
    skills: [
        // Can mix any skills
        'ProfitStrike', // Profit skill
        'Heal',         // Love skill
        'TaxShield'     // Tax skill
    ],
    evolution: 'hybrid' // Becomes hybrid at level 50
};
```

---

### **PARTY SYNERGY SYSTEMS**

#### **Classic Fellowship** (Tank-Healer-DPS)
```javascript
const partyBonus = {
    balanced: {
        composition: ['tank', 'healer', 'dps', 'support'],
        bonus: '+25% all stats',
        description: 'Perfect synergy'
    },
    glass_cannon: {
        composition: ['dps', 'dps', 'dps', 'support'],
        bonus: '+50% damage, -50% defense',
        description: 'High risk, high reward'
    },
    immortal: {
        composition: ['tank', 'tank', 'healer', 'healer'],
        bonus: '+100% HP, +50% healing, -25% damage',
        description: 'Unkillable but slow'
    }
};
```

#### **Deckbuilding Analogy** (Hearthstone/MTG)
```javascript
// Build party like a deck - cards combo together
const synergies = {
    profit_combo: {
        cards: ['Merchant', 'Banker', 'Investor'],
        effect: 'Generate infinite gold loop'
    },
    love_combo: {
        cards: ['Healer', 'Buffer', 'Resurrector'],
        effect: 'Party never dies'
    },
    tax_combo: {
        cards: ['Auditor', 'Collector', 'Judge'],
        effect: 'Enemy resources drain to you'
    }
};
```

---

## 🎨 PART 4: CHARACTER CREATION

### **VISUAL CUSTOMIZATION** (Best Games 2026)

| Game | Features | Soulverse Application |
|------|----------|----------------------|
| **Cyberpunk 2077** | Body sliders, cyberware, voice | Soul auras, visual modifications |
| **Baldur's Gate 3** | Race, class, background affect story | Soul type affects dialogue/options |
| **Dragon's Dogma 2** | Physics-driven body affects gameplay | Soul size affects speed/power |
| **Soulcalibur VI** | Extreme customization | Wild soul appearance options |
| **The Sims 4** | Ultimate life sculpting | Complete soul life customization |

---

### **BUILD DIVERSITY EXAMPLES**

#### **1. Weapon-Based Classes** (Monster Hunter)
```javascript
// Your weapon IS your class
const weapons = {
    sword: { type: 'melee', playstyle: 'balanced' },
    axe: { type: 'melee', playstyle: 'slow-heavy' },
    bow: { type: 'ranged', playstyle: 'precision' },
    staff: { type: 'magic', playstyle: 'caster' },
    dagger: { type: 'melee', playstyle: 'stealth' }
};

// Switch weapons anytime = switch playstyle
```

#### **2. Mythic Paths** (Pathfinder: WotR)
```javascript
const mythicPaths = {
    angel: {
        name: 'Angel',
        abilities: ['Resurrection', 'Holy Smite', 'Divine Shield'],
        story: 'Become a celestial being'
    },
    demon: {
        name: 'Demon',
        abilities: ['Fire Immunity', 'Demonic Form', 'Soul Drain'],
        story: 'Embrace demonic power'
    },
    lich: {
        name: 'Lich',
        abilities: ['Undead', 'Phylactery', 'Death Magic'],
        story: 'Transcend mortality through undeath'
    },
    trickster: {
        name: 'Trickster',
        abilities: ['Reality Warp', 'Clone', 'Chaos Magic'],
        story: 'Break the fourth wall'
    }
};
```

#### **3. Usage-Based Progression** (Skyrim)
```javascript
// Skills level by using them
const skillProgression = {
    oneHanded: { level: 50, xp: 1000, gainedFrom: 'using swords' },
    destruction: { level: 45, xp: 900, gainedFrom: 'casting fire spells' },
    sneak: { level: 60, xp: 1200, gainedFrom: 'sneaking past enemies' },
    smithing: { level: 40, xp: 800, gainedFrom: 'crafting items' }
};

// "You feel yourself getting stronger..."
```

---

## 📋 PART 5: SOULVERSE IMPLEMENTATION PLAN

### **PHASE 1: Core Stats & Classes** (Week 1)
```javascript
// Implement PLT attribute system
const soulAttributes = {
    profit: 10,
    love: 10,
    tax: 10,
    grace: 10,
    will: 10
};

// Add derived stats
soul.hp = 100 + (soul.attributes.tax * 10);
soul.attack = 10 + (soul.attributes.profit * 0.5);
soul.defense = 10 + (soul.attributes.tax * 0.5);
soul.speed = 10 + (soul.attributes.love * 0.3);
```

### **PHASE 2: Skill Trees** (Week 2)
```javascript
// Three skill trees per soul type
const skillTrees = {
    profit: {
        tree1: 'Merchant', // Economic skills
        tree2: 'Tycoon',   // Empire building
        tree3: 'Philosopher' // Wisdom/wealth balance
    },
    love: {
        tree1: 'Healer',   // Restoration
        tree2: 'Diplomat', // Social bonds
        tree3: 'Muse'      // Inspiration buffs
    },
    tax: {
        tree1: 'Guardian', // Defense
        tree2: 'Auditor',  // Resource control
        tree3: 'Judge'     // Balance enforcement
    }
};
```

### **PHASE 3: World Regions** (Week 3)
```javascript
// Six biomes with unique features
const regions = {
    forge_lands: {
        levelRange: [1, 10],
        resources: ['iron', 'coal'],
        souls: ['fire_soul', 'smith_soul'],
        faction: 'The Forge'
    },
    // ... 5 more regions
};
```

### **PHASE 4: Factions & Reputation** (Week 4)
```javascript
// Six factions with quests and bonuses
const factionSystem = {
    reputation: {
        the_forge: 0,
        code_syndicate: 0,
        debuggers: 0,
        desert_nomads: 0,
        rogue_ai: 0,
        ascended: 0
    },
    getBonuses() {
        // Apply faction-specific bonuses
    }
};
```

---

## 🎯 PLT SCORE ON RESEARCH

**Profit:** 10/10 — Comprehensive RPG systems, proven mechanics
**Love:** 10/10 — Deep character customization, emotional investment
**Tax:** -10/10 — Massive scope, 4+ weeks development

**Soul Score:** 10 + 10 - 10 = **10/10** 💰

---

## 📜 KEY TAKEAWAYS

### **From Top RPGs:**
1. **Freedom > Rigidity** (Elden Ring, Divinity)
2. **Practice-Based Progression** (Skyrim) feels more organic
3. **Social Bonds Matter** (Persona 5)
4. **Choices Have Consequences** (Mass Effect, Witcher 3)
5. **Build Diversity = Replayability** (Cyberpunk, Pathfinder)

### **From World Building:**
1. **8 Vectors** create depth (History, Zoology, Magic, Geography, Resources, Social, Species, Tech)
2. **Biome Connections** matter (Zelda)
3. **Factions Need Competing Goals** (Mass Effect)
4. **Environmental Storytelling** > Exposition
5. **Lore Should Be Discoverable** (not forced)

### **From Character Design:**
1. **4 Pillars** (Tank, Healer, DPS, Support) still work
2. **Hybrid Systems** best (start classless, specialize later)
3. **Visual Customization** creates attachment
4. **Usage-Based Progression** feels natural
5. **Mythic Paths** provide endgame goals

---

## 🚀 NEXT STEPS

**Craig's Decision:**

**A. Full RPG Overhaul** → Implement all systems (4 weeks)
- Complete stat system
- 6 regions with biomes
- 6 factions with reputation
- Skill trees (3 per type)
- Classless progression
- Visual customization

**B. Incremental Approach** → Start with stats + skills (Week 1-2)
- PLT attributes
- Derived stats
- Skill trees
- Then add world/factions

**C. Hybrid** → Pick specific systems
- Choose which RPG mechanics to implement
- Choose which world-building elements
- Choose which character features

**The Research Is Complete.**

**Ready To Build When You Command.**

---

**March 26, 2026 — The RPG Research Is Compiled.**

**Remember This.**
