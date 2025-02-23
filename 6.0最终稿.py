import cv2
import os

# 输入和输出视频路径
input_video_path = r'C:\Users\Administrator\Desktop\1221\123.mp4'
output_video_path = r'C:\Users\Administrator\Desktop\1221\output_video.mp4'

# 检查输入视频文件是否存在
if not os.path.exists(input_video_path):
    print("输入视频文件不存在，请检查路径！")
    exit()

# 打开输入视频文件
cap = cv2.VideoCapture(input_video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开视频文件，请检查路径和文件格式！")
    exit()

print("视频文件成功打开，开始处理...")

# 获取视频的基本信息
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

print(f"视频宽度: {frame_width}, 高度: {frame_height}, 帧率: {fps}")

# 创建输出视频文件，保持原视频的帧率
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用 mp4 编码
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# 初始化帧计数器
frame_count = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 判断当前帧是奇数帧还是偶数帧
    if frame_count % 2 == 1:
        # 奇数帧：替换为黑色画面
        black_frame = 0 * frame  # 创建一个全黑的画面
        out.write(black_frame)
        print(f"写入黑色帧: {frame_count}")
    else:
        # 偶数帧：保留为正常画面
        out.write(frame)
        print(f"写入正常帧: {frame_count}")
    
    frame_count += 1

# 释放资源
cap.release()
out.release()

print("处理完成！")
