import pytest

from weatherAPI import weather_data_download

def test1():
  assert "message" not in weather_data_download((42.3656,71.0096),"us")
  assert "message" not in weather_data_download("London", "us") 
  assert "message" not in weather_data_download(65201, "us")