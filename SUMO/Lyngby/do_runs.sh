python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.928, "veh_diesel": 0.0, "veh_ev": 0.072}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars/baseline.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.9, "veh_diesel": 0.0, "veh_ev": 0.10}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars/ev_10.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.85, "veh_diesel": 0.0, "veh_ev": 0.15}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars/ev_15.xml --step-length 1.0 -b 0 -e 7200 --seed 720

python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.85, "veh_diesel": 0.0, "veh_ev": 0.20}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars/ev_20.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.46, "veh_diesel": 0.0, "veh_ev": 0.54}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars/ev_54.xml --step-length 1.0 -b 0 -e 7200 --seed 720





python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.928, "veh_diesel": 0.0, "veh_ev": 0.072}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/trucks/baseline.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.928, "veh_diesel": 0.0, "veh_ev": 0.072}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 0.95, "truck_hybrid": 0.05}'
sumo -c osm.sumocfg --emission-output outputs/trucks/ev_5.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.928, "veh_diesel": 0.0, "veh_ev": 0.072}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 0.90, "truck_hybrid": 0.10}'
sumo -c osm.sumocfg --emission-output outputs/trucks/ev_10.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.928, "veh_diesel": 0.0, "veh_ev": 0.072}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 0.85, "truck_hybrid": 0.15}'
sumo -c osm.sumocfg --emission-output outputs/trucks/ev_15.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.928, "veh_diesel": 0.0, "veh_ev": 0.072}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 0.8, "truck_hybrid": 0.2}'
sumo -c osm.sumocfg --emission-output outputs/trucks/ev_20.xml --step-length 1.0 -b 0 -e 7200 --seed 720







python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.6783067241344423, "veh_diesel": 0.3216932758655578, "veh_ev": 0.0}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars_dis/baseline.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.75, "veh_diesel": 0.25, "veh_ev": 0.0}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars_dis/dis_25.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.80, "veh_diesel": 0.2, "veh_ev": 0.0}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars_dis/dis_20.xml --step-length 1.0 -b 0 -e 7200 --seed 720

python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.85, "veh_diesel": 0.15, "veh_ev": 0.0}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars_dis/dis_15.xml --step-length 1.0 -b 0 -e 7200 --seed 720


python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.90, "veh_diesel": 0.1, "veh_ev": 0.0}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 1.0, "truck_hybrid": 0.0}'
sumo -c osm.sumocfg --emission-output outputs/cars_dis/dis_10.xml --step-length 1.0 -b 0 -e 7200 --seed 720







python vehicle_dist.py 'osm.passenger.trips.xml' '{"veh_petrol": 0.46, "veh_diesel": 0.0, "veh_ev": 0.54}'
python vehicle_dist.py 'osm.truck.trips.xml' '{"truck_petrol": 0.8, "truck_hybrid": 0.2}'
sumo -c osm.sumocfg --emission-output outputs/etc/ev_54_truck_20.xml --step-length 1.0 -b 0 -e 7200 --seed 720