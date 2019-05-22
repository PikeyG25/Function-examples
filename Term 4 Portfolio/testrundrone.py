from pyparrot.Minidrone import Mambo

# If you are using BLE: you will need to change this to the address of YOUR mambo
# if you are using Wifi, this can be ignored
mamboAddr = "e0:14:3f:cd:3d:fc"

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    # get the state information
    print("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("taking off!")
    mambo.safe_takeoff(5)

    if (mambo.sensors.flying_state != "emergency"):
        print("flying state is %s" % mambo.sensors.flying_state)
        
        #insert movement code here
        #pitch=forward backward movement
        #roll=left right tilt
        #yaw= left right turn
        #vertical movement = hieght, negatives go towards ground but not too close, -20 is fine for chair
        #duration= the length of the command
        
        
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-8, duration=2)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        mambo.fly_direct(roll=0, pitch=25, yaw=0, vertical_movement=0, duration=4.25)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        
        mambo.fly_direct(roll=15, pitch=0, yaw=0, vertical_movement=0, duration=2)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        mambo.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0, duration=2.5)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        mambo.fly_direct(roll=-15, pitch=0, yaw=0, vertical_movement=0, duration=2.8)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        mambo.fly_direct(roll=0, pitch=-25, yaw=0, vertical_movement=0, duration=3.5)
        
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=16, duration=2)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        mambo.fly_direct(roll=20, pitch=0, yaw=0, vertical_movement=0, duration=2.6)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        mambo.fly_direct(roll=0, pitch=-25, yaw=0, vertical_movement=0, duration=3.25)
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=2)
        
        
        #mambo.fly_direct(roll=-30, pitch=10, yaw=-30, vertical_movement=0, duration=4)
        #mambo.fly_direct(roll=-40, pitch=10, yaw=-40, vertical_movement=0, duration=2)
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=3)
        
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-15, duration=1)
        #mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=3)
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=1)
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=1)
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=1)
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=1)
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=1)
        #mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=0, duration=1)
        success = mambo.flip(direction="front")
        print("landing")
        print("flying state is %s" % mambo.sensors.flying_state)
        mambo.safe_land(5)
        mambo.smart_sleep(5)

    print("disconnect")
    mambo.disconnect()
