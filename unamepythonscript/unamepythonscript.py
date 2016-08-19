#!/usr/bin/python3
# Script name: uname.py
# Purpose: Illustrate Python OOP capabilities to write shell scripts more easily
# License: GPL v3 (http://www.gnu.org/license/gpl.html)

# Copyright (C) 2016 Liberty Parker
# Github: liberty1997 / QQ: 969829149 / Wechat: ljh888666_
# Email: liberty1997 (at) yeah (dot) net

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# ( at your option ) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.   If not, see .

# REVISION HISTORY
# DATE        VERSION AUTHOR		CHANGE DESCRIPTION
# ---------   ------- --------------    -----------------
# 2016-08-19   1.0    Liberty Parker     Initial version

#########第一行的内容一定要顶头写!

### 导入 os 模块
import os

### 将 os.uname()的输出赋值给 systemInfo 变量
### os.uname() 会返回五个字符串元组 (sysname, nodename, release, version, machine)
### 参见文档: https://docs.python.org/3.2/library/os.html#module-os
systemInfo = os.uname()

### 这是一个固定的数组， 用于描述脚本输出的字段标题
headers = ["Operating system","Hostname","Release","Version","Machine"]

### 初始化索引值， 用于定义每一步迭代中
### systemInfo 和字段标题的索引
index = 0

### 字段标题变量的初始值
caption = ""

### 值变量的初始值
values = ""

### 分割线变量的初始值
separators = ""

### 开始循环
for item in systemInfo:
 if len(item) < len(headers[index]):
    ### 一个包含横线的字符串， 横线长度的等于item[index]或 headers[index]
    ### 要重复一个字符，用引号圈起来并用星号(*)乘以所需的重复次数
    separators = separators + "-" * len(headers[index]) + " "
    caption = caption + headers[index] + " "
    values = values + systemInfo[index] + " " * (len(headers[index]) - len(item)) + " "
 else:
    separators = separators + "-" * len(item) + " "
    caption = caption + headers[index] + " " * (len(item) - len(headers[index]) + 1)
    values = values + item + " "
    ### 索引加 1
 index = index + 1
### 终止循环

### 输出转换为大写的变量(字段标题)名
print(caption.upper())

### 输出分割线
print(separators)

# 输出值(systemInfo 中的项目)
print(values)
 
### 步骤:
### 1) 保持该脚本为unamepythonscript.py并通过如下命令给其执行权限:
### chmod +x unamepythonscript.py
### 2) 执行它:
### ./unamepythonscript.py
