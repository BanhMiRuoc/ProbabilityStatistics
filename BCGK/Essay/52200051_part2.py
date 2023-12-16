import numpy as np
import cv2
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
#ham can bang bieu do histogram
def equal_histogram(img, histogram):
    #lay kich thuoc chieu rong va chieu cao cua anh
    h = img.shape[0]
    w = img.shape[1]
    #tao mot ma tran de chua cac gia tri sau khi can bang
    after_equal_histogram = np.zeros(257)
    #dung vong lap de chay tu 0->255 de tinh tong so xuat hien cua gia tri
    for i in range(0, len(after_equal_histogram)):
        after_equal_histogram[i] = sum(histogram[:i])
    #loai bo cac phan tu co gia tri mau = 0, do cac gia tri nay khong can can bang
    after_equal_histogram = after_equal_histogram[1:]
    #tinh gia tri mau toi da va toi thieu
    max_value = max(after_equal_histogram)
    min_value = min(after_equal_histogram)
    #tinh toan de can bang gia tri mau
    new_histogram = [int(((f-min_value)/(max_value-min_value))*255) for f in after_equal_histogram]
    #dung vong lap de tao ra hinh anh voi cac gia tri mau da duoc can bang
    for i in range(h):
        for j in range(w):
            img[i, j] = new_histogram[img[i, j]]
    return img
def print_histogram(img, histogram, name_pic, name_his):
    #tao khung anh chua hinh anh va histogram cua chung
    fig = plt.figure()
    #chia cot va dong 
    plt.subplot(122)
    #dan hinh anh hien thi len khung anh (goc phai)
    plt.imshow(img)
    #dat ten cho hinh anh
    plt.title(name_pic)
    plt.subplot(121)
    #dan luoc do hien thi len khung anh (goc trai)
    plt.plot(histogram)
    #dat ten cho luoc do
    plt.title(name_his)
    #hien thi khung anh
    plt.show()
if __name__ == "__main__":
    #ham imread() dung de doc anh mau
    img = cv2.imread("input_img.jpg")
    #in hinh anh va histogram cua chung
    # print_histogram(img, handle_histogram(img), "Original image", "Histogram of original image")
    #tu anh mau, chuyen thanh anh mau xam bang cach dung ham convertColor(hinh anh, bgr to gray)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #luu anh vua chuyen doi vao tep hinh anh
    cv2.imwrite("gray_img.jpg", gray_img)
    #in hinh anh muc xam va histogram cua chung
    # print_histogram(gray_img, handle_histogram(gray_img), "Gray image", "Histogram of gray image before processing")
    #tao bien luu tru bieu do histogram cua hinh xam
    gray_histogram = handle_histogram(gray_img)
    #tao histogram moi chua gia tri da can bang cua histogram truoc do
    new_histogram = equal_histogram(gray_img, gray_histogram)
    #tu gia tri vua can bang, tao thanh 1 anh moi
    cv2.imwrite("output.jpg", new_histogram)
    new_img = cv2.imread("output.jpg")
    #in hinh anh da qua xu ly va histogram can bang
    print_histogram(new_img, new_histogram[2], "Image after processing", "Histogram after processing")
    