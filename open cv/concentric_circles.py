import cv2
import numpy as np



def main():
    img=np.zeros((512,512,3),np.uint8)
    cv2.circle(img,(250,250),150,(255,0,0),-1)                                                                                                                               
    cv2.circle(img,(250,250),110,(0,255,0),-1)
    cv2.circle(img,(250,250),70,(0,255,255),-1)
    cv2.imshow("con.circles",img)
    cv2.waitKey(0)
    cv2.destroyWindow("con.circles")
    
                                                                                                                                                                                                                           
    cv2.imwrite("circle.jpg",img)












if __name__=="__main__":
    main()





