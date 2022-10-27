from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

from sklearn import preprocessing

def label_featurization():
    lbl_enc = preprocessing.LabelEncoder()
    return lbl_enc.fit(["Affirm", "Reverse"])

arguments = [
    Args(),
]

exo_label_featurization = ExerciseFunction(
    label_featurization,
    arguments
)

def labels_featurization(labels):
    lbl_enc = preprocessing.LabelEncoder()
    return lbl_enc.fit_transform(labels)

arguments = [
    Args(["Affirm", "Reverse"]),
    Args(["Affirm", "Reverse", "Complex"]),
    Args(["Gagné", "Perdu"]),
    Args(["janvier"," février"," mars"," avril"," mai"," juin"," juillet"," août"," septembre"," octobre"," novembre"," décembre",])
]

exo_labels_featurization = ExerciseFunction(
    labels_featurization,
    arguments
)

def labels_featurization_pandas(dataframe):
    lbl_enc = preprocessing.LabelEncoder()
    dataframe["label_feature"] = lbl_enc.fit_transform(dataframe["role"].values)
    return dataframe

import pandas as pd

arguments = [
    Args(pd.DataFrame(["Affirm", "Reverse"])),
]

exo_labels_featurization_pandas = ExerciseFunction(
    labels_featurization_pandas,
    arguments
)