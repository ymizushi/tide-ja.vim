import neovim
import scrape from scraper

@neovim.plugin
class TestPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function("TestFunction", sync=True)
    def testfunction(self, args):
        self.nvim.current.line = ('Command with args: {}, range: {}' .format(args, range))

    @neovim.command("TideJa", range='', nargs='*')
    def testcommand(self, args, range):
        date = 
        if range == 2
            place = args[0]
            date = args[1]
        elif 
        else
        self.nvim.current.line = ('Command with place: {}, date: {}'.format(args, range))
