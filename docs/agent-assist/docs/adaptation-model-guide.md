---
url: https://docs.cloud.google.com/agent-assist/docs/adaptation-model-guide/
title: Set up Speech-to-Text model adaptation \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:42:36.052944+00:00
---

# Set up Speech-to-Text model adaptation  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/adaptation-model-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Set up Speech-to-Text model adaptation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Agent Assist uses the [Speech-to-Text model adaptation](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model) to improve transcription quality by recognizing certain phrases more frequently than others. This page provides a guide to setting up model adaptation for Speech-to-Text transcription.

## Use the Speech-to-Text console

You can create only global phrase sets with the Speech-to-Text console. Regional phrase sets must be created using the Speech-to-Text API.

  1. In the Google Cloud console, go to the **Speech-to-Text** page. [Go to Speech-to-Text](https://console.cloud.google.com/speech)
  2. Click **Model Adaptations**.
  3. Click **add_box New Resource**.
  4. Choose the **Phrase set** resource and API version **V1** , then fill in the phrases and boost values, then copy the [phrase set](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model#improve_recognition_of_words_and_phrases) name.
  5. Click **Save**.
  6. Navigate to the [Agent Assist console](https://agentassist.cloud.google.com/).
  7. Click **Conversation Profiles** , then choose the conversation profile you want to edit.
  8. Go to the **Phrase sets** section and paste the phrase set name.

**Note:** The Chirp 3 model in the Speech-to-Text config doesn't support adaptation with prebuilt phrase sets. Check [Transcription with Chirp 3](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription-with-chirp3) for details on using Chirp 3 with inline phrase sets for Voice Transcription.

## Use the Speech-to-Text API

  1. Create a phrase set script by following the [speech recognition instructions](https://docs.cloud.google.com/speech-to-text/docs/adaptation).
  2. Run the following Python script to update your conversation profile: 
         
         # Conversation Profile to update
         PROJECT_ID = "sample-project"
         LOCATION = "global"
         CONVERSATION_PROFILE_ID = "sample-conversation-profile"
         # Speech model adaptation resource names
         SPEECH_ADAPTATION_PHRASES = ["projects/sample-project/locations/global/phraseSets/sample-phrase-sets"]
         
         
         
         import google.auth
         from google.auth.transport.requests import AuthorizedSession
         
         
         
         
         
         scopes=['https://www.googleapis.com/auth/cloud-platform']
         credentials, project = google.auth.default(
           scopes=scopes,
           quota_project_id=PROJECT_ID,
         )
         session = AuthorizedSession(credentials)
         
         
         
         
         
         profile_url = f"https://dialogflow.googleapis.com/v2beta1/projects/{PROJECT_ID}/locations/{LOCATION}/conversationProfiles/{CONVERSATION_PROFILE_ID}"
         get_response = session.get(profile_url)
         print("Checking for existing ConversationProfile...")
         print(get_response.status_code)
         print(get_response.json())
         if get_response.status_code == 200:
           patch_response = session.patch(
              profile_url,
              params={
                 "updateMask": "sttConfig.phraseSets"
              },
              json={
                 "sttConfig": {
                    "phraseSets": SPEECH_ADAPTATION_PHRASES
                 }
              }
           )
           print("Updating ConversationProfile...")
           print(patch_response.status_code)
           print(patch_response.json())
         




### Regional phrase sets

While Speech-to-Text model adaptation supports only English (`en-US`), you can configure phrase sets for other language regions with the Speech-to-Text API. This is particularly useful when transcribing English conversations that take place in those regions.

Use the following sample command to create regional phrase sets with the Speech-to-Text API.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -H "X-Goog-User-Project: sample_project" \
        -d @sample_phrase_sets.json \
    "https://us-speech.googleapis.com/v1/projects/sample-project/locations/us/phraseSets"

The json file `@sample_phrase_sets.json` contains the following contents of the phrase sets: 
    
    
    {
      "parent": "projects/sample-project/locations/us",
      "phraseSetId": "sample-phrase-sets",
      "phraseSet": {
        "name": "sample-phrase-sets",
        "phrases": [
          {
            "value": "Some phrase",
            "boost": 20
          }
        ]
      }
    }
    

For a conversation profile in a single Dialogflow region, the following table shows the corresponding Speech-to-Text region in which to create your phrase set. Dialogflow region | Speech-to-Text region  
---|---  
us   
us-central1   
us-east1   
us-east7   
us-west1   
northamerica-northeast1   
northamerica-northeast2 | us   
eu   
europe-west1   
europe-west2   
europe-west3   
europe-west4   
| eu   
australia-southeast1   
asia-northeast1   
asia-south1   
asia-southeast1   
me-west1   
global | global   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
