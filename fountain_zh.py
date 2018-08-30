#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# https://github.com/leeyupeng/fountain-zh

from __future__ import division
import sys
import math
import getopt
import re

UTF_8 = "utf-8"

def str_encode(s):
    if sys.version_info < (3, 0):
        return s.encode(UTF_8)
    else:
        return s

def str_decode(s):
    if sys.version_info < (3, 0):
        return s.decode(UTF_8)
    else:
        return s

PAGE_HEIGHT = 900 # 页面高度
FONT_HEIGHT = 24  # 字体高度
MARGIN = 18              # 文字外边距
SCENE_HEADING_HEIGHT = FONT_HEIGHT + MARGIN
TRANSITION_HEIGHT = FONT_HEIGHT + MARGIN + MARGIN
CHARACTER_HEIGHT = FONT_HEIGHT + MARGIN
LYRIS_HEIGHT = FONT_HEIGHT
ACTION_PER_LINE = 33 # 动作描述每行的最大文字数
DIALOG_PER_LINE = 19 # 台词每行的最大文字数
MORE = str_decode("转下页")   # 跨页台词转下页提示文字
CONT_D = str_decode("继续")  # 跨页台词继续提示文字

try:
    opts, args = getopt.getopt(sys.argv[1:], "sr", ["add-scene-number", "remove-scene-number"])
except getopt.GetoptError:
    print("Invalid args")
    exit(1)

add_scene_number = False
remove_scene_number = False

for o, a in opts:
    if o in ("-s", "--add-scene-number"):
        add_scene_number = True
    if o in ("-r", "--remove-scene-number"):
        remove_scene_number = True

def print_raw(line):
    print(str_encode(line)),

def print_page_break():
    global height
    print("")
    print("===")
    print("")

def smart_print_to_next_page(line, item_height):
    global height
    height = height + item_height
    if (height >= PAGE_HEIGHT - item_height):
        print_page_break()
        print_raw(line)
        height = item_height
    else:
        print_raw(line)

def count_len(c):
    length = 0
    if ord(c) < 128:
        length = 0.5
    else:
        length = 1
    return length

def count_character(line):
    count = 0
    for c in line.strip():
        count = count + count_len(c)
    return count

def smart_print_to_multi_page(line, char_per_line, line_height, type):
    global height
    global current_charater

    char_count = count_character(line)
    new_height = height + ((math.ceil(char_count / char_per_line))) * line_height
    if(type == "action"):
        new_height += MARGIN

    # 如果预测高度未超出分页，则直接打印原内容
    if (new_height < PAGE_HEIGHT):
        height = new_height
        print_raw(line)

    else:
        # 分页打印内容
        cut_position = (math.ceil((PAGE_HEIGHT - height) / line_height)) * char_per_line + 1
        i = 0
        tmp = ""
        char_count_in_new_page = 0
        if (cut_position >= char_count):
            print_raw(line)
            print_page_break()
            height = 0
            return
        for c in line.strip():
            char_len = count_len(c)
            i += char_len
            if ( i >= cut_position and (i - cut_position) < 1):

                # 处理跨页台词，打印 MORE
                if (type == "dialog"):
                    tmp = tmp + "\n(" + MORE + ")\n"

                tmp = tmp + "\n\n===\n\n"
                char_count_in_new_page = 0
                height = 0

                # 处理跨页台词，打印 CONT_D
                if (type == "dialog"):
                    tmp = tmp + current_charater + " (" + CONT_D + ")\n"
                    height = CHARACTER_HEIGHT
                    cut_position = cut_position + math.ceil(((PAGE_HEIGHT - CHARACTER_HEIGHT) / line_height))*char_per_line
                else:
                    cut_position = cut_position + math.ceil((PAGE_HEIGHT / line_height))*char_per_line

            char_count_in_new_page += char_len
            tmp = tmp + c

        height = (math.ceil(char_count_in_new_page / char_per_line)) * line_height
        print_raw(tmp + "\n")

height = 0
next_is_dialog = False
scene_number = 0
current_charater = ""
in_title_page = True
title_page_empty_line = 0

for line in sys.stdin:

    # 删除注释
    line = re.sub(r"\[\[.+\]\]", "", str_decode(line))

   # 在封面页结束处清空高度
    if (in_title_page):
        if(not len(line.strip())):
            title_page_empty_line = title_page_empty_line + 1

        if (title_page_empty_line == 2):
            in_title_page = False
            height = 0

    # 封面页内容、换页符
    if(
    line.startswith("Title:")
    or line.startswith("Author:")
    or line.startswith("Credit:")
    or line.startswith("Source:")
    or line.startswith("===")
    ):
        print_raw(line)
        height = 0

    # 大纲、大纲内容
    elif(line.startswith("#")
    or line.startswith("= ")
    ):
        print_raw(line)

    # 场景标题
    elif(line.startswith(".")):
        scene_number += 1;
        if add_scene_number:
            line = line.strip() + " #" + str(scene_number) + "#" + "\n"
        if remove_scene_number:
            line = re.sub(r" #\d+#", "", line)
        smart_print_to_next_page(line, SCENE_HEADING_HEIGHT)

    # 角色
    elif(line.startswith("@")):
        current_charater = re.search(r"\@([^\(\s]*)", line).group(0)
        smart_print_to_next_page(line, CHARACTER_HEIGHT)
        next_is_dialog = True

    # 换场或居中
    elif(line.startswith(">")):
        smart_print_to_next_page(line, TRANSITION_HEIGHT)

    # 歌词
    elif(line.startswith("~")):
        smart_print_to_next_page(line, LYRIS_HEIGHT)

    # 空行
    elif(not len(line.strip())):
        print_raw(line)
        next_is_dialog = False

    # 动作描述
    elif(line.startswith("!")):
        smart_print_to_multi_page(line, ACTION_PER_LINE, FONT_HEIGHT, "action")

    # 台词或动作
    else:

        # 台词
        if next_is_dialog:
            smart_print_to_multi_page(line, DIALOG_PER_LINE, FONT_HEIGHT, "dialog")
        else:
            smart_print_to_multi_page(line, ACTION_PER_LINE, FONT_HEIGHT, "action")
