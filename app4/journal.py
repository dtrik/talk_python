"""
This is the journal module
"""

import os
def get_path(journal_name):
    """
    method to create the absolute path from a file name
    :param journal_name: name of the journal whose path is to be generated

    """
    filename = os.path.abspath(os.path.join('.','journals',journal_name + '.jrl'))
    return filename


def load(journal_name):
    """
    method to load a journal whose name is provided, if it doesn't exist load blank
    :param journal_name: name of the journal to be loaded

    """
    data = []
    filename = get_path(journal_name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin:
                data.append(entry.rstrip())

    return data


def save(journal_name, journal_data):
    """
    method to save to file name as param, the data passed as param
    :param journal_name: name of the journal to be saved to
    :param journal_data: content to save to file

    """
    filename = get_path(journal_name)
    print("... saving to {}".format(filename))
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry+'\n')


def add_entry(journal_data, text):
    """
    method to add entry to previously opened journal 
    :param journal_data: existing journal content 
    :param text: new content to be added
    """

    journal_data.append(text)


def list_entries(journal_data):
    """
    method to print contents of loaded journal
    :param journal_data: existing journal content
    """
    
    print("Journal contents:")
    for idx, entry in enumerate(journal_data):
        print("Entry #{} is {}".format(idx+1, entry))