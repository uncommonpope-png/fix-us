# MASTER WORLD CODE: NEO-KEMET

**Complete World Generation & Management System**

A modular, extensible foundation defining terrain, regions, buildings, vegetation, and systems for the Neo-Kemet game world.

---

## File Structure Overview

```
NeoKemet/
├── World/
│   ├── Regions/
│   ├── Terrain/
│   ├── Biomes/
│   └── Weather/
├── Buildings/
│   ├── ArchitecturalStyles/
│   ├── Interiors/
│   └── Destructibles/
├── Vegetation/
│   ├── Flora/
│   └── Environmental/
├── Navigation/
│   ├── Roads/
│   ├── Canals/
│   └── Flight/
└── Systems/
    ├── Streaming/
    ├── Physics/
    └── Optimization/
```

---

## 1. WORLD REGIONS MASTER

```csharp
// ============================================
// REGION ENUMERATION
// ============================================

public enum RegionID
{
    DeltaSprawl = 0,
    CorporateDunes = 1,
    NeoKemetCore = 2,
    ExclusionZone = 3,
    TheAether = 4
}

// ============================================
// REGION MASTER DATA
// ============================================

[System.Serializable]
public class RegionData
{
    public RegionID id;
    public string displayName;
    public Vector2 worldPosition;      // Center point in world space
    public Vector2 size;                // Width x Depth in kilometers
    public float minHeight;             // Lowest terrain point (meters)
    public float maxHeight;             // Highest terrain point (meters)
    public BiomeType primaryBiome;
    public BiomeType secondaryBiome;
    public AtmosphericData atmosphere;
    public List<SubRegion> subRegions;
    public List<Landmark> landmarks;
    public List<SpawnPoint> spawnPoints;
    public DifficultyRating difficulty;
    public int recommendedLevel;
}

// ============================================
// SUB-REGION DEFINITION
// ============================================

[System.Serializable]
public class SubRegion
{
    public string name;
    public Vector2 boundsMin;           // Local region coordinates
    public Vector2 boundsMax;
    public float heightOffset;
    public TerrainType terrainType;
    public List<BuildingLot> buildingLots;
    public List<POI> pointsOfInterest;
}

// ============================================
// ATMOSPHERIC CONDITIONS
// ============================================

[System.Serializable]
public class AtmosphericData
{
    public Color ambientLight;
    public Color fogColor;
    public float fogDensity;
    public float visibilityRange;       // Meters
    public bool hasDayNightCycle;
    public List<WeatherType> possibleWeather;
    public float particleDensity;
    public float lightPollution;        // 0-1, affects star visibility
}
```

---

## 2. TERRAIN SYSTEM

```csharp
// ============================================
// TERRAIN GENERATION PARAMETERS
// ============================================

[System.Serializable]
public class TerrainGenerationData
{
    // Heightmap generation
    public float heightmapResolution = 2049;    // Power of two + 1
    public float terrainSize = 8192;            // Meters (8km per region)
    public float heightMultiplier = 500f;       // Max height in meters
    
    // Noise layers
    public NoiseLayer[] noiseLayers;
    
    // Erosion
    public ErosionParameters erosion;
    
    // Splatmap (texture layers)
    public TerrainLayer[] terrainLayers;
    
    // Detail objects (grass, small rocks)
    public DetailLayer[] detailLayers;
    
    // Trees
    public TreeLayer[] treeLayers;
}

// ============================================
// NOISE LAYER FOR HEIGHTMAP
// ============================================

[System.Serializable]
public class NoiseLayer
{
    public float scale;                 // 0.001 - 0.1
    public float amplitude;             // Height contribution
    public float frequency;             // Wavelength
    public int octaves;                 // 1-8
    public float persistence;           // 0.3-0.7
    public float lacunarity;            // 1.5-2.5
    public Vector2 offset;
}

// ============================================
// EROSION SIMULATION
// ============================================

[System.Serializable]
public class ErosionParameters
{
    public int iterations = 50000;
    public float erosionRate = 0.01f;
    public float depositionRate = 0.01f;
    public float evaporationRate = 0.5f;
    public float gravity = 9.8f;
    public float rainfall = 0.5f;
}

// ============================================
// TERRAIN LAYER (SPLATMAP)
// ============================================

[System.Serializable]
public class TerrainLayer
{
    public string name;
    public Texture2D diffuseTexture;
    public Texture2D normalMap;
    public Texture2D maskMap;
    public float metallic;
    public float smoothness;
    public Vector2 tileSize;
    public float minHeight;
    public float maxHeight;
    public float minSteepness;
    public float maxSteepness;
}

// ============================================
// DETAIL LAYER (GRASS, SMALL FLORA)
// ============================================

[System.Serializable]
public class DetailLayer
{
    public string name;
    public GameObject detailPrefab;
    public float density;               // Per square meter
    public float minHeight;
    public float maxHeight;
    public float minSteepness;
    public float maxSteepness;
    public Color dryColor;
    public Color healthyColor;
    public float noiseScale;
}

// ============================================
// TREE LAYER
// ============================================

[System.Serializable]
public class TreeLayer
{
    public string name;
    public GameObject treePrefab;
    public float density;               // Per square meter
    public float minHeight;
    public float maxHeight;
    public float minSteepness;
    public float maxSteepness;
    public float scaleVariation;
    public float rotationVariation;
}
```

---

## 3. BIOME SYSTEM

```csharp
// ============================================
// BIOME ENUMERATION
// ============================================

public enum BiomeType
{
    FloodedUrban,       // Delta Sprawl
    AridDesert,         // Corporate Dunes
    UrbanCore,          // Neo-Kemet Core
    VolcanicWasteland,  // Exclusion Zone
    OrbitalVoid,        // The Aether
    TransitionZone      // Between biomes
}

// ============================================
// BIOME MASTER DATA
// ============================================

[System.Serializable]
public class BiomeData
{
    public BiomeType type;
    public string name;
    public Color groundColor;
    public Color foliageColor;
    public Color waterColor;
    
    // Generation parameters
    public TerrainGenerationData terrainGen;
    public List<FloraSpawnData> flora;
    public List<BuildingStyle> allowedArchitecture;
    
    // Visual effects
    public ParticleSystem ambientParticles;
    public AudioClip ambientAudio;
    public float ambientVolume;
    
    // Gameplay modifiers
    public float movementSpeedModifier = 1f;
    public float staminaDrainModifier = 1f;
    public float stealthBonus;
    public float visibilityBonus;
}
```

---

## 4. BUILDING SYSTEM

```csharp
// ============================================
// BUILDING STYLES
// ============================================

public enum BuildingStyle
{
    AncientEgyptian,
    CyberpunkRetrofit,
    CorporateModern,
    PostApocalyptic,
    Orbital,
    Slum
}

// ============================================
// BUILDING MASTER DATA
// ============================================

[System.Serializable]
public class BuildingData
{
    public string id;
    public string displayName;
    public BuildingStyle style;
    public GameObject exteriorPrefab;
    public GameObject interiorPrefab;
    public Vector3 size;                // Width, Height, Depth
    public bool isEnterable;
    public bool isDestructible;
    public float destructibilityHealth;
    public List<BuildingAttachment> attachments;
    public List<LightFixture> lights;
    public List<InteractablePoint> interactables;
}

// ============================================
// PROCEDURAL BUILDING GENERATION
// ============================================

[System.Serializable]
public class ProceduralBuildingGenerator
{
    public BuildingStyle style;
    public BuildingSize sizeCategory;    // Small, Medium, Large, Monumental
    
    // Modular pieces
    public List<GameObject> bases;       // Foundation pieces
    public List<GameObject> walls;       // Wall segments
    public List<GameObject> columns;     // Egyptian columns
    public List<GameObject> roofs;       // Pyramid, flat, domed
    public List<GameObject> decorations; // Hieroglyphs, neon signs
    public List<GameObject> cyberAddons; // Neon tubes, holograms, screens
    
    // Generation rules
    public float baseHeight;
    public float columnDensity;
    public float decorationDensity;
    public float cyberneticPercentage;   // 0-1, how much cyberpunk overlay
}

// ============================================
// BUILDING LOT
// ============================================

[System.Serializable]
public class BuildingLot
{
    public Vector3 position;
    public Vector2 size;
    public BuildingStyle allowedStyles;
    public BuildingData currentBuilding;
    public bool isOwned;
    public string ownerID;               // Player or NPC faction
    public float propertyValue;
    public LotType type;                 // Residential, Commercial, Industrial, Monumental
}

// ============================================
// LANDMARK (UNIQUE STRUCTURES)
// ============================================

[System.Serializable]
public class Landmark
{
    public string name;
    public LandmarkType type;            // Temple, Pyramid, CorporateHQ, Arena
    public Vector3 position;
    public BuildingData building;
    public bool isEnterable;
    public bool isRaidDungeon;
    public int recommendedPartySize;
    public List<QuestTrigger> quests;
    public List<BossEncounter> bosses;
    public List<LootTable> loot;
}
```

---

## 5. VEGETATION SYSTEM

```csharp
// ============================================
// FLORA TYPES
// ============================================

public enum FloraType
{
    Papyrus,            // Tall reeds for Delta
    LotusFlower,        // Bioluminescent, opens/closes
    CrystalFormation,   // Pink drip crystals
    DesertBrush,        // Dry shrubs for dunes
    PalmTree,           // Traditional oasis trees
    CyberVine,          // Neon-glowing vines on buildings
    AshPlant,           // Grey, dead-looking plants for Exclusion Zone
    VoidBloom           // Zero-g flora for Aether
}

// ============================================
// FLORA SPAWN DATA
// ============================================

[System.Serializable]
public class FloraSpawnData
{
    public FloraType type;
    public GameObject prefab;
    public float spawnDensity;           // Per 100m²
    public float scaleMin;
    public float scaleMax;
    public bool hasAnimation;
    public AnimationType animation;      // Sway, Pulse, Open/Close
    public bool isHarvestable;
    public ResourceType harvestResource;
    public int harvestAmount;
}

// ============================================
// BIOLUMINESCENT FLORA
// ============================================

[System.Serializable]
public class BioluminescentFlora : FloraSpawnData
{
    public Color emissionColor;
    public float emissionIntensity;
    public float pulseSpeed;
    public bool reactsToPlayer;
    public float activationDistance;
}

// ============================================
// ENVIRONMENTAL PROP SYSTEM
// ============================================

[System.Serializable]
public class EnvironmentalProp
{
    public string name;
    public GameObject prefab;
    public PropCategory category;        // Rocks, Debris, Ruins, Vehicles
    public float spawnDensity;
    public float minScale;
    public float maxScale;
    public bool isInteractable;
    public bool hasPhysics;
}
```

---

## 6. ROAD & NAVIGATION SYSTEM

```csharp
// ============================================
// ROAD TYPES
// ============================================

public enum RoadType
{
    AncientStone,       // Original Egyptian roads
    PavedHighway,       // Modern asphalt
    Elevated,           // Sky bridges
    Canal,              // Waterways
    SandTrack,          // Unpaved desert routes
    FlightCorridor      // Designated flight paths
}

// ============================================
// ROAD NETWORK DATA
// ============================================

[System.Serializable]
public class RoadNetworkData
{
    public List<RoadSegment> segments;
    public List<Intersection> intersections;
    public List<TrafficLight> trafficLights;
    public TrafficDensity trafficDensity;
}

// ============================================
// ROAD SEGMENT
// ============================================

[System.Serializable]
public class RoadSegment
{
    public string id;
    public RoadType type;
    public Vector3[] splinePoints;      // Bezier spline path
    public float width;
    public int lanes;
    public bool hasSidewalk;
    public bool hasNeonLighting;
    public GameObject[] decoObjects;    // Streetlights, signs
    public float speedLimit;
    public bool isPlayerDrivable;
}
```

---

## 7. WATER SYSTEM

```csharp
// ============================================
// WATER BODY DATA
// ============================================

[System.Serializable]
public class WaterBodyData
{
    public string name;
    public WaterType type;               // Canal, River, Lake, Ocean
    public Vector3[] boundaryPoints;
    public float waterLevel;
    public float flowSpeed;
    public Vector2 flowDirection;
    public Color waterColor;
    public float turbidity;
    public bool isNavigable;
    public bool isPolluted;
    public float pinkDripConcentration;  // 0-1
    public List<WaterInteraction> interactions;
}

// ============================================
// WATER PHYSICS
// ============================================

[System.Serializable]
public class WaterPhysicsData
{
    public float buoyancyStrength = 10f;
    public float dragCoefficient = 0.99f;
    public float angularDrag = 0.5f;
    public float waveAmplitude = 0.5f;
    public float waveFrequency = 1f;
    public float waveSpeed = 1f;
    public bool hasCurrent;
    public float currentStrength;
}
```

---

## 8. WEATHER SYSTEM

```csharp
// ============================================
// WEATHER TYPES
// ============================================

public enum WeatherType
{
    Clear,
    LightRain,
    HeavyRain,
    Sandstorm,
    PinkStorm,
    Smog,
    AshFall,
    ClearSkies    // Aether only
}

// ============================================
// WEATHER DATA
// ============================================

[System.Serializable]
public class WeatherData
{
    public WeatherType type;
    public string displayName;
    public float durationMin;
    public float durationMax;
    public float transitionTime;
    
    // Visual effects
    public ParticleSystem particleEffect;
    public Material skyboxMaterial;
    public Light sunLight;
    public float lightIntensity;
    public Color fogColor;
    public float fogDensity;
    
    // Audio
    public AudioClip ambientSound;
    public float ambientVolume;
    
    // Gameplay modifiers
    public float visibilityModifier;
    public float movementSpeedModifier;
    public float creatureAggressionModifier;
    public float lootDropModifier;
    public List<WeatherHazard> hazards;
}

// ============================================
// WEATHER HAZARD
// ============================================

[System.Serializable]
public class WeatherHazard
{
    public HazardType type;              // Lightning, AcidRain, Radiation
    public float frequency;              // Occurrences per minute
    public float damagePerSecond;
    public GameObject hazardVisual;
}
```

---

## 9. LIGHTING SYSTEM

```csharp
// ============================================
// LIGHTING ZONES
// ============================================

[System.Serializable]
public class LightingZone
{
    public string name;
    public RegionID region;
    public Bounds bounds;
    
    // Ambient lighting
    public Color ambientLight;
    public float ambientIntensity;
    
    // Sun/Moon
    public Light sun;
    public Light moon;
    public float sunAngle;
    public float moonAngle;
    
    // Artificial lighting density
    public float neonDensity;
    public float streetlightDensity;
    public bool hasDynamicNeon;
    
    // Volumetric lighting
    public bool volumetricFog;
    public float volumetricIntensity;
}

// ============================================
// NEON SIGN DATA
// ============================================

[System.Serializable]
public class NeonSignData
{
    public string text;
    public string hieroglyphicText;      // Optional ancient version
    public Color emissionColor;
    public float flickerRate;
    public bool isAnimated;
    public AnimationType animation;
    public Vector3 position;
    public Vector3 rotation;
    public Vector3 scale;
}
```

---

## 10. STREAMING & OPTIMIZATION

```csharp
// ============================================
// WORLD STREAMING MANAGER
// ============================================

[System.Serializable]
public class WorldStreamingSettings
{
    // Grid system
    public float cellSize = 500f;         // 500m grid cells
    public int loadRadius = 3;            // Load cells within 3 cells of player
    public int unloadRadius = 5;          // Unload beyond 5 cells
    
    // LOD distances
    public float terrainLOD0 = 100f;       // Full detail
    public float terrainLOD1 = 250f;
    public float terrainLOD2 = 500f;
    public float terrainLOD3 = 1000f;
    
    public float buildingLOD0 = 50f;
    public float buildingLOD1 = 150f;
    public float buildingLOD2 = 300f;
    public float buildingLOD3 = 600f;
    
    public float vegetationLOD0 = 30f;
    public float vegetationLOD1 = 80f;
    public float vegetationLOD2 = 150f;
    
    // Impostor system
    public bool useImpostors = true;
    public float impostorDistance = 500f;
    
    // Async loading
    public bool asyncLoading = true;
    public int maxConcurrentLoads = 3;
    public float loadPriorityDistance = 200f;
}

// ============================================
// WORLD CELL
// ============================================

[System.Serializable]
public class WorldCell
{
    public int x;
    public int z;
    public RegionID region;
    public bool isLoaded;
    public bool isActive;
    public List<GameObject> loadedObjects;
    public List<BuildingData> buildings;
    public List<FloraSpawn> flora;
    public List<EnvironmentalProp> props;
    public TerrainData terrain;
}
```

---

## 11. MASTER WORLD CONTROLLER

```csharp
// ============================================
// MASTER WORLD CONTROLLER (MONOBEHAVIOUR)
// ============================================

using UnityEngine;
using System.Collections.Generic;

public class MasterWorldController : MonoBehaviour
{
    // Singleton
    public static MasterWorldController Instance;
    
    // World data
    [Header("World Configuration")]
    public string worldName = "Neo-Kemet";
    public float worldSeed = 1337;
    public List<RegionData> regions;
    public WorldStreamingSettings streamingSettings;
    
    // Runtime state
    private Dictionary<RegionID, RegionData> regionDict;
    private Dictionary<Vector2Int, WorldCell> loadedCells;
    private RegionData currentRegion;
    private Vector3 playerPosition;
    
    // Events
    public System.Action<RegionID> OnRegionChanged;
    public System.Action<WeatherType> OnWeatherChanged;
    public System.Action<Vector3> OnPlayerMoved;
    
    void Awake()
    {
        Instance = this;
        InitializeWorld();
    }
    
    void InitializeWorld()
    {
        // Build region dictionary
        regionDict = new Dictionary<RegionID, RegionData>();
        foreach (var region in regions)
        {
            regionDict[region.id] = region;
        }
        
        // Initialize terrain generators
        foreach (var region in regions)
        {
            InitializeRegionTerrain(region);
        }
        
        // Start streaming system
        StartCoroutine(StreamingUpdate());
        
        // Initialize weather system
        InitializeWeatherSystem();
        
        Debug.Log($"World initialized: {worldName}");
    }
    
    void InitializeRegionTerrain(RegionData region)
    {
        // Generate heightmap based on region biome
        // Generate splatmaps
        // Place flora and buildings
        // Set up lighting zones
    }
    
    System.Collections.IEnumerator StreamingUpdate()
    {
        while (true)
        {
            UpdateLoadedCells();
            yield return new WaitForSeconds(0.5f);
        }
    }
    
    void UpdateLoadedCells()
    {
        // Get player position
        playerPosition = Camera.main.transform.position;
        
        // Calculate current cell
        int centerX = Mathf.FloorToInt(playerPosition.x / streamingSettings.cellSize);
        int centerZ = Mathf.FloorToInt(playerPosition.z / streamingSettings.cellSize);
        
        // Determine current region
        UpdateCurrentRegion(playerPosition);
        
        // Load/unload cells
        for (int x = centerX - streamingSettings.loadRadius; x <= centerX + streamingSettings.loadRadius; x++)
        {
            for (int z = centerZ - streamingSettings.loadRadius; z <= centerZ + streamingSettings.loadRadius; z++)
            {
                Vector2Int cellCoord = new Vector2Int(x, z);
                if (!loadedCells.ContainsKey(cellCoord))
                {
                    LoadCell(cellCoord);
                }
            }
        }
        
        // Unload distant cells
        List<Vector2Int> toUnload = new List<Vector2Int>();
        foreach (var cell in loadedCells)
        {
            int dx = Mathf.Abs(cell.Key.x - centerX);
            int dz = Mathf.Abs(cell.Key.y - centerZ);
            if (dx > streamingSettings.unloadRadius || dz > streamingSettings.unloadRadius)
            {
                toUnload.Add(cell.Key);
            }
        }
        
        foreach (var coord in toUnload)
        {
            UnloadCell(coord);
        }
    }
    
    void UpdateCurrentRegion(Vector3 position)
    {
        foreach (var region in regions)
        {
            float halfWidth = region.size.x / 2;
            float halfDepth = region.size.y / 2;
            
            if (position.x >= region.worldPosition.x - halfWidth &&
                position.x <= region.worldPosition.x + halfWidth &&
                position.z >= region.worldPosition.y - halfDepth &&
                position.z <= region.worldPosition.y + halfDepth)
            {
                if (currentRegion?.id != region.id)
                {
                    currentRegion = region;
                    OnRegionChanged?.Invoke(region.id);
                    ApplyRegionAtmosphere(region);
                }
                break;
            }
        }
    }
    
    void ApplyRegionAtmosphere(RegionData region)
    {
        // Update fog
        RenderSettings.fogColor = region.atmosphere.fogColor;
        RenderSettings.fogDensity = region.atmosphere.fogDensity;
        
        // Update ambient light
        RenderSettings.ambientLight = region.atmosphere.ambientLight;
        
        // Update skybox if needed
        // Update lighting zones
    }
    
    void LoadCell(Vector2Int coord)
    {
        WorldCell cell = new WorldCell
        {
            x = coord.x,
            z = coord.y,
            isLoaded = true,
            isActive = true
        };
        
        // Determine region for this cell
        cell.region = GetRegionForCell(coord);
        
        // Generate terrain for cell
        GenerateCellTerrain(cell);
        
        // Spawn buildings
        SpawnBuildingsInCell(cell);
        
        // Spawn flora
        SpawnFloraInCell(cell);
        
        // Spawn props
        SpawnPropsInCell(cell);
        
        loadedCells[coord] = cell;
    }
    
    void UnloadCell(Vector2Int coord)
    {
        if (loadedCells.TryGetValue(coord, out WorldCell cell))
        {
            // Destroy all loaded objects
            foreach (var obj in cell.loadedObjects)
            {
                if (obj != null)
                    Destroy(obj);
            }
            
            loadedCells.Remove(coord);
        }
    }
    
    RegionID GetRegionForCell(Vector2Int coord)
    {
        Vector3 cellCenter = new Vector3(coord.x * streamingSettings.cellSize, 0, coord.y * streamingSettings.cellSize);
        
        foreach (var region in regions)
        {
            float halfWidth = region.size.x / 2;
            float halfDepth = region.size.y / 2;
            
            if (cellCenter.x >= region.worldPosition.x - halfWidth &&
                cellCenter.x <= region.worldPosition.x + halfWidth &&
                cellCenter.z >= region.worldPosition.y - halfDepth &&
                cellCenter.z <= region.worldPosition.y + halfDepth)
            {
                return region.id;
            }
        }
        
        return RegionID.DeltaSprawl; // Default
    }
    
    void GenerateCellTerrain(WorldCell cell)
    {
        RegionData region = regionDict[cell.region];
        BiomeData biome = GetBiomeData(region.primaryBiome);
        
        // Generate heightmap for this cell
        // Apply terrain layers
        // Create Terrain object
    }
    
    void SpawnBuildingsInCell(WorldCell cell)
    {
        RegionData region = regionDict[cell.region];
        
        // Get building lots for this cell
        // Spawn buildings based on lot data
        // Apply appropriate style for region
    }
    
    void SpawnFloraInCell(WorldCell cell)
    {
        RegionData region = regionDict[cell.region];
        BiomeData biome = GetBiomeData(region.primaryBiome);
        
        foreach (var flora in biome.flora)
        {
            // Spawn based on density and height constraints
        }
    }
    
    void SpawnPropsInCell(WorldCell cell)
    {
        // Spawn rocks, debris, vehicles, etc.
    }
    
    BiomeData GetBiomeData(BiomeType type)
    {
        // Return biome configuration from database
        return new BiomeData(); // Placeholder
    }
    
    void InitializeWeatherSystem()
    {
        // Start weather cycle
        StartCoroutine(WeatherCycle());
    }
    
    System.Collections.IEnumerator WeatherCycle()
    {
        while (true)
        {
            RegionData region = currentRegion;
            if (region != null && region.atmosphere.possibleWeather.Count > 0)
            {
                // Select random weather based on weights
                WeatherType nextWeather = region.atmosphere.possibleWeather[Random.Range(0, region.atmosphere.possibleWeather.Count)];
                
                // Transition to new weather
                TransitionToWeather(nextWeather);
                
                // Wait for duration
                yield return new WaitForSeconds(Random.Range(300f, 1800f)); // 5-30 minutes
            }
            else
            {
                yield return new WaitForSeconds(60f);
            }
        }
    }
    
    void TransitionToWeather(WeatherType weather)
    {
        WeatherData weatherData = GetWeatherData(weather);
        
        // Start coroutine for smooth transition
        StartCoroutine(ApplyWeatherTransition(weatherData));
        
        OnWeatherChanged?.Invoke(weather);
    }
    
    System.Collections.IEnumerator ApplyWeatherTransition(WeatherData weather)
    {
        float elapsed = 0;
        float duration = weather.transitionTime;
        
        Color startFogColor = RenderSettings.fogColor;
        float startFogDensity = RenderSettings.fogDensity;
        
        while (elapsed < duration)
        {
            float t = elapsed / duration;
            
            // Smooth interpolation
            RenderSettings.fogColor = Color.Lerp(startFogColor, weather.fogColor, t);
            RenderSettings.fogDensity = Mathf.Lerp(startFogDensity, weather.fogDensity, t);
            
            elapsed += Time.deltaTime;
            yield return null;
        }
        
        // Activate particle effects
        if (weather.particleEffect != null)
        {
            Instantiate(weather.particleEffect, Camera.main.transform.position, Quaternion.identity);
        }
    }
    
    WeatherData GetWeatherData(WeatherType type)
    {
        // Return weather configuration from database
        return new WeatherData(); // Placeholder
    }
    
    // Public API
    public RegionData GetCurrentRegion() => currentRegion;
    public WeatherType GetCurrentWeather() => currentWeather;
    public Vector3 GetPlayerPosition() => playerPosition;
    public WorldCell GetCellAtPosition(Vector3 position)
    {
        int x = Mathf.FloorToInt(position.x / streamingSettings.cellSize);
        int z = Mathf.FloorToInt(position.z / streamingSettings.cellSize);
        loadedCells.TryGetValue(new Vector2Int(x, z), out WorldCell cell);
        return cell;
    }
}
```

---

## 12. REGION CONFIGURATION EXAMPLES

```csharp
// ============================================
// REGION CONFIGURATION BUILDER
// ============================================

public static class RegionConfigurator
{
    public static RegionData CreateDeltaSprawl()
    {
        return new RegionData
        {
            id = RegionID.DeltaSprawl,
            displayName = "The Delta Sprawl",
            worldPosition = new Vector2(0, 0),
            size = new Vector2(8000, 8000),  // 8km x 8km
            minHeight = -10f,
            maxHeight = 80f,
            primaryBiome = BiomeType.FloodedUrban,
            secondaryBiome = BiomeType.TransitionZone,
            atmosphere = new AtmosphericData
            {
                ambientLight = new Color(0.15f, 0.1f, 0.2f),
                fogColor = new Color(0.5f, 0.4f, 0.6f),
                fogDensity = 0.02f,
                visibilityRange = 500f,
                hasDayNightCycle = true,
                possibleWeather = new List<WeatherType> { WeatherType.Clear, WeatherType.LightRain, WeatherType.HeavyRain, WeatherType.PinkStorm },
                particleDensity = 0.8f,
                lightPollution = 0.9f
            },
            subRegions = new List<SubRegion>
            {
                new SubRegion
                {
                    name = "The Sunken Temples",
                    boundsMin = new Vector2(-2000, -2000),
                    boundsMax = new Vector2(0, 0),
                    heightOffset = -5f,
                    terrainType = TerrainType.FloodedRuins,
                    pointsOfInterest = new List<POI>
                    {
                        new POI { name = "Temple of Sobek", type = POIType.Dungeon, position = new Vector3(-1500, 0, -1500) },
                        new POI { name = "Lotus Pier", type = POIType.Market, position = new Vector3(-500, 0, -500) }
                    }
                },
                new SubRegion
                {
                    name = "The Canal District",
                    boundsMin = new Vector2(0, -2000),
                    boundsMax = new Vector2(2000, 2000),
                    heightOffset = 0f,
                    terrainType = TerrainType.CanalNetwork,
                    pointsOfInterest = new List<POI>
                    {
                        new POI { name = "The Hatchery", type = POIType.CreatureZone, position = new Vector3(1000, 0, 0) },
                        new POI { name = "The Underpass", type = POIType.RacingArea, position = new Vector3(0, 0, 1000) }
                    }
                }
            },
            landmarks = new List<Landmark>
            {
                new Landmark
                {
                    name = "The Sunken Obelisk",
                    type = LandmarkType.Temple,
                    position = new Vector3(-1800, -2, -1200),
                    isEnterable = true,
                    isRaidDungeon = false
                }
            },
            difficulty = DifficultyRating.Easy,
            recommendedLevel = 1
        };
    }
    
    public static RegionData CreateNeoKemetCore()
    {
        return new RegionData
        {
            id = RegionID.NeoKemetCore,
            displayName = "Neo-Kemet Core",
            worldPosition = new Vector2(10000, 0),
            size = new Vector2(12000, 12000),  // 12km x 12km
            minHeight = -20f,   // Undercity
            maxHeight = 1200f,  // Spire top
            primaryBiome = BiomeType.UrbanCore,
            secondaryBiome = BiomeType.TransitionZone,
            atmosphere = new AtmosphericData
            {
                ambientLight = new Color(0.2f, 0.15f, 0.25f),
                fogColor = new Color(0.4f, 0.35f, 0.45f),
                fogDensity = 0.015f,
                visibilityRange = 2000f,
                hasDayNightCycle = true,
                possibleWeather = new List<WeatherType> { WeatherType.Clear, WeatherType.Smog, WeatherType.LightRain, WeatherType.PinkStorm },
                particleDensity = 0.9f,
                lightPollution = 1f
            },
            subRegions = new List<SubRegion>
            {
                new SubRegion
                {
                    name = "Street Level",
                    boundsMin = new Vector2(-4000, -4000),
                    boundsMax = new Vector2(4000, 4000),
                    heightOffset = 0f,
                    terrainType = TerrainType.UrbanStreets,
                    pointsOfInterest = new List<POI>
                    {
                        new POI { name = "Grand Bazaar", type = POIType.Market, position = new Vector3(0, 0, 0) },
                        new POI { name = "Pink Quarter", type = POIType.Slum, position = new Vector3(2000, 0, 1500) },
                        new POI { name = "Neon Canals", type = POIType.SmugglingRoute, position = new Vector3(-1500, -5, 1000) }
                    }
                },
                new SubRegion
                {
                    name = "Mid-Level",
                    boundsMin = new Vector2(-4000, -4000),
                    boundsMax = new Vector2(4000, 4000),
                    heightOffset = 100f,
                    terrainType = TerrainType.SkyBridge,
                    pointsOfInterest = new List<POI>
                    {
                        new POI { name = "Corporate Plaza", type = POIType.Commercial, position = new Vector3(0, 150, 0) },
                        new POI { name = "Sky Gardens", type = POIType.Park, position = new Vector3(2500, 200, -2000) }
                    }
                },
                new SubRegion
                {
                    name = "Sky Level",
                    boundsMin = new Vector2(-2000, -2000),
                    boundsMax = new Vector2(2000, 2000),
                    heightOffset = 500f,
                    terrainType = TerrainType.Penthouse,
                    pointsOfInterest = new List<POI>
                    {
                        new POI { name = "Spire of Anubis", type = POIType.Dungeon, position = new Vector3(0, 600, 0) },
                        new POI { name = "Celestial Observatory", type = POIType.Viewpoint, position = new Vector3(1000, 800, 1000) }
                    }
                }
            },
            landmarks = new List<Landmark>
            {
                new Landmark
                {
                    name = "Spire of Anubis",
                    type = LandmarkType.CorporateHQ,
                    position = new Vector3(0, 0, 0),
                    isEnterable = true,
                    isRaidDungeon = true,
                    recommendedPartySize = 4
                },
                new Landmark
                {
                    name = "Osiris Vaults",
                    type = LandmarkType.Tomb,
                    position = new Vector3(-3000, -15, 2000),
                    isEnterable = true,
                    isRaidDungeon = false
                }
            },
            difficulty = DifficultyRating.MediumHard,
            recommendedLevel = 20
        };
    }
}
```

---

## 13. TERRAIN GENERATOR UTILITY

```csharp
// ============================================
// PROCEDURAL TERRAIN GENERATOR
// ============================================

using UnityEngine;

public class TerrainGenerator : MonoBehaviour
{
    public static TerrainData GenerateTerrain(TerrainGenerationData data, Vector2 offset)
    {
        TerrainData terrainData = new TerrainData();
        terrainData.heightmapResolution = data.heightmapResolution;
        terrainData.size = new Vector3(data.terrainSize, data.heightMultiplier, data.terrainSize);
        
        // Generate heightmap
        float[,] heights = GenerateHeightmap(data, offset);
        terrainData.SetHeights(0, 0, heights);
        
        // Apply erosion
        if (data.erosion.iterations > 0)
        {
            heights = ApplyErosion(heights, data.erosion);
            terrainData.SetHeights(0, 0, heights);
        }
        
        // Generate splatmap
        float[,,] splatmap = GenerateSplatmap(terrainData, data.terrainLayers);
        terrainData.SetAlphamaps(0, 0, splatmap);
        
        return terrainData;
    }
    
    static float[,] GenerateHeightmap(TerrainGenerationData data, Vector2 offset)
    {
        int resolution = (int)data.heightmapResolution;
        float[,] heights = new float[resolution, resolution];
        
        for (int y = 0; y < resolution; y++)
        {
            for (int x = 0; x < resolution; x++)
            {
                float xPos = (float)x / resolution * data.terrainSize;
                float zPos = (float)y / resolution * data.terrainSize;
                
                float height = 0;
                
                foreach (var layer in data.noiseLayers)
                {
                    float noiseX = (xPos + offset.x) * layer.scale + layer.offset.x;
                    float noiseZ = (zPos + offset.y) * layer.scale + layer.offset.y;
                    
                    float noiseValue = Mathf.PerlinNoise(noiseX, noiseZ);
                    
                    // Fractal Brownian Motion for octaves
                    float fbm = 0;
                    float amplitude = layer.amplitude;
                    float frequency = layer.frequency;
                    
                    for (int i = 0; i < layer.octaves; i++)
                    {
                        float nx = noiseX * frequency;
                        float nz = noiseZ * frequency;
                        fbm += Mathf.PerlinNoise(nx, nz) * amplitude;
                        amplitude *= layer.persistence;
                        frequency *= layer.lacunarity;
                    }
                    
                    height += fbm;
                }
                
                heights[y, x] = Mathf.Clamp01(height);
            }
        }
        
        return heights;
    }
    
    static float[,] ApplyErosion(float[,] heights, ErosionParameters erosion)
    {
        // Hydraulic erosion simulation
        int width = heights.GetLength(0);
        int height = heights.GetLength(1);
        
        float[,] water = new float[width, height];
        float[,] sediment = new float[width, height];
        
        for (int i = 0; i < erosion.iterations; i++)
        {
            // Add rain
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    water[x, y] += erosion.rainfall;
                }
            }
            
            // Erode and deposit
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    float heightDiff = 0;
                    float waterFlow = water[x, y];
                    
                    // Flow to lower neighbors
                    // Simplified: move water to lowest neighbor
                    // Full implementation would be more complex
                }
            }
        }
        
        return heights;
    }
    
    static float[,,] GenerateSplatmap(TerrainData terrain, TerrainLayer[] layers)
    {
        int resolution = terrain.alphamapResolution;
        float[,,] splatmap = new float[resolution, resolution, layers.Length];
        
        for (int y = 0; y < resolution; y++)
        {
            for (int x = 0; x < resolution; x++)
            {
                float worldX = (float)x / resolution * terrain.size.x;
                float worldZ = (float)y / resolution * terrain.size.z;
                float height = terrain.GetHeight(y, x);
                float steepness = terrain.GetSteepness(worldX, worldZ);
                
                float[] weights = new float[layers.Length];
                float totalWeight = 0;
                
                for (int i = 0; i < layers.Length; i++)
                {
                    var layer = layers[i];
                    
                    float heightWeight = 1f;
                    if (height < layer.minHeight || height > layer.maxHeight)
                        heightWeight = 0;
                    else
                        heightWeight = 1f - Mathf.Abs((height - layer.minHeight) / (layer.maxHeight - layer.minHeight) - 0.5f) * 2;
                    
                    float steepnessWeight = 1f;
                    if (steepness < layer.minSteepness || steepness > layer.maxSteepness)
                        steepnessWeight = 0;
                    else
                        steepnessWeight = 1f - Mathf.Abs((steepness - layer.minSteepness) / (layer.maxSteepness - layer.minSteepness) - 0.5f) * 2;
                    
                    weights[i] = heightWeight * steepnessWeight;
                    totalWeight += weights[i];
                }
                
                if (totalWeight > 0)
                {
                    for (int i = 0; i < layers.Length; i++)
                    {
                        splatmap[y, x, i] = weights[i] / totalWeight;
                    }
                }
                else
                {
                    splatmap[y, x, 0] = 1; // Default to first layer
                }
            }
        }
        
        return splatmap;
    }
}
```

---

## 14. QUICK START: WORLD INITIALIZATION

```csharp
// ============================================
// GAME MANAGER - QUICK START
// ============================================

using UnityEngine;

public class GameManager : MonoBehaviour
{
    [Header("World Configuration")]
    public MasterWorldController worldController;
    public GameObject playerPrefab;
    public Vector3 playerStartPosition;
    
    void Start()
    {
        InitializeGame();
    }
    
    void InitializeGame()
    {
        // Create world controller if not assigned
        if (worldController == null)
        {
            GameObject worldObj = new GameObject("MasterWorldController");
            worldController = worldObj.AddComponent<MasterWorldController>();
            
            // Build regions
            worldController.regions = new List<RegionData>
            {
                RegionConfigurator.CreateDeltaSprawl(),
                RegionConfigurator.CreateNeoKemetCore()
                // Add other regions
            };
            
            // Configure streaming
            worldController.streamingSettings = new WorldStreamingSettings
            {
                cellSize = 500f,
                loadRadius = 3,
                unloadRadius = 5,
                terrainLOD0 = 100f,
                terrainLOD1 = 250f,
                terrainLOD2 = 500f,
                buildingLOD0 = 50f,
                buildingLOD1 = 150f,
                vegetationLOD0 = 30f
            };
        }
        
        // Spawn player
        if (playerPrefab != null)
        {
            Instantiate(playerPrefab, playerStartPosition, Quaternion.identity);
        }
        
        Debug.Log("Game initialized. Welcome to Neo-Kemet.");
    }
}
```

---

## SYSTEM COMPONENT SUMMARY

| Component | What It Does |
|-----------|--------------|
| **Region System** | Defines all 5 regions with coordinates, biomes, atmosphere |
| **Terrain Generation** | Heightmap, erosion, splatmaps, LOD system |
| **Building System** | Procedural generation, styles, landmarks, lots |
| **Vegetation System** | Flora types, bioluminescence, spawning rules |
| **Navigation** | Roads, canals, flight corridors |
| **Weather System** | Dynamic weather with transitions, hazards |
| **Lighting System** | Zones, neon signs, volumetric fog |
| **Streaming** | Cell-based loading, LOD management, async loading |
| **Master Controller** | Singleton manager for world state |

---

## NEXT STEPS - EXPANSION OPTIONS

1. **Creature System** - Spawning rules, AI behavior, capture mechanics
2. **Faction System** - NPC factions, reputation, territory control
3. **Vehicle System** - Chariots, sand cruisers, flight mechanics
4. **Combat System** - MK/DBZ hybrid implementation
5. **Quest/Heist System** - Mission structure, objectives, rewards

---

**Status:** Foundation complete. Modular and extensible. Ready for system expansion.
