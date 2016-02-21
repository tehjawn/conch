from subprocess import call
import speech_recognition as sr
import wit
import json
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
wit.init()

 #try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
inputSpeech = r.recognize_google(audio)
print(inputSpeech)


#print(format(wit.text_query(inputSpeech, "OK3GYG6TYL4YGW7RTSXNCA4AFSK4Y2JD")))
parsedCommand = json.loads(format(wit.text_query(inputSpeech, "OK3GYG6TYL4YGW7RTSXNCA4AFSK4Y2JD")))
print(">" + parsedCommand['outcomes'][0]['entities']['echo_text'][0]['value'])
#print json.dumps(parsedCommand, sort_keys=True, indent=4)
wit.close()
#except sr.UnknownValueError:
 #   print("Google Speech Recognition could not understand audio")
#except sr.RequestError as e:
 #   print("Could not request results from Google Speech Recognition service; {0}".format(e))

