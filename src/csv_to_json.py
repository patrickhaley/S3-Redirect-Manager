import csv
import json
import os

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

csv_file_path = 'data/redirects.csv'
json_file_path = 'data/website-configuration.json'
new_domain = 'new.domain.com'  # Change this to your new domain

redirects = {"RoutingRules": []}

with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        rule = {
            "Condition": {
                "KeyPrefixEquals": row["Old Path"]
            },
            "Redirect": {
                "Protocol": row["Protocol"],
                "HostName": new_domain,
                "ReplaceKeyPrefixWith": row["New Path"],
                "HttpRedirectCode": row["Status Code"]
            }
        }
        redirects["RoutingRules"].append(rule)

with open(json_file_path, mode='w') as json_file:
    json.dump(redirects, json_file, indent=4)

print(f'JSON configuration saved to {json_file_path}')
