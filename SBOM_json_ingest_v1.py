import json
import pandas as pd


#####Outputs the full contents

with open('F:\\1GIT\\JSON_SBOM\\swScheduler_SW2024_SP02_d240304.json') as fcc_file:
    fcc_data = json.load(fcc_file)
    #print(json.dumps(fcc_data, indent=4, sort_keys=True))

df = pd.json_normalize(fcc_data['components'])

#print(df)
df.to_csv('output.csv')