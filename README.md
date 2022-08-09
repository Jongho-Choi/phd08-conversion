
---- 중요사항 ----

phd08과 관련된 결과물들이 총 14 GB이기 때문에 phd08 raw데이터는 인터넷에서 다운받고 phd08_npy_results phd08_png_results는 따로 python 파일을 구동해서 만들기 바랍니다.

---- 파일 설명 ----

phd08_to_npy.py
phd08 파일을 array 형태로 저장

phd08_to_png.py
phd08 파일을 이미지 형태로 저장

npy_data.py
array 형태의 데이터 전처리 과정

train.ipynb
KCL 모델 학습

---- 폴더 설명 ----

figures
train.ipynb 에서 학습한 train_acc, val_acc 그래프 저장

models
train.ipynb 에서 학습한 KCL 모델 저장

phd08
phd08 데이터셋

phd08_npy_results
array 형태로 변환된 데이터 저장

phd08_png_results
이미지 형태로 변환된 데이터 저장
