import csv
import sys
from collections import defaultdict
from trello import TrelloClient

def main() -> None:
    trello_api_key, trello_token, board_id, file_path = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    bulk_import(trello_api_key=trello_api_key, trello_token=trello_token, board_id=board_id, file_path=file_path)


def bulk_import(trello_api_key: str, trello_token: str, board_id: str, file_path: str) -> None:
    client = TrelloClient(
        api_key=trello_api_key,
        token=trello_token
    )

    board = client.get_board(board_id)
    backlog_list = board.list_lists()[0]
    test = backlog_list.list_cards()[0]

    with open(file_path) as csv_file:
        csv_dict = csv.DictReader(csv_file, delimiter=';')

        items = defaultdict(list)
        user_story = ''
        card = None
        checklist_items = []
        for row in csv_dict:
            category = row["Category"]
            task = row["Task"]
            comment = row["Comment"]
            load = row["Load"]  
            
            if category is '':
                category = "Others"
            else:
                category = " ".join(category.split())
            
            if load is '':
                load = 'X'
            
            if comment is not '':
                comment = '- {}'.format(comment)

            checklist_item = "({}) {} {}".format(load, task, comment)
            items[category].append(checklist_item)

    for key in items:
        card = backlog_list.add_card(name=key)
        card.add_checklist('Tasks', items[key], itemstates=None)
