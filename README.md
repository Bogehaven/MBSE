# MBSE

## Folder Structure

```
.
├── SUMO                        # SUMO Files
│   ├── Lyngby                  # SUMO simulation files for Lyngby (2 hours)
│   └── Lyngby_long             # SUMO simulation files for Lyngby (24 hours)
├── Simulator                   # Main Simulation Files
│   ├── main.py                 # Simulation Script
│   ├── PollutionSimulator.py   # Pollution Implementation 
│   ├── TrafficManager.py       # Convert SUMO traffic to pyGame traffic
│   └── WindSimulator.py        # Wind Implementation
└── 
```

## Simulator Documentation

### Pollution Simulation dependencies
- pygame
- numpy
- perlin_noise

### How to run the simulation
1. Make sure dependencies are installed (`pip3 install pygame, numpy, perlin_noise`)
2. From the command line inside the "Simulator" directory, run `python3 main.py`

### Pollution Simulation instructions
**Possible interactions:**
- Right click: add pollution
- E key: generate random wind with perlin noise
- U key: generate uniform wind
- N key: set wind to 0
- V key: show/hide wind vectors
- G key: show grid
- D key: change self decay value
- L key: change thermal diffusion value
- W key: enable/disable wind
- P key: pause simualtion
- B key: show/hide background map image



