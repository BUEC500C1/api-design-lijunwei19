# Airport weather API-design-lijunwei
api-design-lijunwei19 created by GitHub Classroom


# Preparation
## Download essential files    
clone my repositories:   
```
https://github.com/BUEC500C1/api-design-lijunwei19.git
```
Install Library 
```
pip install requests

pip install pprintpp
```

# Import airport_Weather Fucntion
Import function in your python file. (the path of your python file should be in api-design-lijunwei19/... )
```
from AirportWeatherAPI import airport_Weather 

```

# WeatherAPI.py
Input can be lat&lon or city name or zip cord or id 
```
weather_data_download((40.07080078125,-74.93360137939453, ), "us")

weather_data_download("London", "us") 

weather_data_download(65201, "us")

weather_data_download(2172797, "AU"
```
# AirportWeatherAPI.py
Input airport name
```
airport_Weather("Total Rf Heliport")
```
# Output for both function
```
{
"coord":
      {
       "lon":145.77,
       "lat":-16.92
       },
"weather":
      [{
        "id":802,
        "main":"Clouds",
        "description":"scattered clouds",
        "icon":"03n"}],
 "base":"stations",
 "main":{
        "temp":300.15,
        "pressure":1007,
        "humidity":74,
        "temp_min":300.15,
        "temp_max":300.15},
        "visibility":10000,
 "wind":{
         "speed":3.6,
         "deg":160},
 "clouds":{
         "all":40},
       "dt":1485790200,
 "sys":{"
         type":1,
         "id":8166,
         "message":0.2064,
         "country":"AU",
         "sunrise":1485720272,
         "sunset":1485766550},
         "id":2172797,
         "name":"Cairns",
         "cod":200
         }
 ```
# Reference 
Open Weather API 
```
https://openweathermap.org/
```
