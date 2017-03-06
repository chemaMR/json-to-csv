import json
import pandas as pd
import os
import argparse


def main():

    # Parse commandline arguments
    parser = argparse.ArgumentParser(description='create a csv file gfw climate json file')
    parser.add_argument('--json', '-j', required=True, help='path to json file')
    parser.add_argument('--climate', '-c', help='if this is a climate file, True', action='store_true')

    args = parser.parse_args()

    # Name of csv file
    csv_file = args.json.replace('json', 'csv')

    with open(args.json) as json_data:
        d = json.load(json_data)

    if args.climate:

        d = d['data']

    df = pd.DataFrame(d)

    df.to_csv(csv_file)


if __name__ == "__main__":
    main()

