from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

from sklearn import preprocessing

def label_featurization(label):
    lbl_enc = preprocessing.LabelEncoder()
    return lbl_enc.fit_transform(["Affirm", "Reverse"])[0]

arguments = [
    Args("Affirm"),
    Args("Reverse")
]

exo_label_featurization = ExerciseFunction(
    label_featurization,
    arguments
)

def labels_featurization(labels):
    lbl_enc = preprocessing.LabelEncoder()
    return lbl_enc.fit_transform(["Affirm", "Reverse"])

arguments = [
    Args(["Affirm", "Reverse"]),
]

exo_labels_featurization = ExerciseFunction(
    labels_featurization,
    arguments
)

def labels_featurization_pandas(dataframe):
    lbl_enc = preprocessing.LabelEncoder()
    dataframe["label_feature"] = lbl_enc.fit_transform(dataframe.label.values)
    return dataframe

import pandas as pd

arguments = [
    Args(pd.DataFrame(["Affirm", "Reverse"])),
]

exo_labels_featurization = ExerciseFunction(
    labels_featurization_pandas,
    arguments
)