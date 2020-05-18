class InvalidKeyException(Exception):
    pass

def _to_int_tide(tide_str):
    return int(tide_str.replace(' ', ''))

def _format_tide_str(start, end, row):
    return [
                (
                    (
                        _to_int_tide(row[i: i+2]),
                        _to_int_tide(row[i+2: i+4])
                    ),
                    _to_int_tide(row[i+4: i+7])
                ) for i in range(start, end, 7) if row[i:i+7] != '9999999'
            ]

class TideTable:
    def __init__(self, place, date):
        self._place = place
        self._date = date

    def _key(self):
        year = self._date[0]
        month = format(self._date[1], ' >2')
        day = format(self._date[2], ' >2')
        return "{}{}{}{}".format(year, month, day, self._place)

    def _path(self):
        return "./rplugin/python3/db/{}/{}.txt".format(self._date[0], self._place)

    def _find_row(self, key):
        with open(self._path()) as f:
            for line in f:
                if key in line:
                    return line
        raise InvalidKeyException('invalid key or table')

    def tide_dict(self):
        key = self._key()
        row = self._find_row(key)
        levels = [_to_int_tide(row[i: i+3]) for i in range(0, 72, 3)]
        highs = _format_tide_str(80, 108, row)
        lows = _format_tide_str(108, 136, row)
        return dict(
            levels=levels,
            highs=highs,
            lows=lows,
        )
def tide_dict(place, date):
    table = TideTable(place, date)
    return table.tide_dict()
