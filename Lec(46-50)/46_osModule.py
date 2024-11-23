import os 

'''
if(not os.path.exists("data_46")):
    os.mkdir("data_46")

for i in range(0,100):
    os.mkdir(f"data_46/Day{i+1}")

'''

'''
for i in range (0,100):
    os.rename(f"data_46/Day{i+1}", f"data_46/Tutorial{i+1}")
'''    

for i in range (0,100):
    os.rename(f"data_46/Tutorial{i+1}", f"data_46/Tutorial {i+1}")