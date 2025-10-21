import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

res = requests.get("https://www.basketball-reference.com/players/c/curryst01/gamelog/2025")
soup=BeautifulSoup(res.text, "lxml")