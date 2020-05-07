import pynvim
import datetime

import lxml.html


def plus(a, b):
    return a + b

class Scraper:
    def __init__(self):
        pass

    def request():
        pass

    def scrape(self, place, start_date, end_date):
        # root = lxml.html.parse('http://qiita.com/advent-calendar/2014').getroot()
        # root.cssselect('title')[0].text
        # start_match = re.match(r"(\d{4})/(\d{2})/(\d{2})", start_date)

        # stn = place
        # ys = m.groups[0]
        # ys = m.groups[1]

        return {
            '2020/05/05': {
                'status': None,
                'levels': {
                  '03:18': 172,
                  '15:45': 174,
                  '09:36': 46,
                  '21:46': 48,
                }
            },
            '2020/05/06': {
                'status': 'full',
                'levels': {
                  '03:18': 172,
                  '15:45': 174,
                  '09:36': 46,
                  '21:46': 48,
                }
            }
        }

def scrape(place, start_date, end_date):
    scraper = Scraper()
    return scraper.scrape(place, start_date, end_date)

@pynvim.plugin
class TestPlugin(object):
    PLACE_KEYS= dict(
      KW='川崎',
    )

    def __init__(self, nvim):
        self.nvim = nvim

    def format_tide(self, place, tide):
        output = []
        output += [self.PLACE_KEYS[place]]
        for date, value in tide.items():
            output += [date]
            l = [(k, v) for k, v in value['levels'].items()]
            sorted(l, key=lambda e: int(e[0].replace(':', '')))
            for e in l:
                output += ["\t {} {}".format(e[0], e[1])]
        return output

    @pynvim.command("TideJa", range='', nargs='*')
    def testcommand(self, args, range):
        place = 'KW'
        start_date = datetime.date.today() # TODO: 文字列表現にする
        end_date = datetime.date.today() # TODO: 文字列表現にする
        tide = scrape(place, start_date, end_date)
        if args == 3:
            place = args[1]
            date = args[2]
        elif range == 2:
            place = args[1]
        else:
            pass
        tide_lines = self.format_tide(place, tide)
        self.nvim.command('vsplit')
        self.nvim.command('e [tide-ja.vim]')
        self.nvim.command('set buftype=nowrite')
        self.nvim.current.buffer.append(tide_lines)
