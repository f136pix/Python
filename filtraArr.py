#A função receberá a arr A e o arr B,e irá remover do A tudo o que contém no arr B

def remove_da_lista(arr_a,arr_b):
    arr = []
    for atual in arr_a:
        if(atual not in arr_b):
            arr.append(atual)
        else:
            continue    
    return arr    

