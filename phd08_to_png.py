# -*- coding: cp949 -*-

import argparse
import os
import numpy as np


def parse_args():
    desc = "phd08 �ѱ� �ؽ�Ʈ �����͸� .png �������� ��ȯ���ִ� ��ũ��Ʈ�Դϴ�."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--data_dir', type=str, default='phd08',
                        help='phd08 �ѱ� �����Ͱ� �����ϴ� ���丮', required=True)

    return parser.parse_args()


def file_to_arr(file_full_path):
    f = open(file_full_path)


def main():
    args = parse_args()
    if args is None:
        exit()

    # �������� üũ
    if not os.path.exists(args.data_dir):
        print("ERROR::" + args.data_dir, " �� �������� �ʴ� �����Դϴ�.")
        exit()

    for _, _, files in os.walk(args.data_dir):
        for file in files:
            print("INFO:: converting " + file + "...")
            file_to_arr(args.data_dir + '/' + file)


if __name__ == '__main__':
    main()
