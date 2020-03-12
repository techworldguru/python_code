import sys

### raising the errors forcefully
if 1 < 2 :
    raise ValueError("some error found")




name= "python"
lang  = "unix"

if name != lang :
    print("Both are not equal")
else:
    raise Exception("Error found")
