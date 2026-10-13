---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/secretmanager/v1/projects.secrets/list/
title: Method: googleapis.secretmanager.v1.projects.secrets.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:46.192898+00:00
---

# Method: googleapis.secretmanager.v1.projects.secrets.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/secretmanager/v1/projects.secrets/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.secretmanager.v1.projects.secrets.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists Secrets.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The resource name of the project associated with the Secrets, in the format `projects/*`.  
`filter` |  `string` Optional. Filter string, adhering to the rules in [List-operation filtering](https://cloud.google.com/secret-manager/docs/filtering). List only secrets matching the filter. If filter is empty, all secrets are listed.  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Optional. The maximum number of results to be returned in a single page. If set to 0, the server decides the number of results to return. If the number is greater than 25000, it is capped at 25000.  
`pageToken` |  `string` Optional. Pagination token, returned earlier via ListSecretsResponse.next_page_token.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`ListSecretsResponse`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/secretmanager/v1/Overview#ListSecretsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/list).

### YAML
    
    
    - list:
        call: googleapis.secretmanager.v1.projects.secrets.list
        args:
            parent: ...
            filter: ...
            pageSize: ...
            pageToken: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.secretmanager.v1.projects.secrets.list",
          "args": {
            "parent": "...",
            "filter": "...",
            "pageSize": "...",
            "pageToken": "..."
          },
          "result": "listResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
