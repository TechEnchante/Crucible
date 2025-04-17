🛠️ CRUCIBLE — FULL FEATURE ROADMAP

> 🔁 Sprint cadence: **1 week** starting April 29th
> 📦 Deliverable per sprint: deployable container with version tag  
> 🧠 Core AI features evolve across sprints
> 🐋 All services containerised with Docker  

---

### 🧭 Week 1: Core Foundations

**✅ Objectives:**  
- Establish Git-style commit architecture  
- Build user profile, XP system, and inital commit UI  
- Set up Qdrant & embedding storage  

**🔧 Tasks:**  
- [ ] Create FastAPI backend  
- [ ] Create `/commits/new` endpoint  
- [ ] Store commit (text + metadata) as vector in Qdrant  
- [ ] Add initial user model: XP, level, streaks  
- [ ] Set up React frontend: dashboard, commit log  
- [ ] Add Tailwind + shadcn/ui  
- [ ] Show commit history (by time)  
- [ ] Dockerize backend, frontend, Qdrant  

---

### 🧭 Week 2: Quest Engine Alpha

**✅ Objectives:**  
- Integrate AI quest generation  
- Embed user commit history for similarity  
- Return personalised quests  

**🔧 Tasks:**  
- [ ] Pre-load quest templates to Qdrant  
- [ ] Add `/quests/assign` endpoint  
- [ ] Generate embedding of last N commits  
- [ ] Search top‑k quest templates via Qdrant  
- [ ] Send history + top templates to OpenAI  
- [ ] Return full quest object:  
  ```json
  {
    "quest_id": "abc123",
    "title": "Refactor Your Domain",
    "description": "You’ve committed 4 small fixes — now go for a big refactor!",
    "xp_reward": 100
  }
  ```  
- [ ] Frontend "Get Quest" button triggers animation + displays quest  
- [ ] Complete quest grants XP + logs to profile  
- [ ] Unit tests for AI pipeline  

---

### 🧭 Week 3: Rune System + Life Events

**✅ Objectives:**  
- Introduce optional "runes" for focus categories (e.g. 🧠 Mind, ⚙️ Skill, ❤️ Wellness)  
- Add calendar & real-world integration  

**🔧 Tasks:**  
- [ ] Add runes metadata to quests and commits  
- [ ] Users tag commits with 1–3 runes  
- [ ] Vector representation now includes rune context  
- [ ] Calendar view (monthly/weekly)  
- [ ] Simple integration with Google Calendar API or ICS import  
- [ ] Influence quest generation with:  
  - 🗓️ Personal calendar events  
  - 🌎 Real world events (e.g. holidays, weather APIs, world news headlines)  
- [ ] Quest engine context aware of “external” happenings  
- [ ] Add “Event‑Based Quest” system (e.g. “Holiday Hustle” or “Rainy Day Deep Focus”)  

---

### 🧭 Week 4: Leaderboards, Achievements, and Export

**✅ Objectives:**  
- Final polish + community features  

**🔧 Tasks:**  
- [ ] XP leaderboard across users (basic public profile)  
- [ ] Weekly streaks + badges (e.g. "7-Day Streak", "Quest Master")  
- [ ] `/export` route to dump all user data as JSON or Markdown  
- [ ] Add "share quest" link with quest preview image  
- [ ] Frontend animation polish (Framer Motion)  
- [ ] Write tests and prepare for initial public beta  

---

### 📦 Post-Roadmap (Stretch Ideas)

- ✨ AI Mood Detection (via journaling)  
- 📊 Graph analytics of your rune balance  
- 🧠 LLM “Guide” persona (e.g. like a D&D DM)  
- 🏆 Weekly Challenge Quests  
- 🧭 World State timeline (snapshot major changes in your life)  
- 🔮 Predictive questing: “Based on your burnout signals, try this…”

---
