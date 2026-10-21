---
url: https://docs.cloud.google.com/speech-to-text/docs/medical-models/
title: Recognize speech by using medical models \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:39:05.037226+00:00
---

# Recognize speech by using medical models  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/medical-models/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Recognize speech by using medical models Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Speech-to-Text offers two _medical_ models in addition the other [standard and enhanced speech recognition models](https://docs.cloud.google.com/speech-to-text/docs/v1/transcription-model). The medical models are specifically tailored for recognition of words that are common in medical settings, such as diagnoses, medications, symptoms, treatments, and conditions. If you want to recognize this type of audio data, you can improve your transcription results by using these models.

There are two medical models, each tailored to specific use cases:

  * `medical_conversation`: for conversations between a medical provider—for example, a doctor or nurse—and a patient. Use this model when both a provider and a patient are speaking. Words uttered by each speaker are automatically detected and labeled in the returned transcript.
  * `medical_dictation`: for dictated notes spoken by a single medical provider—for example, a doctor dictating notes about a patient's blood test results.



Use medical models only with the following Cloud Speech-to-Text features. Features omitted from this list can't be used with either medical model. The automatic punctuation feature is enabled by default.

  * [Automatic punctuation](https://docs.cloud.google.com/speech-to-text/docs/v1/automatic-punctuation)
  * [Alternate transcriptions](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-requests#selecting_alternatives)
  * [Word timestamps](https://docs.cloud.google.com/speech-to-text/docs/v1/async-time-offsets)
  * [Word-level confidence](https://docs.cloud.google.com/speech-to-text/docs/v1/word-confidence)



The medical conversation model supports the following features:

  * [Speaker diarization](https://docs.cloud.google.com/speech-to-text/docs/v1/multiple-voices)



The medical dictation model supports the following features:

  * Spoken Punctuation
  * Formatting Commands
  * Spoken Headings



## Send a transcription request

### REST

The following code sample uses the `medical_conversation` model to transcribe an audio file in a public Cloud Storage bucket.

Before using any of the request data, make the following replacements: 

  * `LANGUAGE_CODE`: the BCP-47 code of the language spoken in your audio clip. Medical models are only available for _en-US_.
  * `ENCODING`: the encoding of the audio you want to transcribe. If you are using the public audio sample, the encoding is `LINEAR16`.
  * `PROJECT_ID`: the alphanumeric ID of your Google Cloud project.



HTTP method and URL: 
    
    
    POST https://speech.googleapis.com/v1/speech:recognize

Request JSON body: 
    
    
    {
      "config": {
        "languageCode": "LANGUAGE_CODE",
        "encoding": "ENCODING",
        "model": "medical_conversation"
      },
      "audio": {
        "uri": "gs://cloud-samples-data/speech/medical_conversation_2.wav"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://speech.googleapis.com/v1/speech:recognize"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://speech.googleapis.com/v1/speech:recognize" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
      "results": [
        {
          "alternatives": [
            {
              "transcript": "Um-hum . Yeah. Hello , good morning . Good
              morning . So , tell me what's going on . Uh , sure , so , um , I
              woke up probably three or four days ago , which , uh , wheezing and short of breath .
              Okay , any cough or chest pain ? I cough infrequently , but no ,
              uh , chest pain . Have you been exposed to anyone with covid ?
              Uh , no , and I also took a test , which was negative . Uh , is it getting
              worse , or better ? Uh , it has been getting a lot worse"
            }
          ]
        },
        {
          "alternatives": [
            {
              "transcript": "Okay . Was there something that triggered this exposure to cold , for
              example ? Um , I had a gone hiking , and I got caught in the rain the day
              before this all started ."
            }
          ]
        }
      ]
    }
    

## Spoken punctuation

The medical dictation model supports spoken punctuation for medical notes. This feature is enabled by default, and cannot be disabled. Spoken punctuation is delineated by brackets in the speech transcription. For example, your returned transcription might look similar to the following:

`Patient could be showing signs of trauma [question mark] They said they were [quote] having elevated heart rate [unquote]`.

Cloud Speech-to-Text supports the following spoken punctuation:

  * period
  * comma
  * colon
  * caps
  * slash
  * dash
  * hyphen
  * question mark
  * semicolon
  * quote
  * unquote
  * end quote
  * open parenthesis
  * close parenthesis
  * end parenthesis



## Formatting commands

The medical dictation model supports spoken commands for formatting notes. This feature is enabled by default, and cannot be disabled. The spoken commands will be delineated by brackets in the speech transcription. For example, your returned transcription might look similar to the following:

`[next line] Patient says they are experiencing fever [next point]`.

Cloud Speech-to-Text supports the following spoken commands:

  * next point
  * next number
  * next paragraph
  * caps
  * capitalization
  * new line
  * next item
  * next problem
  * next problem number
  * next row
  * next section
  * number next
  * scratch
  * scratch that
  * end dictation



## Spoken headings

The medical dictation model supports spoken headings for dictated notes. This feature is enabled by default, and cannot be disabled. The headings will be delineated by brackets in the transcription and will be capitalized. For example, your returned transcription might look similar to the following:

`[CURRENT MEDICATIONS] Patient is currently taking no medications`.

Cloud Speech-to-Text supports the following spoken headings:

  * CHIEF COMPLAINT
  * CURRENT MEDICATIONS
  * DISCHARGE MEDICATIONS
  * DISCHARGE PLAN
  * FAMILY HISTORY
  * FINDINGS
  * REVIEW OF SYSTEMS
  * HISTORY OF PRESENT ILLNESS
  * INDICATIONS
  * LABS
  * PAST SURGICAL HISTORY
  * PHYSICAL EXAM
  * REVIEW OF SYSTEMS
  * RADIOLOGY



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
