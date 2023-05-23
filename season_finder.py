def determine_season(country, month):
     seasons = {
         'Australia': {
             'Meteorological': {
                 'December': 'Summer',
                 'January': 'Summer',
                 'February': 'Summer',
                 'March': 'Autumn',
                 'April': 'Autumn',
                 'May': 'Autumn',
                 'June': 'Winter',
                 'July': 'Winter',
                 'August': 'Winter',
                 'September': 'Spring',
                 'October': 'Spring',
                 'November': 'Spring'
             },
             'Noongar': {
                 'December': 'Birak',
                 'January': 'Birak',
                 'February': 'Bunuru',
                 'March': 'Bunuru',
                 'April': 'Djeran',
                 'May': 'Djeran',
                 'June': 'Makuru',
                 'July': 'Makuru',
                 'August': 'Djilba',
                 'September': 'Djilba',
                 'October': 'Kambarang',
                 'November': 'Kambarang'
             }
         },
         'Spain': {
             'Meteorological': {
                 'December': 'Winter',
                 'January': 'Winter',
                 'February': 'Winter',
                 'March': 'Spring',
                 'April': 'Spring',
                 'May': 'Spring',
                 'June': 'Summer',
                 'July': 'Summer',
                 'August': 'Summer',
                 'September': 'Autumn',
                 'October': 'Autumn',
                 'November': 'Autumn'
             }
         },
         'Japan': {
             'Meteorological': {
                 'December': 'Winter',
                 'January': 'Winter',
                 'February': 'Winter',
                 'March': 'Spring',
                 'April': 'Spring',
                 'May': 'Spring',
                 'June': 'Summer',
                 'July': 'Summer',
                 'August': 'Summer',
                 'September': 'Autumn',
                 'October': 'Autumn',
                 'November': 'Autumn'
             }
         },
         'Mauritius': {
             'Meteorological': {
                 'December': 'Summer',
                 'January': 'Summer',
                 'February': 'Summer',
                 'March': 'Summer',
                 'April': 'Summer',
                 'May': 'Autumn',
                 'June': 'Winter',
                 'July': 'Winter',
                 'August': 'Winter',
                 'September': 'Winter',
                 'October': 'Spring',
                 'November': 'Summer'
             }
         },
         'Malaysia': {
             'Meteorological': {
                 'December': 'Northeast Monsoon',
                 'January': 'Northeast Monsoon',
                 'February': 'Northeast Monsoon',
                 'March': 'Inter-monsoon',
                 'April': 'Inter-monsoon',
                 'May': 'Southeast Monsoon',
                 'June': 'Southeast Monsoon',
                 'July': 'Southeast Monsoon',
                 'August': 'Southeast Monsoon',
                 'September': 'Southeast Monsoon',
                 'October': 'Inter-monsoon',
                 'November': 'Inter-monsoon'
             }
         },
         'Sri Lanka': {
             'Meteorological': {
                 'December': 'Northeast Monsoon',
                 'January': 'Northeast Monsoon',
                 'February': 'Northeast Monsoon',
                 'March': 'Inter-monsoon',
                 'April': 'Inter-monsoon',
                 'May': 'Southeast Monsoon',
                 'June': 'Southeast Monsoon',
                 'July': 'Southeast Monsoon',
                 'August': 'Southeast Monsoon',
                 'September': 'Southeast Monsoon',
                 'October': 'Inter-monsoon',
                 'November': 'Inter-monsoon'
             }
         }
     }
 
     if country in seasons:
         country_seasons = seasons[country]
         season_type = input("Choose the season type (1: Meteorological, 2: Noongar): ")
         
         if country == 'Australia' and season_type == '2':
             season_dict = country_seasons['Noongar']
         else:
             season_dict = country_seasons['Meteorological']
         
         if month in season_dict:
             return season_dict[month]
         else:
             return 'Unknown'
     else:
         return 'Unknown'
 
 
 def main():
     country = input("Enter the country: ")
     month = input("Enter the month: ")
     
     season = determine_season(country, month)
     
     print(f"The season in {country} during {month} is {season}")
     
     if season == 'Summer':
         print("Insert summer image here")
     elif season == 'Autumn':
         print("Insert autumn image here")
     elif season == 'Winter':
         print("Insert winter image here")
     elif season == 'Spring':
         print("Insert spring image here")
     else:
         print("Unknown season")
 
 
 if _name_ == '_main_':
     main()