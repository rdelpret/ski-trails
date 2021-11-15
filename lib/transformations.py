import lib.constants

def filter_trails(data, f):

    #TODO take in multiple filters like resort=vail difficulty=black
    # https://stackoverflow.com/questions/36166225/using-the-same-option-multiple-times-in-pythons-argparse/36170308
    '''
    function to handle cli output filtering
    '''
    for x in f:
        fkey, x = x.split("=")

        # Special case to convert from ascii char
        if fkey == "difficulty": 
            x = lib.constants.RATINGS_MAP[x]['sym']
            data = [i for i in data if x.lower() == i[lib.constants.CLI_HEADER.index(fkey)].lower()]
        else:
            data = [i for i in data if x.lower() in i[lib.constants.CLI_HEADER.index(fkey)].lower()]

    return data


def sort_trails(data, skey):
    '''
    function to handle cli output sorting
    '''    

    #default sort
    data.sort(key = lambda x: x[1])
    data.sort(key = lambda x: x[0])

    #TODO sort difficulty in order of green, blue black, terrain park

    # user supplied sort
    if skey: data.sort(key = lambda x: x[lib.constants.CLI_HEADER.index(skey)])
        
    return data