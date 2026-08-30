# Task 2 : Write and Append Data to a File

data = input("Enter text to write to the file : ")

with open("output.txt","wt") as ot:
    ot.write(data+"\n")
    
append_data = input("Enter additional text to append : ")
    
with open("output.txt","at") as ot:
    ot.write(append_data)
    
with open("output.txt","rt") as ot:
    final_content = ot.read()
    print(final_content)