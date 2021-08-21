import os

def get_size(path):
    files = os.listdir(path)
    # print(files)
    size = 0
    if len(files):
        for i in files:
            if os.path.isfile(os.path.join(path,i)):
                size += os.path.getsize(os.path.join(path,i))
            elif os.path.isdir(os.path.join(path,i)):
                size += get_size(os.path.join(path,i))
    elif len(files) == 0:
        size = 0
    return size



if __name__ == '__main__':
    path = input('请输入路径：\n')
    if os.path.isfile(path):
        print('请输入文件夹路径！\n')
    elif os.path.isdir(path):
        size = get_size(path)
        print('文件大小：%.2f MB'%(size/1024/1024))
