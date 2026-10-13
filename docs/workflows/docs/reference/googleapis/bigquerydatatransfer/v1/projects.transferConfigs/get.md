---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/v1/projects.transferConfigs/get/
title: Method: googleapis.bigquerydatatransfer.v1.projects.transferConfigs.get \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:54.636134+00:00
---

# Method: googleapis.bigquerydatatransfer.v1.projects.transferConfigs.get  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/v1/projects.transferConfigs/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.bigquerydatatransfer.v1.projects.transferConfigs.get Stay organized with collections  Save and categorize content based on your preferences. 

Returns information about a data transfer config.

## Arguments

Parameters  
---  
`name` |  `string` Required. The field will contain name of the resource requested, for example: `projects/{project_id}/transferConfigs/{config_id}` or `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`TransferConfig`](https://cloud.google.com/workflows/docs/reference/googleapis/bigquerydatatransfer/v1/Overview#TransferConfig).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/bigquery-transfer/docs/reference/datatransfer/rest/v1/projects.transferConfigs/get).

### YAML
    
    
    - get:
        call: googleapis.bigquerydatatransfer.v1.projects.transferConfigs.get
        args:
            name: ...
        result: getResult

### JSON
    
    
    [
      {
        "get": {
          "call": "googleapis.bigquerydatatransfer.v1.projects.transferConfigs.get",
          "args": {
            "name": "..."
          },
          "result": "getResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
