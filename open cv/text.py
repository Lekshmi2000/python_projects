import cv2
import numpy as np



def main():
    img=np.zeros((512,512,3),np.uint8)
    img[np.where((img==[0,0,0]).all(axis=2))]=[0,255,255]
    cv2.putText(img,"''THANK YOU''",(50,250),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),10)
    cv2.imshow("word",img)
    cv2.waitKey(0)
    cv2.destroyWindow("word")
    cv2.imwrite("word.jpg",img)






















if __name__=="__main__":
    main()
