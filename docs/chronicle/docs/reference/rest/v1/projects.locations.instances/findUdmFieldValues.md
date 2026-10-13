---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findUdmFieldValues/
title: Method: instances.findUdmFieldValues \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:21.054575+00:00
---

# Method: instances.findUdmFieldValues  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findUdmFieldValues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.findUdmFieldValues Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * ValueMatch
    * JSON representation
  * FieldMatch
    * JSON representation



**Full name** : projects.locations.instances.findUdmFieldValues

Finds ingested UDM field values that match a query.

### HTTP request

`GET https://{endpoint}/v1/{instance}:findUdmFieldValues`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. Chronicle instance this request is sent to. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`query` |  `string` Required. The partial UDM field value to match.  
`limit` |  `integer` Optional. The maximum number of value matches to return. The service may return fewer matches than this value. If unspecified, defaults to 250. The maximum value is 1000; values above 1000 will be coerced to 1000. This field replaces the deprecated `pageSize` field.  
  
### Request body

The request body must be empty.

### Response body

Ingested UDM field values that match a query.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "valueMatches": [
        {
          object ([ValueMatch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findUdmFieldValues#ValueMatch))
        }
      ],
      "fieldMatches": [
        {
          object ([FieldMatch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findUdmFieldValues#FieldMatch))
        }
      ],
      "fieldMatchRegex": string,
      "hasMoreMatches": boolean
    }  
  
Fields  
---  
`valueMatches[]` |  `object (`[ValueMatch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findUdmFieldValues#ValueMatch)`)` Values that match the query.  
`fieldMatches[]` |  `object (`[FieldMatch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/findUdmFieldValues#FieldMatch)`)` Fields that might contain a matching value.  
`fieldMatchRegex` |  `string` A regular expression based on the query that can be used to find matching values within the field-level matches.  
`hasMoreMatches` |  `boolean` Indicates if there are more value matches available but were not returned due to the `limit`. This field replaces the deprecated `nextPageToken` field.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.events.findUdmFieldValues`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ValueMatch

A UDM field value that matches the query.

JSON representation  
---  
      
    
    {
      "fieldPath": string,
      "value": string,
      "ingestionTime": string,
      "matchStart": integer,
      "matchEnd": integer
    }  
  
Fields  
---  
`fieldPath` |  `string` The UDM field containing the matching value.  
`value` |  `string` The matching value.  
`ingestionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The approximate time of the last ingestion of the value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`matchStart` |  `integer` The index within `value` where the matching text starts.  
`matchEnd` |  `integer` The index within `value` where the matching text ends (exclusive).  
  
## FieldMatch

A UDM field that might contain a value that matches the query.

JSON representation  
---  
      
    
    {
      "fieldPath": string
    }  
  
Fields  
---  
`fieldPath` |  `string` The UDM field that might contain a matching value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
