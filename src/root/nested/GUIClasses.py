'''
Created on Mar 31, 2015

@author: kahere
'''

import tkinter
import numpy as np
import sys
import os
import tkinter.filedialog as tkFileDialog

class GUI(object):
    '''
    classdocs
    
    Variety of selection functions to provide user interface. About time to make
    these into an actual class.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def selectFromList(self, title, choices):
        '''
        Drop-down menu to select from list of choices
        '''
        
        root = tkinter.Tk()
        root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
        root.title(title)
            
        var = tkinter.StringVar(root)
        var.set(choices[0]) # Initial value
        option = tkinter.OptionMenu(root, var, *choices)
        option.pack(side='left', padx=10, pady=10)
        scrollbar = tkinter.Scrollbar(root)
        scrollbar.pack(side='right', fill='y')
        
        def get_choice():
            select_choice = var.get()
            root.quit()
            return select_choice
        
        button = tkinter.Button(root, text='OK', command=get_choice)
        button.pack(side='left', padx=20, pady=10)
            
        root.mainloop()
        selection = button.invoke()
        root.withdraw()
        return selection
    
    
    def textBox(self, text):
        '''
        Text box
        
        '''
        master = tkinter.Tk()
        
        def cancel():
            master.destroy()
            sys.exit()
        
        tkinter.Label(master, text=(text)).grid(row=0)
        tkinter.Button(master, text='OK', command = cancel).grid(row=1)
        
        tkinter.mainloop()
        
    def browsetoFile(self, title, validfiletype='.csv'):
        # Browse to directory of portfolio file
        root = tkinter.Tk()
        root.withdraw()
        currdir = os.getcwd()
        validfile = False
        while validfile == False: 
            # Continue asking until valid file type is chosen. Had else to default to auto-named file.
            tempdir = tkFileDialog.askopenfilename(parent=root, initialdir=currdir, title=title)
            if len(tempdir) > 0:
                if tempdir.endswith(validfiletype):
                    portfolio_file = tempdir
                    validfile = True
                else:
                    print("Error: File type must be %s." % (validfiletype))
                   
        return portfolio_file         
