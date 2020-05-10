import os
import sys

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def jsonDump(input):
    #! broken, bytes input needs to be string
    import json
    with open('dataset.json', 'w') as fp:
        json.dump(input, fp, sort_keys=True)

def getData(dataset):
    """
    Gets data corresponing to animals
    """
    labels, labelNames, data = dataset.get(b"labels"), dataset.get(b"label_names"), dataset.get(b"data")
    cdataset = {}
    count = 0

    for i in labels:
        count += 1
        if str(i) in "234567":
            cdataset.update({labelNames[i].decode("utf-8") +"_"+ str(count): data[count]})

    return cdataset

def main(filepath):
    """
    Built for the CIFAR-10 Dataset, gets all animals out of the dataset
    """
    dataset = {}

    for root, dir, files in os.walk(os.path.expanduser(filepath)):
        for i in files:
            dataset.update(unpickle(os.path.join(root, i)))
    
    dataset = getData(dataset)

    return dataset

if __name__ == "__main__":
    main(sys.argv[1])