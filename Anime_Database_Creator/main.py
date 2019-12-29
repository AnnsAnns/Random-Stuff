import simplejson as json
import pprint
import requests
import twist

database = {}
x = 0

def get_db_from_notify_moe(filename = "Anime.dat.txt", type = "You'll have to figure that out yourself!"): # Do not use without permissions, this is a really demanding request!
    with open(filename, mode="w") as db:
        db.write(requests.get(f"notify.moe/api/types/{type}/download"))
        

def create_db_from_file(filename = "Anime.dat.txt"):
    with open(filename, mode="r", encoding="utf8") as f:
        for count, line in enumerate(f, start=1):
            if count % 2 == 0:
                temp = json.loads(line)
                database[x] = {}
                database[x].update(temp)
                
                x += 1
            
    with open("database.json", "w") as p:
        p.write(json.dumps(database, indent=4 * " "))

def load_db():
    with open("database.json", "r") as d:
        database = json.load(d)
    return database

def lookup_id(search):
    if search in database:
        return database[search]

def lookup_by_unknown_value(search):
    for anime in database:
        for key in anime:
            
            if type(key) is dict:
                for keykey in key:
                    if database[anime][key][keykey] == search:
                        return database[anime]
                    
            if database[anime].get(key) == search:
                return database[anime]

def update_db_with_twist_db(database = dict):
    
    twist_db = twist.get_anime_list_twist_moe()
    
    for tw_anime in twist_db:
        for db_anime in database:
            
            if tw_anime["alt_title"] == None and tw_anime["title"] == None:
                continue
            
            for db_anime_title in db_anime["title"]:
                if db_anime_title == None:
                    continue
                
                if tw_anime["alt_title"] == db_anime_title or tw_anime["title"] == db_anime_title:
                    anime_is_correct = True
                    
                    database[db_anime]["title"].setdefault("twist_title", tw_anime["title"])
                    database[db_anime]["title"].setdefault("twist_alt_title", tw_anime["alt_title"])
                    
                    database[db_anime].setdefault("twist_moe_slug", tw_anime["slug"])
                    
                    break
            
            if anime_is_correct:
                break
