#os操作
#将文件加下面的各个文件夹进行分类
import os
import shutil


def classify_files(folder_path):
    """
    将文件加下面的各个文件夹进行分类
    :param folder_path: 文件夹路径
    :return:
    """
    # 获取文件夹下的所有文件
    files = os.listdir(folder_path)

    # 创建文件夹
    for file in files:
        file_path = os.path.join(folder_path, file)
        print(f"文件路径:{file_path}")
        if os.path.isfile(file_path):
            # 获取文件后缀名
            file_ext = os.path.splitext(file)[1].replace(".", "")
            #创建文件夹
            if not os.path.exists(os.path.join(folder_path, file_ext)):
                print(f"创建文件夹:{os.path.join(folder_path, file_ext)}")
                os.mkdir(os.path.join(folder_path, file_ext))
            #将文件放到这个文件夹下
            print(f"移动文件到指定目录:{os.path.join(folder_path, file_ext,file)}")
            shutil.move(file_path, os.path.join(folder_path, file_ext,file))

#classify_files("D:\\test\\file\\AB0003")
for root, dirs, _ in os.walk("D:\\test\\file",topdown=True):
     dirs[:] = list(filter(lambda x:len(x)>0,dirs))
     for _dir in dirs:
         classify_files(os.path.join(root, _dir))
     break