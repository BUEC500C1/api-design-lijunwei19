from  AirportWeatherAPI import airport_Weather

import pytest 

def test_airport_weather():
  assert "message" not in airport_Weather("Total Rf Heliport")
  assert "message" not in airport_Weather("Aero B Ranch Airport") 
  assert "message" not in airport_Weather("Newport Hospital & Clinic Heliport")