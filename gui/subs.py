import requests
from bs4 import BeautifulSoup
from urllib import request
from difflib import get_close_matches

root_url = "http://www.yifysubtitles.com/"
search_url = "http://www.yifysubtitles.com/search?q="


def search_subtitles(search_term):
    search_results = []
    source_code = requests.get(search_url + search_term)
    text = source_code.text
    soup = BeautifulSoup(text, "html.parser")
    # print(soup)
    # print(soup.findAll('h3'))
    for tag in soup.findAll('div', {"class": "media-body"}):
        url = root_url+tag.a.get("href")
        search_results.append(url)


    index = filter_search_results(soup.findAll('h3',{"class":"media-heading"}),search_term)
    get_single_detail(search_results[index])


def filter_search_results(data, term):
    movie_list = []
    for i in range(len(data)):
        movie_list.append(data[i].text)
    match=get_close_matches(term, movie_list, cutoff=0.4)
    return movie_list.index(match[0])


def get_single_detail(url):
    source_code = requests.get(url)
    text = source_code.text
    soup = BeautifulSoup(text, "html.parser")
    # print(soup.findAll('tr'))
    for tag in soup.findAll('tr'):
        # print(tag.findAll('span', {"class": "sub-lang"}))
        lang = tag.findAll('span', {"class": "sub-lang"})
        anchor = tag.findAll('a')
        if len(anchor) > 0:
            url = root_url + anchor[0].get("href")
            if str(lang[0].string) == 'English':
                download_subs(url)


def download_subs(link):
    src = requests.get(link)
    soup = BeautifulSoup(src.text, "html.parser")

    for tag in soup.findAll('a', {"class": "download-subtitle"}):
        request.urlretrieve(tag.get("href"), r"F:\subtitle.zip")


# search_subtitles("thor")


