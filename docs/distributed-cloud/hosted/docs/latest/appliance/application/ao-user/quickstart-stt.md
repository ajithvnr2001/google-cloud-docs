---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-stt/
title: Transcribe audio \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:50.496973+00:00
---

# Transcribe audio  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-stt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Transcribe audio Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to transcribe audio files into text using the Speech-to-Text API on Google Distributed Cloud (GDC) air-gapped appliance.

The Speech-to-Text service of Vertex AI on GDC air-gapped appliance recognizes speech from audio files. Speech-to-Text converts the detected audio into text transcriptions using its pre-trained API.

## Before you begin

Before you can start using the Speech-to-Text API, you must have a project with the Speech-to-Text API enabled and have the appropriate credentials. You can also install client libraries to help you make calls to the API. For more information, see [Set up a speech recognition project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-set-up-stt).

## Transcribe audio with the default model

Speech-to-Text performs speech recognition. You send the audio file from which you want to recognize speech directly as content in the API request. The system returns the resulting transcribed text in the API response.

You must provide a `RecognitionConfig` configuration object when making a speech recognition request. This object tells the API how to process your audio data and what kind of output you expect. If a model is not explicitly specified in this configuration object, Speech-to-Text selects a default model. Speech-to-Text on GDC air-gapped appliance only supports the default model.

Follow these steps to use the Speech-to-Text service from a Python script to transcribe speech from an audio file:

  1. [Install the latest version of the Speech-to-Text client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries).

  2. [Set the required environment variables on a Python script](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-set-up-stt#set-env-var).

  3. [Authenticate your API request](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-auth).

  4. Add the following code to the Python script you created:
         
         import base64
         
         from google.cloud import speech_v1p1beta1
         import google.auth
         from google.auth.transport import requests
         from google.api_core.client_options import ClientOptions
         
         audience="https://ENDPOINT:443"
         api_endpoint="ENDPOINT:443"
         
         def get_client(creds):
           opts = ClientOptions(api_endpoint=api_endpoint)
           return speech_v1p1beta1.[SpeechClient](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.services.speech.SpeechClient.html)(credentials=creds, client_options=opts)
         
         def main():
           creds = None
           try:
             creds, project_id = google.auth.default()
             creds = creds.with_gdch_audience(audience)
             req = requests.Request()
             creds.refresh(req)
             print("Got token: ")
             print(creds.token)
           except Exception as e:
             print("Caught exception" + str(e))
             raise e
           return creds
         
         def speech_func(creds):
           tc = get_client(creds)
         
           content="BASE64_ENCODED_AUDIO"
         
           audio = speech_v1p1beta1.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.RecognitionAudio.html)()
           audio.content = base64.standard_b64decode(content)
           config = speech_v1p1beta1.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.RecognitionConfig.html)()
           config.encoding= speech_v1p1beta1.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.RecognitionConfig.html).[AudioEncoding](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.RecognitionConfig.AudioEncoding.html).ENCODING
           config.sample_rate_hertz=RATE_HERTZ
           config.language_code="LANGUAGE_CODE"
           config.audio_channel_count=CHANNEL_COUNT
         
           metadata = [("x-goog-user-project", "projects/PROJECT_ID")]
           resp = tc.recognize(config=config, audio=audio, metadata=metadata)
           print(resp)
         
         if __name__=="__main__":
           creds = main()
           speech_func(creds)
         

Replace the following:

     * `ENDPOINT`: the Speech-to-Text endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status).
     * `PROJECT_ID`: your project ID.
     * `BASE64_ENCODED_AUDIO`: the audio data bytes encoded in a Base64 representation. This string begins with characters that look similar to `ZkxhQwAAACIQABAAAAUJABtAA+gA8AB+W8FZndQvQAyjv`.
     * `ENCODING`: the encoding of the audio data sent in the request, such as `LINEAR16`.
     * `RATE_HERTZ`: sample rate in Hertz of the audio data sent in the request, such as `16000`.
     * `LANGUAGE_CODE`: the language of the supplied audio as a BCP-47 language tag. See the list of [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-stt-supported-langs) and their respective language codes.
     * `CHANNEL_COUNT`: the number of channels in the input audio data, such as `1`.
  5. Save the Python script.

  6. Run the Python script to transcribe audio:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, for example, `speech.py`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
