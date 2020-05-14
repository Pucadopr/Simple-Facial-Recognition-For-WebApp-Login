import json, requests, subprocess, shlex

def execute_request():
    bashCommand = '''curl --request POST --url https://lambda-face-recognition.p.rapidapi.com/recognize 
    --header 'content-type: multipart/form-data' 
    --header 'x-rapidapi-host: lambda-face-recognition.p.rapidapi.com' 
    --header 'x-rapidapi-key: 1794ca7c5emsh4f93122f2da1526p160e99jsn525b3e7ea18c' 
    --form albumkey=437fa409e7fed8b887be429f13d308e350e96ba078f97d6557c685de8f90d583
    --form album=URIMM --form files=@photo.jpg'''

    args = shlex.split(bashCommand)
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    output, error = process.communicate()
    json_obj = json.loads(output)
    return json_obj

def check_confidence(json_obj):
    if json_obj['status'] == 'success':
        if len(json_obj['photos'][0]['tags']) == 0:
            return False
        confidence = json_obj['photos'][0]['tags'][0]['uids'][0]['confidence']
        flag = False
        if confidence > 0.4:
            flag = True
        return flag