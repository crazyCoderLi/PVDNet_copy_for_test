import cv2

video_path = r"../test_data/raw_video/demo1.mp4"

capture = cv2.VideoCapture(video_path)

fps = capture.get(5)
print("fps = ", fps)

