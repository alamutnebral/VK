def unid(key):
    unids = {
        'МФТИ' : 297,
        'КФУ' : 527,
        'ВШЭ' : 128,
        'Иннополис' : 1175264,
    }
    return unids[key]

def kfu_facid(key):
    facids = {
        'МЕХМАТ' : 2802,
        'ВМК' : 2886,
        'ЮРФАК' : 2895,
        'ФИЗФАК' : 3066,
        'ПСИХФАК' : 3073
    }
    return facids[key]
