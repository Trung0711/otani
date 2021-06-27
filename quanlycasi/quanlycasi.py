class casi():
    def __init__ (self,ten1,hang1,tuoi1):
        self.ten=ten1
        self.hang=hang1
        self.tuoi=tuoi1
    
    def nhapthongtin(self):
        self.sdt=input('nhập số điện thoại: ')
        self.diachi= input('nhập địa chỉ: ')
        self.giacase=input('nhập giá dịch vụ:  ')
        self.tinhtrnghonnhan=input('Nhập tình trạng hôn nhân nha:  ')
        print(' trong vòng 14 ngày anh chị có : ')
        self.benh=input('có nghi ngờ mình bị covid-19 hay k: ')
        self.tiepxuc=input('Tiếp xúc với bệnh nhân nghi ngờ là F0 hay không: ')
        self.vungdich=input('có đi từ vùng dịch về khopong: ')
        print('trong vòng 14 ngày anh chị có xuất hiện dấu hiệu nào sau đây:')
        self.sot=input('bạn có bị sốt hay không: ')
        self.ho=input('bạn có bị ho hay không: ')
        self.khotho=input('bạn có khó thở hay không: ')
        self.dauhong=input('bạn có đau họng hay không: ')
        self.metmoi=input('bạn có mệt mỏi hay không: ')
        self.benhnen=input('bệnh nền của anh chị là gì nhỉ: ')

        # code mau
        phone_number = input()
        location = "Helo"
        return phone_number, location

    def inrathongtincanhan(self):
        phone1, location1 = self.nhapthongtin()
        print(phone1, location1)
        print(self.ten)
        print(self.tuoi)
        print(self.hang)
        print(self.sdt)
        print(self.diachi)
        print(self.giacase)
        print(self.tinhtrnghonnhan)
        

    

x=input('nhập tên ca sĩ:  ')     
y=input('Nhập hạng của ca sĩ:  ')
z=input('Nhập tuổi của ca sĩ:  ')
a=casi(x,y,z)
a.nhapthongtin()
# a.inrathongtincanhan()
print(a.sdt)

