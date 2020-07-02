import requests
import datetime

url = "https://api.telegram.org/bot1134951364:AAGpKHO2-SsyFXsxmbpnk68l1vUFE0M8-ik/"


def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if  update_id == last_update(get_updates_json(url))['update_id']:
            print("Hi")
 #           text = get_updates_json(url)
  #          print(text)
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
            update_id += 1


chat_id = get_chat_id(last_update(get_updates_json(url)))
send_mess(chat_id, 'Готов узнать кто ты из шиноби мира МК?')


if __name__ == 'main':
    main()