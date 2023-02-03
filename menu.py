import os
import json


def menu():
    print("hello")
    with open("settings.json", 'r') as f:
        JsonSettings = json.load(f)

        print(JsonSettings)

    input()