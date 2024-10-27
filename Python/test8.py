# find destination city that has no outgoing paths from given paths
def find_destination_path(paths):
    outgoing_cities = set()
    # populate the set with all outgoing cities
    for path in paths:
        outgoing_cities.add(path[0])
    # lets get the destination city
    for path in paths:
        destination_city = path[1]
        if destination_city not in outgoing_cities:
            return destination_city
    return None    

# test
paths = [["Nairobi","Machakos"], ["Machakos","Mtito"], ["Mtito","Mombasa"]]
result = find_destination_path(paths)

print("destination_city", {result})