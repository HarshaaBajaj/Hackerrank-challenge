'''
  For given file 'names_list_00.txt' with the following content,

code1.c
code1.cpp
code1.cs
code2.cs
code3.c
code4.c
code5.cpp

  create new files based off the extensions as follows,

c_names_list_00.txt
cpp_names_list_00.txt
cs_names_list_00.txt

  fill files with content based off orginal file,
c_names_list_00.txt
  code1.c
  code3.c
  code4.c
 etc.,

  Eg input structure:
    root--> names.txt
  Eg output structure:
    root--> names.txt
        --> c_names_list_00.txt
        --> cpp_names_list_00.txt
        --> cs_names_list_00.txt
'''

if __name__=='__main__':
  filename = 'names_list_00.txt' ; l = ['c','cs','cpp']
  for f in l:    
      with open('_'.join([f,filename]),'w') as fh:fh.close() # create all files even if there is no current content to write
  with open(filename) as lines:
      for line in lines:
          with open('_'.join([line.strip().split('.')[-1],filename]), 'a+') as res:
                  res.write(line)      
