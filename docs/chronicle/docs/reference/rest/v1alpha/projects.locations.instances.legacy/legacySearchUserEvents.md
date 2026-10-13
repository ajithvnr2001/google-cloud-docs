---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchUserEvents/
title: Method: legacy.legacySearchUserEvents \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:10.172791+00:00
---

# Method: legacy.legacySearchUserEvents  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchUserEvents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacy.legacySearchUserEvents Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.legacy.legacySearchUserEvents

Legacy endpoint for getting events for a given user.

### HTTP request

`GET https://{endpoint}/v1alpha/{instance}/legacy:legacySearchUserEvents`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. Chronicle instance this request is sent to. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`userIndicator` |  `object (`[UserIndicator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/UserIndicator)`)` Required. User to fetch telemetry data for.  
`timeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` Required. Time range for requested user data [inclusive start time, exclusive end time).  
`maxUserEvents` |  `integer` Maximum number of user events to return. Defaults to a high value if empty / set to 0.  
`maxAssetEvents` |  `integer` Maximum number of asset events to return.  
  
### Request body

The request body must be empty.

### Response body

Response for user telemetry data.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "events": [
        {
          object ([UdmEventInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/UdmEventInfo))
        }
      ],
      "tooManyUserEvents": boolean,
      "tooManyAssetEvents": boolean
    }  
  
Fields  
---  
`events[]` |  `object (`[UdmEventInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/UdmEventInfo)`)` UDM user events and aliased asset events for the requested user and time range. If `useUdm` in request is false, we will include only asset events in this field and put user SDM events in typedUserEvents field.  
`tooManyUserEvents` |  `boolean` Whether we have too many user events.  
`tooManyAssetEvents` |  `boolean` Whether we have too many asset events.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacies.legacySearchUserEvents`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
