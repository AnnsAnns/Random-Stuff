from pprint import pprint as pri
import requests

def get_anime_list_twist_moe(TWIST_X_ACCESS_TOKEN = "1rj2vRtegS8Y60B3w3qNZm5T2Q0TN2NR"):
    database = {}
    
    return requests.get("https://twist.moe/api/anime", headers={"x-access-token": TWIST_X_ACCESS_TOKEN})
        

def create_twist_db(raw):
    database = {}
    
    for anime in raw():
        slug = anime["slug"]["slug"]
        database[slug] = {"id": anime["id"],
                            "title": anime["title"],
                            "alt_title": anime["alt_title"]}
    return database