#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "India": "Delhi",
}

#Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Nice", "Lyon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "India": ["Delhi", "Chennai", "Bangalore"],
}

#Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":12},
    "Germany":{"cities_visted": ["Berlin", "Hamburg", "Stuttgart"],"total_visits":5},
}

#Nesting Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":12
    },
    {
        "country" :"Germany",
        "cities_visted": ["Berlin", "Hamburg", "Stuttgart"],"total_visits":5
    },
]

