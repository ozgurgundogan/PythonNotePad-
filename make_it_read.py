import os,sys
from Tkinter import *

button_counter=0  ## file_reader finds the number of the last button (biggest)


search_words_to_get_biggest_count={				\
		"java" :'$(document).ready(function(){$("#button_', \
		"html" :'<input type="button" id="button_' \
		}

type_of_file={		\
		"js" :'java', \
		"html" :'html' \
		}		


def file_extension_finder(file_path):
	extension=file_path.split(".")
	extension=extension[len(extension)-1]
	return extension

## it returns the max number of button in the file,
## if file is generated before.
def file_reader(file_path):
	available_script=""
	f=open(file_path,'r')
	data=f.read()
	if data.find(str(html_init_creator()))>=0:
		available_script+=data[data.find(str(html_init_creator()))+len(str(html_init_creator())):data.find(str(html_final_creator()))]
		# print "-------------------------------------"
		# print available_script
	f.close()	
	return available_script
		# max_number_in_the_file=0
	# f=open(file_path,'r')
	# lines=f.readlines()
	# file_extension=file_extension_finder(file_path)   ### get file exntesion
	# for line in lines:
	# 	line.find(search_words_to_get_biggest_count[type_of_file[file_extension]])
	# 	written_number_in_the_file=line[len(search_words_to_get_biggest_count[type_of_file[file_extension]])]
	# 	if written_number_in_the_file>max_number_in_the_file:
	# 		max_number_in_the_file=written_number_in_the_file

	# return max_number_in_the_file		

##This block is to create new js ,css and html code.
## No integration with the files.

######
##### NOTICE IT OVERWRITES
def file_writer(file_path_with_name,context):
	f=open(file_path_with_name,'w')
	f.write(context)
	f.write("\n")
	f.close()
	print "Paragraph is added ! "


## it checks whether the file is generated or not 
def file_generated_checker(file_path_with_name):
	try:
		f=open(file_path_with_name)
		f.close()
		return True
	except Exception, e:
		return False

def _th_finder(context):
	search_word='<button type="button" class="btn btn-info" data-toggle="collapse" data-target="#tab_'
	num=context.find(search_word)  ## num for finding search element
	maxima=0			## this is for finding 
	while(num>0):
		# print "found: ",
		# print int(context[context.find(search_word)+len(search_word)])
		# print "maxima: ",
		# print maxima
		maxima+=1
		# if int(context[context.find(search_word)+len(search_word)])>maxima:
		# 	maxima=context[context.find(search_word)+len(search_word)]
		num=context.find(search_word,num+1)
	return int(maxima)	



###
###
##### TOTALLY RELATED WITH CREATING NEW FILES
###
###


def html_init_creator():
	script_initial=""
	script_initial+='<!DOCTYPE html>'
	script_initial+='\n'
	script_initial+='<html>'
	script_initial+='\n'
	script_initial+='<head>'
  	script_initial+='\n'
  	script_initial+='<meta name="viewport" content="width=device-width, initial-scale=1">'
  	script_initial+='\n'
  	script_initial+='<link rel="stylesheet" href="bootstrap.min.css">'
  	script_initial+='\n'
  	script_initial+='</head>'
  	script_initial+='\n'
  	script_initial+='<body>'

  	return script_initial

def html_partial_creator(paragraph,title,id_for_button=0):
	script_partial=""
	script_partial+='<div class="container">'
	script_partial+="\n"
	script_partial+='<button type="button" class="btn btn-info" data-toggle="collapse" data-target="#tab_'
	script_partial+=str(id_for_button)
	script_partial+='">'
	script_partial+="\n"
	script_partial+=title
	script_partial+='</button><br\>'
	script_partial+="\n"
	script_partial+='<div id="tab_'
	script_partial+=str(id_for_button)
	script_partial+='" class="collapse">'
	script_partial+="\n"
	script_partial+=paragraph
	script_partial+="\n"
	script_partial+='</div>'
	script_partial+="\n"
	script_partial+='</div>'
	script_partial+='<br/>'
	return script_partial

def html_final_creator():
	script_final=""
	script_final+='<script src="jquery.min.js"></script>'
	script_final+='<script src="bootstrap.min.js"></script>'
	script_final+='</body>'
	script_final+='</html>'

	return script_final

def new_script_creator(file_path_with_name,title,content):
	new_script=""
	new_script+=str(html_init_creator())
	new_script+="\n"
	new_script+=str(html_partial_creator(content,title))
	new_script+="\n"
	new_script+=html_final_creator()

	file_writer(file_path_with_name,new_script)			

def already_written_script_creator(file_path_with_name,title,content,_th):
	new_script=""
	new_script+=str(html_init_creator())
	new_script+="\n"
	new_script+=str(file_reader(file_path_with_name))
	new_script+="\n"
	new_script+=str(html_partial_creator(content,title,_th))
	new_script+="\n"
	new_script+=html_final_creator()
	file_writer(file_path_with_name,new_script)


###Main Caller
def main(file_path_with_name,title,content):
	if file_generated_checker(file_path_with_name)==True:
		# print str(file_reader(file_path_with_name))
		# print 
		th=_th_finder(str(file_reader(file_path_with_name)))
		# print th
		already_written_script_creator(file_path_with_name,title,content,th)
	else:
		new_script_creator(file_path_with_name,title,content)


def main2():
	global einit
	global text
	global e1

	root = Tk()

	text = Text(root)
	einit = Entry(root)
	e1 = Entry(root)
	

	L1 = Label(root, text="Path",pady=10)
	L1.pack()
	einit.pack()
	
	L2 = Label(root, text="Title",pady=10)
	L2.pack()
	e1.pack()

	L3 = Label(root, text="Paragraph",pady=10)
	L3.pack()
	# e1.pack()
	text.pack(padx=10,pady=10)
	L4 = Label(root,pady=10)
	L4.pack()
	b = Button(root, text="Save", width=10, command=callback_for_title)
	b.pack()

	

	root.mainloop()


def callback_for_title():
	global e1
	global text
	global einit
	path="./"+str(einit.get())
	title=e1.get() 
	content=text.get("1.0",END)
	e1.delete(0,END)
	text.delete(0.0,END)
	main(path,title,content)

	

		
main2()
# main("./code_Creator/nebileyim.html","agagagagagag","123asd")