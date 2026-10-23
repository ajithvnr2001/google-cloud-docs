---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-firestore/
title: Connector for Firestore \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:03.241349+00:00
---

# Connector for Firestore  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Firestore Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Firestore within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Firestore API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Firestore connector:
    # Create and retrieve a Firestore document
    # Export the document to a Cloud Storage bucket (which must already exist)
    # Delete the document
    # Expected output: "SUCCESS"
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - collection: "example-collection"
          - document: "example-document"
    - create_document:
        call: googleapis.firestore.v1.projects.databases.documents.createDocument
        args:
          collectionId: ${collection}
          parent: ${"projects/" + project_id + "/databases/(default)/documents"}
          query:
            documentId: ${document}
          body:
            fields:
              fieldA:
                stringValue: abc
              fieldB:
                integerValue: 123
    - get_document:
        call: googleapis.firestore.v1.projects.databases.documents.get
        args:
          name: ${"projects/" + project_id + "/databases/(default)/documents/" + collection + "/" + document}
        result: got
    - check:
        switch:
          - condition: ${got.fields.fieldA.stringValue == "abc" AND int(got.fields.fieldB.integerValue) == 123}
            next: export
    - failed:
        raise: ${"got unexpected document" + "fieldA:" + got.fields.fieldA.stringValue + " fieldB:" + string(got.fields.fieldB.integerValue)}
    - export:
        call: googleapis.firestore.v1.projects.databases.exportDocuments
        args:
          name: ${"projects/" + project_id + "/databases/(default)"}
          body:
            outputUriPrefix: "gs://EXAMPLE_BUCKET"  # replace EXAMPLE_BUCKET placeholder with existing bucket
            collectionIds:
              - ${collection}
    - drop:
        call: googleapis.firestore.v1.projects.databases.documents.delete
        args:
          name: ${"projects/" + project_id + "/databases/(default)/documents/" + collection + "/" + document}
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
