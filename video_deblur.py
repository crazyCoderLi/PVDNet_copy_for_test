import os
from vfutils.frame2video import frame2video
from vfutils.video2frame import video2frame
import argparse



import subprocess





if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-n", "--name", type=str, help="video name")
    parse.add_argument("-t", "--target", type=str, help="target video name")
    parse.add_argument("-i", "--frame_interval", type=int, help="interval to sample frames of video")


    args = parse.parse_args()

    # break the source video into frames that can be handled by the deblur module
    fps = video2frame(
        os.path.join(r"test_data/raw_video", args.name),
        os.path.join(r"test_data/random", args.name),
        args.frame_interval
    )

    # invoke the deblur module by cli
    cmd = "CUDA_VISIBLE_DEVICES=0 python run.py --mode PVDNet_DVD --config config_PVDNet --data random --ckpt_abs_name ckpt/PVDNet_DVD.pytorch"
    p = subprocess.Popen(cmd, shell=True)
    return_code = p.wait()

    # join the deblured frames into the target video
    frame2video(
        os.path.join(r"test_data/resultvideo", args.target),
        #os.path.join(r"test_data/random", args.name)

        r"/content/PVDNet_copy_for_test/test_data/resultvideo/PVDNet_TOG2021/PVDNet_DVD/result/quanti_quali/PVDNet_DVD/random/2021/png/output/random",
        fps
    )

    print("end!")