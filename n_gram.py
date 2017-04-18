# !/usr/bin/env Python
# coding: utf-8
# python: v-3.6.0
# n-gram

import os
import os.path

n_gram = 4
rootdir = '/home/zsy/python_code/wyp_4_18/sip2'
result_list = {}


def dir_list(path):

    file_list = os.listdir(path)
    for filename in file_list:
        filepath = os.path.join(path, filename)

        if os.path.isfile(filepath):
            # print(filepath)
            file_object = open(filepath)

            try:
                all_the_text = file_object.read()
            except Exception as e:
                print(e)
                continue
            finally:
                file_object.close()

            file_long = len(all_the_text)
            # print(file_long)
            if file_long >= n_gram:
                if file_long > 64:
                    num = 64
                else:
                    num = file_long
            else:
                continue

            for i in range(1, num-n_gram+2):
                n_gram_temp = "".join(all_the_text[i:i + n_gram])  # .encode('utf-8')
                if n_gram_temp not in result_list:  # 词频统计
                    result_list[n_gram_temp] = 0  # 典型的字典操作
                result_list[n_gram_temp] += 1
        else:
            dir_list(filepath)

if __name__ == '__main__':
    dir_list(rootdir)
    print(result_list)
    sort_list = sorted(result_list.items(), key=lambda item: item[1])  # 转为list
    for i in sort_list:
        print(i)
