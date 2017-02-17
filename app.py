#-*- coding: utf-8 -*-
# Created by JHJ on 2017. 2. 14.

if __name__ == '__main__':
    import speech_recognition as sr
    import sys
    from utils.my_requests import get_news
    from konlpy.tag import Twitter

    twitter = Twitter()

    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print "말해보세요!"
        audio = r.listen(source)

    try:
        speech_string = r.recognize_google(audio, language='ko-KR')
        print(speech_string)
        print(speech_string.replace(' ', ''))
        morphemes = twitter.nouns(speech_string.replace(' ', ''))
        print(morphemes)

        if u'뉴스' in morphemes or u'유스' in morphemes:
            try:
                news_index = morphemes.index(u'뉴스')
            except ValueError:
                news_index = morphemes.index(u'유스')
            else:
                news_index = len(morphemes) - 1

            query = ' '.join(morphemes[:news_index])
            print get_news(query, sys.argv[1], sys.argv[2])

    except sr.UnknownValueError:
        print "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Google Speech Recognition service; {0}".format(e)
