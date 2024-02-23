from drone import drone
import time

df = drone()
df.connect()
df.disarm()
df.trim(0, 0, 0, 0)
df.takeoff()
while df.takeoff(): 
    df.get_battery()
    time.sleep(1)  
df.land()  

if __name__ == '__main__':
     bat = drone.get_battery()
     while True:
         print(bat.read())
