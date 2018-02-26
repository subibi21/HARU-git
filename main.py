#-*- coding: utf-8 -*- 
import wita
import wit
import speech
import datetime
from detector import hotword
from os import listdir
from os.path import abspath, dirname
import json
import sys
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'api.ai client_access_token'
class Main:
      def __init__(self):
          self.detector = hotword.hotword()
          self.speaker = speech.speech()
          self.speaker.speak(u'안녕하세요')
          self.speaker.speak(u'하루를 시작합니다..')
          

      def main_flow(self):
        
          ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
          request = ai.text_request()
          request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
          request.time_zone = 'Asia/Tokyo'

          print('[haru] recording now')
          self.speaker.speak(u'말씀하세요')
          rec = wita.RecognizeSpeech('myspeech.wav', 3)
          print(rec)
          post = rec
          request.query = post
          byte_response = request.getresponse().read()
          json_response = byte_response.decode('utf8').replace("'", '"') # replaces all quotes with double quotes
          response = json.loads(json_response)
          message = response['result']['fulfillment']['speech']
          if message == "":
             self.speaker.speak(u'없는 명령어 입니다.')
             self.detector.start_detection(self.main_flow)
          else:
              self.speaker.speak(message)
          



              self.detector.start_detection(self.main_flow)




      def run(self):
          # Detecting wake-up word.
          self.detector.start_detection(self.main_flow)

if __name__ == "__main__":
    print('[HARU] Starting the HARU')
    haru = Main()
    haru.run()

