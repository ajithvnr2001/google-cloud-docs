---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-firestore-write/
title: Write to Firestore through an HTTP request \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:19.525985+00:00
---

# Write to Firestore through an HTTP request  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-firestore-write/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Write to Firestore through an HTTP request Stay organized with collections  Save and categorize content based on your preferences. 

Makes an authenticated request within a workflow, using OAuth 2.0 to write to Firestore.

## Code sample

### YAML
    
    
    - initialize:
        assign:
          - project: "myproject123"
          - collection: "myEntries"
          - document: "Visits"
    - write_item:
        call: http.request
        args:
          url: ${"https://firestore.googleapis.com/v1/projects/"+project+"/databases/(default)/documents/"+collection+"/"+document}
          auth:
            type: OAuth2
          method: PATCH
          body:
            name: ${"projects/"+project+"/databases/(default)/documents/"+collection+"/"+document}
            fields:
              Counter:
                integerValue: 7

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
