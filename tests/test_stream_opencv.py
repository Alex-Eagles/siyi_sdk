import cv2

cap = cv2.VideoCapture("rtsp://192.168.144.25:8554/main.264", cv2.CAP_FFMPEG)

# Print attributes
print("---------BEFORE---------")
print(f"Frame width: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}")
print(f"Frame height: {int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
print(f"FPS: {int(cap.get(cv2.CAP_PROP_FPS))}")

# Reduce buffer size for lower latency
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# Set lower resolution and frame rate to reduce latency
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 15)

# Print attributes, after changing them
print("---------AFTER---------")
print(f"Frame width: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}")
print(f"Frame height: {int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
print(f"FPS: {int(cap.get(cv2.CAP_PROP_FPS))}")

if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Camera Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
