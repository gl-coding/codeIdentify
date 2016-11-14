import os
import json
import base64
import time

import hashlib

class ConvertToCode:
    __imgpath = ""

    def genFilename(self, src):
        des = src + str(time.time())
        m2 = hashlib.md5()
        m2.update(des)
        return m2.hexdigest()


    def webDataToimg(self, webdata):
        jsondata = json.loads(webdata)
        base64code = jsondata["base64"]

        self.__imgpath = self.genFilename(base64code)

        imgdata = base64.b64decode(base64code)
        imgfile = open(self.__imgpath, 'wb')
        imgfile.write(imgdata)
        imgfile.close()
        
    def rmFile(self, path):
        if os.path.exists(path):
            os.remove(path)

    def imgToCode(self):
        #self.__imgpath = "img.png"
        codefile_path = self.__imgpath + ".txt"

        self.rmFile(codefile_path)
        
        if (not os.path.exists(self.__imgpath)):
            return "picture not exists"

        command = "tesseract " + self.__imgpath + " " + self.__imgpath + " -l eng"
        os.system(command)
        
        count = 0
        wait_time = 3
        while (not os.path.exists(codefile_path)):
            time.sleep(1)
            count += 1
            if count == wait_time:
                return "convert time too long"

        resFile = open(codefile_path, "r")
        res = resFile.read()
        resFile.close()
        
        self.rmFile(codefile_path)
        self.rmFile(self.__imgpath)

        return res
    
    def webDataToCode(self, webdata):
        self.webDataToimg(webdata)
        res = self.imgToCode()
        return res


def run():
    test = ConvertToCode()
    print test.genFilename("test")
    print test.imgToCode()

#run()
