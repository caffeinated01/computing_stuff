flights = [
    ['NYC', 'LON', 7, 450],   # New York City to London
    ['TOK', 'SYD', 10, 780],  # Tokyo to Sydney
    ['PAR', 'DXB', 6, 380],   # Paris to Dubai
    ['SFO', 'HKG', 14, 920],  # San Francisco to Hong Kong
    ['RIO', 'CPT', 11, 850],  # Rio de Janeiro to Cape Town
    ['AMS', 'BKK', 11, 720],  # Amsterdam to Bangkok
    ['LAX', 'AKL', 13, 890],  # Los Angeles to Auckland
    ['IST', 'SIN', 10, 680],  # Istanbul to Singapore
    ['YVR', 'DEL', 14, 950],  # Vancouver to Delhi
    ['MEX', 'BCN', 12, 820],  # Mexico City to Barcelona
    ['JNB', 'PEK', 15, 1050], # Johannesburg to Beijing
    ['ZRH', 'BUE', 14, 980],  # Zurich to Buenos Aires
    ['CAI', 'SEL', 12, 790],  # Cairo to Seoul
    ['MIA', 'MLE', 18, 1200], # Miami to Malé (Maldives)
    ['LIS', 'YYZ', 8, 520]    # Lisbon to Toronto
]

# a)
def total_flight_times(flights):
    total = 0
    for flight in flights:
        total += flight[2]
    return total
    
    """
    list comprehension accepted
    """

# b)
def longest_flight(flights):
    longest = 0
    index = None
    
    for i in range(len(flights)):
        if flights[i][2] > longest:
            longest, index = flights[i][2], i

    """
    OR
    for i,v in enumerate(flights):
        if v[2] > longest:
            longest, index = v[2], i

    list comprehension accepted
    """

    return flights[index]
    
# c)
# 1.
print("Total flight times: {} hours".format(total_flight_times(flights)))
# 2.
departure, destination, time, price = longest_flight(flights)
print("Longest flight: {} to {}, {} hours, ${}".format(departure, destination, time, price))

# d)
# 1.
def find_route(flights, start, end):
    for flight in flights:
        if flight[0] == start and flight[1] == end:
            return flight[2]
    return -1

print('\n')

# 2.
while True:
    route = input('Enter a route to check: ').split(' ')
    
    if len(route) == 2 and all(len(country) == 3 for country in route):
        break
    
    """
    OR 
    if len(route) == 2 and len(route[0]) == 3 and len(route[1]) == 3:
        break
    """

start, end = route[0].upper(), route[1].upper() # OR start, end = [country.upper() for country in route]
route_time = find_route(flights, start, end)
if route_time != -1:
    print("{} to {} exists, flight time is {} hours".format(start, end, route_time))
else:
    print("{} to {} does not exist".format(start, end))

print('\n')

# e)
# 1. 
def update_flight_times(flights, delay):
    new_flights = []
    
    for flight in flights:
        new_flights.append([flight[0], flight[1], flight[2]+delay, flight[3]])
    return new_flights

# 2.
new_flights = update_flight_times(flights, 20)

for i in range(len(new_flights)):
    departure = new_flights[i][0]
    destination = new_flights[i][1]
    time = new_flights[i][2]
    original_time = flights[i][2]
    print('Updated time: {} to {}, {} hours (originally {} hours)'.format(departure, destination, time, original_time))

print('\n')

# f)
# 1.
def discount_prices(flights):
    new_flights = []
    
    for flight in flights:
        time = flight[2]
        price = flight[3]
        
        if time < 8:
            multiplier = 0.95
        elif time >= 8 and time <= 11:
            multiplier = 0.90
        elif time > 11:
            multiplier = 0.85
            
        price *= multiplier
        
        new_flights.append([flight[0], flight[1], flight[2], price, round((1-multiplier)*100)])
        
    """
    use of list comprehension is the cleaner method here
    """
    return new_flights
    
# 2.
new_flights = discount_prices(flights)

for i in range(len(new_flights)):
    departure = new_flights[i][0]
    destination = new_flights[i][1]
    price = new_flights[i][3]
    original_price = flights[i][3]
    discount = new_flights[i][4]

    print('Updated price, {}% discount: {} to {}, ${} (originally ${})'.format(discount, departure, destination, price, original_price))