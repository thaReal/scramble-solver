Zynga Scramble Solver Bot
=========================
Still an early, experimental version but with everything configured correctly
(see below) the bot works fairly well and should manage to hit about 90% - 98% 
of the possible words during a regular game. 

There are a lot of little bugfixes and optimizations that need to be done that
I'll do my best to document/implement. Make sure to read /doc/notes.txt 


Setup
-----
First of all, this code is designed for use with an Asus Nexus 7 Tablet. Also, 
while it's been running on windows also with *I think* the only modification 
being the bytemapping in the dictionary file, (for some reason) I've moved back
to Linux and have made tweaks since then so if you're trying to get this to run
you'll probably have better luck with a Unix based OS. Otherwise, try 
commenting/uncommenting the corresponding lines of code in /src/solver.py for
Windows.

- MonkeyRunner

Getting MonkeyRunner from the Android SDK to work with the bot correctly is
really all that needs to be set up, which can range from simple to extremely
frustrating. There's plenty of information availible with the SDK and elsewhere 
to get it set up - essentially once adb can see your attached device you should 
be good to go.

So while I plan to add this to some sort of configuration file, for the moment 
the simplest method I came up with was creating a static link to your
monkeyrunner executeable in the /src/ directory.

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
	

