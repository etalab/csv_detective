from csv_detective.process_text import _process_text

PROPORTION = 1

def _is(header):
    '''Returns 1 if the (processed) header matches one of the expected words combination, else 0'''

    words_combinations_list = ['latlon wgs', 'latlon', 'geo point', 'geo point 2d', 'wgs84', 'geolocalisation', 'geo', 'coordonnees finales', 'coordonnees', 'coordonnees ban', 'xy', 'geometry x y', 'coordonnees insee', 'coordonnees geographiques', 'position', 'coordonnes gps', 'geopoint', 'geom x y', 'coord gps', 'latlong', 'position geographique', 'c geo', 'coordonnes geoloc', 'lat lon', 'code geo', 'geo localisation', 'coordonnes geo', 'geo cp', 'x y', 'geo coordinates', 'point geo', 'point geo insee', 'coordonnees geoloc']
    processed_header = _process_text(header)

    return float(any([words_combination == processed_header for words_combination in words_combinations_list]))