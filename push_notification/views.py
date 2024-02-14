from django.http import HttpResponse
from django.shortcuts import render
from firebase_admin import messaging
import firebase_admin
from firebase_admin import credentials
import requests, json
import google.auth.transport.requests
from google.oauth2 import service_account


service_account_file_path = "C:\\Users\\Vaibhav\\Desktop\\New folder (2)\\notification\\push_notification\\service_account.json"
cred = credentials.Certificate(service_account_file_path)
firebase_admin.initialize_app(cred)



PROJECT_ID = 'notification-2a4ae'
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/messages:send'
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT


def index(request):
    return render(request, 'index.html')


def showFirebaseJS(request):
  return render(request, 'firebaseJS.html')


def send_notification(registration_ids, message_title, message_description, topic):
    res = messaging.subscribe_to_topic(registration_ids, topic=topic)
    message = messaging.Message(
        topic="news",
        notification=messaging.Notification(
            title=message_title,
            body=message_description
        )
    )
    response = messaging.send(message);
    return HttpResponse("Subscribed to topic & Message Sent")


# SOME JS is missing which does not show notification on DESKTOP, RESOLVE THAT ISSUE
def send(request):
    registration = [
      "cJETG0wBaiaAD__82onqvn:APA91bGkRxgx1gW12mdrp0-Z1GwS0C7FJ10OWZgbz5xEdGUgG1Ku8sFvcMfR8H2fhVcdpQGQOYcXdfKS_j90VKWDARJ8frmI53ev33RiPIi9jIDSBO1GSW1rYkYxQD2NpEduu9rjYbqI",
      "eQG0FZFLEQWMgs-_55cRZF:APA91bEEkUHV6cXp12R_mWFY5LtyXDFq91PyVOYTiuqdSukz_K7cwKGYoZHCiwK1j8ByqqEVX7y70c1KtcQywnJbYGE9Gor6gZHwudKm9aEpsmB13NWM6RCFcFiDZtydM4lwEn_3NjSB",
    ]
    title = "Solvify Hub"
    description = "hello Vaibhav, this message is from firebase push notification"
    topic = "news"

    result = send_notification(registration, title, description, topic)
    return HttpResponse(result)





# def _get_access_token():
#   credentials = service_account.Credentials.from_service_account_file(service_account_file_path, scopes=SCOPES)
#   request = google.auth.transport.requests.Request()
#   credentials.refresh(request)
#   return credentials.token


# def _send_fcm_message(fcm_message):
#   """Send HTTP request to FCM with given message.
#   Args:
#     fcm_message: JSON object that will make up the body of the request.
#   """
#   # [START use_access_token]
#   headers = {
#     'Authorization': 'Bearer ' + _get_access_token(),
#     'Content-Type': 'application/json; UTF-8',
#   }
#   # [END use_access_token]
#   response = requests.post(FCM_URL, data=json.dumps(fcm_message), headers=headers)

#   if response.status_code == 200:
#     print('Message sent to Firebase for delivery, response:')
#     print(response.text)
#   else:
#     print('Unable to send message to Firebase')
#     print(response.text)


# def _build_common_message():
#   return {
#     'message': {
#       'topic': 'news',
#       'notification': {
#         'title': 'FCM Notification',
#         'body': 'Notification from FCM'
#       }
#     }
#   }
