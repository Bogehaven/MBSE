#!/bin/bash
python "$SUMO_HOME/tools/randomTrips.py" -n osm.net.xml --fringe-factor 5 -p 0.525366 -o osm.passenger.trips.xml -r osm.passenger.rou.xml -e 3600 --vehicle-class passenger --vclass passenger --prefix veh --min-distance 300 --trip-attributes "departLane=\"best\"" --fringe-start-attributes "departSpeed=\"max\"" --allow-fringe.min-length 1000 --lanes --validate
python "$SUMO_HOME/tools/randomTrips.py" -n osm.net.xml --fringe-factor 5 -p 0.788049 -o osm.truck.trips.xml -r osm.truck.rou.xml -e 3600 --vehicle-class truck --vclass truck --prefix truck --min-distance 600 --fringe-start-attributes "departSpeed=\"max\"" --trip-attributes "departLane=\"best\"" --validate
