import pyautogui
import cv2
import numpy as np
import time

resolution = pyautogui.screenshot().size
codec = cv2.VideoWriter_fourcc(*"XVID")

filename = "Recording.avi"
fps = 15.0
frame_time = 1.0 / fps

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)
cv2.moveWindow("Live", 0, 0)

try:
    while True:
        start_time = time.time()

        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        out.write(frame)
        cv2.imshow("Live", frame)

        if cv2.waitKey(1) == ord("q"):
            break

        elapsed = time.time() - start_time
        if elapsed < frame_time:
            time.sleep(frame_time - elapsed)
except KeyboardInterrupt:
    pass
finally:
    out.release()
    cv2.destroyAllWindows()