import pynvim
from datetime import datetime
from .tide_table import tide_dict, InvalidKeyException
from .constants import PLACE_KEYS

@pynvim.plugin
class TestPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    def format_tide(self, place, date, tide):
        output = ["[tide-ja.vim]"]
        output += [PLACE_KEYS[place]]
        output += ["20{}-{}-{}".format(date[0], date[1], date[2])]
        highlows = tide["highs"] + tide["lows"]
        for e in sorted(highlows, key=lambda e: int(e[0][0])):
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
        if len(args) == 2:
            place = args[0]
            date = tuple([int(s) for s in args[1].split('-')])
        elif len(args) == 1:
            place = args[0]
        self.nvim.err_write("target:{}\n".format(date))

        try:
            tide = tide_dict(place, date)
        except InvalidKeyException:
            self.nvim.err_write("target month or day is invalid\n")
        except FileNotFoundError:
            self.nvim.err_write("Place key or target year is invalid\n")
        else:
            tide_line = self.format_tide(place, date, tide)
            self.nvim.command('vsplit')
            self.nvim.command('e [tide-ja.vim]')
            self.nvim.command('set buftype=nowrite')
            self.nvim.current.buffer.append(tide_line, -2)


