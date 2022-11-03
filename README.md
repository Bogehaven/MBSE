# MBSE

Pollution Simulation dependencies
=======================
- pygame
- numpy
- perlin_noise

Pollution Simulation instructions
=======================
Run main.py to execute the simulator. \
Possible interactions:
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

TODO
========================
- Export data about position and speed at each timestep for each vehicle using SUMO
- Load this data with python in the simulator
- Insert pollution using this data and draw vehicles it over the map (as little dots)
- Tune parameters so it is realistic
- Try different scenarios


