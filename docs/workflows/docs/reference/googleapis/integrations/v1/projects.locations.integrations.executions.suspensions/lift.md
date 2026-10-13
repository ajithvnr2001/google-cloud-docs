---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/integrations/v1/projects.locations.integrations.executions.suspensions/lift/
title: Method: googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.lift \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:23.351072+00:00
---

# Method: googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.lift  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/integrations/v1/projects.locations.integrations.executions.suspensions/lift/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.lift Stay organized with collections  Save and categorize content based on your preferences. 

  * Lifts suspension for advanced suspension task. Fetch corresponding suspension with provided suspension Id, resolve suspension, and set up suspension result for the Suspension Task.



## Arguments

Parameters  
---  
`name` |  `string` Required. The resource that the suspension belongs to. "projects/{project}/locations/{location}/products/{product}/integrations/{integration}/executions/{execution}/suspensions/{suspenion}" format.  
`location` |  `string` Location of the HTTP endpoint. For example, if location is set to `us-central1`, the endpoint https://us-central1-integrations.googleapis.com will be used. If not set, the global endpint will be used. See [service endpoints](https://cloud.google.com/application-integration/docs/reference/rest#service-endpoint).  
`body` |  `object ([GoogleCloudIntegrationsV1alphaLiftSuspensionRequest](https://cloud.google.com/workflows/docs/reference/googleapis/integrations/v1/Overview#GoogleCloudIntegrationsV1alphaLiftSuspensionRequest))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GoogleCloudIntegrationsV1alphaLiftSuspensionResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/integrations/v1/Overview#GoogleCloudIntegrationsV1alphaLiftSuspensionResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions.suspensions/lift).

### YAML
    
    
    - lift:
        call: googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.lift
        args:
            name: ...
            body:
                suspensionResult: ...
        result: liftResult

### JSON
    
    
    [
      {
        "lift": {
          "call": "googleapis.integrations.v1.projects.locations.integrations.executions.suspensions.lift",
          "args": {
            "name": "...",
            "body": {
              "suspensionResult": "..."
            }
          },
          "result": "liftResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
