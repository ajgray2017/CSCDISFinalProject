import os
import sys

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def jsonDump(input):
    #! broken
    import json
    with open('dataset.json', 'w') as fp:
        json.dump(input, fp)

def main(filepath):

    dataset = {}
    testDataset = {}
    dataLabels = {}

    print(filepath)

    for root, dir, files in os.walk(os.path.expanduser(filepath)):
        print(files)
        for i in files:
            print(i)
            dataset.update(unpickle(os.path.join(root, i)))

    return dataset

if __name__ == "__main__":
    main(sys.argv[1])