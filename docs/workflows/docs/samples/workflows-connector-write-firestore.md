---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-write-firestore/
title: Connector for Firestore (write) \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:57.550410+00:00
---

# Connector for Firestore (write)  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-write-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Firestore (write) Stay organized with collections  Save and categorize content based on your preferences. 

Writes to Firestore using a Workflows connector.

## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Firestore connector:
    # Write data to a document in the default Firestore database
    # Expected output: "projects/PROJECT_ID/databases/(default)/documents/peopleDatabase/smith.j"
    - init_variables:
        assign:
          - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - collection: "peopleDatabase"
          - document: "smith.j"
          - values_to_write:
              FirstName:
                stringValue: "John"
              LastName:
                stringValue: "Smith"
              Age:
                integerValue: 32
    - write_to_firestore:
        call: googleapis.firestore.v1.projects.databases.documents.patch
        args:
          name: ${"projects/"+project+"/databases/(default)/documents/"+collection+"/"+document}
          body:
            fields: ${values_to_write}
        result: write_result
    - last:
        return: ${write_result.name}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
