import statistics as sta
#Function mean() - ham gia tri trung binh cong
def func_mean():
    #Khoi tao tap du lieu voi kieu du lieu: int (integer)
    data = [2,5, 7, 3, 9]
    #Khoi tao mot bien chua gia tri trung binh
    mean = sta.mean(data)
    #in gia tri ra man hinh
    print("Mean = ", mean)
    #kieu du lieu cua ket qua tra ve tu ham mean()
    print("Kieu du lieu cua Mean: " ,type(mean))
func_mean()
#function fmean() - ham gia tri trung binh cong co trong so
def func_fmean():
    ''' Khoi tao bo du lieu:
    - Diem qua trinh 1
    - Diem qua trinh 2
    - Diem giua ky
    - Diem cuoi ky
    '''
    data = [10, 7, 8.3, 7.5]
    #Khoi tao bien chua 4 trong so: 10%, 20%, 20%, 50%
    weights = [0.1, 0.2, 0.2, 0.5]
    #khoi tao bien chua gia tri trung binh tu ham fmean()
    fmean = sta.fmean(data, weights)
    #in gia tri ra man hinh 
    print("Gia tri fmean = " ,fmean)
    #kieu du lieu cua gia tri trung binh 
    print("Kieu du lieu cua fmean: " ,type(fmean))
    '''so sanh:
    fmean(data)
    fmean(data, weights = None)
     mean(data)
    '''
    print("Fmean(weights = None) = " ,sta.fmean(data, weights=None))
    print("Fmean (khong set weights) = ", sta.fmean(data))
    print("Mean = " ,sta.mean(data))
    #ket qua ca 3 ham deu nhu nhau
func_fmean()
#function geometric_mean() - ham gia tri trung binh nhan
def func_geometric_mean():
    #khoi tao bo so lieu
    data = [2, 18, 9, 23, 10]
    #khoi tao bien chua gia tri trung binh nhan
    result = sta.geometric_mean(data)
    #in ket qua ra man hinh
    print("Gia tri trung binh = ", result)
    #lam tron so bang ham round(so can lam tron, chu so thap phan muon lam tron)
    print("Gia tri trung binh lam tron = ",round(result, 4))
func_geometric_mean()
#function harmonic_mean() - ham gia tri trung binh deu hoa
def func_harmonic_mean():
    #khoi tao bo so lieu
    data = [3, 2, 12, 18, 25]
    #khoi tao bo trong so
    weights = [1, 2, 3, 1, 1]
    #in gia tri trung binh dieu hoa voi trong so
    print("Gia tri trung binh dieu hoa co trong so = " ,sta.harmonic_mean(data, weights))
    #in gia tri trung binh dieu hoa khong co trong so
    print("Gia tri trung binh dieu hoa khong co trong so = ", sta.harmonic_mean(data, weights=None))
func_harmonic_mean()
#function median() - ham gia tri trung vi
def func_median():
    #khoi tao bo so lieu voi so luong le
    data_odd = [1, 3, 5]
    #khoi tao bo so lieu voi so luong chan
    data_even = [1, 3, 5, 7]
    #median cua bo so lieu co so luong le
    print("Median voi bo so lieu le = ", sta.median(data_odd))
    #median cua bo so lieu co so luong chan
    print("Median voi bo so lieu chan = ",sta.median(data_even))
func_median()
#function median_low() - ham gia tri trung vi thap
def func_median_low():
    #khoi tao bo so lieu voi so luong chan
    data_even = [1, 3, 5, 7]
    #median cua bo so lieu voi so luong chan
    print("Median voi bo so lieu chan = ",sta.median(data_even))
    #median_low cua bo so lieu voi so luong chan
    print("Median_low voi bo so lieu chan = ",sta.median_low(data_even))
func_median_low()
#function median_high() - ham gia tri trung binh thap
def func_median_high():
    #khoi tao bo so lieu co so luong chan
    data_even = [1, 3, 5, 7]
    #median cua bo so lieu voi so luong chan
    print("Median voi bo so lieu chan = ",sta.median(data_even))
    #median_high cua bo so lieu voi so luong chan
    print("Median_high voi bo so lieu chan = ",sta.median_high(data_even))
func_median_high()
#function median_grouped() - ham tinh trung vi cho du lieu lien tuc
def func_median_grouped():
    #khoi tao bo so lieu
    data = [2, 4, 4, 5, 11]
    #median_grouped voi default interval
    print("Median_grouped voi default interval = ",sta.median_grouped(data))
    #median_grouped voi interval = 2
    print("Median_grouped voi interval tham so = ",sta.median_grouped(data, 2))
func_median_grouped()
#function mode() - ham tinh yeu vi
def func_mode():
    #khoi tao bo du lieu so
    numbers_data = [2, 4, 4, 5, 5, 5, 23, 23, 23, 23, 23, 51]
    #khoi tao bo du lieu chu
    strings_data = ["trang", "mai", "mai", "ruoc"]
    #in ket qua ra man hinh
    print("Mode cua du lieu so = " ,sta.mode(numbers_data))
    print("Mode cua du lieu chu = " ,sta.mode(strings_data))
func_mode()
#function multimode() - ham tinh dong yeu vi
def func_multimode():
    #khoi tao bo so lieu
    data = [1, 1, 2, 2, 3, 6, 8, 8]
    #in ket qua ra man hinh
    print("Mode cua bo so lieu = ", sta.mode(data))
    print("Multimode cua bo so lieu = ", sta.multimode(data))
func_multimode()
#function quantiles() - tu phan vi cua bo so lieu
def func_quantiles():
    #khoi tao bo so lieu
    data = [10, 20, 30, 40, 50]
    #in cac gia tri tai cac diem cat
    print("Gia tri tai cac diem cat: ", sta.quantiles(data, n = 3))
func_quantiles()
#function stdev() - Do lech chuan cua khong gian mau
def func_standard_deviation():
    #khoi tao bo so lieu
    data = [18, 2, 4, 25, 12, 3]
    #in gia tri ra man hinh
    print("Do lech chuan voi mean la tham so = ", sta.stdev(data, 10))
    print("Do lech chuan voi default mean = ", sta.stdev(data))
    print("Do lech chuan voi set None mean = ", sta.stdev(data, xbar = None))
func_standard_deviation()
#function variance() - Phuong sai cua khong gian mau
def func_variance():
    #khoi tao bo so lieu
    data = [18, 2, 4, 25, 12, 3]
    #in ket qua ra man hinh
    print("Phuong sai voi mean la tham so = ", sta.variance(data, 10))
    print("Phuong sai voi default mean = ", sta.variance(data))
    print("Phuong sai (xbar = None) = ", sta.variance(data, xbar = None))
func_variance()
#function pstdev() - Do lech chuan cua tong the
def func_pstdev():
    #khoi tao bo so lieu
    data = [1.8, 2.0, 2.0, 2.5, 1.2, 2.03]
    #in ket qua ra man hinh
    print("Do lech chuan voi mean la tham so = ", sta.pstdev(data, 2))
    print("Do lech chuan voi default mean = ", sta.pstdev(data))
    print("Do lech chuan (mu = None) = ", sta.pstdev(data, mu = None))
func_pstdev()
#function pvariance() - phuong sai cua tong the
def func_pvariance():
    #khoi tao bo du lieu
    data = [1.8, 2.0, 2.0, 2.5, 1.2, 2.03]
    #in ket qua ra man hinh
    print("Phuong sai voi mean la tham so = ", sta.pvariance(data, 2))
    print("Phuong sai voi default mean = ", sta.pvariance(data))
    print("Phuong sai (mu = None) = ", sta.pvariance(data, mu = None))
#function covariance() - hiep phuong sai
def func_covariance():
    #khoi tao bo so lieu x va y
    x = [2, 4, 8, 10, 14, 16]
    y = [1, 3, 6, 9, 10, 12]
    #in ket qua ra man hinh
    print("Hiep phuong sai cua x va y = ", sta.correlation(x, y))
func_covariance()
#function correlation() - He so tuong quan Pearson
def func_correlation():
    #khoi tao bo so lieu x va y
    x = [2, 4, 8, 10, 14, 16]
    y = [1, 3, 6, 9, 10, 12]
    #Khoi tao bien chua hiep phuong sai cua x va y
    cov_x_y = sta.covariance(x, y)
    #khoi tao bien chua do lech chuan cua x va y
    sigma_x = sta.stdev(x)
    sigma_y = sta.stdev(y)
    #khoi tao bien chua he so tuong quan Peason theo cong thuc toan hoc
    pearson_x_y = cov_x_y/(sigma_x*sigma_y)
    #khoi tao bien tinh he so quan he theo ham co san
    func_pearson_x_y = sta.correlation(x, y)
    #in ket qua ra man hinh
    print("He so tuong quan theo cong thuc: ", pearson_x_y)
    print("He so tuong quan theo ham co san: ", func_pearson_x_y)
func_correlation()
#function linear_regression() - do doc va do bu cua so lieu
def func_linear_regression():
    #tao hai mang cac gia tri cua x va y
    x = [10, 11, 12, 13, 14]
    y = [15, 16, 17, 18, 19]
    #tinh do dong va do bu cua duong hoi quy tuyen tinh tren x va y
    slope, intercept = sta.linear_regression(x, y, proportional=False)
    slope1, intercept1 = sta.linear_regression(x, y, proportional=True)
    #in ket qua ra man hinh
    print("do bu va do doc khong dua vao ti le pham vi du lieu = ", slope, intercept)
    print("do bu va do doc phu thuoc vao ti le pham vi du lieu = ", slope1, intercept1)
func_linear_regression()
#function NormalDist() - tao ra doi tuong co du lieu phan phoi chuan
def func_normal_dist():
    #Khoi tao bien chua doi tuong co phan phoi chuan
    #voi mu = 100, sigma = 15
    dist = sta.NormalDist(100, 15)
    #in ra cac thuoc tinh cua doi tuong
    print("Gia tri trung binh = ",dist.mean)
    print("Gia tri trung vi = ", dist.median)
    print("Gia tri yeu vi = ", dist.mode)
    print("Gia tri do lech chuan = ", dist.stdev)
    print("Gia tri phuong sai = " ,dist.variance)
    '''du lieu tu ki thi DGNL 2022 cua DHQGHN
    diem trung binh ~ 80, do lech chuan ~ 14 voi thang 150'''
    #khoi tao doi tuong voi phan phoi chuan
    DGNL = sta.NormalDist(80, 14)
    '''ti le % thi sinh co diem o khoang (90-100)
    ham cdf(): tinh xac suat cua bien ngau nhien nam trong khoang xac dinh
    '''
    fraction = DGNL.cdf(100 + 0.5) - DGNL.cdf(90 - 0.5)
    print("Ty le thi sinh co diem nam trong khoang (90-100) = ",round(fraction*100.0, 1))
    #theo DHQGHN: co khoang ~17.5% thi sinh co diem trong khoang 90-100
func_normal_dist()
#function from_samples() - tao ra cac gia tri phan phoi chuan dua tren du lieu ngau nhien
def func_from_samples():
    #khoi tao
    data = [5, 6, 7, 8, 9, 10]
    #tao bien chua doi tuong phan phoi chuan
    normal_distribution = sta.NormalDist.from_samples(data)
    #in ket qua mu, sigma cua phan phoi chuan ra man hinh
    print(normal_distribution)
func_from_samples()