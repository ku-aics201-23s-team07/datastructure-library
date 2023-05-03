from avl_tree import module

locations = [
    {
        "name": "신정문 주차장",
        "latitude": 36.60924342720994,
        "longitude": 127.28889446545843,
        "scooters": [
            {
                "id": "scooter001",
                "battery": 70,
                "repair": False
            }
        ]
    },
    {
        "name": "학술정보원",
        "latitude": 36.60987854046684,
        "longitude": 127.28710841905747,
        "scooters": [
            {
                "id": "scooter002",
                "battery": 50,
                "repair": False
            }
        ]
    },
    {
        "name": "과기2관",
        "latitude": 36.61087905080802,
        "longitude": 127.28700593927432,
        "scooters": [
            {
                "id": "scooter003",
                "battery": 30,
                "repair": True
            }
        ]
    },
    {
        "name": "ICT 융합관",
        "latitude": 36.60913903276567,
        "longitude": 127.28358476879771,
        "scooters": [
            {
                "id": "scooter004",
                "battery": 100,
                "repair": False
            }
        ]
    }
]

avl_tree = module.AVLTree()

for location in locations:
    avl_tree.insert(location)

target_location = {
    "latitude": 36.60857621133895,
    "longitude": 127.28904846065954
}

nearest_scooter = None
nearest_location = None
min_distance = float('inf')

for location in locations:
    distance = avl_tree._distance(location, target_location)
    if distance < min_distance:
        for scooter in location['scooters']:
            if not scooter['repair']:
                nearest_scooter = scooter
                nearest_location = location
                min_distance = distance

if nearest_scooter:
    print(f"The nearest scooter is {nearest_scooter['id']} in {nearest_location['name']} width {nearest_scooter['battery']}% battery")
else:
    print("No available scooter found.")