import requests
import json
import os
response_API = requests.get('http://localhost:8090/control/get?room=test')
data = response_API.text
parse_json = json.loads(data)
channelkey = parse_json["data"]
cmd = "ffmpeg -re -stream_loop -1 -i test.flv -c copy -f flv -flvflags no_duration_filesize rtmp://localhost:1935/live/"+channelkey
os.system (cmd)
