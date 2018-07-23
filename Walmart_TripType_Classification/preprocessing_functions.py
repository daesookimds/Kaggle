def desc_tagger(dic, value):
    '''
    DepartmentDescription get number tag 1~68
    For using desc_tagger must execute 'from functools import partial'
    '''
    return dic.get(value)


def upc_3456_to_10(x):
    '''
    convert 3, 4, 5 length of Upc to 10 length of Upc
    '''
    if len(x) == 5:
        x = '00'+x
        x = list(x)
        return '00002'+ x[0]+x[1]+x[2]+x[3]+x[4]
    elif len(x) == 6:
        x = list(x)
        if x[0] == '3':
            return '00004'+'0'+x[0]+x[1]+x[2]+x[3]
        elif x[0] == '4':
            return '00004'+'0'+x[0]+x[1]+x[2]+x[3]
        else:
            return '00002'+'0'+x[0]+x[1]+x[2]+x[3]
    elif len(x) == 7:
        x = list(x)
        if x[0] == '5':
            return '00002'+'5'+x[1]+x[2]+x[3]+x[4]
        elif x[0] == '8':
            return '00003'+'8'+x[1]+x[2]+x[3]+x[4]
        elif x[0] == '9':
            return '00004'+'9'+x[1]+x[2]+x[3]+x[4]
    elif len(x) == 8:
        x = list(x)
        return '0000'+x[0]+x[1]+x[2]+x[3]+x[4]+x[5]
    else:
        return x


def upc_789101112_to_10(x):
    '''
    convert 7~12 lengtho of Upc to 10 length of Upc
    '''
    length = len(x)
    if length == 9:
        x = '000'+x
        x = list(x)
        return x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]
    elif length == 10:
        x = '00'+x
        x = list(x)
        return x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]
    elif length == 11:
        x = '0'+x
        x = list(x)
        return x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]
    elif length == 12:
        x = list(x)
        return x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]
    elif length == 13:
        x = list(x)
        return x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]+x[10]
    elif length == 14:
        x = list(x)
        return x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]
    else:
        return x


def company_part_Upc(x):
    '''
    make company part of Upc
    '''
    if len(x) == 14:
        return "".join(list(x)[1:6])
    elif len(x) == 10:
        return "".join(list(x)[0:5])


def product_part_Upc(x):
    '''
    make product part of Upc
    '''
    if len(x) == 14:
        return "".join(list(x)[6:11])
    elif len(x) == 10:
        return "".join(list(x)[5:10])
