#Parker Gowans
#1/19
import sys
#########################################################################
def open_file(file_name,mode):
    try:
        the_file = open(file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name,"Ending program.\n",e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
            return the_file
#########################################################################
def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

file = open_file("test_file.txt","w")
file.write("This/ is a/ Test")
file.close()
file = open_file("test_file.txt","r")
line = next_line(file)
print(line)
