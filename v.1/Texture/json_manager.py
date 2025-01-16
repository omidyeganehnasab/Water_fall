import json
import os

class objects :
    def varible(a = False, b = False, c = False, d = False, e = False)->bool:

        vertices    = config["vertices"] if a else None
        edges       = config["edge"]     if b else None
        surfaces    = config["surface"]  if c else None
        colors      = config["color"]    if d else None
        nesbat      = config["nesbat"]   if e else None
        
        return vertices, edges, surfaces, colors, nesbat 
        
    def open_file(name):
        global config
        file = open(f"Texture/{name}.json", "r", encoding="utf-8")
        config = json.load(file)
    
    