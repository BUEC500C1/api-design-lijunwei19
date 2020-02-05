from airport2cityname import Airport2CN

from weatherAPI import weather_data_download

def airport_Weather(airport_name):

  country, city_name = Airport2CN(airport_name)

  weather_data = weather_data_download(city_name, country)

  return weather_data


# def main() :
  
#   print (airport_Weather("Total Rf Heliport"))

# if __name__ == '__main__':

#   main()