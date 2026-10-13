---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/integrations/v1/projects.locations.integrations.executions.suspensions/list/
title: Method: googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:59.471643+00:00
---

# Method: googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/integrations/v1/projects.locations.integrations.executions.suspensions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * Lists suspensions associated with a specific execution. Only those with permissions to resolve the relevant suspensions will be able to view them.



## Arguments

Parameters  
---  
`parent` |  `string` Required. projects/{gcp_project_id}/locations/{location}/products/{product}/integrations/{integration_name}/executions/{execution_name}  
`filter` |  `string` Standard filter field.  
`orderBy` |  `string` Field name to order by.  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Maximum number of entries in the response.  
`pageToken` |  `string` Token to retrieve a specific page.  
`location` |  `string` Location of the HTTP endpoint. For example, if location is set to `us-central1`, the endpoint https://us-central1-integrations.googleapis.com will be used. If not set, the global endpint will be used. See [service endpoints](https://cloud.google.com/application-integration/docs/reference/rest#service-endpoint).  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GoogleCloudIntegrationsV1alphaListSuspensionsResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/integrations/v1/Overview#GoogleCloudIntegrationsV1alphaListSuspensionsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions.suspensions/list).

### YAML
    
    
    - list:
        call: googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.list
        args:
            parent: ...
            filter: ...
            orderBy: ...
            pageSize: ...
            pageToken: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.list",
          "args": {
            "parent": "...",
            "filter": "...",
            "orderBy": "...",
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
