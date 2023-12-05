import requests
import json
import datetime

def callAPI(notificationTitle, notificationDetail):

  #notificationTitle = 'Service Down'
  #notificationDetail = 'Service Down'
  createddate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  url = "https://astrocloud.webhook.office.com/webhookb2/f7f40d76-7e35-4830-ba04-80c093af1e4d@84934ccb-279a-44ec-ac04-af10fec22a71/IncomingWebhook/56992099b8914e20bc73650fdefde9e3/80b00fec-c770-49d1-9567-9eb1360de7db"

  payload = json.dumps({
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "0076D7",
    "summary": "Monitoring notification for Netflix service",
    "sections": [
      {
        "activityTitle": notificationTitle,
        "activitySubtitle": notificationDetail,
        "activityImage": "https://cdn.hashnode.com/res/hashnode/image/upload/v1647410910018/spTELtuIz.jpeg",
        "facts": [
          {
            "name": "Assigned to",
            "value": "MCR Team"
          },
          {
            "name": "Date",
            "value": createddate
          },
          {
            "name": "Status",
            "value": "Not started"
          }
        ],
        "markdown": True
      }
    ],
    "potentialAction": [
      {
        "@type": "ActionCard",
        "name": "Add a comment",
        "inputs": [
          {
            "@type": "TextInput",
            "id": "comment",
            "isMultiline": False,
            "title": "Add a comment here for this task"
          }
        ],
        "actions": [
          {
            "@type": "HttpPOST",
            "name": "Add comment",
            "target": "https://docs.microsoft.com/outlook/actionable-messages"
          }
        ]
      },
      {
        "@type": "ActionCard",
        "name": "Change status",
        "inputs": [
          {
            "@type": "MultichoiceInput",
            "id": "list",
            "title": "Select a status",
            "isMultiSelect": "false",
            "choices": [
              {
                "display": "In Progress",
                "value": "1"
              },
              {
                "display": "Active",
                "value": "2"
              },
              {
                "display": "Closed",
                "value": "3"
              }
            ]
          }
        ],
        "actions": [
          {
            "@type": "HttpPOST",
            "name": "Save",
            "target": "https://docs.microsoft.com/outlook/actionable-messages"
          }
        ]
      }
    ]
  })
  headers = {
    'Content-Transfer-Encoding': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)


#callAPI('Netflix Service Down Alert','Netflix playback error')
