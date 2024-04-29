from mailjet_rest import Client
import os

api_key = 'b42834fa96fbcd0c92350476c845a050'
api_secret = os.environ["MAIL_CONNECTION"]


def send_email(id, data):
  mailjet = Client(auth=(api_key, api_secret), version='v3.1')
  data = {
      'Messages': [{
          "From": {
              "Email": "jl567056@dal.ca",
              "Name": "Joel Kuruvilla"
          },
          "To": [{
              "Email": data["email"],
              "Name": data["full_name"]
          }],
          "Subject": "Application Submitted Sucessfully",
          "TextPart": "My first Mailjet email",
          "HTMLPart":
          "This email confrims that the form used on this application has successfully been processed. Thank you for checking out my project!",
          "CustomID": "AppGettingStartedTest"
      }]
  }

  result = mailjet.send.create(data=data)
  print(result.status_code)
  print(result.json())
