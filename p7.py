# Task 1: Read a File and Handle Errors
line_no = 0
try:
    
    with open("sample.txt","rt") as sp:
        content = sp.readlines()
    
        for line in content:
            line_no+=1
            print(f"line {line_no}: {line}",end="")

except FileNotFoundError:
    print(f"Error : the file 'sample.txt' was not found.")