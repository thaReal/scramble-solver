Notes
=====
This file is/will contain essentially random notes and ideas I have that either
don't fit or aren't ready to be called either a TODO or a bug. 


Program Hierarchy
-----------------
> solver_core
	- StatsGetter
	- SolutionFile
	- WordDictionary
	- GameEngine
	
> solver
	- ChainRoot
	- WordChain
	- Worker
	
*** Problem is that GameEngine takes all the extra classes I need from solver 
	core and packs them with 1 worker to solve a puzzle. I need to pass game
	engine back to solver core so that I can use a worker pool to implement 
	multithreaded solving.
	
	Idea is to create a work Queue and then have GameEngine push all the initial
	ChainRoot's to it. I'll already have the output files loaded but I'm going
	to need to include some type of lock to make it threadsafe. Finally, each 
	worker can grab a copy of the dictionary file from the GameEngine that they 
	can close out when they finish.
	
	New thought: Rather than try to create locks on the output file, I should 
	be able to use a second Queue to just write any solutions workers return 
	since one single-threaded read through this should be a fairly quick 
	operation. I can either create a seperate Queue for each file or just use 
	one and have them sorted as they get pulled out at the end.
	

