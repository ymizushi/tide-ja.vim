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
                  '03:18': 172
                  '15:45': 174,
                  '09:36': 46,
                  '21:46': 48,
                }
            },
            '2020/05/06': {
                status: 'full',
                levels: {
                  '03:18': 172
                  '15:45': 174,
                  '09:36': 46,
                  '21:46': 48,
                }
            }
        }


def scrape(place, date):
    scraper = Scraper()
    return scraper.scrape(place, date)
