import azure.cognitiveservices.speech as speechsdk
# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "8d997fd93eaa464ab700491799f075d2", "westus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Receives a text from console input.
print("Type some text that you want to speak...")
text = input()

# Synthesizes the received text to speech.
# The synthesized speech is expected to be heard on the speaker with this line executed.
result = speech_synthesizer.speak_text_async(text).get()

# Checks result.
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")



if __name__ == "__main__":
    subscription_key = "8d997fd93eaa464ab700491799f075d2"
    #app = TextToSpeech(subscription_key)
    #app.get_token()
    #app.save_audio()
    #get_token(subscription_key)
    # eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJyZWdpb24iOiJ3ZXN0dXMiLCJzdWJzY3JpcHRpb24taWQiOiJkMGYzZTk0NmE2ODM0MTNjYTMzMDJhYjVhOTJlOWY4NiIsInByb2R1Y3QtaWQiOiJTcGVlY2hTZXJ2aWNlcy5GcmVlIiwiY29nbml0aXZlLXNlcnZpY2VzLWVuZHBvaW50IjoiaHR0cHM6Ly9hcGkuY29nbml0aXZlLm1pY3Jvc29mdC5jb20vaW50ZXJuYWwvdjEuMC8iLCJhenVyZS1yZXNvdXJjZS1pZCI6IiIsInNjb3BlIjoic3BlZWNoc2VydmljZXMiLCJhdWQiOiJ1cm46bXMuc3BlZWNoc2VydmljZXMud2VzdHVzIiwiZXhwIjoxNTgyMDQwMTQ5LCJpc3MiOiJ1cm46bXMuY29nbml0aXZlc2VydmljZXMifQ.Z_WgKHcgcHfbjjcRQvwrawC2cgQXgmS-UX9SNuPI1i4 

# Request module must be installed.
# Run pip install requests if necessary.







