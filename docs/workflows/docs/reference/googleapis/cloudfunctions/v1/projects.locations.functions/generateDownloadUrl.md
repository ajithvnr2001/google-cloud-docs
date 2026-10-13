---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudfunctions/v1/projects.locations.functions/generateDownloadUrl/
title: Method: googleapis.cloudfunctions.v1.projects.locations.functions.generateDownloadUrl \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:25.219491+00:00
---

# Method: googleapis.cloudfunctions.v1.projects.locations.functions.generateDownloadUrl  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudfunctions/v1/projects.locations.functions/generateDownloadUrl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.cloudfunctions.v1.projects.locations.functions.generateDownloadUrl Stay organized with collections  Save and categorize content based on your preferences. 

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within minutes after generation. For more information about the signed URL usage see: https://cloud.google.com/storage/docs/access-control/signed-urls

## Arguments

Parameters  
---  
`name` |  `string` Required. The name of function for which source code Google Cloud Storage signed URL should be generated.  
`body` |  `object ([GenerateDownloadUrlRequest](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudfunctions/v1/Overview#GenerateDownloadUrlRequest))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GenerateDownloadUrlResponse`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudfunctions/v1/Overview#GenerateDownloadUrlResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/generateDownloadUrl).

### YAML
    
    
    - generateDownloadUrl:
        call: googleapis.cloudfunctions.v1.projects.locations.functions.generateDownloadUrl
        args:
            name: ...
            body:
                versionId: ...
        result: generateDownloadUrlResult

### JSON
    
    
    [
      {
        "generateDownloadUrl": {
          "call": "googleapis.cloudfunctions.v1.projects.locations.functions.generateDownloadUrl",
          "args": {
            "name": "...",
            "body": {
              "versionId": "..."
            }
          },
          "result": "generateDownloadUrlResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
