import requests
import json


class Octadesk:
    def __init__(self, username, APItoken, baseUrl='https://api.octadesk.services'):
        self.username = username
        self.APItoken = APItoken
        self.baseUrl = baseUrl
        self.bearerToken = None

    # Método de login utilizando a APItoken
    def login(self, url='/login/apiToken'):

        headers = {'Content-Type': 'application/json',
                   'username': self.username,
                   'apiToken': self.APItoken}

        res = requests.post(self.baseUrl + url, headers=headers)

        if 'token' in res.json():
            self.bearerToken = 'Bearer ' + res.json()['token']
            return self.bearerToken
        else:
            return res.json()

    # Método para criar ticket com o mínimo de parâmetros
    def ticketCreate(self, title, body, tags, toEmail, toDomain, url='/tickets'):

        ticket = {
                  "requester": {
                    "email": self.username,
                    "name": ""
                  },
                  "numberChannel": 0,
                  "summary": title,
                  "tags": tags,
                  "inbox": {
                      "domain": toDomain,
                      "email": toEmail
                  },
                  "comments": {
                      "description": {
                          "content": body
                      }
                  }
                }

        headers = {'Content-Type': 'application/json',
                   'Authorization': self.bearerToken}
        res = requests.post(self.baseUrl + url, headers=headers, data=json.dumps(ticket))
        return res.json()['number']
