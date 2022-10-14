#!/usr/bin/python
# -- coding: utf-8 --
import reportDAO
import csv
import json
import pandas as pd
import os
## from configparser import ConfigParser

## config = ConfigParser()
## config.read("config/serverConfig.cfg")

## PATH_EXPORT_CSV = config["EXPORT"]["path_csv"]
## PATH_EXPORT_JSON = config["EXPORT"]["path_json"]
PATH_EXPORT_CSV = "/var/www/html/data/csv/channel_resources.csv"
PATH_EXPORT_JSON = "/var/www/html/data/csv/channel_resources.json"

def main():
    list_result = reportDAO.getData()
    list_data_csv = []

    if( os.path.exists(PATH_EXPORT_CSV) ):
        os.remove(PATH_EXPORT_CSV)
        
    if( os.path.exists(PATH_EXPORT_JSON) ):
        os.remove(PATH_EXPORT_JSON)

    for row in list_result:
        channel_name = str(row['channel_name']).replace(";",",")
        title = str(row['title']).replace(";",",")
        kind = str(row['kind']).replace(";",",")
        list_data_csv.append({'Canal': channel_name,'Recurso': title,'Tipo': kind,'Peso(bytes)': row['file_size']})
     
    df = pd.DataFrame(list_data_csv)
    df.reset_index(drop=True)
    df.to_csv(PATH_EXPORT_CSV,sep=';',encoding='utf-8-sig',index=False)

    json_object = json.dumps(list_result, indent=4)
    with open(PATH_EXPORT_JSON, "w") as outfile:
        outfile.write(json_object)

main()

