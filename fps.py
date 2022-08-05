
def advance_fps(frame, new, prev, cv2):
    fps = 1/(new -prev)
    fps = int(fps)
    fps = str(fps)
    cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (100, 255, 0), 3, 1)
    prev = new
    return prev
