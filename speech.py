# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import pygame
from urllib2 import Request
from urlparse import urlparse
from pygame import mixer, time

client_id = ""
client_secret = ""

class speech():
    """ TTS Module class.

    This class speaks the text of answer about user's question using Naver Korean TTS API.
    You can check the references at 'https://developers.naver.com/docs/labs/tts/'.
    """

    def play_sound(self, file_path):
        """ Play the sound of mp3 file using pygame mixer.

        Args:
            file_path : The file path of the mp3 file that user wants to play.
        """
        mixer.pre_init(44100, -16, 2, 256)
        mixer.init(frequency=16000, buffer=24000)
        pygame.init()
        mixer.music.load('/home/pi/response.mp3')
        mixer.music.play(loops=1)

        while mixer.music.get_busy():
            time.Clock().tick(100)

    def speak(self, input_text):
        """ Request TTS API with input_text and then save the output as mp3.

        Args:
            input_text : The input text of the answer from the user's question.
        """
        data = "speaker=mijin&speed=0&text=" + unicode(input_text);

        q = Request("https://openapi.naver.com/v1/voice/tts.bin")
        q.add_header("X-Naver-Client-Id", client_id)
        q.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib2.urlopen(q, data=data.encode('utf-8'))
        rescode = response.getcode()

        if(rescode == 200):
            response_body = response.read()
            filename = 'response.mp3'

            with open(filename, 'wb') as f:
                f.write(response_body)
                
            os.system('omxplayer -o local /home/pi/response.mp3')
        else:
            print("Error Code:" + rescode)
