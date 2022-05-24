import numpy as np
import os

file_dir_KCL = 'D:\\Codestates\\section4\\project4\\Korean_commercial_letters\\'
file_name = 'Korean_commercial_letters_2350.txt'

with open(file_dir_KCL + file_name, "r", encoding='cp949') as file: ## encoding='cp949'(or 'euc-kr) ==> 한글 인코딩 
    strings = file.readlines()

KCL = list(*strings)
print(KCL)
print('한글 상용 글자 2350자 :',len(KCL))


file_dir = 'D:\\Codestates\\section4\\project4\\Korean_commercial_letters\\phd08-conversion\\phd08_npy_results\\'
data_name = 'phd08_data_'
label_name = 'phd08_labels_'

dirList = os.listdir(file_dir)
print(int(len(dirList)/2))

## 손글씨 데이터와 라벨 파일들 결합
#raw_data  = file_dir + data_name + str(1) + '.npy'
raw_label = file_dir + label_name + str(1) + '.npy'
#npy_data = np.load(raw_data)
npy_label= np.load(raw_label)
for i in range(1,int(len(dirList)/2)):
    #raw_data  = file_dir + data_name + str(i) + '.npy'
    raw_label = file_dir + label_name + str(i) + '.npy'
    #temp_data = np.load(raw_data)
    temp_label= np.load(raw_label)
    #npy_data = np.concatenate([npy_data, temp_data])
    npy_label = np.concatenate([npy_label, temp_label])
#npy_data

## 한글 라벨링(KCL에 저장되어 있는 2350 단어를 npy_label 순서에 맞게 npy_label_kor에 저장)
#npy_label_kor = np.zeros(len(npy_label)).astype(str)
npy_label_num = np.zeros(len(npy_label)).astype(str)
for i in range(int((len(npy_label))/500)):
    npy_label_num[i*500:i*500+500] = i #KCL[i]

## 각각 데이터/라벨/한글라벨 파일로 저장
#out_data  = file_dir + data_name + '.npy'
#out_label = file_dir + label_name + '.npy' 
#out_label_kor = file_dir + label_name + 'kor' + '.npy'
out_label_num = file_dir + label_name + 'num' + '.npy'

#np.save(out_data, npy_data)
#np.save(out_label, npy_label)
#np.save(out_label_kor, npy_label_kor)
np.save(out_label_num, npy_label_num)

## 저장된 파일 로딩 후 확인
#npy_data_test = np.load(out_data)
#npy_label_test = np.load(out_label)
#npy_label_kor_test = np.load(out_label_kor)
npy_label_num_test = np.load(out_label_num)
#npy_data_test.shape, npy_label_test.shape, npy_label_kor_test.shape
print(npy_label_num_test.shape)