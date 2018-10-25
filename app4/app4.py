import journal

def main():
    """
    This is the main function that prints the header
    Then it starts the event loop that exits on 'x'
    """

    print_header()
    run_event_loop()


def print_header():
    print('---------------------------')
    print('       JOURNAL APP')
    print('---------------------------')
    print()


def run_event_loop():
    """
    Event loop which asks user for journal name and loads from directory
    Then user can add to or list journal contents
    Saves back to loaded journal on exit
    """

    journal_name = input("Which journal do you want to work on?")
    if not journal_name:
        journal_name = 'default'
    
    journal_data = journal.load(journal_name)

    print("What do you want to do in your journal?")
    cmd = None
    while cmd != 'x':
        cmd = input("[A]dd an entry, [L]ist all entries or E[x]it? ")
        cmd = cmd.lower().strip()
        if cmd == 'a':
            text = input("Type your input here: ")
            journal.add_entry(journal_data, text)

        elif cmd == 'l':
            journal.list_entries(journal_data)

        elif cmd != 'x':
            print("Unable to process command '{}'".format(cmd))

    journal.save(journal_name, journal_data)
    print("Done, goodbye!")


if __name__ == "__main__":
    main()