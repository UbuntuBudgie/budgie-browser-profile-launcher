#!/usr/bin/python3

# This file is part of Browser Profile Launcher

# Copyright © 2018 Serdar ŞEN <serdarbote@gmail.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.


import os
import errno
import datetime


class Log():

    def __init__(self, appConfigFolderName):

        self.TAG = "FileLog"
        self.logErrorOn = True
        self.logDebugOn = True
        self.logInfoOn = True

        self.ERROR_TAG = "Log e"
        self.DEBUG_TAG = "Log d"
        self.INFO_TAG = "Log i"

        dirPath = os.path.expanduser("~") + "/.cache/" + appConfigFolderName
        self.makeDirIfNotExist(dirPath)
        self.filePath = dirPath + "/log"

    # gets datatime
    def getDateTime(self):
        return datetime.datetime.now()

    #makes dir
    def makeDirIfNotExist(self, path):
        if (path is not ""):
            try:
                os.makedirs(path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    ########################
    # Error log
    ########################
    def e(self, TAG, msg):
        if (self.logErrorOn):
            logText = "\n[%s %s in %s] :\n%s\n" % (self.getDateTime(), self.ERROR_TAG, TAG, str(msg))
            with open(self.filePath, "a+") as file:
                file.write(logText)

    ########################
    # Debug log
    ########################
    def d(self, TAG, msg):
        if (self.logDebugOn):
            logText = "\n[%s %s in %s] :\n%s\n" % (self.getDateTime(), self.DEBUG_TAG, TAG, str(msg))
            with open(self.filePath, "a+") as file:
                file.write(logText)


    ########################
    # İnfo log
    ########################
    def i(self, TAG, msg):
        if (self.logInfoOn):
            logText = "\n[%s %s in %s] :\n%s\n" % (self.getDateTime(), self.INFO_TAG, TAG, str(msg))
            with open(self.filePath, "a+") as file:
                file.write(logText)


    #just reminder
    # def tryExceptTemplate(self):
    #     try:
    #         #the job here
    #     except IOError as err:
    #         self.fileLog.e(self.TAG, "I/O error({0}): {1} : %s" % err)
    #     except ValueError:
    #         self.fileLog.e(self.TAG, "Could not convert data to an integer.")
    #     except:
    #         self.fileLog.e(self.TAG, "Unexpected error: %s" % sys.exc_info()[0])
    #         raise
