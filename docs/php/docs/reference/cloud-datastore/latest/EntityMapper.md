---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityMapper/
title: Cloud Datastore Client - Class EntityMapper (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:39.047325+00:00
---

# Cloud Datastore Client - Class EntityMapper (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityMapper/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class EntityMapper (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class EntityMapper.

Utility methods for mapping between datastore and [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity).

## Namespace

Google \ Cloud \ Datastore

## Methods 

### __construct

Create an Entity Mapper

**Parameters**  
---  
**Name** | **Description**  
`projectId` |  `string`   
The datastore project ID  
`encode` |  `bool`   
Whether to encode blobs as base64.  
`returnInt64AsObject` |  `bool`   
If true, 64 bit integers will be returned as a [Google\Cloud\Core\Int64](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Int64.html) object for 32 bit platform compatibility.  
  
### responseToEntityProperties

Convert an entity response to properties, excludes and meanings.

**Parameters**  
---  
**Name** | **Description**  
`entityData` |  `array`   
The incoming entity  
`className` |  `string`   
The name of a class to use as the entity. Must implement [EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface).  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### objectToRequest

Translate an Entity to a datastore representation.

**Parameter**  
---  
**Name** | **Description**  
`entity` |  `[EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface)`   
The input entity.  
**Returns**  
---  
**Type** | **Description**  
`array` | A Datastore [Entity](https://cloud.google.com/datastore/reference/rest/v1/Entity)  
  
### convertValue

Convert a Datastore value object to a simple value

**Parameters**  
---  
**Name** | **Description**  
`type` |  `string`   
The value type  
`value` |  `mixed`   
The value  
`className` |  `string`   
[optional] The object type to decode to, if type is entityValue.  
**Returns**  
---  
**Type** | **Description**  
`mixed` |   
  
### valueObject

Format values for the API

**Parameters**  
---  
**Name** | **Description**  
`value` |  `mixed`   
  
`exclude` |  `bool`   
[optional] If true, value will be excluded from datastore indexes.  
`meaning` |  `int`   
[optional] The Meaning value. Maintained only for backwards compatibility.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### objectProperty

Convert different object types to API values

**Parameter**  
---  
**Name** | **Description**  
`value` |  `mixed`   
The value object  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
## Constants 

### DATE_FORMAT
    
    
    Value: 'Y-m-d\TH:i:s.uP'

### DATE_FORMAT_NO_MS
    
    
    Value: 'Y-m-d\TH:i:sP'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
