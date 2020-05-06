import pynvim
import datetime

import lxml.html

class Scraper:
    PLACE_KEYS=(
        "KW", # 川崎
    )

    def __init__(self):
        pass

    def request():
        pass

    def scrape(self, place, start_date, end_date):
        root = lxml.html.parse('http://qiita.com/advent-calendar/2014').getroot()
        root.cssselect('title')[0].text
        start_match = re.match(r"(\d{4})/(\d{2})/(\d{2})", start_date)

        stn = place
        ys = m.groups[0]
        ys = m.groups[1]

        return {
            '2020/05/05': {
                'status': 'full',
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
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("TideJa", range='', nargs='*')
    def testcommand(self, args, range):
        place = 'KW'
        date = datetime.date.today() # TODO: 文字列表現にする
        tide = scrape(place, date)
        if args == 3:
            place = args[1]
            date = args[2]
        elif range == 2:
            place = args[1]
        else:
            pass
        self.nvim.current.line = ('Command with place: {}, date: {}, tide: {}'.format(place, date, tide))
