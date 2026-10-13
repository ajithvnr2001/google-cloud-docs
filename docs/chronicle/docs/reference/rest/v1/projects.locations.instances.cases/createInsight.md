---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/createInsight/
title: Method: cases.createInsight \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:56.482551+00:00
---

# Method: cases.createInsight  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/createInsight/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: cases.createInsight Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.createInsight

Adds an insight to a Case. Insights are analyst-provided or automation-generated notes, observations, or critical pieces of information discovered during the case investigation.

### HTTP request

`POST https://{endpoint}/v1/{name}:createInsight`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Case to create Insight for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "triggeredBy": string,
      "title": string,
      "content": string,
      "entityIdentifier": string,
      "severity": enum ([CaseInsightSeverity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseInsightSeverity)),
      "type": enum ([CaseInsightType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseInsightType)),
      "additionalDataType": enum ([CaseInsightType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseInsightType)),
      "additionalData": string,
      "additionalDataTitle": string,
      "entityType": string,
      "alertIdentifier": string,
      "isFavorite": boolean
    }  
  
Fields  
---  
`triggeredBy` |  `string` Optional. User who triggered the case insight.  
`title` |  `string` Required. Insight title.  
`content` |  `string` Required. Insight content.  
`entityIdentifier` |  `string` Optional. Entity identifier.  
`severity` |  `enum (`[CaseInsightSeverity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseInsightSeverity)`)` Optional. Case insight severity.  
`type` |  `enum (`[CaseInsightType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseInsightType)`)` Optional. Case insight type.  
`additionalDataType` |  `enum (`[CaseInsightType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseInsightType)`)` Optional. Case additional data insight type.  
`additionalData` |  `string` Optional. Case Insight additional data.  
`additionalDataTitle` |  `string` Optional. Case Insight additional data.  
`entityType` |  `string` Optional. Entity type.  
`alertIdentifier` |  `string` Optional. Alert identifier to create insight for.  
`isFavorite` |  `boolean` Optional. Is Favoriting Insight.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.cases.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
