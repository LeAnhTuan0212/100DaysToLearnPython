travel_log = [
    {   "country":"France", 
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"], 
    },
    {   "country":"Germany",
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    },
]
def add_new_country(country, visits, cities_visited):
    new_country = {}
    new_country["country"] = country
    new_country["total_visits"] = visits
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
for _ in travel_log:
    print(_)