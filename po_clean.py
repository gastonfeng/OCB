# -*- coding: utf-8 -*-
# Copyright 2017 Jarvis (www.odoomod.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os

def clean(addons_path,lang_keep=['zh_CN']):
    module_name_list = os.listdir(addons_path)
    clean_count = 0
    for module_name in module_name_list:
        module_lang_path = '%s/%s/i18n'%(addons_path,module_name)
        if os.path.exists(module_lang_path):
            for lang_file in os.listdir(module_lang_path):
                lang_name,lang_ext = lang_file.split('.')
                if lang_name not in lang_keep and lang_ext == 'po':
                    i18n_file_path = '%s/%s'%(module_lang_path,lang_file)
                    os.remove(i18n_file_path)
                    clean_count += 1
                    print(i18n_file_path)
    print(clean_count)


if __name__ == '__main__':
    # this script clean useless po files, save your diskspace and boost pycharm
    # default keep zh_CN translation
    # place this file in odoo root path or define odoo addons path, and execute
    # 此脚本清理无用的PO文件，节省磁盘空间并加速PyCharm启动
    # 默认保留简体中文（zh_CN）翻译
    # 放置此文件于Odoo的根目录，或指定Odoo的addons路径，并执行
    addons_path = '../odoo/addons'
    clean(addons_path,['zh_CN'])