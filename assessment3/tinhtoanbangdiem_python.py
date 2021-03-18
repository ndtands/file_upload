'''
@ class name: BANGDIEM
@ method    : load_dulieu, tinhdiem_trungbinh, luudiem_trungdiem
'''
class BANGDIEM():
    def __init__(self,dir_file):
        self.dir_file=dir_file
    
    def load_dulieu(self):
        with open(self.dir_file,"r") as f:
             content = f.read().splitlines()    #delete \n
        return content
    
    def tinhdiem_trungbinh(self,list_file):
        _monhoc = [x.strip() for x in list_file[0].split(",")][1:]
        _out=dict()
        for i in list_file[1:]:
            temp = i.split(":")
            _out[temp[0].strip()]={}
            diem_all = [x.strip() for x in temp[1].strip().split(";")]
            for i,line in enumerate(diem_all):
                diem = [x.strip() for x in line.split(",")]
                if len(diem)==4:
                    _out[temp[0].strip()][_monhoc[i]]=round(0.05*float(diem[0])+0.1*float(diem[1])+0.15*float(diem[2])+0.7*float(diem[3]),2)
                elif (len(diem)==5):
                    _out[temp[0].strip()][_monhoc[i]]=round(0.05*float(diem[0])+0.1*float(diem[1])+0.1*float(diem[2])+0.15*float(diem[3])+0.6*float(diem[4]),2)
        return _out
            
    def luudiem_trungdiem(self,directory,all_tb):
        _filedir  = directory +"diem_trungbinh.txt"
        _f        = open(_filedir,"w")
        name     = [x for x in all_tb.keys()]
        mon      =  list(all_tb[list(all_tb)[0]])
    
        Line1    ="Ma HS,"+",".join(mon)+"\n"
        _f.write(Line1)
        for name in all_tb:
            list_diem = [str(x) for x in all_tb[name].values()]
            line = name +":"+";".join(list_diem)+"\n"
            _f.write(line)
        _f.close()
        
#DEBUG
#bangdiem =BANGDIEM("diem_chitiet.txt")
#a= bangdiem.load_dulieu()
#b= bangdiem.tinhdiem_trungbinh(a)
#bangdiem.luudiem_trungdiem("",b)

'''
@ class name    : DANHGIA
@ inheritance   : BANGDIEM
@ method        : xeploai_hocsinh, xeploai_thidaihoc_hocsinh
'''
class DANHGIA(BANGDIEM):
    def __init__(self,file_name):
        self.file_name =file_name
        BANGDIEM.__init__(self,file_name)
    
    def xeploai_hocsinh(self,list_file):
        _monhoc = [x.strip() for x in list_file[0].split(",")][1:]
        out=dict()
        for i in list_file[1:]:
            temp = i.split(":")
            name=temp[0].strip()
            out[name]={}
            _dict_temp = {}
            diemtb_all = [(x.strip()) for x in temp[1].strip().split(";")]
            for i,diem in enumerate(diemtb_all):
                _dict_temp[_monhoc[i]]=diem
            tb=0.0
            for mon,diem  in _dict_temp.items():
                if (mon=="Toán" or mon =="Văn" or mon=="Anh"):
                    tb += float(diem)*2.0
                elif (mon=="Lý" or mon =="Hóa" or mon=="Sinh" or mon =="Sử" or mon=="Địa"):
                    tb += float(diem)*1.0
            tb=tb/11.0
            if (tb >9.0):
                if (all(float(x)>8.0 for x in _dict_temp.values())):
                    out[name]="Xuat sac"
                elif (all(float(x)>6.5 for x in _dict_temp.values())):
                    out[name]="Gioi"
                elif (all(float(x)>5.0 for x in _dict_temp.values())):
                    out[name]="Kha"
                elif (all(float(x)>4.5 for x in _dict_temp.values())):
                    out[name]="TB Kha"
                else:
                    out[name]="TB"
            elif (tb>8.0):
                if (all(float(x)>6.5 for x in _dict_temp.values())):
                    out[name]="Gioi"
                elif (all(float(x)>5.0 for x in _dict_temp.values())):
                    out[name]="Kha"
                elif (all(float(x)>4.5 for x in _dict_temp.values())):
                    out[name]="TB Kha"
                else:
                    out[name]="TB"
            elif (tb>6.5):
                if (all(float(x)>5.0 for x in _dict_temp.values())):
                    out[name]="Kha"
                elif (all(float(x)>4.5 for x in _dict_temp.values())):
                    out[name]="TB Kha"
                else:
                    out[name]="TB"
            elif (tb>6.0):
                if (all(float(x)>4.5 for x in _dict_temp.values())):
                    out[name]="TB Kha"
                else:
                    out[name]="TB"
            else:
                out[name]="TB"
        return out

    def xeploai_thidaihoc_hocsinh(self,list_file):
        _monhoc = [x.strip() for x in list_file[0].split(",")][1:]
        out=dict()
        for i in list_file[1:]:
            temp = i.split(":")
            name=temp[0].strip()
            out[name]={}
            _dict_temp = {}
            danhgia=dict()
            diemtb_all = [(x.strip()) for x in temp[1].strip().split(";")]
            for i,diem in enumerate(diemtb_all):
                _dict_temp[_monhoc[i]]=diem
            A  =  float(_dict_temp["Toán"]) + float(_dict_temp["Lý"])   + float(_dict_temp["Hóa"])
            A1 =  float(_dict_temp["Toán"]) + float(_dict_temp["Lý"])   + float(_dict_temp["Anh"])
            B  =  float(_dict_temp["Toán"]) + float(_dict_temp["Sinh"]) + float(_dict_temp["Hóa"])
            C  =  float(_dict_temp["Văn"])  + float(_dict_temp["Sử"])   + float(_dict_temp["Địa"])
            D  =  float(_dict_temp["Toán"]) + float(_dict_temp["Văn"])  + float(_dict_temp["Anh"])*2
            #Khoi A
            danhgia["A"]= 1 if (A >= 24) else 2 if (A <24 or A>=18) else 3 if(A<18 or A>=12) else 4
            #Khoi A1
            danhgia["A1"]= 1 if (A1 >= 24) else 2 if (A1 <24 or A1>=18) else 3 if(A1<18 or A1>=12) else 4
            #Khoi B
            danhgia["B"]= 1 if (B >= 24) else 2 if (B <24 or B>=18) else 3 if(B<18 or B>=12) else 4
            #Khoi C
            danhgia["C"]= 1 if (C >= 21) else 2 if (C <21 or C>=15) else 3 if(C<15 or C>=12) else 4
            #Khoi D
            danhgia["D"]= 1 if (D >= 32) else 2 if (D <32 or D>=24) else 3 if(D<24 or D>=20) else 4
            out[name]=list(danhgia.values())
        return out

#DEBUG
#danhgia = DANHGIA("diem_trungbinh.txt")
#l = danhgia.load_dulieu()
#print(danhgia.xeploai_thidaihoc_hocsinh(l))

'''
@ class name    : TUNHIEN
@ inheritance   : DANHGIA
@ method        : xeploai_thidaihoc_hocsinh dung overiding
'''
class TUNHIEN(DANHGIA):
    def __init__(self,file_name):
        self.file_name =file_name
        DANHGIA.__init__(self,file_name)
    
    def xeploai_thidaihoc_hocsinh(self,list_file):
        _monhoc = [x.strip() for x in list_file[0].split(",")][1:]
        out=dict()
        for i in list_file[1:]:
            temp = i.split(":")
            name=temp[0].strip()
            out[name]={}
            _dict_temp = {}
            danhgia=dict()
            diemtb_all = [(x.strip()) for x in temp[1].strip().split(";")]
            for i,diem in enumerate(diemtb_all):
                _dict_temp[_monhoc[i]]=diem
            A  =  float(_dict_temp["Toán"]) + float(_dict_temp["Lý"])   + float(_dict_temp["Hóa"])
            B  =  float(_dict_temp["Toán"]) + float(_dict_temp["Sinh"]) + float(_dict_temp["Hóa"])
            A1 =  float(_dict_temp["Toán"]) + float(_dict_temp["Lý"])   + float(_dict_temp["Anh"])
            #Khoi A
            danhgia["A"]= 1 if (A >= 24) else 2 if (A <24 or A>=18) else 3 if(A<18 or A>=12) else 4
            #Khoi A1
            danhgia["A1"]= 1 if (A1 >= 24) else 2 if (A1 <24 or A1>=18) else 3 if(A1<18 or A1>=12) else 4
            #Khoi B
            danhgia["B"]= 1 if (B >= 24) else 2 if (B <24 or B>=18) else 3 if(B<18 or B>=12) else 4
            out[name]=list(danhgia.values())
        return out
'''
@ class name    : XAHOI
@ inheritance   : DANHGIA
@ method        : xeploai_thidaihoc_hocsinh dung overiding
'''
class XAHOI(DANHGIA):
    def __init__(self,file_name):
        self.file_name =file_name
        DANHGIA.__init__(self,file_name)
    
    def xeploai_thidaihoc_hocsinh(self,list_file):
        _monhoc = [x.strip() for x in list_file[0].split(",")][1:]
        out=dict()
        for i in list_file[1:]:
            temp = i.split(":")
            name=temp[0].strip()
            out[name]={}
            _dict_temp = {}
            diemtb_all = [(x.strip()) for x in temp[1].strip().split(";")]
            for i,diem in enumerate(diemtb_all):
                _dict_temp[_monhoc[i]]=diem
            C  =  float(_dict_temp["Văn"])  + float(_dict_temp["Sử"])   + float(_dict_temp["Địa"])
            #Khoi C
            danhgia= 1 if (C >= 21) else 2 if (C <21 or C>=15) else 3 if(C<15 or C>=12) else 4
            out[name]=danhgia
        return out

'''
@ class name    : COBAN
@ inheritance   : DANHGIA
@ method        : xeploai_thidaihoc_hocsinh dung overiding
'''
class COBAN(DANHGIA):
    def __init__(self,file_name):
        self.file_name =file_name
        DANHGIA.__init__(self,file_name)
    
    def xeploai_thidaihoc_hocsinh(self,list_file):
        _monhoc = [x.strip() for x in list_file[0].split(",")][1:]
        out=dict()
        for i in list_file[1:]:
            temp = i.split(":")
            name=temp[0].strip()
            out[name]={}
            _dict_temp = {}
            diemtb_all = [(x.strip()) for x in temp[1].strip().split(";")]
            for i,diem in enumerate(diemtb_all):
                _dict_temp[_monhoc[i]]=diem
            D  =  float(_dict_temp["Toán"]) + float(_dict_temp["Văn"])  + float(_dict_temp["Anh"])*2
             #Khoi D
            danhgia= 1 if (D >= 32) else 2 if (D <32 or D>=24) else 3 if(D<24 or D>=20) else 4
            out[name]=danhgia
        return out

'''
@ function name : main
@ input         : diem_chitiet.txt va duong dan output
@ Note          : Luu 2 bang diem "diem_trungbinh.txt" va "diem_chitiet.txt" va "danhgia_hocsinh.txt" 
'''
def main(file_diemchitiet,dir):
    #Luu diem trung binh
    bangdiem    =   BANGDIEM(file_diemchitiet)
    load        =   bangdiem.load_dulieu()
    tinh_tb     =   bangdiem.tinhdiem_trungbinh(load)
    bangdiem.luudiem_trungdiem(dir,tinh_tb)

    #Luu danh gia
    file_diemtrungbinh = dir + "diem_trungbinh.txt"

    danhgia     =   DANHGIA(file_diemtrungbinh)
    load_dg     =   danhgia.load_dulieu()
    xeploai     =   danhgia.xeploai_hocsinh(load_dg)

    tunhien     =   TUNHIEN(file_diemtrungbinh)
    load_tn     =   tunhien.load_dulieu()
    xl_tunhien  =   tunhien.xeploai_thidaihoc_hocsinh(load_tn)

    xahoi       =   XAHOI(file_diemtrungbinh)
    load_xh     =   xahoi.load_dulieu()
    xl_xahoi    =   xahoi.xeploai_thidaihoc_hocsinh(load_xh)

    coban       =   COBAN(file_diemtrungbinh)
    load_cb     =   coban.load_dulieu()
    xl_coban    =   coban.xeploai_thidaihoc_hocsinh(load_cb)
    _filedir    =   dir +"danhgia_hocsinh.txt"
    _f          =   open(_filedir,"w")
    line1       =   ["Ma HS","xeploai_TB chuan","xeploai_A","xeploai_A1","xeploai_B","xeploai_C","xeploai_D"]
    Line1       =   ",".join(line1)+"\n"
    _f.write(Line1)
    for name in xeploai:
        line    = name+";"+xeploai[name]+";"+";".join([str(i) for i in xl_tunhien[name]])\
                +";"+str(xl_xahoi[name])+";"+str(xl_coban[name])+"\n"
        _f.write(line)
    _f.close()



if __name__ == "__main__":
    file_diemchitiet = "diem_chitiet.txt"
    dir              = ""
    main(file_diemchitiet,dir)
    print("Done")