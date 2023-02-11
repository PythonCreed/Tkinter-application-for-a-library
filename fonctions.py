import pickle

def import_data(b):
    file = open(b,'rb')
    return pickle.load(file)
    file.close()

def export_data(a,b):
    file = open(b,'wb')
    pickle.dump(a,file)
    file.close()