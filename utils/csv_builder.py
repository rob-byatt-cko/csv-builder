import math
import time

def add_headers(data: tuple, file_name: str):
    _write_file(_format_csv_line(data), file_name)

def append_file_with_data_rows(file_name: str, row_count: list, data_builder: object, batch_size: int = 50000):
    '''
    Appends data rows to a file based on data_builder object
    Amount of rows is defined by row_count argument
    '''
    batches = _batch_items_to_write(row_count, batch_size)
    print(f"Writting {row_count} records to {file_name} in {len(batches)} batches of {batch_size} records")
    start_time = time.time()
    file = open(file_name, 'a')
    for index, item in enumerate(batches):
        data = _get_granular_data_list(item, data_builder)
        file.write(data)
        elapsed_time = time.time() - start_time
        print(f"batch {index +1} of {len(batches)} written. Elapsed time {elapsed_time}")
    file.close

def _write_file(content: str, file_name: str):
    file = open(file_name, 'w')
    file.write(content)
    file.close

def _get_granular_data_list(record_count: int, data_builder:object):
    data = [_format_csv_line(data_builder().__dict__.values()) for i in range(record_count)]
    return ' '.join(data)

def _format_csv_line(data: tuple) -> str:
    return ", ".join([str(item) for item in data]) + '\n'

def _batch_items_to_write(row_count: int, batch_size = 50000) -> list :
    '''
    Groups row_count into batches. Returns batches as a list
    For example:
    if row count is 12 and batch size is 5 function will return [5, 5, 2]
    if row count is 2 and batch size is 5 function will return [2]
    '''
    values = []
    split = row_count / batch_size
    frac, whole = math.modf(split)
    for i in range(round(whole)):
        values.append(batch_size)
    if(frac > 0): values.append(round(frac * batch_size))
    return values