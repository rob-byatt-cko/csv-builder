import argparse
from data.data_sample.sample_builder import build_sample_csv

parser = argparse.ArgumentParser(description='Create data for Finance testing')
parser.add_argument('-r',
                    '--rows', 
                    metavar='',
                    action='store',
                    type=int,
                    help='amount of rows to create',
                    required= False)

if __name__ == "__main__":
    args = parser.parse_args()
    row_count = args.rows if args.rows else 10
    build_sample_csv(row_count)