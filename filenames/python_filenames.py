#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
path = "/home/liberty/myAlgorithmchengxu"
filenames = os.listdir(path)
for name in filenames:
    print(name)

print(len(filenames))
