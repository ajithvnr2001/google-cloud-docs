---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacyTestRuleStreaming/
title: Method: legacy.legacyTestRuleStreaming \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:22.807647+00:00
---

# Method: legacy.legacyTestRuleStreaming  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacyTestRuleStreaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacy.legacyTestRuleStreaming Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * ExecutionError
    * JSON representation



**Full name** : projects.locations.instances.legacy.legacyTestRuleStreaming

legacy.legacyTestRuleStreaming tests the given rule text over a specified time range and streams detections/errors back without persisting them.

### HTTP request

`POST https://{endpoint}/v1alpha/{instance}/legacy:legacyTestRuleStreaming`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. Chronicle instance this request is sent to. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "ruleText": string,
      "rule": string,
      "startTime": string,
      "endTime": string,
      "maxDetections": integer,
      "scope": string,
      "simulatedDataVisibility": enum ([SimulatedDataVisibility](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dashboardScheduledReports#SimulatedDataVisibility))
    }  
  
Fields  
---  
`ruleText` |  `string` Optional. The rule text to test as a UTF-8 string.  
`rule` |  `string` Optional. The rule resource name of the curated rule to test. Format: projects/{project}/locations/{location}/instances/{instance}/rules/{rule} The rule resource's rule text to test. Either the ruleText or the rule name must be present, but not both. If both are present, an error will be returned.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The start time of the time range of events to test the rule text over. If unspecified, will default to 12 hours before endTime.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The end time of the time range of events to test the rule text over. If unspecified, will either default to 12 hours after startTime, or the current day bucket if startTime is also unspecified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`maxDetections` |  `integer` Optional. The maximum number of detections to return. The service may return fewer than this value. If unspecified, at most 1,000 detections will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.  
`scope` |  `string` Optional. The data access scope to use to run the rule. This field is only required if data access control is enabled. If reference lists are used in the rule, validations will be performed against this scope to ensure that the reference lists are compatible with both the user's and the rule's scopes. The scope should be in the format: "projects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{scope}".  
`simulatedDataVisibility` |  `enum (`[SimulatedDataVisibility](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dashboardScheduledReports#SimulatedDataVisibility)`)` Optional. Specifies visibility of simulated data to include in test results. If set to SIMULATED_DATA_EXCLUDED or SIMULATED_DATA_VISIBILITY_UNSPECIFIED, simulated events are filtered out at the event level before rule evaluation. Consequently, any Detection that would have included simulated events (i.e., those containing any simulated events) is prevented from being generated if the simulated events are required for the rule to match. If a rule can match using only real events, a Detection is generated but will not include any associated simulated events.  
  
### Response body

legacy.legacyTestRuleStreaming response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "ruleCompilationError": {
        object ([RuleCompilationError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/RuleCompilationError))
      },
      "tooManyDetections": boolean,
      "progressPercent": number,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "detection": {
        object ([Collection](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Collection))
      },
      "executionError": {
        object ([ExecutionError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacyTestRuleStreaming#ExecutionError))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`ruleCompilationError` |  `object (`[RuleCompilationError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/RuleCompilationError)`)` The compilation error generated from the rule text.  
`tooManyDetections` |  `boolean` Indicates if the request would have streamed more detections than maxResults allows.  
`progressPercent` |  `number` The progress percent of the run, from 0.0-100.0.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`detection` |  `object (`[Collection](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Collection)`)` A detection generated from the test. The following fields will not be set because the detection is not persisted: - createdTime - detection[_].rule_id - detection[_].rule_version id will be set, but cannot be passed to other methods to retrieve the detection since it is not persisted.  
`executionError` |  `object (`[ExecutionError](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacyTestRuleStreaming#ExecutionError)`)` An execution error generated from the test.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacies.legacyTestRuleStreaming`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ExecutionError

An execution error generated from the test.

JSON representation  
---  
      
    
    {
      "error": {
        object ([Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "timeRange": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval))
      }
    }  
  
Fields  
---  
`error` |  `object (`[Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The error status corresponding with the execution error.  
`timeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` The event time range that the execution error corresponds with.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
