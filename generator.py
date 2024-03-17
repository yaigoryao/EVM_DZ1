def cond_table(n):
    num = n;
    i = num;
    digits = 0;
    while i > 0:
        i//=2;
        digits+=1;
    _cur = "";
    _next = "";
    _func = "";
    print("N  |Исход.сост.|След. сост.|Функ. пер.")
    print("пп |  | | | |  |  | | | |  |  | | | | ")
    print("===+==|=|=|=|==+==|=|=|=|==+==|=|=|=|=")
    for i in range(0, num):
        _cur = f'{i:05b}';
        _next = f'{(i+1):05b}';
        _func = "";
        for j in range(len(_cur)):
            if(_cur[j] == _next[j]): _func+=_cur[j];
            elif (_cur[j] == '0' and _next[j] == '1'): _func += "Δ";
            else: _func += "∇";
        _p="";
        if(i < 10): _p = " ";
        print(i,_p+"|", "|".join(list(_cur)),"|", "|".join(list(_next)),"|", "|".join(list(_func)));
    
    _func = "";
    for c in _next:
        if(c == "1"): _func+="∇";
        else: _func+="0";
    print(num,"|", "|".join(list(_next)), "|", "|".join(list("0"*digits)),"|", "|".join(list(_func)));

def carno(n):
    num = n;
    i = num;
    digits = 0;
    while i > 0:
        i//=2;
        digits+=1;
    _cur = "";
    _next = "";
    _func = "";
   
    carno = dict();
    for i in range(0, 2**digits):
        carno[f'{i:05b}'] = list("X"*5);
    
    for i in range(0, num):
        _cur = f'{i:05b}';
        _next = f'{(i+1):05b}';
        _func = "";
        for j in range(len(_cur)):
            if(_cur[j] == _next[j]): _func+=_cur[j];
            elif (_cur[j] == '0' and _next[j] == '1'): _func += "Δ";
            else: _func += "∇";
        for j in range(len(_func)):
            carno[_cur][j] = _func[j];
        #print(i, _cur, _next, _func);
    
    _func = "";
    for c in _next:
        if(c == "1"): _func+="∇";
        else: _func+="0";
    for j in range(len(_func)):
        carno[_next][j] = _func[j];
    cols = ["000", "001", "011", "010", "110", "111", "101", "100"]
    rows = ["00", "01", "11", "10"];
    
    chrs = "EDCBA";
    for i in range(digits):
        print("=========================================");
        print(f"F {chrs[i]}", end="\n\n")
        print("EDC", end=" ");
        for col in cols: 
            print(col, end=" ");
        print();
        print("BA")
        c = 0;
        for row in rows:
            print(rows[c], end=" ");
            for col in cols:
                print("{:>3}".format(carno[col+row][i]), end=" ")
            print();
            c+=1;
        print("=========================================");
        
        # print();
        # print();
        # print();

# carno(26);

def jk(n, t):
    num = n;
    i = num;
    digits = 0;
    while i > 0:
        i//=2;
        digits+=1;
    _cur = "";
    _next = "";
    _func = "";
   
    carno = dict();
    for i in range(0, 2**digits):
        carno[f'{i:05b}'] = list("X"*5);
    
    for i in range(0, num):
        _cur = f'{i:05b}';
        _next = f'{(i+1):05b}';
        _func = "";
        for j in range(len(_cur)):
            if(_cur[j] == _next[j]): _func+=_cur[j];
            elif (_cur[j] == '0' and _next[j] == '1'): _func += "Δ";
            else: _func += "∇";
        for j in range(len(_func)):
            carno[_cur][j] = _func[j];
        #print(i, _cur, _next, _func);
    
    _func = "";
    for c in _next:
        if(c == "1"): _func+="∇";
        else: _func+="0";
    for j in range(len(_func)):
        carno[_next][j] = _func[j];
    cols = ["000", "001", "011", "010", "110", "111", "101", "100"]
    rows = ["00", "01", "11", "10"];
    
    transitions = {"J": {"0": "0", "1": "X", "Δ": "1", "∇": "X", "X": "X"},
                   "K": {"0": "X", "1": "0", "Δ": "X", "∇": "1", "X": "X"}}; #для J и K
    for i in range(digits):
        print("=========================================");
        print(f"{t}{i+1}", end="\n\n")
        print("EDC", end=" ");
        for col in cols: 
            print(col, end=" ");
        print();
        print("BA")
        c = 0;
        for row in rows:
            print(rows[c], end=" ");
            for col in cols:
                print("{:>3}".format(transitions[t][carno[col+row][i]]), end=" ")
            print();
            c+=1;
        print("=========================================");

num = 26;

cond_table(26);
carno(num)
jk(num, "J");
jk(num, "K");
    #print(num, _next, "0"*digits, _func);
# num = 27;
# i = num;
# digits = 0;
# while i > 0:
#     i//=2;
#     digits+=1;
# _cur = "";
# _next = "";
# _func = "";
# print("N  | Тек   | След  | Функ")
# print("===+=======+=======+======")
# for i in range(0, num):
#     _cur = f'{i:05b}';
#     _next = f'{(i+1):05b}';
#     _func = "";
#     for j in range(len(_cur)):
#         if(_cur[j] == _next[j]): _func+=_cur[j];
#         elif (_cur[j] == '0' and _next[j] == '1'): _func += "Δ";
#         else: _func += "∇";
#     #print(i, " |", _cur, "|", _next,"|", _func);
#     print(";".join(list(_func)));
    
# _func = "";
# for c in _next:
#     if(c == "1"): _func+="∇";
#     else: _func+="0";
# print(num+1, " |", _next, "|", "0"*digits, "|", _func);