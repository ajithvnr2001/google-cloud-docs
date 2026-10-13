---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/fetchRecommendation/
title: Method: caseAlerts.fetchRecommendation \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:08.439811+00:00
---

# Method: caseAlerts.fetchRecommendation  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/fetchRecommendation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: caseAlerts.fetchRecommendation Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * RecommendationResponseState



**Full name** : projects.locations.instances.cases.caseAlerts.fetchRecommendation

Fetches a previously generated AI-driven recommendation for an alert. Use this method to retrieve suggested actions or insights derived from similar historical alerts.

### HTTP request

`GET https://{endpoint}/v1/{parent}/caseAlerts:fetchRecommendation`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The unique name(ID) of the CaseAlert.  
  
### Query parameters

Parameters  
---  
`recommendationId` |  `string` Required. The requested recommendation id.  
  
### Request body

The request body must be empty.

### Response body

Response message for caseAlerts.fetchRecommendation.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "recommendation": string,
      "alertIdentifierToCaseId": {
        string: integer,
        ...
      },
      "marketplaceActionsTriggeredManually": [
        string
      ],
      "state": enum ([RecommendationResponseState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/fetchRecommendation#RecommendationResponseState))
    }  
  
Fields  
---  
`recommendation` |  `string` Output only. The recommendation text.  
`alertIdentifierToCaseId` |  `map (key: string, value: integer)` Output only. Mapping of alert identifiers to case IDs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`marketplaceActionsTriggeredManually[]` |  `string` Optional. List of marketplace actions triggered manually.  
`state` |  `enum (`[RecommendationResponseState](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseAlerts/fetchRecommendation#RecommendationResponseState)`)` Output only. The recommendation response state.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.caseAlerts.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## RecommendationResponseState

The recommendation response state.

Enums  
---  
`RECOMMENDATION_RESPONSE_STATE_UNSPECIFIED` | The recommendation response state is unspecified.  
`RUNNING` | The recommendation is running.  
`SUCCEEDED` | The recommendation is succeeded.  
`FAILED` | The recommendation is failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
