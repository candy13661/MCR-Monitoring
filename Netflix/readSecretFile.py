import json


class secret:
     def __init__(self, service):
        # -- Opening JSON file
        try:
            credential = open(r'C:\Users\mtmunian\OneDrive - MEASAT Broadcast Network Systems Sdn. Bhd\Desktop\Project\MCR Monitoring\secret\secret.json')
        except:
            print("Unable to locate Secret file. Ensure Secret file is present")

        # -- returns JSON object as a dictionary
        try:
            data = json.load(credential)
        except:
            print("Unable to read secret data. Ensure secret format is intact (JSON)")

        # -- Iterating through the json list
        for secret in data[service]:
            appUsrnm = secret["username"]
            appPass = secret["password"]
            #print(ntflxUsrnm)
            #print(ntflxPass)
        self.appUsrnm = appUsrnm
        self.appPass = appPass

        # -- Closing file
        credential.close()

#try:
    #p1 = secret("Netflix")
    #print(p1.appUsrnm)
    #print(p1.appPass)
#except:
    #print("Error reading JSON file - Please ensure file is exist and format is intact")
