---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-batch-messages/
title: Retrieving HL7v2 messages in bulk \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:39.583372+00:00
---

# Retrieving HL7v2 messages in bulk  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-batch-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Retrieving HL7v2 messages in bulk Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to bulk read messages from an HL7v2 store using the [`projects.locations.datasets.hl7V2Stores.messages.batchGet`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores.messages/batchGet) method. You can use `batchGet` to retrieve up to 100 HL7v2 messages with a single call.

You can use the [`projects.locations.datasets.hl7V2Stores.messages.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/get) message to retrieve a single HL7v2 message at a time, but if you have many messages, you might encounter excessive network costs. To retrieve multiple messages in one API call, use `batchGet`.

## Getting HL7v2 messages in bulk

The following samples show how to get the contents of HL7v2 messages in bulk.

For more information, see [`projects.locations.datasets.hl7V2Stores.messages.batchGet`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores.messages/batchGet).

### curl

To get HL7v2 messages in bulk, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the HL7v2 store
  * An access token
  * The query parameter `names` with the names of the HL7v2 messages you want to retrieve. For each `names` value, enter the fully qualified path to the message in the format: `projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID`



The following sample shows a `GET` request using `curl`.
    
    
    curl -X GET \
          -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
          "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID
          /locations/LOCATION/datasets/DATASET_ID
          /hl7V2Stores/HL7V2_STORE_ID/messages:batchGet?names=MESSAGE_NAME_1&names=MESSAGE_NAME_2&names=
          MESSAGE_NAME_3&view=FULL"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "messages" : [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID"
        }
      ]
    }
    

### PowerShell

To get HL7v2 messages in bulk, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the HL7v2 store
  * An access token
  * The query parameter `names` with the names of the HL7v2 messages you want to retrieve. For each `names` value, enter the fully qualified path to the message in the format: `projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID`



The following sample shows a `GET` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages:batchGet?names=MESSAGE_NAME_1&names=MESSAGE_NAME_2&names=MESSAGE_NAME_3&view=FULL" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "messages" : [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/MESSAGE_ID"
        }
      ]
    }
    

## See also

  * [Creating and managing HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
