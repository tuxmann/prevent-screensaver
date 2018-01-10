import os
import time
import pyautogui

pyautogui.FAILSAFE = False				# Prevents the script from stopping when the PC is locked.
idle = False

###			Functions			###
def user_not_idle():
	global idle
	mouse_position = pyautogui.position()		# Get the mouse position.
	time.sleep(300)
	if pyautogui.position() == mouse_position:	# User is currently idle.
		pyautogui.press('ctrlleft')				# Press the Ctrl key.
		idle = True								# Change idle status to exit loop.

def user_is_idle():
	global idle
	mouse_position = pyautogui.position()		# Get the mouse position.
	time.sleep(15)
	if pyautogui.position() != mouse_position:	# User is not idle.
		idle = False							# Change idle status to exit loop.
	else:
		pyautogui.press('ctrlleft')				# Press the Ctrl key.
	

def post_time():
	#print ("post_time", idle)
	localtime = time.asctime( time.localtime(time.time()) ) #Get the time
	if idle == True:
		print ("User gone at ", localtime)		# Idle
	if idle == False:
		print ("User back at ", localtime)		# Not Idle
		print ()


###			Main Program		###
print ("Program started...")					# Let the user know we got here.

while True:						# Main While Loop.
	while idle == False:		# User is not idle loop.
		user_not_idle()
	
	post_time()					# Announce that the user is idle.
	
	while idle == True:			# User is not idle loop.
		user_is_idle()
	
	post_time()					# Announce that the user is not idle.
