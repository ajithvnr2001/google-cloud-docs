---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-firestore-read/
title: Connector for Firestore (read) \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:20.469945+00:00
---

# Connector for Firestore (read)  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connect-firestore-read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Firestore (read) Stay organized with collections  Save and categorize content based on your preferences. 

Reads from Firestore using a Workflows connector.

## Code sample

### YAML
    
    
    - initialize:
        assign:
          - project: "myproject123"
          - collection: "myEntries"
          - document: "Report"
    - read_item:
        try:
          call: http.get
          args:
            url: ${"https://firestore.googleapis.com/v1/projects/"+project+"/databases/(default)/documents/"+collection+"/"+document}
            auth:
              type: OAuth2
          result: document_value
        except:
          as: e
          steps:
            - is_the_key_found:
                switch:
                  - condition: ${e.code == 404}
                    next: document_not_found
                  - condition: ${e.code == 403}
                    next: auth_error
        next: document_found
    - document_not_found:
        return: "Document not found."
    - auth_error:
        return: "Authentication error."
    - document_found:
        return: ${document_value.body.fields.LastName.stringValue}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
