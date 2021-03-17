'''
Function name: tinhdiem_trungbinh(file)

Description: Tính toán điểm trung bình của sinh viên theo từng môn học

Input: file diem_chitiet.txt tự định nghĩa theo yêu cầu

Output: Đúng format sau : {‘Nguyen Hai Nam’: {‘Toan’: 9.00; ‘Ly’: 8.55, …}, ‘Ha Thi Hoa’: {…‘Su’: 9.00; ‘Dia’: 8.55}

Note: Làm tròn 2 chữ số
'''
def tinhdiem_trungbinh(file):
    _load = open(file,"r")
    _strs=dict()
    _monhoc=[]
    _out=dict()
    for i,line in enumerate(_load):
        line =line.lstrip()
        if(i==0):
            monhoc=[x.strip() for x in line.split(',')]
        else:
            pos =line.find(":")
            detail=[x.strip() for x in line[pos+1:].split(";")]
            _strs[line[:pos]]={}
            for i in range(0,len(monhoc)-1):
                _strs[line[:pos]][monhoc[i+1]]=[x.strip() for x in detail[i].split(",")]
    for name in _strs:
        _out[name]={}
        for i in _strs[name]:
            diem=_strs[name][i]
            if (len(_strs[name][i])==4):
                _out[name][i]=round(0.05*float(diem[0])+0.1*float(diem[1])+0.15*float(diem[2])+0.7*float(diem[3]),2)
            elif (len(_strs[name][i])==5):
                _out[name][i]=round(0.05*float(diem[0])+0.1*float(diem[1])+0.1*float(diem[2])+0.15*float(diem[3])+0.6*float(diem[4]),2)
    _load.close()
    return _out

#DEBUG
#file_diemchitiet = "diem_chitiet.txt"
#print(tinhdiem_trungbinh(file_diemchitiet))


'''
Function name: luudiem_trungbinh(directory,all_tb)

Description: Lưu điểm trung bình ra 1 file có tên là "diem_trungbinh.txt" theo đường dẫn có sẵn

Input: đường dẫn cho thư mục để lưu và dict của điểm đã tính ở function trên

Output: Lưu file đúng format đã yêu cầu
'''
def luudiem_trungbinh(directory,all_tb):
    _filedir  = directory +"diem_trungbinh.txt"
    _f        = open(_filedir,"w")
    mon      =  list(all_tb[list(all_tb)[0]])
    Line1    ="Ma HS,"+",".join(mon)+"\n"
    _f.write(Line1)
    for name in all_tb:
        list_diem = [str(x) for x in all_tb[name].values()]
        line = name +":"+";".join(list_diem)+"\n"
        _f.write(line)
    _f.close()


#DEBUG
#file_diemchitiet = "diem_chitiet.txt"
#dir              = ""
#luudiem_trungbinh(dir,tinhdiem_trungbinh(file_diemchitiet))

'''
Function name: main(file_diem,dir_tb)

Input: đường dẫn của file diem_chitiet.txt và khai báo đường ra của file diem_trungbinh.txt.

Output: Thực hiện hai nhiệm vụ ở trên.
'''

def main(file_diem,dir_tb):
    luudiem_trungbinh(dir_tb,tinhdiem_trungbinh(file_diem))

if __name__ == "__main__":
    file_diemchitiet = "diem_chitiet.txt"
    dir              = ""
    main(file_diemchitiet,dir)
    print("Done")