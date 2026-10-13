---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findEntityAlerts/
title: Method: instances.findEntityAlerts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:19.570191+00:00
---

# Method: instances.findEntityAlerts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findEntityAlerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.findEntityAlerts Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.findEntityAlerts

Get alerts for an entity. The API returns a maximum of 1000 alerts for the requested entity.

### HTTP request

`GET https://{endpoint}/v1/{instance}:findEntityAlerts`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The ID of the Instance to summarize entity for. Format: `projects/{project}/locations/{location}/instances/{instance}`  
  
### Query parameters

Parameters  
---  
`timeRange` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` Required. Time range to retrieve the alerts for [Inclusive start time, exclusive end time).  
Identifier to find the entity. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`entityId` |  `string` ID of the entity.  
`fieldAndValue` |  `object (`[FieldAndValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FieldAndValue)`)` Field path or type with value to identify entity.  
End of mutually exclusive fields.  
  
### Request body

The request body must be empty.

### Response body

Response message to retrieve alerts for an entity.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "alertCounts": [
        {
          object ([AlertCountByRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/AlertCountByRule))
        }
      ],
      "hasMoreAlerts": boolean,
      "timeline": {
        object ([Timeline](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Timeline))
      }
    }  
  
Fields  
---  
`alertCounts[]` |  `object (`[AlertCountByRule](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/AlertCountByRule)`)` Rule names with alert count for each.  
`hasMoreAlerts` |  `boolean` Indicates if there are more alerts than the limit (1000 currently).  
`timeline` |  `object (`[Timeline](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/Timeline)`)` Bucketed timeline with alert count.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.entities.findEntityAlerts`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
