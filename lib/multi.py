import threading

def multiproc(threads):
    '''
    generic fork function
    '''
    for t in threads:
        t.start()
    for t in threads:
        t.join()