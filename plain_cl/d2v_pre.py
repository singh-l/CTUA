import pandas as pd
from sklearn import preprocessing
def d2v_pre(path):
    data = pd.read_csv(path)
    label_encoding = preprocessing.LabelEncoder()
    data['class'] = label_encoding.fit_transform(data['class'].astype(str))
    data.to_csv(path[:len(path)-4]+'_doc2vec.csv')