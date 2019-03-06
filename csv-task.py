import sys

import pandas as pd
from money_parser import price_str


FEED_CSV_FILENAME = 'feed.csv'
FEED_SAMPLE_CSV_FILENAME = 'feed_sample.csv'

# Column Names
COL_PRODUCT_NAME = 'product_name'
COL_PRICE = 'price'
COL_PRICE_EDITED = 'price_edited'

# Part 2 Regex (Knit w/o Jumper)
PART_2_REGEX = '^(?=.*Knit)(?!.*Jumper).*'


def main(argv):
    if argv[1] == FEED_CSV_FILENAME:
       step_1(argv)
    elif argv[1] == FEED_SAMPLE_CSV_FILENAME:
        step_2(argv)


def step_2(argv):
    data_frame = pd.read_csv(argv[1])
    df_filter = get_df_filter_by_regex(data_frame, PART_2_REGEX, COL_PRODUCT_NAME)
    data_frame = data_frame[~df_filter]
    data_frame.to_csv(argv[3])


def get_df_filter_by_regex(df, regex, column_name):
    return df[column_name].str.contains(regex)


def step_1(argv):
    create_csv_from_tsv(argv[1], argv[3])
    data_frame = pd.read_csv(argv[3])
    create_new_column_in_csv(data_frame,
                             COL_PRICE_EDITED,
                             data_frame[COL_PRICE].apply(lambda x: extract_price_from_string(x)), argv[3])


def create_new_column_in_csv(data_frame, column_name, data_frame_column, file_name):
    data_frame[column_name] = data_frame_column
    data_frame.to_csv(file_name)


def extract_price_from_string(price):
    return price_str(price)


def create_csv_from_tsv(tsv_file_name, csv_output_file_name):
    csv_table = pd.read_csv(tsv_file_name, sep='\t')
    csv_table.to_csv(csv_output_file_name, index=False)


if __name__ == "__main__":
    main(sys.argv[1:])
