import json
import os
import sys

import websocket
import time


def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def on_message(ws, message):
    print("Received", message)


def on_error(ws, error):
    print("Received", error)


def on_close(ws, close_status_code, close_msg):
    print("Closed", close_status_code, close_msg)


def on_open(ws):
    print("Connected\n")
    send_messages()


def send_messages():
    while True:
        start = input("Start Server?")
        if start == "y":
            time.sleep(5)
            # Join Room
            with open(get_resource_path('res/JoinRoom.json'), 'r') as json_file:
                data = json.load(json_file)
                ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

            # Start Betting
            time.sleep(5)
            with open(get_resource_path('res/StartBet.json'), 'r') as json_file:
                data = json.load(json_file)
                ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

            player_betting()

            # Card Distribution
            time.sleep(3)
            with open(get_resource_path('res/CardDistribution.json'), 'r') as json_file:
                data = json.load(json_file)
                ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)


def player_betting():
    # Player 1 Finished Bet
    time.sleep(2)
    with open(get_resource_path('res/Player1Bet.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

    time.sleep(2)
    with open(get_resource_path('res/Player1BetFinished.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

    # Player 2 Finished Bet
    time.sleep(2)
    with open(get_resource_path('res/Player2Bet.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

    time.sleep(2)
    with open(get_resource_path('res/Player2BetFinished.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

    # Player 3 Finished Bet
    time.sleep(2)
    with open(get_resource_path('res/Player3Bet.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

    time.sleep(2)
    with open(get_resource_path('res/Player3BetFinished.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

    # Player 4 Finished Bet
    time.sleep(2)
    with open(get_resource_path('res/Player4Bet.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

    time.sleep(2)
    with open(get_resource_path('res/Player4BetFinished.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

    # Player 5 Finished Bet
    time.sleep(2)
    with open(get_resource_path('res/Player5Bet.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)

    time.sleep(2)
    with open(get_resource_path('res/Player5BetFinished.json'), 'r') as json_file:
        data = json.load(json_file)
        ws.send(json.dumps(data), opcode=websocket.ABNF.OPCODE_TEXT)


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://socketsbay.com/wss/v2/4/05db90c5178c173e63af62155ce998e8/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
