import subprocess
from constants import PLACE_KEYS

for key in PLACE_KEYS.keys():
    subprocess.call('curl https://www.data.jma.go.jp/gmd/kaiyou/data/db/tide/suisan/txt/20{year}/{place}.txt -o ../db/{year}/{place}.txt'.format(year=20, place=key), shell=True)
