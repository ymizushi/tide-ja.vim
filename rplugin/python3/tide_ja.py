import pynvim
import datetime

class Scraper:
    PLACE_KEYS=(
        "KW", # 川崎
    )

    def __init__(self):
        pass

    def scrape(self, place, date):
        return {
            '2020/05/05': {
                status: None,
                levels: {
                  '03:18': 172,
                  '15:45': 174,
                  '09:36': 46,
                  '21:46': 48,
                }
            },
            '2020/05/06': {
                status: 'full',
                levels: {
                  '03:18': 172,
                  '15:45': 174,
                  '09:36': 46,
                  '21:46': 48,
                }
            }
        }

def scrape(place, date):
    scraper = Scraper()
    return scraper.scrape(place, date)

@pynvim.plugin
class TestPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("TideJa", range='', nargs='*')
    def testcommand(self, args, range):
        place = 'KW'
        date = datetime.date.today() # TODO: 文字列表現にする
        tide = scrape(place, date)
        if range == 2:
            place = args[0]
            date = args[1]
        elif range == 1:
            date = args[0]
        else:
            pass
        self.nvim.current.line = ('Command with place: {}, date: {}, tide: {}'.format(args, range, tide))




