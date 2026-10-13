---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/secretmanager/v1/projects.secrets/patch/
title: Method: googleapis.secretmanager.v1.projects.secrets.patch \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:46.378286+00:00
---

# Method: googleapis.secretmanager.v1.projects.secrets.patch  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/secretmanager/v1/projects.secrets/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.secretmanager.v1.projects.secrets.patch Stay organized with collections  Save and categorize content based on your preferences. 

Updates metadata of an existing Secret.

## Arguments

Parameters  
---  
`name` |  `string` Required. Output only. The resource name of the Secret in the format `projects/*/secrets/*`.  
`updateMask` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` Required. Specifies the fields to be updated.  
`body` |  `object ([Secret](https://docs.cloud.google.com/workflows/docs/reference/googleapis/secretmanager/v1/Overview#Secret))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`Secret`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/secretmanager/v1/Overview#Secret).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/patch).

### YAML
    
    
    - patch:
        call: googleapis.secretmanager.v1.projects.secrets.patch
        args:
            name: ...
            updateMask: ...
            body:
                etag: ...
                expireTime: ...
                labels: ...
                replication:
                    automatic:
                        customerManagedEncryption:
                            kmsKeyName: ...
                    userManaged:
                        replicas: ...
                rotation:
                    nextRotationTime: ...
                    rotationPeriod: ...
                topics: ...
                ttl: ...
        result: patchResult

### JSON
    
    
    [
      {
        "patch": {
          "call": "googleapis.secretmanager.v1.projects.secrets.patch",
          "args": {
            "name": "...",
            "updateMask": "...",
            "body": {
              "etag": "...",
              "expireTime": "...",
              "labels": "...",
              "replication": {
                "automatic": {
                  "customerManagedEncryption": {
                    "kmsKeyName": "..."
                  }
                },
                "userManaged": {
                  "replicas": "..."
                }
              },
              "rotation": {
                "nextRotationTime": "...",
                "rotationPeriod": "..."
              },
              "topics": "...",
              "ttl": "..."
            }
          },
          "result": "patchResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
