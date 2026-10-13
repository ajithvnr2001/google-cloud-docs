---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/Overview/
title: Transcoder API Connector Overview \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:18.949349+00:00
---

# Transcoder API Connector Overview  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/Overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Transcoder API Connector Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Workflows connector defines the built-in functions that can be used to access other Google Cloud products within a workflow.

This page provides an overview of the individual connector. There is no need to import or load connector libraries in a workflow—connectors work out of the box when used in a call step.

## Transcoder API

This API converts video files into formats suitable for consumer distribution. For more information, see the Transcoder API overview. To learn more, see the [Transcoder API documentation](https://cloud.google.com/transcoder/docs/).

## Transcoder connector sample

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

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "project": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}"
                },
                {
                  "location": "${sys.get_env(\"GOOGLE_CLOUD_LOCATION\")}"
                }
              ]
            }
          },
          {
            "get_list": {
              "call": "googleapis.transcoder.v1.projects.locations.jobs.list",
              "args": {
                "parent": "${\"projects/\" + project + \"/locations/\" + location}"
              },
              "result": "response"
            }
          },
          {
            "the_end": {
              "return": "${response}"
            }
          }
        ]
      }
    }

## Module: googleapis.transcoder.v1.projects.locations.jobTemplates

Functions  
---  
`[create](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/v1/projects.locations.jobTemplates/create)` | Creates a job template in the specified region.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/v1/projects.locations.jobTemplates/delete)` | Deletes a job template.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/v1/projects.locations.jobTemplates/get)` | Returns the job template data.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/v1/projects.locations.jobTemplates/list)` | Lists job templates in the specified region.  
  
## Module: googleapis.transcoder.v1.projects.locations.jobs

Functions  
---  
`[create](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/v1/projects.locations.jobs/create)` | Creates a job in the specified region.  
`[delete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/v1/projects.locations.jobs/delete)` | Deletes a job.  
`[get](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/v1/projects.locations.jobs/get)` | Returns the job data.  
`[list](https://docs.cloud.google.com/workflows/docs/reference/googleapis/transcoder/v1/projects.locations.jobs/list)` | Lists jobs in the specified region.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
