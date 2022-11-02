SUMO simulation setup for Østerbro

### How to open
Open `osm.sumocfg` in the SUMO GUI app

### Files
- `osm.vehicle.types.xml`: Contains vehicle definitions
- `osm.passenger.trips.xml`: Contains the routes and vehicle types for passenger cars
- `osm.truck.trips.xml`: Contains the routes and vehicle types for trucks
- `vehicle_dist.py`: Script for changing the distribution of vehicle types for a group of vehicles

### How to run vehicle distribution script

**Dependencies:**
- Beautifulsoup4
- lxml

Run it from command line: `python vehicle_dist.py '<filename>' '<dictionary_containing_probabilities>'`

`python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.5, "veh_diesel": 0.2, "veh_hybrid": 0.2, "veh_ev": 0.1}'`
`python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 0.9, "truck_hybrid": 0.3}'`

## Running SUMO from cmd
`sumo -c osm.sumocfg --emission-output emissions.xml  --emission-output.geo true`


### Documentations
- SUMO Emissions: https://github.com/eclipse/sumo/blob/main/docs/web/docs/Models/Emissions.md
- SUMO Emission Types: https://github.com/eclipse/sumo/blob/main/docs/web/docs/Models/Emissions/HBEFA4-based.md

### To-Do
- Export emissions from SUMO to Python
- Add different symbols for vehicle types
- Change color of vehicles to reflect pollution
