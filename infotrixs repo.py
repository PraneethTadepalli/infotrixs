import requests
import time


API_KEY = "eac81d125d0240e293b111742231209"
BASE_URL = "https://api.weatherapi.com/v1/"

# Initialize a list to store favorite cities
favorite_cities = []

# Function to fetch weather data by city name
def get_weather(city):
    url = f"{BASE_URL}current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print("Error:", data["error"]["message"])
    else:
        weather = data["current"]
        print(f"Weather in {city}:")
        print(f"Temperature: {weather['temp_c']}°C")
        print(f"Condition: {weather['condition']['text']}")
        print(f"Wind Speed: {weather['wind_kph']} km/h")

# Function to add a city to the favorite list
def add_favorite(city):
    if city not in favorite_cities:
        favorite_cities.append(city)
        print(f"{city} added to favorites!")
    else:
        print(f"{city} is already in your favorites.")

# Function to remove a city from the favorite list
def remove_favorite(city):
    if city in favorite_cities:
        favorite_cities.remove(city)
        print(f"{city} removed from favorites!")
    else:
        print(f"{city} is not in your favorites.")

# Function to display the list of favorite cities
def list_favorites():
    print("Favorite Cities:")
    for city in favorite_cities:
        print(city)

# Function to auto-refresh weather for favorite cities
def auto_refresh(interval):
    if not favorite_cities:
        print("You have no favorite cities to auto-refresh.")
        return

    while True:
        for city in favorite_cities:
            get_weather(city)
        time.sleep(interval)

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Check weather by city")
        print("2. Add city to favorites")
        print("3. Remove city from favorites")
        print("4. List favorite cities")
        print("5. Auto-refresh weather for favorites")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            get_weather(city)
        elif choice == "2":
            city = input("Enter city name to add to favorites: ")
            add_favorite(city)
        elif choice == "3":
            city = input("Enter city name to remove from favorites: ")
            remove_favorite(city)
        elif choice == "4":
            list_favorites()
        elif choice == "5":
            interval = int(input("Enter refresh interval in seconds (15-30 seconds recommended): "))
            auto_refresh(interval)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Goodbye!")
