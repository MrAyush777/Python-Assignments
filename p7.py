lineNo=1
try:
    
    with open("sample.txt","r") as fs:
        for line in fs:
            print(f"{line.strip()}")
except FileNotFoundError:
    print()