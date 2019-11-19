import sys

import json
import h5py
import os
import os.path
import numpy as np
import random
import logging

import opts

opt = opts.parse_opt()

story_h5 = h5py.File(opt.story_h5, 'r', driver='core')['story'] # 存储句子转换为的id
full_story_h5 = h5py.File(opt.full_story_h5, 'r', driver='core')['story'] # 存储故事转换为的id
desc_h5 = h5py.File(opt.desc_h5, 'r', driver='core')['story'] # 存储caption
story_line = json.load(open(opt.story_line_json)) # 存储所有数据
id2word = story_line['id2words']
story_ids = {'train': [], 'val': [], 'test': []}
description_ids = {'train': [], 'val': [], 'test': []}
story_ids['train'] = list(story_line['train'].keys())
story_ids['val'] = list(story_line['val'].keys())
story_ids['test'] = list(story_line['test'].keys())
description_ids['train'] = list(story_line['image2caption']['train'].keys())
description_ids['val'] = list(story_line['image2caption']['val'].keys())
description_ids['test'] = list(story_line['image2caption']['test'].keys())

delete_story_ids = {'train': [], 'val': [], 'test': []}
# 遍历所有story，将caption为空的项去除
for split in ['train', 'val', 'test']:
    for story_id in story_ids[split]:
        is_delete = False
        story = story_line[split][story_id]
        for flickr_id in story['flickr_id']:
            if flickr_id not in story_line['image2caption'][split]:
                is_delete = True
                break
        if is_delete == True:
            del story_line[split][story_id]

# f = h5py.File("full_story.h5", "w")
# f.create_dataset("story", data=data)
# f.close()
# f = h5py.File("story.h5", "w")
# f.create_dataset("story", data=data)
# f.close()
# f = h5py.File("description.h5", 'w')
# f.create_dataset("story", data=text_array)
# f.close()
with open("story_line.json", 'w') as f:
    story_line_json = json.dumps(story_line)
    f.write(story_line_json)
    f.close()