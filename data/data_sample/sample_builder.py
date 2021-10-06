from utils.csv_builder import add_headers, append_file_with_data_rows
from data.data_sample.sample_data import SampleData

def build_sample_csv(row_count: int) -> str :
    file_name = 'sample.csv'
    add_headers(SampleData.get_headers(), file_name)
    append_file_with_data_rows(file_name, row_count, SampleData)