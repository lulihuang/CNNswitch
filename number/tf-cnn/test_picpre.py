#encoding:utf-8
import cv2 as cv
import os


def picPre(test_img_fold,test_img_list,out_dir):
    #load image
    img_name_list=[]
    for i in range(len(test_img_list)):
        img_name = test_img_list[i]
        img_path = os.path.join(test_img_fold, img_name)
        image = cv.imread(img_path)
        #grayscale
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        #binary 
        ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#    cv.imshow("OTSU", binary)
        #reverse color
        dst = cv.bitwise_not(binary)
#    cv.imshow("reserve",dst)
        
        cv.imwrite(out_dir+'/'+img_name,dst)
    

test_img_fold = './train_images/9'
test_img_list = os.listdir(test_img_fold)
out_dir = './train_images_after/9'
if not os.path.exists(out_dir):#如果路径不存在
    os.makedirs(out_dir)
print(len(test_img_list))
picPre(test_img_fold, test_img_list,out_dir)




#cv.waitKey()
#cv.destroyAllWindows()

