---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/list/
title: Method: projects.locations.experiments.list \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:44.017482+00:00
---

# Method: projects.locations.experiments.list  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/list/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  Method: projects.locations.experiments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists all experiments in a specified project and location.

### HTTP request

`GET https://faulttesting.googleapis.com/v1alpha/{parent=projects/*/locations/*}/experiments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location from which to list experiments. Format: `projects/{projectId}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of experiments to return. Fault Injection Testing may return fewer. If unspecified, at most 1000 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token received from a previous list call, used to retrieve the subsequent page.When paginating, all other parameters provided to `experiments.list` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter expression to restrict the experiments returned. Example: `state="INJECTED"`. Returns only experiments matching the expression. Follows <https://google.aip.dev/160> and supports all fields.  
  
### Request body

The request body must be empty.

### Response body

List experiments for a specified project.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "experiments": [
        {
          object ([Experiment](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments#Experiment))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`experiments[]` |  `object (`[Experiment](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments#Experiment)`)` The experiments from the specified project, ordered from newest to oldest based on creation time.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.experiments.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
