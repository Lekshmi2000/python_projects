import cv2
def main():
   cap=cv2.VideoCapture("cheetah.mp4")
   if cap.isOpened()==False:
       print("error reading the video")
#else:
   count=0   
   while(cap.isOpened()):
        check,img=cap.read()
        if(check==True):
            cv2.imshow("frames",img)
            count=count+1
            cv2.imwrite(".\\images\\{}.jpg".format(count),img)
            cv2.waitKey(1)
            cv2.destroyWindow('frames')
        else:
            break
   print(count)     
   cap.release()            
                
    
   
