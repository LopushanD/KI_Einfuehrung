
"""
TO DO

        - rewrite grid constructor (so that grid doesn't need any initial start and end node in it) and rethink ways grid gets to know where it's start and end nodes are located
        (self.start,self.end) (make something like a method that lets grid scan itself. it has to be called after user painted positions of start and end in the grid)
                * after that rewrite program initialization and start in Controller
        
        
        - think about restrictions of parameters that can be handled. Now you can freely choose any parameters for field and grid, that is prone to cause bugs 
        
        - change the classes so, that they can be more comfortably controlled from Controller class
                * like add specific attribut to classes that Controller class can look at, to know that should be done next 
        
        
        - Now when there's no path, you get expection. Turn it into pop up, that tells that there's no way available
        
        - go through code and program architecture and refactor it where needed
        
        - write documentation for the program
        
        - upgrade random obstacle generator
        
        - transform dialogs to GUI 
"""


