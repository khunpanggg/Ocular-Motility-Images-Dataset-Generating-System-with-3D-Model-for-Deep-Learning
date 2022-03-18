import numpy as np
import cv2
import os
from natsort import natsorted

box1_l1 = []
box1_l2 = []
box1_l3 = []
box1_l4 = []

box2_l1 = []
box2_l2 = []
box2_l3 = []
box2_l4 = []

box3_l1 = []
box3_l2 = []
box3_l3 = []
box3_l4 = []

box4_l1 = []
box4_l2 = []
box4_l3 = []
box4_l4 = []

box5_l1 = []
box5_l2 = []
box5_l3 = []
box5_l4 = []

box6_l1 = []
box6_l2 = []
box6_l3 = []
box6_l4 = []


path = 'dataset/'
path_p1_l1 = 'nRSRnLIO'
path_p1_l2 = 'abRSRnLIO'
path_p1_l3 = 'nRSRabLIO'
path_p1_l4 = 'abRSRabLIO'

path_p2_l1 = 'nRIOnLSR'
path_p2_l2 = 'abRIOnLSR'
path_p2_l3 = 'nRIOabLSR'
path_p2_l4 = 'abRIOabLSR'

path_p3_l1 = 'nRLRnLMR'
path_p3_l2 = 'abRLRnLMR'
path_p3_l3 = 'nRLRabLMR'
path_p3_l4 = 'abRLRabLMR'

path_p4_l1 = 'nRMRnLLR'
path_p4_l2 = 'abRMRnLLR'
path_p4_l3 = 'nRMRabLLR'
path_p4_l4 = 'abRMRabLLR'

path_p5_l1 = 'nRIRnLSO'
path_p5_l2 = 'abRIRnLSO'
path_p5_l3 = 'nRIRabLSO'
path_p5_l4 = 'abRIRabLSO'

path_p6_l1 = 'nRSOnLIR'
path_p6_l2 = 'abRSOnLIR'
path_p6_l3 = 'nRSOabLIR'
path_p6_l4 = 'abRSOabLIR'


#number of each label and append to list

box1_l1 = [file for file in natsorted(os.listdir(path + path_p1_l1))]

box1_l2 = [file for file in natsorted(os.listdir(path + path_p1_l2))]

box1_l3 = [file for file in natsorted(os.listdir(path + path_p1_l3))]

box1_l4 = [file for file in natsorted(os.listdir(path + path_p1_l4))]


box2_l1 = [file for file in natsorted(os.listdir(path + path_p2_l1))]

box2_l2 = [file for file in natsorted(os.listdir(path + path_p2_l2))]

box2_l3 = [file for file in natsorted(os.listdir(path + path_p2_l3))]

box2_l4 = [file for file in natsorted(os.listdir(path + path_p2_l4))]


box3_l1 = [file for file in natsorted(os.listdir(path + path_p3_l1))]

box3_l2 = [file for file in natsorted(os.listdir(path + path_p3_l2))]

box3_l3 = [file for file in natsorted(os.listdir(path + path_p3_l3))]

box3_l4 = [file for file in natsorted(os.listdir(path + path_p3_l4))]


box4_l1 = [file for file in natsorted(os.listdir(path + path_p4_l1))]

box4_l2 = [file for file in natsorted(os.listdir(path + path_p4_l2))]

box4_l3 = [file for file in natsorted(os.listdir(path + path_p4_l3))]

box4_l4 = [file for file in natsorted(os.listdir(path + path_p4_l4))]


box5_l1 = [file for file in natsorted(os.listdir(path + path_p5_l1))]

box5_l2 = [file for file in natsorted(os.listdir(path + path_p5_l2))]

box5_l3 = [file for file in natsorted(os.listdir(path + path_p5_l3))]

box5_l4 = [file for file in natsorted(os.listdir(path + path_p5_l4))]


box6_l1 = [file for file in natsorted(os.listdir(path + path_p6_l1))]

box6_l2 = [file for file in natsorted(os.listdir(path + path_p6_l2))]

box6_l3 = [file for file in natsorted(os.listdir(path + path_p6_l3))]

box6_l4 = [file for file in natsorted(os.listdir(path + path_p6_l4))]


#create folder
dataset_home_new = 'datasetmergefile_mix_pack9/'
newdir = dataset_home_new + 'train/'
os.makedirs(newdir, exist_ok=True)


#for label1(normal)
for i in range(len(box1_l1)):
    img1 = cv2.imread(path+path_p1_l1 + '/' + box1_l1[i])
    img2 = cv2.imread(path+path_p2_l1 + '/' + box2_l1[i])
    img3 = cv2.imread(path+path_p3_l1 + '/' + box3_l1[i])
    img4 = cv2.imread(path+path_p4_l1 + '/' + box4_l1[i])
    img5 = cv2.imread(path+path_p5_l1 + '/' + box5_l1[i])
    img6 = cv2.imread(path+path_p6_l1 + '/' + box6_l1[i])
    
    row1 = np.hstack((img1, img2))
    row2 = np.hstack((img3, img4))
    row3 = np.hstack((img5, img6))

    ver = np.vstack((row1, row2, row3))
    cv2.imwrite(newdir + 'normal.' + str(i+1) + '.jpg', ver)
    # print('normal.' + str(i+1) + '.jpg')
    # cv2.imshow('ver',ver)
    cv2.waitKey(0)


#for label2(abRnL)
for i in range(len(box1_l2)):
    img1 = cv2.imread(path+path_p1_l2 + '/' + box1_l2[i])
    img2 = cv2.imread(path+path_p2_l2 + '/' + box2_l2[i])
    img3 = cv2.imread(path+path_p3_l2 + '/' + box3_l2[i])
    img4 = cv2.imread(path+path_p4_l2 + '/' + box4_l2[i])
    img5 = cv2.imread(path+path_p5_l2 + '/' + box5_l2[i])
    img6 = cv2.imread(path+path_p6_l2 + '/' + box6_l2[i])
    
    row1 = np.hstack((img1, img2))
    row2 = np.hstack((img3, img4))
    row3 = np.hstack((img5, img6))

    ver = np.vstack((row1, row2, row3))
    cv2.imwrite(newdir + 'abRnL.' + str(i+1) + '.jpg', ver)
    cv2.waitKey(0)


#for label3(nRabL)
for i in range(len(box1_l3)):
    img1 = cv2.imread(path+path_p1_l3 + '/' + box1_l3[i])
    img2 = cv2.imread(path+path_p2_l3 + '/' + box2_l3[i])
    img3 = cv2.imread(path+path_p3_l3 + '/' + box3_l3[i])
    img4 = cv2.imread(path+path_p4_l3 + '/' + box4_l3[i])
    img5 = cv2.imread(path+path_p5_l3 + '/' + box5_l3[i])
    img6 = cv2.imread(path+path_p6_l3 + '/' + box6_l3[i])
    
    row1 = np.hstack((img1, img2))
    row2 = np.hstack((img3, img4))
    row3 = np.hstack((img5, img6))

    ver = np.vstack((row1, row2, row3))
    cv2.imwrite(newdir + 'nRabL.' + str(i+1) + '.jpg', ver)
    cv2.waitKey(0)


#for label3(abRabL)
for i in range(len(box1_l4)):
    img1 = cv2.imread(path+path_p1_l4 + '/' + box1_l4[i])
    img2 = cv2.imread(path+path_p2_l4 + '/' + box2_l4[i])
    img3 = cv2.imread(path+path_p3_l4 + '/' + box3_l4[i])
    img4 = cv2.imread(path+path_p4_l4 + '/' + box4_l4[i])
    img5 = cv2.imread(path+path_p5_l4 + '/' + box5_l4[i])
    img6 = cv2.imread(path+path_p6_l4 + '/' + box6_l4[i])
    
    row1 = np.hstack((img1, img2))
    row2 = np.hstack((img3, img4))
    row3 = np.hstack((img5, img6))

    ver = np.vstack((row1, row2, row3))
    cv2.imwrite(newdir + 'abRabL.' + str(i+1) + '.jpg', ver)
    cv2.waitKey(0)
    