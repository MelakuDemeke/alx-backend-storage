#!/usr/bin/env python3
import requests

def get_page(url: str) -> str:
    req = requests.get(url)
    req_text = req.text
    return req_text
