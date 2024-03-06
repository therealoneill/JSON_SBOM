import json
import csv
import pandas as pd
from extract import json_extract


#####Outputs the full contents

with open('F:\\1GIT\\JSON_SBOM\\swScheduler_SW2024_SP02_d240304.json') as fcc_file:
    fcc_data = json.load(fcc_file)
    #print(json.dumps(fcc_data, indent=4, sort_keys=True))

data = fcc_data["components"][1]

components = json_extract(data,'bom-ref')
print(components)