"""
This will batch rename a group of files in a given directory,
once you pass the current and new extensions

批量修改文件后缀
"""
import os
import argparse


# 批量重命名
def batch_rename(work_dir, old_ext, new_ext):
    """
    :param work_dir: 需要修改文件的绝对路径  如(..\hello-world\file_tools\pic)
    :param old_ext: 需要修改的后缀名称   如(.png)
    :param new_ext: 修改后的后缀名称    如(.jpg)
    :return:  返回修改后的文件名称列表
    """
    # 循环获取目录文件名称
    for filename in os.listdir(work_dir):
        # 切割文件名称和后缀
        split_file =os.path.splitext(filename)
        # 获取后缀名称
        file_ext = split_file[1]

        # 判断当前文件后缀是否与需修改后缀一致
        if file_ext == old_ext:
            # 后缀一致，修改文件后缀并拼接文件名称
            newfile = split_file[0] + new_ext

            # 重命名文件名称
            os.rename(os.path.join(work_dir, filename), os.path.join(work_dir, newfile))

    # 输出修改后的文件名称列表
    print("rename is done! ")
    print(os.listdir(work_dir))


# 命令行参数解析
def get_parser():
    """
    :return:
    """
    # 添加参数化对象
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    # 添加一个参数WORK_DIR
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    # 添加一个参数OLD_EXT
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    # 添加一个参数NEW_EXT
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    # 返回参数对象
    return parser


def main():
    """
    :return:
    """
    # adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args())

    # Set the variable work_dir with the first argument passed
    work_dir = args['work_dir'][0]
    # Set the variable old_ext with the second argument passed
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    # Set the variable new_ext with the third argument passed
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
    main()
