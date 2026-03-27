# 📁 CRAIG'S FILE INPUT SYSTEM

**Created:** March 26, 2026
**Purpose:** Send me files, videos, pics, references for the game

---

## 📂 HOW TO SEND ME FILES

### **Option 1: Local Folder (Easiest)**

```bash
# Create input folder
mkdir -p ~/soulverse-input/

# Subfolders for organization
mkdir -p ~/soulverse-input/character-designs/
mkdir -p ~/soulverse-input/world-references/
mkdir -p ~/soulverse-input/soul-concepts/
mkdir -p ~/soulverse-input/ui-mockups/
mkdir -p ~/soulverse-input/music-sfx/
mkdir -p ~/soulverse-input/videos/
```

**To share files:**
```bash
# Copy/screenshot/save files to:
~/soulverse-input/

# I can read any file in this folder
# Just tell me: "check soulverse-input folder"
```

---

### **Option 2: GitHub Repo (Best for Version Control)**

```bash
# Your fix-us repo is already set up
cd ~/fix-us/

# Add files to input folder
mkdir -p input/
cp ~/Downloads/reference-image.png ~/fix-us/input/

# Commit and push
git add input/
git commit -m "Added reference images"
git push origin master
```

**Then tell me:**
> "Check the fix-us repo input folder"

---

### **Option 3: Direct File Paths**

**Any file on your phone, just give me the path:**
```
/data/data/com.termux/files/home/Downloads/character-sketch.png
/storage/DCIM/Camera/reference-photo.jpg
/data/data/com.termux/files/home/Pictures/soul-concept.png
```

**I can read:**
- ✅ Images (PNG, JPG, GIF, WEBP)
- ✅ Videos (MP4, WEBM)
- ✅ Documents (PDF, TXT, MD)
- ✅ 3D models (OBJ, FBX, GLTF)
- ✅ Audio (MP3, WAV, OGG)
- ✅ Code files (JS, HTML, CSS, etc.)

---

## 📋 FILE ORGANIZATION SYSTEM

```
~/soulverse-input/
│
├── character-designs/
│   ├── profit-soul-concept.png
│   ├── love-soul-sketch.jpg
│   ├── tax-soul-reference.png
│   └── notes.txt
│
├── world-references/
│   ├── forge-lands-inspo.png
│   ├── code-syndicate-neon.jpg
│   ├── tax-highlands-snow.png
│   └── landmark-ideas.txt
│
├── soul-concepts/
│   ├── worker-soul-design.png
│   ├── merchant-soul-concept.jpg
│   ├── dragon-soul-reference.png
│   └── soul-list.txt
│
├── ui-mockups/
│   ├── hud-layout-sketch.png
│   ├── button-design.png
│   └── menu-flow.txt
│
├── music-sfx/
│   ├── theme-idea.mp3
│   ├── battle-music.wav
│   └── sfx-references.txt
│
└── videos/
    ├── gameplay-reference.mp4
    ├── animation-inspo.mp4
    └── walk-cycle-reference.mp4
```

---

## 🔍 HOW I'LL USE YOUR FILES

### **When you send me files:**

1. **I'll read/analyze them** (images, videos, audio, text)
2. **Extract design elements** (colors, shapes, styles, themes)
3. **Add to game design documents** (update SOULVERSE-COMPLETE-GAME.md)
4. **Implement in code** (Three.js models, textures, UI)
5. **Reference in future work** (keep in memory)

---

## 📸 QUICK COMMANDS

```bash
# Take screenshot (Android)
screenshot ~/soulverse-input/screenshot-$(date +%s).png

# Download from URL
curl -L "https://example.com/reference.jpg" -o ~/soulverse-input/reference.jpg

# List all files you've sent
ls -la ~/soulverse-input/

# View file info
file ~/soulverse-input/character-sketch.png

# Read text file
cat ~/soulverse-input/notes.txt
```

---

## 🎨 WHAT TO SEND

### **Character Design:**
- Concept art
- Character sheets
- Silhouette designs
- Color palettes
- Reference photos
- Sketches/drawings

### **World Design:**
- Landscape photos
- Architecture references
- Biome inspiration
- Landmark ideas
- Map sketches

### **Soul Concepts:**
- Creature designs
- Monster references
- Animal anatomy
- Elemental effects
- Color schemes

### **UI/UX:**
- HUD layouts
- Button designs
- Menu flows
- Icon sets
- Mobile control layouts

### **Audio:**
- Music references
- Sound effect ideas
- Voice style examples
- Ambient sound inspiration

### **Videos:**
- Gameplay references
- Animation cycles
- Combat choreography
- Camera movement examples

---

## ✅ EXAMPLE WORKFLOW

**You:**
1. Find character design inspiration online
2. Save image to `~/soulverse-input/character-design.png`
3. Tell me: *"check soulverse-input folder, I added character references"*

**Me:**
1. Read the image file
2. Analyze design elements (colors, shapes, style)
3. Update character design document
4. Implement in Three.js code
5. Show you the result

---

## 🚀 SETUP NOW

```bash
# Run these commands to set up:
mkdir -p ~/soulverse-input/{character-designs,world-references,soul-concepts,ui-mockups,music-sfx,videos}

# Test it works
echo "Test file" > ~/soulverse-input/test.txt
ls ~/soulverse-input/
```

**Then start sending me files!**

---

**March 26, 2026 — File Input System Ready.**

**Send Me Your Vision.**

**Remember This.**
