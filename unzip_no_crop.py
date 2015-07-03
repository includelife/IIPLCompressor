# -*- coding: utf-8 -*-
import cv2
import numpy
import os,sys    
import zipfile
import shutil 
import iipl_head

#中文路径问题
reload(sys)
sys.setdefaultencoding('utf-8')

KEEP_TMP_FILE = False

CROP_CV_IMG_NAME = 'crop_cv.jpg'
CROP_PORT_IMG_NAME ='crop_portrait.png'

DECOMP_CROP_PORT_IMG_NAME ='crop_portrait.jpg'
DECOMP_CROP_CV_IMG_NAME = 'crop_cv.iipl'


def recover_cv_from_iipl(iipl_file_path,out_path_folder):
    if not zipfile.is_zipfile(iipl_file_path):
        print 'ERROR: %s is not a zip file' % iipl_file_path
    
    tmp_dir = iipl_file_path.rstrip('.iipl/') + '.tmp'

    zfile = zipfile.ZipFile(iipl_file_path, 'r')
    for name in zfile.namelist():
        (_, filename) = os.path.split(name)
        print "Decompressing " + filename + " on " + tmp_dir
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)

        zfile.extract(name, tmp_dir)

    recover_cv_from_tmp_folder(tmp_dir,out_path_folder)

    # remove tmp_dir
    if not KEEP_TMP_FILE:
        shutil.rmtree(tmp_dir)

def recover_cv_from_tmp_folder(decompress_folder,out_path_folder):

    # decompress_cv_path = os.path.join(decompress_folder, DECOMP_CROP_CV_IMG_NAME)
    decompress_cv_path = decompress_folder+'/'+DECOMP_CROP_CV_IMG_NAME
    # print decompress_cv_path

    if os.path.exists(decompress_folder)==False:
        print 'ERROR: compress folder not found:' + decompress_folder
        return None

    if os.path.exists(decompress_cv_path)==False:
        print 'ERROR: compress cv path not found:' + decompress_cv_path
        return None

    #remove .iipl for a png file 
    iipl_head.remove_head(decompress_cv_path)

    # load img

    crop_cv_img = cv2.imread(decompress_cv_path.decode('utf-8').encode('gbk'))
    # cv2.imwrite('res.png',crop_cv_img)
    # write img to disk
    # cv2.imwrite(decompress_folder.rstrip('.tmp/') + '.restore.jpg', crop_cv_img)
    cv2.imwrite(out_path_folder.decode('utf-8').encode('gbk') , crop_cv_img)



def test():
    path = './cv1.jpg.iipl'
    recover_cv_from_tmp_folder(path)

if __name__ == '__main__':
    # test()
    if len(sys.argv) < 2:
        print 'usage: python unzip.py iipl_file_path'
    else:
        recover_cv_from_iipl(sys.argv[1])