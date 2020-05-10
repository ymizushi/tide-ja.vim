class TideTable:
    def __init__(self, place, date):
        self._place = place
        self._date = date

    def _key(self):
        year = self._date[0]
        month = format(self._date[1], ' >2')
        day = format(self._date[2], ' >2')
        return "{}{}{}{}".format(year, month, day)
    def _path(self):
        return "db/{}/{}.txt".format(self._date[0], self._place)

    def _find_row(self, key):
        self.
        # TODO: implement
        return "65 47 39 44 61 8611313715315915414212711210310110812113514614914212710620 1 1KW 9 3159194914999999999999999 2 7 39144210199999999999999"

    def tide_dict(self):
        key = self._key()
        row = self._find_row(key)
        # TODO: implement
        return dict(
            levels=[65,47,39,44,61,86,113,137,153,159,154,142,127,112,103,101,108,121,135,146,149,142,127,106],
            high=[
                ((9,3), 159),
                ((19,49), 149),
            ],
            low=[
                ((2,7), 39),
                ((14,42), 101),
            ]
        )
def tide_dict(place, date):
    table = TideTable(place, date)
    return table.tide_dict()
