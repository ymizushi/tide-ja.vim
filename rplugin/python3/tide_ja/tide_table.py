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
        return "db/{}/{}.txt".format(self._date[0], self._place)

    def _find_row(self, key):
        with open(self._path()) as f:
            for line in f:
                if key in line:
                    return line
        raise Exception('invalid key or table')

    def tide_dict(self):
        key = self._key()
        row = self._find_row(key)
        levels = [int(row[i: i+3].replace(' ', '')) for i in range(0, 72, 3)]
        highs = [(
                    (
                        int(row[i: i+2].replace(' ', '')),
                        int(row[i+2: i+4].replace(' ', ''))
                    ),
                    int(row[i+4: i+7].replace(' ', ''))
                    ) for i in range(80, 108, 7) if row[i:i+7] != '9999999']
        lows = [((
                        int(row[i: i+2].replace(' ', '')),
                        int(row[i+2: i+4].replace(' ', ''))
                    ), int(row[i+4: i+7].replace(' ', ''))) for i in range(108, 136, 7) if row[i:i+7] != '9999999']
        return dict(
            levels=levels,
            highs=highs,
            lows=lows,
        )
def tide_dict(place, date):
    table = TideTable(place, date)
    return table.tide_dict()
