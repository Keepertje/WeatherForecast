import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

class Ledstrip():

	ledpixels = None

	def __init__(self):
		self.ledpixels = [0] * 25

	def writestrip(self):
		spidev = file("/dev/spidev0.0", "w")
		for i in range(len(self.ledpixels)):
			spidev.write(chr((self.ledpixels[i]>>16) & 0xFF))
			spidev.write(chr((self.ledpixels[i]>>8) & 0xFF))
			spidev.write(chr(self.ledpixels[i] & 0xFF))
		spidev.close()
		time.sleep(0.002)

	def Color(self,r, g, b):
		return ((r  & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0xFF)
	
	def colorwipe(self,c,delay):
		for i in range(25):
			self.setpixelcolor(i,c)
			self.writestrip()
			time.sleep(delay)
	
	def allColor2(self,colorList):	
		for i in range(4):
			curC = self.Color([i][0],[i][1],[i][2])
			for n in range(6):
				p = (n*i)-(6-n)
				self.setpixelcolor(p,curC)
		self.writestrip()
		time.sleep(0.05)
		
	def allColor(self,pixels,c,wait):
	    for i in range(len(pixels)):
			self.setpixelcolor(i,c)
            self.writestrip()
            time.sleep(wait)
	
		
	def rainbow(self):
	 r = 255
         g = 0
         b = 0
         for i in range(255):
                g = i
                r = 255-i
                self.allColor(self.ledpixels, self.Color(r,g,b),0.02)
       	 for i in range(255):
                b = i
                g = 255-i
                self.allColor(self.ledpixels,self.Color(r,g,b),0.02)
         for i in range(255):
                r = i
                b = 255-i
                self.allColor(self.ledpixels,self.Color(r,g,b),0.02)


	
	def setpixelcolor(self,n, r, g, b):
		if(n >= len(self.ledpixels)):
			return
		self.ledpixels[n] = Color(r,g,b)

	def setpixelcolor(self,n, c):
		if (n >= len(self.ledpixels)):
			return
		self.ledpixels[n] = c
