import cv2
import os
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db,storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,
    {
    'databaseURL':"https://face-attendance-realtime-b2948-default-rtdb.firebaseio.com/",
    'storageBucket':"face-attendance-realtime-b2948.appspot.com"
})


# Importing th mode images into a list
folderPath = 'images'
PathList = os.listdir(folderPath)
imgList = []
studentIds = []

for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    # print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])

    filename = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)



print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)


    return encodeList

print("Encodeing is Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownwithIds = [encodeListKnown,studentIds]
print("Encoding complete")

file = open("Encodefile.p",'wb')
pickle.dump(encodeListKnownwithIds,file)
file.close()
print("File Saved")