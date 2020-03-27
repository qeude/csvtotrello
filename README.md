# csvtotrello

💻 Basic Python script to bulk import CSV backlog into Trello

## 🛠 Install
`pip install csvtotrello`

## 🎉 Get started
- Get your trello API key from [here](https://trello.com/app-key).
- Get your board id.
- `csvtotrello <trello_api_key> <trello_api_token> <board_id> <file_path_to_csv>`

## 🗂 CSV template
Your csv file should look like below
| Category        | Task           | Comment     | Load     |
| --------------- | :------------: | :------:    | :-------:|
| user story1 name| task1 name     | any comment | task load|
| user story1 name| task2 name     | any comment | task load|
| user story2 name| task3 name     | any comment | task load|

