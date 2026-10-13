---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/storage/v1/defaultObjectAccessControls/update/
title: Method: googleapis.storage.v1.defaultObjectAccessControls.update \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:47.655290+00:00
---

# Method: googleapis.storage.v1.defaultObjectAccessControls.update  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/storage/v1/defaultObjectAccessControls/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.storage.v1.defaultObjectAccessControls.update Stay organized with collections  Save and categorize content based on your preferences. 

Updates a default object ACL entry on the specified bucket.

## Arguments

Parameters  
---  
`bucket` |  `string` Required. Name of a bucket.  
`entity` |  `string` Required. The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.  
`userProject` |  `string` The project to be billed for this request. Required for Requester Pays buckets.  
`body` |  `object ([ObjectAccessControl](https://docs.cloud.google.com/workflows/docs/reference/googleapis/storage/v1/Overview#ObjectAccessControl))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`ObjectAccessControl`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/storage/v1/Overview#ObjectAccessControl).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/update).

### YAML
    
    
    - update:
        call: googleapis.storage.v1.defaultObjectAccessControls.update
        args:
            bucket: ...
            entity: ...
            userProject: ...
            body:
                bucket: ...
                domain: ...
                email: ...
                entity: ...
                entityId: ...
                etag: ...
                generation: ...
                id: ...
                kind: ...
                object: ...
                projectTeam:
                    projectNumber: ...
                    team: ...
                role: ...
                selfLink: ...
        result: updateResult

### JSON
    
    
    [
      {
        "update": {
          "call": "googleapis.storage.v1.defaultObjectAccessControls.update",
          "args": {
            "bucket": "...",
            "entity": "...",
            "userProject": "...",
            "body": {
              "bucket": "...",
              "domain": "...",
              "email": "...",
              "entity": "...",
              "entityId": "...",
              "etag": "...",
              "generation": "...",
              "id": "...",
              "kind": "...",
              "object": "...",
              "projectTeam": {
                "projectNumber": "...",
                "team": "..."
              },
              "role": "...",
              "selfLink": "..."
            }
          },
          "result": "updateResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
