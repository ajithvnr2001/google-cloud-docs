---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/main/
title: Main workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:53.838407+00:00
---

# Main workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/main/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Main workflow Stay organized with collections  Save and categorize content based on your preferences. 

A workflow source file can contain only one main workflow and, as a best practice, we recommend placing your main workflow in a `main` block.

If a workflow has a [subworkflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows), the main workflow must be placed in a `main` block. Similarly, for a workflow to receive [runtime arguments](https://docs.cloud.google.com/workflows/docs/reference/syntax/runtime-args) there must be a `main` block.

### YAML
    
    
      main:
          params: [MAP_NAME]
          steps:
              - STEP_NAME:
                  ...
              ...
      

### JSON
    
    
        {
          "main": {
            "params": [
              "MAP_NAME"
            ],
            "steps": [
              {
                "STEP_NAME": {
                  ...
                }
              },
              ...
            ]
          }
        }
        

Inside the main workflow, you can define the [steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps) you want and their order of execution using the Workflows syntax. Every workflow must have at least one step.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
