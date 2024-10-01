import os
import time
for i in range(1,600):
    with open('../Text/ASCII-Image'+str(i)+'.txt', 'r') as file:
        content = file.read()
        
    time.sleep(0.05)
    os.system('cls')
    print(content)