Zynga Scramble Solver Bot
=========================
Still an early, experimental version but with everything configured correctly
(see below) the bot works fairly well and should manage to hit about 90% - 98% 
of the possible words during a regular game. 

| Warning: Still Under Construction |


Basic Instructions
------------------
All control is [for the moment] being handled by 'appmanager.py'. For a regular game, get to the matchup screen and then run appmanager with no arguments. For 
tournament mode, run 'appmanager.py -t'. 

Additional funtionality is being added and well eventually be rolled into an 
optparse interface.


Dependencies / Running
----------------------

<<<<<<< HEAD
=======
> cd scramble-bot/src/
> ln -s /path/to/android-sdk/tools/monkeyrunner


Usage
-----
WARNING: THIS SECTION IS OUTDATED!!!

This is the part that needs to definitely get streamlined (but also breaks 
things the most) although usage is still fairly simple. Write now I only wrote
a Unix version of this but it works virtually the same in Windows.

1. change into the src directory and run scramble_core.py which is the actual 
   puzzle solving engine.
   
   > cd /src/
   > python scramble_core.py
   
2. Now the program should prompt you to input the puzzle letters. Start a game 
   and quickly try to memorize a line or two and then pause and type it in. 
   Repeat until you have all 16 letters and then hit 'Enter' to run the 
   program. NOTE: you should be leaving the game paused while the solver is 
   running. I typically read two lines at a time and have ~1:55 on the clock 
   after I'm done entering the puzzle.

3. When the solver completes it will print out how many words it found and also
   output a 'solution.txt' file that will be fed into monkeyrunner. Press 
   'Enter' once more so the program completes. With the device plugged into the 
   computer and the game still paused run the following command:
   
   > ./monkeyrunner monkey_manager.py
   
   If everything works correctly the python script should load the solution 
   file, find your device, and then begin running through entering each word. It
   should exit by itself once it reaches the end of the file (usually before the
   puzzle is done, using just one freeze powerup).
   
* This has been improved significantly but could still use some additional 
(new) fixes that I'll be documenting. For individual games change to the source
directory and run the following command:

	> python appmanager.py
	

>>>>>>> 6205239c67fbb13007201c99d1fcb1cd84954355
