import cv2
import numpy as np
import matplotlib.pyplot as plt
#ham tinh bieu do histogram cua hinh anh
def handle_histogram(img):
    #lay kich thuoc chieu rong va chieu cao cua anh
    h = img.shape[0]
    w = img.shape[1]
    #tao mot ma tran de chua cac gia tri histogram
    before_equal_histogram = np.zeros(256)
    #dung vong lap de dem tan so tich luy cua gia tri mau tai moi pixel
    for i in range(h):
        for j in range(w):
            value_gray_point = img[i, j]
            before_equal_histogram[value_gray_point] += 1
    return before_equal_histogram
#ham so sanh cac pixel cua anh goc va anh tham chieu
def matching_pixel(ori_hist, ref_hist):
  #tinh phan phoi tich luy cua anh goc va anh tham chieu
  ori_cdf = ori_hist.cumsum()
  ref_cdf = ref_hist.cumsum()
  #khoi tao histogram sau khi so khop tu 2 histogram
  hist_matching = np.zeros(256)
  for i in range(len(hist_matching)):
    for j in range(len(hist_matching)):
      if(ref_cdf[j] <= ori_cdf[i]):
        hist_matching[i] = j
  return hist_matching
if __name__ == "__main__":
  #ham imread() dung de doc anh dau vao va anh tham chieu
  ori_img = cv2.imread('input_img_slight.jpg')
  ref_img = cv2.imread('input_img_dark.jpg')
  #chuyen hinh anh mau dau vao thanh anh xam
  gray_ori_img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2GRAY)
  gray_ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)
  #tinh histogram cua anh dau vao va anh tham chieu
  ori_his = handle_histogram(gray_ori_img)
  ref_his = handle_histogram(gray_ref_img)
  #so khop 2 hinh anh
  competi_pixel = matching_pixel(ori_his, ref_his)
  #tu histogram tao nen hinh anh goc
  for i in range(ori_img.shape[0]):
        for j in range(ori_img.shape[1]):
            gray_ori_img[i, j] = competi_pixel[gray_ori_img[i, j]]
  #hien thi hinh anh
  fig, axes = plt.subplots(1, 3)
  #anh goc
  axes[0].imshow(ori_img)
  axes[0].set_title("Original image")
  #anh tham chieu
  axes[1].imshow(ref_img)
  axes[1].set_title("Reference image")
  #anh sau khi xu li
  axes[2].imshow(gray_ori_img)
  axes[2].set_title("Use matching histogram")
  #hien thi figure
  plt.show()