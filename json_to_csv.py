import json
import pandas as pd
import os


def json_to_csv(json_file):

    csv_file = json_file.replace('json', 'csv')

    with open(json_file) as json_data:
        d = json.load(json_data)

    dict_list = d['data']

    df = pd.DataFrame(dict_list)

    df.to_csv(csv_file)
