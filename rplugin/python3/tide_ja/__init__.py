import pynvim
from datetime import datetime
from tide_table import tide_dict

@pynvim.plugin
class TestPlugin(object):
    PLACE_KEYS= dict(
      KW='川崎',
    )

    def __init__(self, nvim):
        self.nvim = nvim

    def format_tide(self, place, date, tide):
        output = []
        output += [self.PLACE_KEYS[place]]
        output += ["20{}-{}-{}".format(date[0], date[1], date[2])]
        highlows = tide.highs + tide.lows
        sorted(highlows, key=lambda e: int(e[0][0]))
        for e in highlows:
            output += ["{}:{} {}cm".format(e[0][0], e[0][1], e[1])]
        return output

    @pynvim.command("TideJa", range='', nargs='*')
    def testcommand(self, args, range):
        place = 'KW'
        today = datetime.today() 
        date = (
            int(str(today.year)[-2:]),
            today.month,
            today.day
        )
        if args == 3:
            place = args[1]
            date = tuple(args[2].split('-'))
        elif range == 2:
            place = args[1]
        else:
            pass

        tide = tide_dict(place, date)
        tide_line = self.format_tide(place, date, tide)
        self.nvim.command('vsplit')
        self.nvim.command('e [tide-ja.vim]')
        self.nvim.command('set buftype=nowrite')
        self.nvim.current.buffer.append(tide_line)
