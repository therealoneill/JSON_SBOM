import json
import pandas as pd


#####Outputs the full contents

with open('F:\\1GIT\\JSON_SBOM\\swScheduler_SW2024_SP02_d240304.json') as fcc_file:
    fcc_data = json.load(fcc_file)
    #print(json.dumps(fcc_data, indent=4, sort_keys=True))

#print(len(fcc_data["components"]))
#print((fcc_data["components"][0]["bom-ref"]))
    
for component in fcc_data["components"]:
    print(component["name"])
    for subcomponent in component["components"]:
        print(subcomponent["name"])
        for hash in subcomponent["hashes"]:
            print(hash["alg"])
    #print(component["components"])
    print(component["purl"])
    print(component["type"])

