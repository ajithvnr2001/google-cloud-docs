---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/folders/getIamPolicy/
title: Method: googleapis.cloudresourcemanager.v3.folders.getIamPolicy \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:40.093862+00:00
---

# Method: googleapis.cloudresourcemanager.v3.folders.getIamPolicy  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/folders/getIamPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.cloudresourcemanager.v3.folders.getIamPolicy Stay organized with collections  Save and categorize content based on your preferences. 

Gets the access control policy for a folder. The returned policy may be empty if no such policy or resource exists. The `resource` field should be the folder's resource name, for example: "folders/1234". The caller must have `resourcemanager.folders.getIamPolicy` permission on the identified folder.

## Arguments

Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`body` |  `object ([GetIamPolicyRequest](https://cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/Overview#GetIamPolicyRequest))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`Policy`](https://cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/Overview#Policy).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/resource-manager/reference/rest/v3/folders/getIamPolicy).

### YAML
    
    
    - getIamPolicy:
        call: googleapis.cloudresourcemanager.v3.folders.getIamPolicy
        args:
            resource: ...
            body:
                options:
                    requestedPolicyVersion: ...
        result: getIamPolicyResult

### JSON
    
    
    [
      {
        "getIamPolicy": {
          "call": "googleapis.cloudresourcemanager.v3.folders.getIamPolicy",
          "args": {
            "resource": "...",
            "body": {
              "options": {
                "requestedPolicyVersion": "..."
              }
            }
          },
          "result": "getIamPolicyResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
