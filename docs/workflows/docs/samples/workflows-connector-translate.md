---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-translate/
title: Connector for Cloud Translation \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:21.381508+00:00
---

# Connector for Cloud Translation  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-translate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud Translation Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud Translation within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Translation API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/translate/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Translate connector:
    # Translate text from English to French
    # Create and delete a glossary (see https://cloud.google.com/translate/docs/advanced/glossary)
    # Expected output: "SUCCESS"
    - init:
        assign:
          - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - location_id: "us-central1"
          - glossary_id: "example-glossary-id"
    - list_supported_translation:
        call: googleapis.translate.v2.languages.list
        args:
          target: "fr"
    - basic_translate:
        call: googleapis.translate.v2.translations.translate
        args:
          q: "hello world"
          target: "fr"
          format: "text"
          source: "en"
    - create_glossary:
        call: googleapis.translate.v3.projects.locations.glossaries.create
        args:
          parent: ${"projects/" + project_id + "/locations/" + location_id}
          body:
            name: ${"projects/" + project_id + "/locations/" + location_id + "/glossaries/" + glossary_id}
            inputConfig:
              gcsSource:
                inputUri: "gs://translate-glossary-source/glossary.csv"
            languagePair:
              sourceLanguageCode: "en-US"
              targetLanguageCode: "fr-CA"
    - list_glossaries:
        call: googleapis.translate.v3.projects.locations.glossaries.list
        args:
          parent: ${"projects/" + project_id + "/locations/" + location_id}
    - delete_glossary:
        call: googleapis.translate.v3.projects.locations.glossaries.delete
        args:
          name: ${"projects/" + project_id + "/locations/" + location_id + "/glossaries/" + glossary_id}
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
