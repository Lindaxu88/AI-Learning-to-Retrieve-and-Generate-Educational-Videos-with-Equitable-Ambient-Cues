import os
path = r'D:\yolov5-5.0\VOCdevkit\VOC2007\Annotations'
files = os.listdir(path)
i = 1
for picture in files:
    # old name
    old = os.path.join(path, picture)
    # new name
    new = picture.replace(picture, str(i) + '.xml')
    # add a path
    new = os.path.join(path, new)
    # modify the file name
    os.rename(old, new)
    i = i + 1
print('DONE')
