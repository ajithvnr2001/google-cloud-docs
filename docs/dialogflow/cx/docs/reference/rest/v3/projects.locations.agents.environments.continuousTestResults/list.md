---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.continuousTestResults/list/
title: Method: projects.locations.agents.environments.continuousTestResults.list \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:02.214509+00:00
---

# Method: projects.locations.agents.environments.continuousTestResults.list  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.continuousTestResults/list/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.environments.continuousTestResults.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * ContinuousTestResult
    * JSON representation
  * AggregatedTestResult
  * Try it!



Fetches a list of continuous test results for a given environment.

### HTTP request

`GET https://{endpoint}/v3/{parent=projects/*/locations/*/agents/*/environments/*}/continuousTestResults`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The environment to list results for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.environments.get`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return in a single page. By default 100 and at most 1000.  
`pageToken` |  `string` The nextPageToken value returned from a previous list request.  
  
### Request body

The request body must be empty.

### Response body

The response message for [Environments.ListTestCaseResults][].

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "continuousTestResults": [
        {
          object ([ContinuousTestResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.continuousTestResults/list#ContinuousTestResult))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`continuousTestResults[]` |  `object (`[ContinuousTestResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.continuousTestResults/list#ContinuousTestResult)`)` The list of continuous test results.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ContinuousTestResult

Represents a result from running a test case in an agent environment.

JSON representation  
---  
      
    
    {
      "name": string,
      "result": enum ([AggregatedTestResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.continuousTestResults/list#AggregatedTestResult)),
      "testCaseResults": [
        string
      ],
      "runTime": string
    }  
  
Fields  
---  
`name` |  `string` The resource name for the continuous test result. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/continuousTestResults/<ContinuousTestResultID>`.  
`result` |  `enum (`[AggregatedTestResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.continuousTestResults/list#AggregatedTestResult)`)` The result of this continuous test run, i.e. whether all the tests in this continuous test run pass or not.  
`testCaseResults[]` |  `string` A list of individual test case results names in this continuous test run.  
`runTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time when the continuous testing run starts.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## AggregatedTestResult

The overall result for a continuous test run in an agent environment.

Enums  
---  
`AGGREGATED_TEST_RESULT_UNSPECIFIED` | Not specified. Should never be used.  
`PASSED` | All the tests passed.  
`FAILED` | At least one test did not pass.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
