import cv2
import os

# RTSP_URL ="https://msk.rtsp.me/7RepJRzoTaTnv3XM106qmw/1688629931/hls/KPbwo57M.m3u8?ip=178.34.62.123" # Головатого Северная

RTSP_URL='https://www.youtube.com/embed/8xvDwLqW2Aw'

RTSP_URL ="https://www.kubzsk.ru/cam/stream.webm" #фонтан у здания суда







import cv2

output_file = 'output_video.mp4'  # Specify the output file name


cap = cv2.VideoCapture(RTSP_URL)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

# Get video stream properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a VideoWriter object to save the frames
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Specify the codec (e.g., XVID, MJPG, etc.)
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Display the frame
        cv2.imshow('frame', frame)
        
        # Write the frame to the output video file
        out.write(frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()









