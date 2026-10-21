---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-transcoder/
title: Connector for Transcoder \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:22.293327+00:00
---

# Connector for Transcoder  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-transcoder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Transcoder Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Transcoder within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transcoder API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Transcoder API connector.
    # This workflow sends a List request to Transcoder API.
    main:
      steps:
        - init:
            assign:
              - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              - location: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}
        - get_list:
            call: googleapis.transcoder.v1.projects.locations.jobs.list
            args:
              parent: ${"projects/" + project + "/locations/" + location}
            result: response
        - the_end:
            return: ${response}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
