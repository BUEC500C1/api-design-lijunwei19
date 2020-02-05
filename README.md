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

# Reference 
Open Weather API 
```
https://openweathermap.org/
```
