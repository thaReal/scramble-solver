import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()
package = 'com.zynga.scramble'

# activity = 'com.example.android.myapplication.MainActivity'

# sets the name of the component to start
# runComponent = package + '/' + activity

# Runs the component
device.startActivity(component=package)

# Presses the Menu button
device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot
result = device.takeSnapshot()

# Writes the screenshot to a file
result.writeToFile('myproject/shot1.png','png')
