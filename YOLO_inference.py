
# Ensure that the ultralytics package is installed before running this script.
# You can install it using: pip install ultralytics

from ultralytics import YOLO


model=YOLO('yolov8x')

results=model.predict('input_video/football_video.mp4',save=True)

print(results[0])

print("=======================================")

for box in results[0].boxes:
    print(box)
