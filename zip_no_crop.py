# -*- coding: utf-8 -*-
import cv2
import numpy
import os,sys
import zipdir
import shutil 
import iipl_head
import subprocess


def resource_path(relative_path):
    if hasattr(sys,'_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.abspath('.')
    return os.path.join(base_path,relative_path)

#中文路径问题
reload(sys)
sys.setdefaultencoding('utf-8')

MIDDLE_PROCESS_DEBUG = False
GENERATE_BINARY_CV_IMG = True

COMPRESS_PORT_IMG = True

GENERATE_GRAY_PORT_IMG = not COMPRESS_PORT_IMG
GENERATE_BINARY_PORT_IMG = not GENERATE_GRAY_PORT_IMG


KEEP_TMP_FILE = False

CROP_CV_IMG_NAME = 'crop_cv.png'
CROP_PORT_IMG_NAME ='crop_portrait.jpg'



# input: image path
# output: .iipl (.zip) file with same name containing: 
#     crop_cv.png
def compress_cv_with_image(img_path,out_path,level):
    # img_path = str(img_path)
    if os.path.exists(img_path) == False:
        print "ERROR: image path not exist: " + (img_path)
        return

    # create folder with pic name
    tmp_folder = out_path +     '.tmp/'
    if os.path.isdir(tmp_folder):
        shutil.rmtree(tmp_folder)
    os.mkdir(tmp_folder)

    # get the image
    # print type(img_path)
    # print img_path
    img_path = img_path.decode('utf-8').encode('gbk')
    # print type(img_path)
    # print img_path
    img_gray = cv2.imread(img_path,0)
    # cv2.imwrite('1.png',img)

    # save as binary
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    img_bin = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,7)

    # cv2.imwrite('2.png',img_bin)
    #compress cv with opencv png
    png_paras = list()
    png_paras.append(cv2.IMWRITE_PNG_COMPRESSION)
    png_paras.append(9)
    if GENERATE_BINARY_CV_IMG:
        save_path = os.path.join(tmp_folder, CROP_CV_IMG_NAME)
        save_path = save_path.decode('utf-8').encode('gbk')
        cv2.imwrite(save_path, img_bin, png_paras)

    # TODO compress these file with pngout
    print '========TODO========\ncompress these file with pngout' 
    crop_cv_tmp_path = os.path.join(tmp_folder, CROP_CV_IMG_NAME)
    # crop_portrait_tmp_path = os.path.join(tmp_folder, CROP_PORT_IMG_NAME)
    # print crop_cv_tmp_path 
    # crop_cv_tmp_path.decode('utf-8').encode('gbk')  
    # print crop_portrait_tmp_path
    cmd = "optipng.exe "+ (crop_cv_tmp_path)

    # os.system(cmd)
    para = level
    subprocess.call([resource_path('res\\optipng.exe'),para,crop_cv_tmp_path.encode('gbk')])
    #rename png file as iipl file
    iipl_tmp_path = crop_cv_tmp_path.rstrip('.png')+'.iipl'

    os.rename(crop_cv_tmp_path,iipl_tmp_path)

    # os.remove(crop_cv_tmp_path)
    # os.remove(crop_portrait_tmp_path)

    iipl_head.add_head(iipl_tmp_path)

    # compress restul to .zip but rename as .iipl 
    iipl_file_path = tmp_folder.rstrip('.tmp/')+'.iipl'
    zipdir.zipdir(tmp_folder, iipl_file_path)

    # remove .tmp folder
    if not KEEP_TMP_FILE:
        shutil.rmtree(tmp_folder)

def test():
    img_path = './cv1.jpg'
    compress_cv_with_image(img_path)

if __name__ == '__main__':
    # test()

    if len(sys.argv) < 2:
        print 'usage: python zip.py image_path.jpg'
    else:
        compress_cv_with_image(sys.argv[1])
