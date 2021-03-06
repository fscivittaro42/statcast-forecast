import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup

def get_soup(url):
    """
    Takes in a url and returns the parsed BeautifulSoup code for that url with
    handling capabilities if the request 'bounces'.

    Inputs: the url

    Returns: BeautifulSoup code for the url
    """

    s = requests.Session()

    retries = Retry(
        total = 10,
        backoff_factor = 0.1,
        status_forcelist = [500, 502, 503, 504]
        )

    s.mount('http://', HTTPAdapter(max_retries = retries))

    return BeautifulSoup(s.get(url).text, 'html.parser')


def get_weightings(year):
    """
    Takes in a year (str or int) and returns a list containing the necessary WOBA
    constants for that year.

    Inputs: year

    Returns: a dict of wOBA weightings for the given year
    """

    url = 'http://www.fangraphs.com/guts.aspx?type=cn'
    soup = get_soup(url)
    year = str(year)

    headers = soup.find('a', text = 'Season').parent.parent
    correct_weightings = soup.find('td', text = year).parent


    def clean_soup(dirty_soup):
        """
        Takes in a soup element and returns a list of desired strings
        extracted from the soup code.
        """

        new_list = []

        for item in dirty_soup:
            new_list.append(item)

        new_list.pop(0)
        new_list.pop()
        final_list = []

        for item in new_list:
            final_list.append(item.get_text())

        return final_list

    header_list = clean_soup(headers)
    weightings_list = clean_soup(correct_weightings)

    weightings_dict = {}

    for header, weighting in zip(header_list, weightings_list):
        weightings_dict[header] = weighting

    return weightings_dict