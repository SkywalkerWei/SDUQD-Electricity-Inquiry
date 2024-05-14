import ElectricityInquiry

if __name__ == '__main__':
    acc=str(input("校园卡卡号：(6位数字)\n"))
    bui=str(input("宿舍楼：(字母+数字)\n"))
    roo=str(input("房间号：\n"))
    print("该房间剩余电量："+ElectricityInquiry.query(acc, bui, roo)+"元")
    input()