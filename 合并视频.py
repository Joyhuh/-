import cv2
import os

# 输入和输出视频路径
video1_path = r'C:\Users\Administrator\Desktop\1121\1.mp4'
video2_path = r'C:\Users\Administrator\Desktop\1121\2.mp4'
output_video_path = r'C:\Users\Administrator\Desktop\1121\merged_video.mp4'

# 检查输入视频文件是否存在
if not os.path.exists(video1_path) or not os.path.exists(video2_path):
    print("输入视频文件不存在，请检查路径！")
    exit()

# 打开两个输入视频文件
cap1 = cv2.VideoCapture(video1_path)
cap2 = cv2.VideoCapture(video2_path)

# 检查视频是否成功打开
if not cap1.isOpened() or not cap2.isOpened():
    print("无法打开视频文件，请检查路径和文件格式！")
    exit()

print("视频文件成功打开，开始处理...")

# 获取视频的基本信息
frame_width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))

frame_width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))

# 确保两个视频的分辨率和帧率相同
if frame_width1 != frame_width2 or frame_height1 != frame_height2:
    print("两个视频的分辨率不同，无法合并！")
    exit()

if fps1 != fps2 or fps1 != 60:
    print("两个视频的帧率不同或不是60fps，无法合并！")
    exit()

# 创建输出视频文件，帧率为120fps
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用 mp4 编码
out = cv2.VideoWriter(output_video_path, fourcc, 120, (frame_width1, frame_height1))

# 初始化帧计数器
frame_count = 0

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    
    # 如果两个视频都读取完毕，则退出循环
    if not ret1 and not ret2:
        break
    
    # 从第一个视频读取一帧并写入输出视频
    if ret1:
        out.write(frame1)
        print(f"写入视频1的帧: {frame_count}")
        frame_count += 1
    
    # 从第二个视频读取一帧并写入输出视频
    if ret2:
        out.write(frame2)
        print(f"写入视频2的帧: {frame_count}")
        frame_count += 1

# 释放资源
cap1.release()
cap2.release()
out.release()

print("处理完成！")
