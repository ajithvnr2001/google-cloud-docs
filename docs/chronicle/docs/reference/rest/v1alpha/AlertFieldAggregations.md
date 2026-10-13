---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations/
title: AlertFieldAggregations \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:55.595887+00:00
---

# AlertFieldAggregations  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  AlertFieldAggregations Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AlertFieldAggregation
    * JSON representation
  * AlertFieldValueCount
    * JSON representation
  * AlertFieldValue
    * JSON representation

JSON representation  
---  
      
    
    {
      "fields": [
        {
          object ([AlertFieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldAggregation))
        }
      ]
    }  
  
Fields  
---  
`fields[]` |  `object (`[AlertFieldAggregation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldAggregation)`)`  
  
## AlertFieldAggregation

JSON representation  
---  
      
    
    {
      "fieldName": string,
      "baselineAlertCount": integer,
      "alertCount": integer,
      "tooManyValues": boolean,
      "valueCount": integer,
      "allValues": [
        {
          object ([AlertFieldValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldValueCount))
        }
      ],
      "topValues": [
        {
          object ([AlertFieldValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldValueCount))
        }
      ],
      "bottomValues": [
        {
          object ([AlertFieldValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldValueCount))
        }
      ]
    }  
  
Fields  
---  
`fieldName` |  `string`  
`baselineAlertCount` |  `integer`  
`alertCount` |  `integer`  
`tooManyValues` |  `boolean`  
`valueCount` |  `integer`  
`allValues[]` |  `object (`[AlertFieldValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldValueCount)`)`  
`topValues[]` |  `object (`[AlertFieldValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldValueCount)`)`  
`bottomValues[]` |  `object (`[AlertFieldValueCount](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldValueCount)`)`  
  
## AlertFieldValueCount

JSON representation  
---  
      
    
    {
      "value": {
        object ([AlertFieldValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldValue))
      },
      "baselineAlertCount": integer,
      "alertCount": integer
    }  
  
Fields  
---  
`value` |  `object (`[AlertFieldValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AlertFieldAggregations#AlertFieldValue)`)`  
`baselineAlertCount` |  `integer`  
`alertCount` |  `integer`  
  
## AlertFieldValue

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "stringValue": string,
      "int32Value": integer,
      "uint32Value": integer,
      "int64Value": string,
      "uint64Value": string,
      "floatValue": number,
      "doubleValue": number,
      "enumValue": string,
      "boolValue": boolean,
      "bytesValue": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`stringValue` |  `string`  
`int32Value` |  `integer`  
`uint32Value` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)`  
`uint64Value` |  `string`  
`floatValue` |  `number`  
`doubleValue` |  `number`  
`enumValue` |  `string`  
`boolValue` |  `boolean`  
`bytesValue` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A base64-encoded string.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
