from airport2cityname import Airport2CN

import pytest

def test_Airport2CN():
  name = ["Total Rf Heliport", "Kitchen Creek Helibase Heliport", "Lt World Airport","R J D Heliport","Bailey Generation Station Heliport"] 
  con_city = [("us","bensalem"), ('us', 'pine valley'), ('us', 'lithonia'), ("us", "coatesville"), ('us', 'chesterton')]

  for i in range(len(name)):
    assert Airport2CN( name[i].lower() ) == con_city[i]
