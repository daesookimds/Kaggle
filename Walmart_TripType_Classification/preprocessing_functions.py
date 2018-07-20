def desc_tagger(dic, value):
    '''
    DepartmentDescription get number tag 1~68
    For using desc_tagger must execute 'from functools import partial'
    '''
    return dic.get(value)


def upc_91011_to_12(x):
    '''
    convert 9, 10, 11 length of Upc to 12 length of Upc
    '''
    length = len(x)
    if length == 11:
        return '000'+x
    elif length == 12:
        return '00'+x
    elif length == 13:
        return '0'+x
    elif length == 14:
        return x
    else:
        return x


def upc_78_to_12(x):
    '''
    convert 7, 8 length of Upc to 12 length of Upc
    '''
    if len(x) == 9:
        x = '0'+x
        x = list(x)
        if x[6] == '0':
            return '0'+x[1]+x[2]+x[6]+'0000'+x[3]+x[4]+x[5]+x[7]
        elif x[6] == '1':
            return '0'+x[1]+x[2]+x[6]+'0000'+x[3]+x[4]+x[5]+x[7]
        elif x[6] == '2':
            return '0'+x[1]+x[2]+x[6]+'0000'+x[3]+x[4]+x[5]+x[7]
        elif x[6] == '3':
            return '0'+x[1]+x[2]+x[3]+'00000'+x[4]+x[5]+x[7]
        elif x[6] == '4':
            return '0'+x[1]+x[2]+x[3]+x[4]+'00000'+x[5]+x[7]
        else:
            return '0'+x[1]+x[2]+x[3]+x[4]+x[5]+'0000'+x[6]+x[7]
    elif len(x) == 10:
        x = list(x)
        if x[6] == '0':
            return '0'+x[1]+x[2]+x[6]+'0000'+x[3]+x[4]+x[5]+x[7]
        elif x[6] == '1':
            return '0'+x[1]+x[2]+x[6]+'0000'+x[3]+x[4]+x[5]+x[7]
        elif x[6] == '2':
            return '0'+x[1]+x[2]+x[6]+'0000'+x[3]+x[4]+x[5]+x[7]
        elif x[6] == '3':
            return '0'+x[1]+x[2]+x[3]+'00000'+x[4]+x[5]+x[7]
        elif x[6] == '4':
            return '0'+x[1]+x[2]+x[3]+x[4]+'00000'+x[5]+x[7]
        else:
            return '0'+x[1]+x[2]+x[3]+x[4]+x[5]+'0000'+x[6]+x[7]
    else:
        return x


def upc_345_to_10(x):
    '''
    convert 3, 4, 5 length of Upc to 10 length of Upc
    '''
    if len(x) == 5:
        x = '00'+x
        return '00002'+x
    elif len(x) == 6:
        x = list(x)
        if x[0] == '3':
            return '00001'+'0'+x[0]+x[1]+x[2]+x[3]
        elif x[0] == '4':
            return '00001'+'0'+x[0]+x[1]+x[2]+x[3]
        else:
            return '00002'+'0'+x[0]+x[1]+x[2]+x[3]
    elif len(x) == 7:
        x = list(x)
        if x[0] == '5':
            return '00002'+'5'+x[1]+x[2]+x[3]+x[4]
        elif x[0] == '8':
            return '00003'+'8'+x[1]+x[2]+x[3]+x[4]
        elif x[0] == '9':
            return '00001'+'9'+x[1]+x[2]+x[3]+x[4]
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
