import os, pyautogui, time

pyautogui.FAILSAFE = False				# Prevents the script from stopping when the PC is locked.
idle = False
date = time.asctime( time.localtime(time.time()) )[:3]

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
	if pyautogui.position() != mouse_position:	# User has moved the mouse.
		idle = False							# Change idle status to exit loop.
	else:
		pyautogui.press('ctrlleft')				# Press the Ctrl key.

def post_time():
	global idle_start, date
	localtime = time.asctime( time.localtime(time.time()) ) #Get the time
	if date != localtime[:3]:	# Print date if changed.
		print ('\n'+date)
		date = localtime[:3]
	if idle == True:
		idle_start = time.asctime( time.localtime(time.time()) )[11:-8]
	if idle == False:
		idle_stop =  time.asctime( time.localtime(time.time()) )[11:-8]
		print ("User idle at " + idle_start + "    User back at " +  idle_stop)		# Not Idle


###			Main Program		###
print ("Program started...")					# Let the user know we got here.
print ('\n'+date[:3])
while True:						# Main While Loop.
	while idle == False:		# User is not idle loop.
		user_not_idle()
	post_time()					
	
	while idle == True:			# User is idle loop.
		user_is_idle()
	post_time()					# Announce that the user is not idle.
