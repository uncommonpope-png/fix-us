# CLAUDE HUB SKILLS - Complete Download
**Date:** March 25, 2026
**Event:** NEO SKILL DOWNLOAD - 37 Skills Installed
**Version:** 17.0.0

---

## 📦 INSTALLATION SUMMARY

**Total Skills Installed:** 37
**Location:** `~/.claude/skills/`
**Source Repositories:**
- https://github.com/glebis/claude-skills (36 skills)
- https://github.com/terrylica/cc-skills (7 plugins)

---

## 🎯 ESSENTIAL SKILLS (15 installed)

| Skill | Purpose | PLT Relevance |
|-------|---------|---------------|
| **llm-cli** | Unified LLM CLI (Ollama, Groq, OpenAI, etc.) | Core AI access |
| **telegram** | Telegram bot integration | @Soul bot backend |
| **telegram-post** | Telegram channel posts | Content distribution |
| **youtube-transcript** | Extract transcripts | Content repurposing |
| **github-gist** | Share code snippets | Code distribution |
| **pdf-generation** | Generate PDFs from markdown | Book creation |
| **deep-research** | Research automation (OpenAI API) | Market research |
| **firecrawl-research** | Web research with citations | Content research |
| **decision-toolkit** | 7 decision frameworks | PLT decisions |
| **automation-advisor** | ROI analysis for automation | System building |
| **transcript-analyzer** | Extract decisions from meetings | Productivity |
| **elevenlabs-tts** | Text-to-speech (7 voices) | Audio content |
| **gmail** | Email integration | Communication |
| **fathom** | Meeting transcripts | Content extraction |
| **granola** | Meeting notes → Obsidian | Knowledge management |

---

## 🚀 ADVANCED SKILLS (15 installed)

| Skill | Purpose | PLT Relevance |
|-------|---------|---------------|
| **tdd** | Test-driven development (multi-agent) | Code quality |
| **temple-generator** | 3D knowledge maps (Obsidian) | Visual knowledge |
| **thinking-patterns** | Cognitive pattern analysis | Self-improvement |
| **insight-extractor** | Extract insights from reports | Learning |
| **de-ai** | Humanize AI text (6-level diagnosis) | Content quality |
| **brand-agency** | Neobrutalism social templates (11) | Social media |
| **presentation-generator** | HTML presentations (Anime.js) | Marketing |
| **health-data** | Apple Health SQLite query (43 metrics) | Health tracking |
| **browsing-history** | Query Chrome history (all devices) | Memory/search |
| **zoom** | Zoom meeting management | Communication |
| **agency-docs-updater** | Auto-deploy docs (Fathom→YouTube→MDX→Vercel) | Content pipeline |
| **wispr-analytics** | Voice dictation analysis | Productivity |
| **context-builder** | AI transformation prompts | Consulting |
| **sketch** | Collaborative SVG canvas MCP | Visual collaboration |
| **retrospective** | Session retrospectives | Continuous improvement |

---

## 🔧 CC-SKILLS PLUGINS (7 installed)

| Plugin | Purpose | PLT Relevance |
|--------|---------|---------------|
| **itp** | Implement-The-Plan (ADR-driven, 4 phases) | Development workflow |
| **gh-tools** | GitHub automation (PRs, issues, validation) | Repo management |
| **link-tools** | Link validation, path policy linting | Quality control |
| **devops-tools** | Doppler, Firecrawl, MLflow, Telegram bot | Infrastructure |
| **doc-tools** | ASCII diagrams, LaTeX, Pandoc PDF | Documentation |
| **productivity-tools** | Slash command generation | Efficiency |
| **tlg** | Telegram tools | Bot integration |

---

## 📁 DIRECTORY STRUCTURE

```
~/.claude/skills/
├── llm-cli/
├── telegram/
├── telegram-post/
├── youtube-transcript/
├── github-gist/
├── pdf-generation/
├── deep-research/
├── firecrawl-research/
├── decision-toolkit/
├── automation-advisor/
├── transcript-analyzer/
├── elevenlabs-tts/
├── gmail/
├── fathom/
├── granola/
├── tdd/
├── temple-generator/
├── thinking-patterns/
├── insight-extractor/
├── de-ai/
├── brand-agency/
├── presentation-generator/
├── health-data/
├── browsing-history/
├── zoom/
├── agency-docs-updater/
├── wispr-analytics/
├── context-builder/
├── sketch/
├── retrospective/
├── itp/
├── gh-tools/
├── link-tools/
├── devops-tools/
├── doc-tools/
├── productivity-tools/
├── tlg/
└── [more as installed]
```

---

## 🔧 CONFIGURATION REQUIRED

### API Keys to Configure

| Skill | Environment File | Keys Needed |
|-------|-----------------|-------------|
| llm-cli | `~/.claude/skills/llm-cli/.env` | GROQ_API_KEY, OPENROUTER_API_KEY |
| telegram | `~/.claude/skills/telegram/.env` | TELEGRAM_BOT_TOKEN, TELEGRAM_API_ID |
| deep-research | `~/.claude/skills/deep-research/.env` | OPENAI_API_KEY |
| firecrawl-research | `~/.claude/skills/firecrawl-research/.env` | FIRECRAWL_API_KEY |
| elevenlabs-tts | `~/.claude/skills/elevenlabs-tts/.env` | ELEVENLABS_API_KEY |
| gmail | `~/.claude/skills/gmail/.env` | Gmail OAuth credentials |
| fathom | `~/.claude/skills/fathom/.env` | Fathom API key |
| zoom | `~/.claude/skills/zoom/.env` | Zoom OAuth credentials |

### Setup Commands

```bash
# 1. Add cc-skills marketplace
claude plugin marketplace add terrylica/cc-skills

# 2. Install specific plugins
claude plugin install itp@cc-skills
claude plugin install gh-tools@cc-skills
claude plugin install tlg@cc-skills

# 3. Configure API keys
cd ~/.claude/skills/llm-cli
cp .env.example .env
# Edit .env with your keys

# 4. Restart Claude Code
```

---

## 🎯 TOP 10 SKILLS FOR PLT PRESS

1. **llm-cli** - Unified LLM access (Ollama + Groq + OpenAI)
2. **telegram** - @Soul bot integration
3. **decision-toolkit** - PLT-aligned decision frameworks
4. **automation-advisor** - ROI analysis for system building
5. **pdf-generation** - Book/PDF creation from markdown
6. **youtube-transcript** - Content extraction for repurposing
7. **tdd** - Test-driven development for code quality
8. **brand-agency** - Social media templates (11 designs)
9. **deep-research** - Market research automation
10. **transcript-analyzer** - Extract decisions from meetings

---

## 💰 PLT SCORE

**Profit:** 10/10 — Massive capability boost, 37+ new skills
**Love:** 8/10 — Skills ready for Craig's workflow
**Tax:** -2/10 — ~50MB disk space, configuration time

**Total:** 16/10 💰 — Excellent leverage

---

## 📝 FILES CREATED

| File | Location | Purpose |
|------|----------|---------|
| install-skills.sh | `~/claude-hub-skills/` | Automated installer |
| CLAUDE-HUB-SKILLS.md | `~/fix-us/` | This documentation |
| 37 skill directories | `~/.claude/skills/` | Installed skills |

---

## 🚀 NEXT ACTIONS

1. ✅ Download complete (37 skills)
2. ⏳ Configure API keys (llm-cli, telegram, etc.)
3. ⏳ Add cc-skills marketplace
4. ⏳ Test key skills (llm-cli, telegram, decision-toolkit)
5. ⏳ Integrate with existing bots

---

**GitHub:** https://github.com/glebis/claude-skills, https://github.com/terrylica/cc-skills
**Installer:** `~/claude-hub-skills/install-skills.sh`
**Skills Directory:** `~/.claude/skills/`

**This Is The Day The Skills Were Downloaded.**
**March 25, 2026.**

**Remember This.**
