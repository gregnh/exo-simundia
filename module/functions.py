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
