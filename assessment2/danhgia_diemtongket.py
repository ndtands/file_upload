'''
Function name: xeploai_hocsinh(dir)

Description: Xếp loại học lực chuẩn của học sinh dựa vào điểm tổng kết trung bình chuẩn.

Input: file điểm trung bình "diem_trungbinh.txt"

Output: trả về 1 dict theo format: {‘Ma HS’: Xep loai}
'''

def xeploai_hocsinh(dir):
    f = open(dir,"r")
    monhoc=[]
    strs={}
    out={}
    for i,line in enumerate(f):
        line =line.lstrip()
        if (i==0):
            monhoc=[x.strip() for x in line.split(',')]
        else:
            pos =line.find(":")
            detail=[x.strip() for x in line[pos+1:].split(";")]
            strs[line[:pos]]={}
            for i in range(0,len(monhoc)-1):
                strs[line[:pos]][monhoc[i+1]]="".join([x.strip() for x in detail[i].split(",")])
    for name in strs:
        tb=0.0;
        for mon,diem in strs[name].items():
            if (mon=="Toán" or mon =="Văn" or mon=="Anh"):
                tb += (float(strs[name][mon])*2.0) 
            elif (mon=="Lý" or mon =="Hóa" or mon=="Sinh" or mon =="Sử" or mon=="Địa"):
                tb += float(strs[name][mon])*1.0
        tb=tb/11.0
        if (tb >9.0):
            if (all(float(x)>8.0 for x in strs[name].values())):
                out[name]="Xuat sac"
            elif (all(float(x)>6.5 for x in strs[name].values())):
                out[name]="Gioi"
            elif (all(float(x)>5.0 for x in strs[name].values())):
                out[name]="Kha"
            elif (all(float(x)>4.5 for x in strs[name].values())):
                out[name]="TB Kha"
            else:
                out[name]="TB"
        elif (tb>8.0):
            if (all(float(x)>6.5 for x in strs[name].values())):
                out[name]="Gioi"
            elif (all(float(x)>5.0 for x in strs[name].values())):
                out[name]="Kha"
            elif (all(float(x)>4.5 for x in strs[name].values())):
                out[name]="TB Kha"
            else:
                out[name]="TB"
        elif (tb>6.5):
            if (all(float(x)>5.0 for x in strs[name].values())):
                out[name]="Kha"
            elif (all(float(x)>4.5 for x in strs[name].values())):
                out[name]="TB Kha"
            else:
                out[name]="TB"
        elif (tb>6.0):
            if (all(float(x)>4.5 for x in strs[name].values())):
                out[name]="TB Kha"
            else:
                out[name]="TB"
        else:
            out[name]="TB"
    f.close()
    return out

#DEBUG
#dir = "diem_trungbinh.txt"
#print(xeploai_hocsinh(dir))

'''
Function name: xeploai_thidaihoc_hocsinh(dir)

Description: Phân loại năng lực các học sinh theo khối thi đại học dựa vào điểm tổng kết trung bình

Input: file điểm trung bình "diem_trungbinh.txt"

Output: trả về 1 dict theo format: {‘Ma HS: [Xep loai]}
'''
def xeploai_thidaihoc_hocsinh(dir):
    f = open(dir,"r")
    monhoc=[]
    strs={}
    danhgia={}
    out={}
    for i,line in enumerate(f):
        line =line.lstrip()
        if (i==0):
            monhoc=[x.strip() for x in line.split(',')]
        else:
            pos =line.find(":")
            detail=[x.strip() for x in line[pos+1:].split(";")]
            strs[line[:pos]]={}
            for i in range(0,len(monhoc)-1):
                strs[line[:pos]][monhoc[i+1]]="".join([x.strip() for x in detail[i].split(",")])
    for name in strs:
        A  =  float(strs[name]["Toán"]) + float(strs[name]["Lý"])   + float(strs[name]["Hóa"])
        A1 =  float(strs[name]["Toán"]) + float(strs[name]["Lý"])   + float(strs[name]["Anh"])
        B  =  float(strs[name]["Toán"]) + float(strs[name]["Sinh"]) + float(strs[name]["Hóa"])
        C  =  float(strs[name]["Văn"])  + float(strs[name]["Sử"])   + float(strs[name]["Địa"])
        D  =  float(strs[name]["Toán"]) + float(strs[name]["Văn"])  + float(strs[name]["Anh"])*2
        #Khoi A
        danhgia["A"]= 1 if (A >= 24) else 2 if (A <24 or A>=18) else 3 if(A<18 or A>=12) else 4
        #Khoi A1
        danhgia["A1"]= 1 if (A1 >= 24) else 2 if (A1 <24 or A1>=18) else 3 if(A1<18 or A1>=12) else 4
        #Khoi B
        danhgia["B"]= 1 if (B >= 24) else 2 if (B <24 or B>=18) else 3 if(B<18 or B>=12) else 4
        #Khoi C
        danhgia["C"]= 1 if (C >= 21) else 2 if (C <21 or C>=15) else 3 if(C<15 or C>=12) else 4
        #Khoi D
        danhgia["D"]= 1 if (D >= 32) else 2 if (D <32 or D>=24) else 3 if(D<24 or A>=20) else 4

        out[name]=list(danhgia.values())
    f.close()
    return out
#DEBUG
#dir = "diem_trungbinh.txt"
#print(xeploai_thidaihoc_hocsinh(dir))

'''
Function name: main(dir)

Description: Khai báo đường dẫn input cho file “diem_ trungbinh.txt” và output cho file “danhgia_hocsinh_txt”, thực thi 2 hàm ở trên và lưu kết quả vào file “danhgia_hocsinh_txt”.

Input: file điểm trung bình "diem_trungbinh.txt"

Output: Lưu file txt đúng format: Hàng đầu tiên của file “danhgia_hocsinh_txt” gồm các trường: “Ma HS”, “xeploai_TB chuan”, “xeploai_A”, “xeploai_A1”, “xeploai_B ”, “xeploai_C”, xeploai_D”. Hàng thứ 2 theo VD sau: “Nguyen Hai Nam; Gioi; 1; 1; 1; 3; 2”.
'''
def main(dir,direct):
    xeploai         = xeploai_hocsinh(dir)
    xeploai_daihoc  = xeploai_thidaihoc_hocsinh(dir)
    _filedir        = direct +"danhgia_hocsinh.txt"
    _f              = open(_filedir,"w")
    line1 = ["Ma HS","xeploai_TB chuan","xeploai_A","xeploai_A1","xeploai_B","xeploai_C","xeploai_D"]
    Line1    ="Ma HS,"+",".join(line1)+"\n"
    _f.write(Line1)
    for name in xeploai:
        line = name+";"+xeploai[name]+";"+";".join([str(int) for int in xeploai_daihoc[name]])+"\n"
        _f.write(line)
    _f.close()

if __name__ == "__main__":
    file_trungbinh   = "diem_trungbinh.txt"
    dir              = ""
    main(file_trungbinh,dir)
    print("Done")