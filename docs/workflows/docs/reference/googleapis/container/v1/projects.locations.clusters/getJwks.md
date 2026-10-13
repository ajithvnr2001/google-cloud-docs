---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/projects.locations.clusters/getJwks/
title: Method: googleapis.container.v1.projects.locations.clusters.getJwks \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:04.448517+00:00
---

# Method: googleapis.container.v1.projects.locations.clusters.getJwks  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/projects.locations.clusters/getJwks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.container.v1.projects.locations.clusters.getJwks Stay organized with collections  Save and categorize content based on your preferences. 

Gets the public component of the cluster signing keys in JSON Web Key format. This API is not yet intended for general use, and is not available for all clusters.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The cluster (project, location, cluster id) to get keys for. Specified in the format `projects/*/locations/*/clusters/*`.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GetJSONWebKeysResponse`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#GetJSONWebKeysResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/getJwks).

### YAML
    
    
    - getJwks:
        call: googleapis.container.v1.projects.locations.clusters.getJwks
        args:
            parent: ...
        result: getJwksResult

### JSON
    
    
    [
      {
        "getJwks": {
          "call": "googleapis.container.v1.projects.locations.clusters.getJwks",
          "args": {
            "parent": "..."
          },
          "result": "getJwksResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
