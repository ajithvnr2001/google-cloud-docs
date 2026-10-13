---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/extractSyslog/
title: Method: instances.extractSyslog \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:18.263576+00:00
---

# Method: instances.extractSyslog  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances/extractSyslog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: instances.extractSyslog Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.extractSyslog

instances.extractSyslog extracts structured part of log from a unstructured log by running a grok regex over it. The target field indicates the structured part. For a raw log: "123.249.198.123 structured_part" And preprocess config this: regex: "%{IP:Principal_ip} %{GREEDYDATA:data}", target: "data" This will generate: map<string, string> {"data": "structured_part"}

### HTTP request

`POST https://{endpoint}/v1/{instance}:extractSyslog`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The name of the parent resource, which is the SecOps instance associated with the request. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "preprocessConfig": {
        object ([PreProcessConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FieldExtractors#PreProcessConfig))
      },
      "log": string
    }  
  
Fields  
---  
`preprocessConfig` |  `object (`[PreProcessConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FieldExtractors#PreProcessConfig)`)` PreProcessConfig holds the GROK expression to extract the syslog header.  
`log` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw log.A base64-encoded string.  
  
### Response body

Response message for instances.extractSyslog.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "fieldMappings": {
        string: string,
        ...
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      }
    }  
  
Fields  
---  
`fieldMappings` |  `map (key: string, value: string)` map of extracted fields.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. Error message if any, when running grokRegex over the log.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.parserExtensions.removeSyslog`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
