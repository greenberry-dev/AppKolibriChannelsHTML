import reportDAO
import csv
import json
from configparser import ConfigParser

config = ConfigParser()
config.read("config/serverConfig.cfg")

PATH_EXPORT_CSV = config["EXPORT"]["path_csv"]
PATH_EXPORT_JSON = config["EXPORT"]["path_json"]

def main():
    list_result = reportDAO.getData()
    list_data_csv = []

    fieldnames_csv = ['Canal', 'Recurso', 'Tipo', 'Peso(bytes)']
    for row in list_result:
        list_data_csv.append({'Canal': row['channel_name'],'Recurso': row['title'],'Tipo': row['kind'],'Peso(bytes)': row['file_size']})
     
    with open(PATH_EXPORT_CSV, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames_csv)
        writer.writeheader()
        writer.writerows(list_data_csv)

    json_object = json.dumps(list_result, indent=4)
    with open(PATH_EXPORT_JSON, "w") as outfile:
        outfile.write(json_object)

main()

