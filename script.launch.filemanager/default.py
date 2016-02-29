# -*- coding: utf-8 -*-
# Copyright (c) 2016 Correl J. Roush, Gerónimo Oñativia

import os
import sys
import xbmc
import xbmcaddon

__script_id__ = 'script.launch.filemanager'
__settings__ = xbmcaddon.Addon(id=__script_id__)
_ = __settings__.getLocalizedString

BASE_ADDON_PATH = xbmc.translatePath(__settings__.getAddonInfo('path'))

if __name__ == '__main__':
    xbmc.executebuiltin("Notification(%s,%s,1500,%s)"%(_(32000), _(32002), BASE_ADDON_PATH + "/notification.png"))
    launch_path = __settings__.getSetting('launch_path')
    if launch_path:
        xbmc.executebuiltin("ActivateWindow(FileManager,%s)" % launch_path)
    else:
        xbmc.executebuiltin("ActivateWindow(FileManager)")
