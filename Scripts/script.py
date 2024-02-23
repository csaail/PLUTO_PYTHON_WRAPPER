from drone import drone
 
drone=drone()
drone.connect()

#trim(Roll,Pitch,Throttle,Yaw)
drone.trim(-10,0,0,0)
drone.disarm()  
drone.takeoff()

print("Increasing throttle speed")
drone.throttle_speed(5,1) #(value, Duration)
#print("pitch")
#drone.pitch_speed(40)
#Backflip
#drone.flip()

#drone.get_roll()
#drone.get_pitch()

#creating a square
#print("forward")
#drone.pitch_speed(50)
drone.land()
drone.disarm()
"""
print("pitch 1")
drone.roll_speed(50)
drone.pitch_speed(-50)
drone.roll_speed(-50)

#forward-backward-forward-land
drone.pitch_speed(50)
drone.pitch_speed(-50)
drone.pitch_speed(-25)



#Backflip
#drone.flip()

"""

