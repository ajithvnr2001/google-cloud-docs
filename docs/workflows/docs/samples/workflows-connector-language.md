---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-language/
title: Connector for Cloud Natural Language \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:51.308685+00:00
---

# Connector for Cloud Natural Language  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-language/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Cloud Natural Language Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Cloud Natural Language within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Natural Language API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/language/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Cloud Language connector:
    # Analyze and classify text samples and log the results
    # Expected output: "SUCCESS"
    - init:
        assign:
          - docType: "PLAIN_TEXT"
    - analyze_entities:
        call: googleapis.language.v1.documents.analyzeEntities
        args:
          body:
            document:
              type: ${docType}
              language: "en"
              content: "Eiffel Tower"
            encodingType: "UTF8"
        result: response_analyze
    - log_analyze_result:
        call: sys.log
        args:
          data: ${response_analyze}
          severity: "INFO"
    - classify_text:
        call: googleapis.language.v1.documents.analyzeSentiment
        args:
          body:
            document:
              type: ${docType}
              language: "en"
              content: "I love Workflows!"
            encodingType: "UTF8"
        result: response_classify
    - log_classify_result:
        call: sys.log
        args:
          data: ${response_classify}
          severity: "INFO"
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
