from csv_detective.process_text import _process_text

PROPORTION = 1

def _is(header):
    '''Returns 1 if the (processed) header matches one of the expected words combination, else 0'''

    words_combinations_list = ['datetime', 'timestamp', 'osm_timestamp', 'date', 'created at', 'last update', 'date maj', 'createdat', 'date naissance', 'date donnees'] #Almost same as IS0, no example in data
    processed_header = _process_text(header)

    return float(any([words_combination == processed_header for words_combination in words_combinations_list]))