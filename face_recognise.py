import os
import cv2 as cv
import numpy as np

people=['modi','ben_afflick','musk']

# p=[]
# for i in os.listdir(r'C:\Users\DELL\Pictures'):
#     p.append(i)
# print(p)    
    
DIR=r'C:\Users\DELL\Pictures'
haar_cascade=cv.CascadeClassifier('haar_cascade.xml')
features=[]
labels=[]
def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            # print(f'No. of faces found={ len(faces_rect)}')
            
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()

print("TRAINING DONE-----------   ")
# print(f'Length of the features ={len(features)}')
# print(f'Length of the labels = {len(labels)}')                     
features=np.array(features,dtype='object')
labels=np.array(labels)

face_recognizer=cv.face.LBPHFaceRecognizer_create()

# Train the recoginzer on the features list and the labels list

face_recognizer.train(features,labels)
face_recognizer.save("face_trained.yml") 

  
np.save('features.npy' , features)
np.save('albels.npy' , labels)