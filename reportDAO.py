import sqlite3
from sqlite3 import Error
## from configparser import ConfigParser

## config = ConfigParser()
## config.read("config/serverConfig.cfg")

## DB_PATH_KOLIBRI = config["SQLITE"]["path"]
DB_PATH_KOLIBRI = "/ubuntu/home/.kolibri/db.sqlite3"

def getData():
    conn = None
    list_data = []
    try:
        sql = ""
        sql = sql + "SELECT "
        sql = sql + "    cn.channel_id, "
        sql = sql + "    cmd.name as channel_name,"
        sql = sql + "    cn.title, "
        sql = sql + "    cn.kind, "
        sql = sql + "    (  "
        sql = sql + "        SELECT sum(clf.file_size) "
        sql = sql + "        FROM content_file cf  "
        sql = sql + "            INNER JOIN content_localfile clf  "
        sql = sql + "            ON(clf.id = cf.local_file_id)  "
        sql = sql + "        WHERE cf.contentnode_id = cn.id AND clf.available = 1 "
        sql = sql + "    ) as file_size "
        sql = sql + "FROM  "
        sql = sql + "content_contentnode cn INNER JOIN content_channelmetadata cmd ON(cmd.id = cn.channel_id)   "
        sql = sql + "WHERE cn.level <> 0 and cn.kind <> 'topic' and cn.available = 1  ORDER BY cn.channel_id,cn.id "

        conn = sqlite3.connect(DB_PATH_KOLIBRI,uri=True)
        result = conn.execute(sql)        
        for row in result:
            list_data.append({ "channel_id": row[0],"channel_name": row[1],"title": row[2],"kind": row[3],"file_size": row[4] })
        return list_data
    except Error as e:
        print(e)
        list_data = []
    finally:
        if conn:
            conn.close()
        return list_data