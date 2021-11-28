import cv2
import os
def video2frame(video_path, frame_path, frame_interval):
    if not os.path.isdir(frame_path):
        os.mkdir(frame_path)

    vidcap = cv2.VideoCapture(video_path)
    (cap, frame) = vidcap.read()

    if cap == False:
        print('cannot open video file')
    count = 0

    while cap:
        cv2.imwrite(os.path.join(frame_path, '%.6d.jpg' % count), frame)
        print('%.6d.jpg' % count)
        count += 1
        for i in range(frame_interval):
            (cap, frame) = vidcap.read()


if __name__ == "__main__":
    video_path = r"../test_data/raw_video/demo1.mp4"
    frame_path = r"../test_data/random/test_video_1"

    video2frame(video_path, frame_path)

