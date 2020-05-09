import os

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def open(filepath):

    dataset = {}
    testDataset = {}
    dataLabels = {}

    for root, dir, files in os.walk(os.path.expanduser(filepath)):
        for i in files:
            dataset.update(unpickle(os.path.join(root, i)))

    return dataset

if __name__ == "__main__":
    open()