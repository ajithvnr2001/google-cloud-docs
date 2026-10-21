---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-batch-translation/
title: Run a batch translation using the Cloud Translation connector \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:00:56.846207+00:00
---

# Run a batch translation using the Cloud Translation connector  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-batch-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Run a batch translation using the Cloud Translation connector Stay organized with collections  Save and categorize content based on your preferences. 

Runs a batch translation using the Cloud Translation connector.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Invoke a Google Cloud service using a connector](https://docs.cloud.google.com/workflows/docs/invoke-connector-to-gcp-service)
  * [Run a batch translation using the Cloud Translation connector](https://docs.cloud.google.com/workflows/docs/tutorials/translation-connector)



## Code sample

### YAML
    
    
    main:
      steps:
      - init:
          assign:
          - projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - location: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}
          - inputBucketName: ${projectId + "-input-files"}
          - outputBucketName: ${projectId + "-output-files-" + string(int(sys.now()))}
      - createOutputBucket:
            call: googleapis.storage.v1.buckets.insert
            args:
              project: ${projectId}
              body:
                name: ${outputBucketName}
      - batchTranslateText:
          call: googleapis.translate.v3beta1.projects.locations.batchTranslateText
          args:
              parent: ${"projects/" + projectId + "/locations/" + location}
              body:
                  inputConfigs:
                    gcsSource:
                      inputUri: ${"gs://" + inputBucketName + "/*"}
                  outputConfig:
                      gcsDestination:
                        outputUriPrefix: ${"gs://" + outputBucketName + "/"}
                  sourceLanguageCode: "en"
                  targetLanguageCodes: ["es", "fr"]
          result: batchTranslateTextResult

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
