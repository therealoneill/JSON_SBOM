import json

with open('F:\\1GIT\\JSON_SBOM\\swScheduler_SW2024_SP02_d240304.zip.cyclonedx.json') as fcc_file:
    fcc_data = json.load(fcc_file)
    print(json.dumps(fcc_data, indent=4, sort_keys=True))