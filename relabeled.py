import os
##Codigo para reescribir todas las etiquetas a 0. "CAR"
labels_path1 = "vehicles.v2-release.yolov8-obb/train/labels/"
labels_path2 = "vehicles.v2-release.yolov8-obb/test/labels/"
labels_path3 = "vehicles.v2-release.yolov8-obb/valid/labels/"

def relabel(labels_path):
    for root, _, files in os.walk(labels_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                new_lines = []
                for line in lines:
                    parts = line.strip().split()
                    if parts and parts[0] == '4':
                        parts[0] = '0' 
                        new_lines.append(' '.join(parts) + '\n')
                with open(file_path, 'w') as f:
                    f.writelines(new_lines)

relabel(labels_path3)
