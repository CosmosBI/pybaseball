import io

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

from . import cache
from .utils import most_recent_season, sanitize_date_range


def get_soup(start_dt, end_dt):
    # get most recent standings if date not specified
    if((start_dt is None) or (end_dt is None)):
        print('Error: a date range needs to be specified')
        return None
    url = "http://www.baseball-reference.com/leagues/daily.cgi?user_team=&bust_cache=&type=p&lastndays=7&dates=fromandto&fromandto={}.{}&level=mlb&franch=&stat=&stat_value=0".format(start_dt, end_dt)
    s = requests.get(url).content
    # a workaround to avoid beautiful soup applying the wrong encoding
    s = str(s).encode()
    return BeautifulSoup(s, features="lxml")

  