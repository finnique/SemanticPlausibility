import json
import matplotlib.pyplot as plt
import numpy as np

def read_jason(PATH,file_name):
    full_path = PATH + file_name
    with open(full_path, 'r') as JSON:
        json_list = json.load(JSON)

    return json_list

def count_labels(json_list):
    labels = {}
    for i in json_list:
        label = i["label"]

        if label not in labels.keys():
            labels[label] = 1
        else:
            labels[label] += 1

    sorted_labels = dict(sorted(labels.items()))
    return sorted_labels

def count_modifier(json_list):
    modifier_lst = {}
    count_modifier = 0
    for i in json_list:
        value = i["modifier"]

        if value not in modifier_lst.keys():
            modifier_lst[value] = 1
        else:
            modifier_lst[value] += 1

        count_modifier += 1

    print(f'modifier count: {count_modifier}')

    return modifier_lst

def count_nouns(json_list):
    noun_lst = {}
    count_nouns = 0
    for i in json_list:
        value = i["noun"]

        if value not in noun_lst.keys():
            noun_lst[value] = 1
        else:
            noun_lst[value] += 1

        count_nouns += 1

    print(f'noun count: {count_nouns}')
    return noun_lst

# file path
PATH = "datasets/adept/train-dev-test-split/"
files = ["test.json", "train.json", "val.json"]

# count labels for test data
test_data = read_jason(PATH,files[0])
test_labels = count_labels(test_data)
print("Test data:")
print(test_labels)

# count labels for train data
train_data = read_jason(PATH,files[1])
train_labels = count_labels(train_data)
print("Train data:")
print(train_labels)

# count labels for val data
val_data = read_jason(PATH,files[2])
val_labels = count_labels(val_data)
print("Validation data:")
print(val_labels)

train_modifier = count_modifier(train_data)
train_noun = count_nouns(train_data)
print(sorted(train_modifier.items(), key=lambda x:x[1], reverse=True))
print(sorted(train_noun.items(), key=lambda x:x[1], reverse=True))

# plot data
x = ['train', 'test', 'val']

# assign counts from each dataset to corresponding labels
label_0, label_1, label_2, label_3, label_4 = [], [], [], [], []
label_0.extend([train_labels[0], test_labels[0], val_labels[0]])
label_1.extend([train_labels[1], test_labels[1], val_labels[1]])
label_2.extend([train_labels[2], test_labels[2], val_labels[2]])
label_3.extend([train_labels[3], test_labels[3], val_labels[3]])
label_4.extend([train_labels[4], test_labels[4], val_labels[4]])

print(label_0)

# plot bars in stack manner
plt.bar(x, label_0, color='C0')
plt.bar(x, label_1, bottom=np.array(label_0), color='C1')
plt.bar(x, label_2, bottom=np.array(label_0)+np.array(label_1), color='C2')
plt.bar(x, label_3, bottom=np.array(label_0)+np.array(label_1)+np.array(label_2), color='C3')
plt.bar(x, label_4, bottom=np.array(label_0)+np.array(label_1)+np.array(label_2)+np.array(label_3), color='C4')
plt.xlabel("Splits")
plt.ylabel("Labels")
plt.legend(["Impossible", "Less Likely", "Equally Likely", "More Likely", "Necessarily True"])
plt.title("ADEPT: Label distribution across splits")
plt.show()


