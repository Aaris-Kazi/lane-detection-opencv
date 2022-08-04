import cv2
# import time
# FPS_SMOOTHING = 0.9

# def showfps(frame, prev, fps): 
#     now = time.time()
#     fps = (fps*FPS_SMOOTHING + (1/(now - prev))*(1.0 - FPS_SMOOTHING))
#     print("fps: {:.1f}".format(fps))
#     font = cv2.FONT_HERSHEY_DUPLEX
#     cv2.putText(frame, "fps: {:.1f}".format(fps), (246, 26), font, 0.5, (0, 255, 0), 1)
#     return now, fps

def advance_fps(frame, new, prev):
    fps = 1/(new -prev)
    fps = int(fps)
    fps = str(fps)
    cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
    prev = new
    return prev
