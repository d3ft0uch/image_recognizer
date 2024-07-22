import requests
from serpapi import GoogleSearch
from flask import current_app

from app.main.exceptions import ApiException


def upload_to_imgbb(base_64_img: str):
    r = requests.post('https://api.imgbb.com/1/upload', data={"key": current_app.config["IMG_BB_KEY"], "image": base_64_img})
    data = r.json()
    if data.get("error"):
        raise ApiException(message=data["error"]["message"], code=data["status_code"])
    return data.get("data", {}).get("url")


def google_lens(url: str):
    params = {
        "engine": "google_lens",
        "url": url,
        "no_cache": "true",
        "api_key": current_app.config['SERP_API_KEY'],
    }

    search = GoogleSearch(params)
    r = search.get_dict()
    if r.get("error"):
        raise ApiException(r["error"], 400)
    matches = []

    for item in r['visual_matches']:
        matches.append({
            "source": item.get('source'),
            "title": item.get('title'),
            "link": item.get('link'),
            "price": item['price'].get('extracted_value') if 'price' in item else None,
            "currency": item['price'].get('currency') if 'price' in item else None,
            "thumbnail": item.get('thumbnail')
        })
    return matches


def find_matches(base_64_img: str):
    image_url = upload_to_imgbb(base_64_img)
    return google_lens(url=image_url)
