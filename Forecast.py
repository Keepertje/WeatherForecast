import requests
#from Ledstrip import Ledstrip


try:
	forecast = requests.get("http://api.wunderground.com/api/b5ed728d92fe3c96/forecast/q/NL/Utrecht.json")
except requests.exceptions.ConnectionError:
    print("No interwebs O_o")
	
data = forecast.json()
#ledstrip = None
white = None
lBlue = None
blue = None
lGreen = None
green = None
yellow = None
orange = None
red  = None

#print(data['forecast']['simpleforecast']['forecastday'].keys)
def fillColorDays():
	#allColor(12, ledstrip.color(0,0,0,0),0)
	i = 0
	j = 1
	for day in data['forecast']['simpleforecast']['forecastday']:
		if( j < 0 ):
			colorDay( day['conditions'], day['high']['celsius'], i, i+1, i+2, i+3)
		else:
			colorDay( day['conditions'], day['high']['celsius'], i+3, i+2, i+1, i)	
		i = i + 4
		j = j * -1
		#print (day['date']['weekday'] + ":")
		#print ("Conditions: ", day['conditions'])
		#print ("High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C", '\n')
		#i = i + 1
	#inbouwen voor ledjes
	#ledstrip.writestrip()

def colorDay(condition, temp,l1,l2,l3,l4):
	print("Condition " + condition)
	print("Temperature " + temp + " color " + temperature(int(temp)) )
	turnOnLights = conditionLight(condition,l1,l2,l3,l4)
	#for i in range(len(turnOnLights)):
		#print(turnOnLights[i])
		#setpixels
	print(turnOnLights)
	
#moet een string returnen, kunnen meerdere mogelijk zijn  (party cloud = zon en wolken)
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
		return [88]
	else: #Fog,Mist,Haze, (ligth)Snow, Ice Crystals
		return [999]
		
	#	return 1
		#contains chance
	#elif(condition contains cloud )
		#contains party 
	#elif condition contains sun
	#elif condition contains snow 
	#elif 
	
#return color	
def temperature(temp):
	if(temp < 0):
		return "white"
	elif(temp < 5 and temp >= 0):
		return "lBlue"
	elif(temp < 10 and temp >= 5):
		return "blue"
	elif(temp < 15 and temp >= 10):
		return "lGreen"
	elif(temp < 20 and temp >= 15):
		return "green"
	elif(temp < 25 and temp >= 20):		
		return "yellow"
	elif(temp < 30 and temp >= 25):
		return "orange"
	else:
		return "red"
		
if __name__ == "__main__":
	#ledstrip = Ledstrip()
	#<0		wit 
	#white = ledstrip.Color(255,255,255,0.5)
	#0-5	lichtblauw 
	#lBlue = ledstrip.Color(100,100,255,0.5)
	#6-10   blauw 
	#blue  = ledstrip.Color(0,0,255) 
	#11-15  lichtgroen 
	#lGreen = ledstrip.Color(100,255,100,0.5)
	#16-20  groen 
	#green = ledstrip.Color(0,255,0,0.5)
	#21-25  geel  
	#yellow = ledstrip.Color(255,255,0,0.5)
	#26-30  oranje  
	#orange = ledstrip.Color(255,100,0,0.5)
	#30+    rood   255 0 0
	#red   = ledstrip.Color(255,0,0,0.5)
	fillColorDays()