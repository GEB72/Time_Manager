import pickle
import os

data_dir = os.getcwd() + "/data"


def pickle_me(data):
    with open(data_dir + "/data.pkl", "wb") as pickle_file:
        pickle.dump(data, pickle_file)


def unpickle_me():
    try:
        with open(data_dir + "/data.pkl", "rb") as pickle_file:
            return pickle.load(pickle_file)
    except FileNotFoundError:
        pickle_me({})
