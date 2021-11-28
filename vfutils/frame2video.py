import cv2
import os
import numpy as np

def frame2video(video_path, frame_path):

    frames = os.listdir(frame_path)
    # print(frames)
    first_frame = cv2.imread(os.path.join(frame_path, frames[0]))
    first_frame = np.array(first_frame)
    first_frame.dtype = np.uint8
    # print(os.path.join(frame_path, frames[0]))
    # print(first_frame)
    H, W, C = first_frame.shape
    size = (W, H)
    print(size)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(video_path, fourcc, 40, size)
    for frame in frames:
        print("writing", frame)
        out.write(cv2.imread(os.path.join(frame_path, frame)))

    out.release()
    print("释放")

if __name__ == "__main__":
    frame2video(r"../test_data/resultvideo/demo1.avi",
                r"../test_data/random/test_video_1")
    print("结束")
