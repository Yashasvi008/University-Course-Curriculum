# -*- coding: utf-8 -*-
"""
@author: Yashasvi
"""


import tkinter as tk 
from tkinter import filedialog 
from tkinter import messagebox 
from main1 import readcsv
from main1 import Graph
from main1 import Course
import traceback

class Run_File:
    input_filename = ''
    
    @staticmethod
    def file_check():
        if(Run_File.g.acyclic()):
                messagebox.showwarning("Cycle Detected", "Check the interpendencies, Semester Plan not possible")
                print("Graph has a cycle, Semester Plan not possible")
        else:
                print("No cycle detected, Semester plan is possible!")
                messagebox.showinfo("No cycle detected", "Input file is correct, Semester plan is possible!")
                btn_viewplan = tk.Button(window, text = "View Semester Plan", command = Run_File.plan_courses)
                btn_viewplan.grid(column= 0, row = 3, pady = 10)

        
    
    @staticmethod
    def plan_courses():
        print ("Following is a Topological Sort of the given graph")
        plan = Run_File.g.topologicalSort()
        Run_File.display_result(plan)
               
# Function for opening the file explorer window 
    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select Input File in csv format", \
                                       filetypes = (("Text files", "*.csv*"), ("all files","*.*"))) 
    	# Change label contents 
        if(filename == ""):
            label_file_explorer.configure(text="No File Chosen")
        else:
            label_file_explorer.configure(text="File Chosen: "+filename)
            Run_File.input_filename = filename
            Run_File.g = readcsv(Run_File.input_filename)
            Run_File.file_check()
        
        
    def display_result(plan):
        result = tk.Tk()
        result.title("University Course Curriculum") 
      
        # set the configuration of GUI window 
        result.geometry("2000x1000") 
        
        heading = tk.Label(result, text = "Proposed Course Curriculum", 
                              font=('calibre', 12))
        
        heading.grid(row=0,padx=50,pady=10)
        
        listboxes = []
        for sem in plan:
            listbox = tk.Listbox(result, height = 5,  width = 32,  bg = "#CDE3F7",   
                             font = "Helvetica", 
                             fg = "black") 
            
            # insert elements by their index and names.
            for i,crsid in enumerate(sem):
                listbox.insert(i, Run_File.g.idmap[crsid].title + "    " + Run_File.g.idmap[crsid].name)
                
            listboxes.append(listbox)
            
            
        i = 0
        j = 1
        for listbox in listboxes:
            label = tk.Label(result, text = "Semester" + str(i+1), font = ('calibre', 14))
            if(j<=4):
                label.grid(row=1, column = i)
                listbox.grid(row=2, column = i, padx = 10, pady = 15)
            else:
                label.grid(row = 3, column = i-4)
                listbox.grid(row=4, column = i-4, padx = 10)
            i += 1
            j+=1
        
        result.mainloop()
        
            
class Add_new_Course:
    @staticmethod  
    def submit():
        new_crs_info = []
        
        try:
            #getting the values entred in entry boxes
            name=Add_new_Course.name_entry.get() 
            title=Add_new_Course.title_entry.get()
            prof=Add_new_Course.prof_entry.get()
            credit=Add_new_Course.credit_entry.get()
            idno=Add_new_Course.idno_entry.get()
            prereq=Add_new_Course.prereq_entry.get()
                    
            #adding them into a list
            new_crs_info.extend([name,title,prof,credit,idno])
                    
            #seperating the dependencies in a seperate list
            prereq_ids = prereq.split(",")
                    
            #combining that list with the list having all info of new course
            new_crs_info.extend(prereq_ids)
            
            #making the entry boxes empty for another entry
            Add_new_Course.name_var.set("") 
            Add_new_Course.title_var.set("")
            Add_new_Course.prof_var.set("")
            Add_new_Course.credit_var.set("")
            Add_new_Course.idno_var.set("")
            Add_new_Course.prereq_var.set("")
            
            Run_File.g.addcourse(new_crs_info)
            Run_File.file_check()
            
        except Exception as ex:
            error_detail = "Exception {} Traceback {}".format(str(ex), traceback.format_exc())
            messagebox.showwarning("Invalid Input", "Please enter Valid Course details!\n" + error_detail)
            print(error_detail)
            
            
            
    
    @staticmethod
    def newCourse():
        root = tk.Tk() 
        Add_new_Course.name_var=tk.StringVar() 
        Add_new_Course.title_var=tk.StringVar()
        Add_new_Course.prof_var=tk.StringVar()
        Add_new_Course.credit_var=tk.StringVar()
        Add_new_Course.idno_var = tk.StringVar()
        Add_new_Course.prereq_var = tk.StringVar()
      
      
        # set the title of GUI window 
        root.title("University Course Curriculum") 
        window.config(background = "#CDE3F7")
      
        root.geometry("600x400") 
        
        name_label = tk.Label(root, text = 'Course name', 
                          font=('calibre', 
                                10, 'bold')) 
       
        # creating a entry for input 
        # name using widget Entry 
        Add_new_Course.name_entry = tk.Entry(root, textvariable = Add_new_Course.name_var, 
                                             font=('calibre',10,'normal')) 
           

        title_label = tk.Label(root, text = 'Course Title', 
                               font = ('calibre',10,'bold')) 
           
     
        Add_new_Course.title_entry=tk.Entry(root, textvariable = Add_new_Course.title_var, 
                                            font = ('calibre',10,'normal'),) 
        
        prof_label = tk.Label(root, text = 'Course Professor', 
                              font = ('calibre',10,'bold')) 
           
     
        Add_new_Course.prof_entry=tk.Entry(root, textvariable = Add_new_Course.prof_var, 
                                           font = ('calibre',10,'normal'),) 
        
        credit_label = tk.Label(root, text = 'Course Credits', 
                                font = ('calibre',10,'bold')) 
           
      
        Add_new_Course.credit_entry=tk.Entry(root, textvariable = Add_new_Course.credit_var, 
                                             font = ('calibre',10,'normal'),) 
        
        idno_label = tk.Label(root, text = 'Course ID', 
                              font = ('calibre',10,'bold')) 
           
        
        Add_new_Course.idno_entry=tk.Entry(root, textvariable = Add_new_Course.idno_var, 
                                           font = ('calibre',10,'normal'),) 
        
        prereq_label = tk.Label(root, text = 'Prerequisite IDs', 
                                font = ('calibre',10,'bold')) 
           
      
        Add_new_Course.prereq_entry=tk.Entry(root, textvariable = Add_new_Course.prereq_var, 
                                             font = ('calibre',10,'normal'),) 
        
        # creating a button using the widget  
        # Button that will call the submit function  
        sub_btn=tk.Button(root,text = 'Submit', command = Add_new_Course.submit) 
               
        # placing the label and entry in 
        # the required position using grid 
        # method 
        name_label.grid(row=0,column=0) 
        Add_new_Course.name_entry.grid(row=0,column=1) 
        title_label.grid(row=1,column=0) 
        Add_new_Course.title_entry.grid(row=1,column=1)
        prof_label.grid(row=2,column=0)
        Add_new_Course.prof_entry.grid(row=2,column=1)
        credit_label.grid(row=3,column=0)
        Add_new_Course.credit_entry.grid(row=3,column=1)
        idno_label.grid(row=4,column=0)
        Add_new_Course.idno_entry.grid(row=4,column=1)
        prereq_label.grid(row=5,column=0)
        Add_new_Course.prereq_entry.grid(row=5,column=1)
        
         
        sub_btn.grid(row=6,column=1) 
           
        # performing an infinite loop  
        # for the window to display 
        root.mainloop()
  
   


																								
window = tk.Tk()

# Set window title 
window.title('University Course Curriculum') 

# Set window size 
window.geometry("950x500") 

#Set window background color 
window.config(background = "#CDE3F7") 

# Create a File Explorer label 
label_file_explorer = tk.Label(window, text = "Select input file containing courses and their details", width = 60, height = 4, fg = "blue") 
label_file_explorer.config(font=("Courier", 20))

button_explore = tk.Button(window, text = "Browse Files", command = Run_File.browseFiles)
print(Run_File.input_filename)

btn_addcrs = tk.Button(window, text = "Add new course", command = Add_new_Course.newCourse)

# Specifying positions
label_file_explorer.grid(column = 0, row = 0) 
    
button_explore.grid(column = 0, row = 1, pady=10) 
btn_addcrs.grid(column= 0, row = 2, pady = 10)
        
# Let the window wait for any events 
window.mainloop()
