def main():
    city = input("City: ")
    crime_code = input("Crime code: ")
    crime_data = read_crime_data()
    display_crime_data(crime_data, city, crime_code)

def read_crime_data():
    crime_data = {}
    with open("crimedata.txt") as f:
        for line in f:
            line = line.strip()
            crime_id, city, crime_type, crime_code = line.split("\t")
            crime_data[crime_id] = (city, crime_type, crime_code)
    return crime_data

def display_crime_data(crime_data, city, crime_code):
    count = 0
    for crime_id in crime_data:
        if crime_data[crime_id][0] == city and crime_data[crime_id][2] == crime_code:
            count += 1
            crime_type = crime_data[crime_id][1]
    print("{} in {}: {}".format(crime_type, city, count))

main()
