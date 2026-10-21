---
url: https://docs.cloud.google.com/speech-to-text/docs/word-confidence/
title: Specify word-level accuracy confidence levels \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:24.166621+00:00
---

# Specify word-level accuracy confidence levels  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/word-confidence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Specify word-level accuracy confidence levels Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can specify that Cloud Speech-to-Text indicate a value of accuracy, or [confidence level](https://docs.cloud.google.com/speech-to-text/docs/basics#confidence-values), for individual words in a transcription.

## Word-level confidence

When the Cloud Speech-to-Text transcribes an audio clip, it also measures the degree of accuracy for the response. The response sent from Cloud STT states the confidence level for the entire transcription request as a number between 0.0 and 1.0. The following code sample shows an example of the confidence level value returned by Cloud STT.
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "how old is the Brooklyn Bridge",
              **"confidence": 0.96748614**
            }
          ]
        }
      ]
    }
    

In addition to the confidence level of the entire transcription, Cloud STT can also provide the confidence level of individual words within the transcription. The response then includes [`WordInfo`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v2/projects.locations.recognizers/recognize#wordinfo) details in the transcription, indicating the confidence level for individual words as shown in the following example.
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "how old is the Brooklyn Bridge",
              "confidence": 0.98360395,
              "words": [
                {
                  "startOffset": "0s",
                  "endOffset": "0.300s",
                  "word": "how",
                  **"confidence": SOME NUMBER**
                },
                ...
              ]
            }
          ]
        }
      ]
    }
    

## Enable word-level confidence in a request

The following code snippet demonstrates how to enable word-level confidence in a transcription request to Cloud Speech-to-Text using local and remote files.

### Use a local file

### REST

Refer to the [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v2/projects.locations.recognizers/recognize) API endpoint for complete details.

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 

The following example show how to send a `POST` request using `curl`, where the body of the request enables word-level confidence.
    
    
    curl -s -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        https://speech.googleapis.com/v2/projects/{project}/locations/global/recognizers/{recognizers}:recognize \
        --data '{
        "config": {
            "features": {
                "enableWordTimeOffsets": true,
                "enableWordConfidence": true
            }
    **},**
        "uri": "gs://cloud-samples-tests/speech/brooklyn.flac"
    }' > word-level-confidence.txt

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format, saved to a file named `word-level-confidence.txt`.
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "how old is the Brooklyn Bridge",
              "confidence": 0.98360395,
              "words": [
                {
                  "startOffset": "0s",
                  "endOffset": "0.300s",
                  "word": "how",
                  "confidence": 0.98762906
                },
                {
                  "startOffset": "0.300s",
                  "endOffset": "0.600s",
                  "word": "old",
                  "confidence": 0.96929157
                },
                {
                  "startOffset": "0.600s",
                  "endOffset": "0.800s",
                  "word": "is",
                  "confidence": 0.98271006
                },
                {
                  "startOffset": "0.800s",
                  "endOffset": "0.900s",
                  "word": "the",
                  "confidence": 0.98271006
                },
                {
                  "startOffset": "0.900s",
                  "endOffset": "1.100s",
                  "word": "Brooklyn",
                  "confidence": 0.98762906
                },
                {
                  "startOffset": "1.100s",
                  "endOffset": "1.500s",
                  "word": "Bridge",
                  "confidence": 0.98762906
                }
              ]
            }
          ],
          "languageCode": "en-us"
        }
      ]
    }
    

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech_v1p1beta1 as speech
    
    client = speech.SpeechClient()
    
    speech_file = "resources/Google_Gnome.wav"
    
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_word_confidence=True,
    )
    
    response = client.recognize(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
        print(
            "First Word and Confidence: ({}, {})".format(
                alternative.words[0].word, alternative.words[0].confidence
            )
        )
    
    return response.results

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
