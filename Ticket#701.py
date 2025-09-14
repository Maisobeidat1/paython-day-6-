Ticket#702
import os
try:
    if os.path.exists("grades.txt"):
        with open("grades.txt", "r") as f:
            data = f.read()
            else
            print("data")
            with open("grades.txt","w") as f:
                f.write("")
except exxception as e:
    print(data,e)
