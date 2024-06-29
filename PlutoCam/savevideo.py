import plutocam
drone = plutocam.LWDrone()


drone.set_time()

with open('out.h264', 'wb') as fp:
    for frame in drone.start_video_stream():
        fp.write(frame.frame_bytes)
