from bs4 import BeautifulSoup


def add_infos(data_dict, titles, descriptions, spectacle_counter):
    """
    Adding title and description of spectacles in dictionary
    :param data_dict: [dict]
    :param titles: list of titles [list]
    :param descriptions: list of descriptions [list]
    :param spectacle_counter: counter for the data dictionary keys [int]
    :return: tuple
    """
    assert spectacle_counter != 0
    assert "spectacle_{}".format(spectacle_counter) not in data_dict.keys()
    assert len(titles) == len(descriptions), "Mismatch between the number of items in each list"

    # if the data_dict is empty, the first key string ends by 1
    for i, info in enumerate(zip(*[titles, descriptions])):
            key = "spectacle_{}".format(spectacle_counter)
            data_dict[key] = {"title": info[0].text, "description": info[1].text.strip()}
            spectacle_counter += 1
    return data_dict, spectacle_counter


def parsing_html_page(url, requester):
    """Parse html page into BeautifulSoup object"""
    response = requester.request('GET', url)
    soup = BeautifulSoup(response.data)
    return soup


def get_infos(page, requester, data_dict, spectacle_counter):
    soup = parsing_html_page("https://www.billetreduc.com/one-man-show/R/3/{}".format(page),
                             requester)

    titles = soup.find_all("a", {"class": "head"})
    descriptions = soup.find_all("div", {"class": "libellepreliste"})
    data_dict, spectacle_counter = add_infos(data_dict, titles, descriptions, spectacle_counter)
    return data_dict, spectacle_counter
