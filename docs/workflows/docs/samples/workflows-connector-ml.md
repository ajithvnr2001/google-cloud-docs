---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-ml/
title: Connector for AI Platform Training and Prediction \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:12.349760+00:00
---

# Connector for AI Platform Training and Prediction  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-ml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for AI Platform Training and Prediction Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access VertexAI (AI Platform) within a workflow. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [AI Platform Training & Prediction API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/ml/Overview)



## Code sample

### YAML
    
    
    # This workflow expects following items to be provided through input argument for execution:
    #   - projectID (string)
    #     - The user project ID.
    #
    # Expected successful output: "SUCCESS"
    
    main:
      params: [args]
      steps:
        - init:
            assign:
              - project_id: ${args.projectID}
        - list_jobs:
            call: googleapis.ml.v1.projects.jobs.list
            args:
              parent: ${"projects/" + project_id}
            result: jobs
        - list_locations:
            call: googleapis.ml.v1.projects.locations.list
            args:
              parent: ${"projects/" + project_id}
            result: locations
        - the_end:
            return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
