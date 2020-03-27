import csv
from trello import TrelloClient


def bulk_import(trello_api_key, trello_token, board_id, file_path):
    client = TrelloClient(
        api_key=trello_api_key,
        token=trello_token
    )

    board = client.get_board(board_id)
    backlog_list = board.list_lists()[0]
    test = backlog_list.list_cards()[0]

    with open(file_path) as csv_file:
        csv_dict = csv.DictReader(csv_file, delimiter=';')

        user_story = ''
        card = None
        checklist_items = []
        for row in csv_dict:
            category = row["Category"]
            task = row["Task"]
            comment = row["Comment"]
            load = row["Load"]  

            checklist_items.append(task + " (" + load +")" )
            if user_story != category:
                if card is not None and checklist_items :
                    card.add_checklist('Tasks', checklist_items, itemstates=None)
                    checklist_items = []
                user_story = category
                card = backlog_list.add_card(name=category)
