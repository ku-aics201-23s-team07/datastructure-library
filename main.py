import json
from avl_tree import avl_module
from heap_queue import heap_queue_module

def location_filter(locations):
    processed_locations = []

    for location in locations:
        scooters = location['scooters']
        num_scooters = len(scooters)

        if num_scooters == 0 or all(scooter['repair'] for scooter in scooters):
            continue

        processed_locations.append(location)

    return processed_locations

locations = [
    {
        "location_id": "DJS123D",
        "name": "신정문 주차장",
        "latitude": 36.60924342720994,
        "longitude": 127.28889446545843,
        "scooters": [
            {
                "id": "scooter001",
                "battery": 70,
                "repair": False
            },
                        {
                "id": "scooter002",
                "battery": 40,
                "repair": False
            },
                        {
                "id": "scooter003",
                "battery": 10,
                "repair": False
            },
                        {
                "id": "scooter004",
                "battery": 90,
                "repair": False
            },
                        {
                "id": "scooter005",
                "battery": 20,
                "repair": False
            },
                        {
                "id": "scooter006",
                "battery": 100,
                "repair": False
            }
        ]
    },
    {
        "location_id": "DK203D",
        "name": "학술정보원",
        "latitude": 36.60987854046684,
        "longitude": 127.28710841905747,
        "scooters": [
            {
                "id": "scooter002",
                "battery": 50,
                "repair": False
            },
                        {
                "id": "scooter002",
                "battery": 50,
                "repair": True
            }
        ]
    },
    {
        "location_id": "MMD2349",
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
        "location_id": "SDO1239",
        "name": "ICT 융합관",
        "latitude": 36.60913903276567,
        "longitude": 127.28358476879771,
        "scooters": [
        ]
    }
]

locations = location_filter(locations)

#AVL-Tree 초기화
location_avl_tree = avl_module.LocationAVLTree()

for location in locations:
    location_avl_tree.insert(location)

#AVL-Tree에서 이름으로 Node찾기
search_result_node = location_avl_tree.search("DJS123D")
print("=============== found node =================")
print(f"location: {search_result_node.location}")
print(f"scooters: {search_result_node.scooters}")

#AVL-Tree를 이용해 가장 가까운 그룹 찾기
target_location = {
    "latitude": 36.60857621133895,
    "longitude": 127.28904846065954
}

nearest_location = location_avl_tree.find_nearest_location(target_location)

print("============ nearest location ==============")
if nearest_location == None:
    print("No available scooter found.")
print(f"The nearest location is {nearest_location[0].locationName} with {nearest_location[1]}m")
print("============================================")

# 배터리상태가 가장 좋고 수리가 필요없는 scooter를 찾기
scooters_heap = heap_queue_module.build_heap(nearest_location[0].scooters)

max_battery_scooter = None
for scooter in scooters_heap:
    if scooter["repair"] == False:
        if max_battery_scooter is None or scooter["battery"] > max_battery_scooter["battery"]:
            max_battery_scooter = scooter

print(max_battery_scooter)