import os
from vfutils.frame2video import frame2video
from vfutils.video2frame import video2frame
import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-n", "--name", type=str, help="video name")
    parse.add_argument("-t", "--target", type=str, help="target video name")


    args = parse.parse_args()

    video2frame(os.path.join(r"../test_data/raw_video", args.name), os.path.join(r"../test_data/random", args.name), 1)
    os.system("!CUDA_VISIBLE_DEVICES=0 python run.py --mode PVDNet_DVD --config config_PVDNet --data random --ckpt_abs_name ckpt/PVDNet_DVD.pytorch")
    frame2video(os.path.join(r"../test_data/resultvideo", args.target), os.path.join(r"../test_data/random", args.name))

    print("end!")