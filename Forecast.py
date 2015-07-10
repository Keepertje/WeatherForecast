import requests
from Ledstrip import Ledstrip


try:
	forecast = requests.get("http://api.wunderground.com/api/ APIKEY /forecast/q/NL/Utrecht.json")
except requests.exceptions.ConnectionError:
    print("No interwebs O_o")
	
data = forecast.json()
ledstrip = None
white = None
lBlue = None
blue = None
lGreen = None
green = None
yellow = None
orange = None
red  = None
black = None
ledHash = None

# vul de led hashmap, schrijf de kleuren naar de pixel
def fillColorDays():
	i = 1
	j = 1
	for day in data['forecast']['simpleforecast']['forecastday']:
		if( j < 0 ):
			colorDay( day['conditions'], day['high']['celsius'], i+3,i+2,i+1,1)
		else:
			colorDay( day['conditions'], day['high']['celsius'], i, i+1, i+2, i+3)	
		i = i + 4
		j = j * -1
	for key in ledHash:
		print(key)
		ledstrip.setpixelcolor(key,ledHash[key])
	ledstrip.writestrip()

#zet in de hashmap de led die gekleurd moet worden + de kleur
def colorDay(condition, temp,l1,l2,l3,l4):
	print("Condition " + condition)
	print("Temperature " + temp)# + " color " + temperature(int(temp)) )
	turnOnLights = conditionLight(condition,l1,l2,l3,l4)
	for i in turnOnLights:
		ledHash[i] = temperature(int(temp))
#		print("ledjes: " + i)
	print(turnOnLights)
	
#returned een lijst van de ledjes die een kleur moeten krijgen
def conditionLight(condition,l1,l2,l3,l4):
	if ('Rain' in condition):
		if ('Chance' in condition):
			return[l1,l2]
		else:
			return [l1]
	elif('Cloud' in condition or 'Overcast' in condition):
		if ('Partly' in condition or 'Scattered' in condition):
			return [l2,l3]
		else:
			return [l2]
	elif('Clear' in condition):
		return [l3]
	elif('Snow' in condition):
		return [l4]
	elif('Fog' in condition or 'Mist' in condition):
		return [0]
	else: #Fog,Mist,Haze, (ligth)Snow, Ice Crystals
		return [0]
#return color	
def temperature(temp):
	if(temp < 0):
		return white
	elif(temp < 5 and temp >= 0):
		return lBlue
	elif(temp < 10 and temp >= 5):
		return blue
	elif(temp < 15 and temp >= 10):
		return lGreen
	elif(temp < 20 and temp >= 15):
		return green
	elif(temp < 25 and temp >= 20):		
		return yellow
	elif(temp < 30 and temp >= 25):
		return orange
	else:
		return red
		
if __name__ == "__main__":
	ledstrip = Ledstrip()
	ledstrip.colorwipe(ledstrip.Color(0,0,0),0)
	#<0		wit 
	white = ledstrip.Color(255,255,255)
	#0-5	lichtblauw 
	lBlue = ledstrip.Color(100,100,255)
	#6-10   blauw 
	blue  = ledstrip.Color(0,0,255) 
	#11-15  lichtgroen 
	lGreen = ledstrip.Color(100,255,100)
	#16-20  groen 
	green = ledstrip.Color(0,255,0)
	#21-25  geel  
	yellow = ledstrip.Color(255,255,0)
	#26-30  oranje  
	orange = ledstrip.Color(255,100,0)
	#30+    rood   255 0 0
	red   = ledstrip.Color(255,0,0)
	black = ledstrip.Color(0,0,0)
	ledHash={}
	fillColorDays()
