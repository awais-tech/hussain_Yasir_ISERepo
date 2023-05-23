def check_temperature(city, temperature, time):
     temperature_data = {
         'Perth': {
             'Morning': 18.2,
             'Evening': 23.0
         },
         'Melbourne': {
             'Morning': 13.5,
             'Evening': 18.9
         },
         'Sydney': {
             'Morning': 18.8,
             'Evening': 23.4
         },
         'Adelaide': {
             'Morning': 16.5,
             'Evening': 21.0
         }
     }
 
     if city in temperature_data:
         if time in temperature_data[city]:
             avg_temperature = temperature_data[city][time]
             temp_difference = temperature - avg_temperature
             
             if temp_difference > 5:
                 return f"The temperature in {city} {time} is {temperature}°C, which is {temp_difference}°C above the average temperature."
             elif temp_difference < -5:
                 return f"The temperature in {city} {time} is {temperature}°C, which is {abs(temp_difference)}°C below the average temperature."
             else:
                 return f"The temperature in {city} {time} is {temperature}°C, which is close to the average temperature."
         else:
             return 'Unknown Time'
     else:
         return 'Unknown City'
 
 
 def main():
     city = input("Enter the city: ")
     temperature = float(input("Enter the temperature: "))
     time = input("Enter the time (Morning/Evening): ")
 
     result = check_temperature(city, temperature, time)
 
     print(result)
 
 
 if _name_ == '_main_':
     main()