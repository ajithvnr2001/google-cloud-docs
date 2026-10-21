---
url: https://docs.cloud.google.com/speech-to-text/docs/locations/
title: Regional availability \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:39.280214+00:00
---

# Regional availability  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Regional availability Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In Cloud Speech-to-Text API V2, there are different availabilities in different regions. To understand the availabilities, use the Locations API.

## Location Metadata

Each location returned by the Locations API has metadata associated with it that details the languages, models, and model features that are available. A sample location with its metadata is shown below.
    
    
    {
      "locationId": "europe-west1",
      "metadata": {
        "languages": {
          "models": {
            "es-ES": {
              "modelFeatures": {
                "latest_long": {
                  "modelFeature": [
                    {"feature": "profanity_filter", "releaseState": "GA"},
                    {"feature": "spoken_punctuation", "releaseState": "GA"},
                    {"feature": "automatic_punctuation", "releaseState": "GA"},
                    {"feature": "speaker_diarization", "releaseState": "PREVIEW_DIARIZATION"},
                  ]
                }
              }
            }
          }
        }
      }
    }
    

## Filtering in List Locations

When listing all availabilities, a filter can be used. The different criteria that can be used to filter are the following:

  * `language` Optional. The BCP-47 language tag of the language desired.
  * `model` Optional. The model desired.
  * `model_feature` Optional. The model feature desired.



A sample filter query is shown below. Please see [filter syntax](https://google.aip.dev/160) for further reference.
    
    
    "language = en-US AND model = latest_long AND model_feature != profanity_filter"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
