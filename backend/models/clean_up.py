import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder


def clean_up(X, enc = None):
    numerical_X = X[["amt"]].copy()
    numerical_X[["amt"]] = numerical_X[["amt"]].astype("float64")
    date_information = pd.DatetimeIndex(pd.to_datetime(X["trans_date_trans_time"]))
    numerical_X["year"] = date_information.year
    numerical_X["month"] = date_information.month
    numerical_X["day"] = date_information.day
    numerical_X["time"] = date_information.second + 60 * date_information.minute + 3600 * date_information.hour
    numerical_X["age"] = (pd.to_datetime(X["trans_date_trans_time"]) - pd.to_datetime(X["dob"])).dt.days
    numerical_X = numerical_X.apply(pd.to_numeric, errors = 'coerce')
    numerical_X = numerical_X.fillna(numerical_X.median())
    categorical_X = X[["cc_num", "merchant", "category", "city", "job"]].copy()
    categorical_X[["cc_num"]] = categorical_X[["cc_num"]].astype("int64")
    categorical_X["merchant"] = categorical_X["merchant"].apply(lambda x : x.replace("fraud_", "", 1))
    if not enc:
        enc = {}
        for column in categorical_X:
            current_encoder = OrdinalEncoder(handle_unknown='use_encoded_value',
                                unknown_value=-1)
            categorical_X[column] = current_encoder.fit_transform(categorical_X[column].to_frame())
            categorical_X[column] = categorical_X[column].astype("category")
            enc[column] = current_encoder
    else:
        for column in categorical_X:
            current_encoder = enc[column]
            categorical_X[column] = current_encoder.transform(categorical_X[column].to_frame())
            categorical_X[column] = categorical_X[column].astype("category")
    return pd.concat([numerical_X, categorical_X], axis = 1), enc
