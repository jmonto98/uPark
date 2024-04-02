#from django.test import TestCase
from datetime import datetime

# Create your tests here.

def test():
    date = "2024-04-01 20:28:29.512442"
    date2 = "14/03/2024 04:12:00"
    date2 = datetime.strptime(date2, "%d/%m/%Y %H:%M:%S")
    
    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(date)
    print(date2)
    print(now)

test()