---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface/
title: Cloud Datastore Client - Class EntityInterface (2.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:38.885337+00:00
---

# Cloud Datastore Client - Class EntityInterface (2.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Datastore Client - Class EntityInterface (2.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0  2.0.6  1.34.2  1.33.1  1.32.3  1.31.0  1.30.0  1.29.2  1.28.2  1.26.0  1.25.0  1.24.4  1.23.0  1.22.1  1.21.2  1.19.0  1.18.1  1.17.1 

Reference documentation and code samples for the Cloud Datastore Client class EntityInterface.

Defines an interface for Datastore Entities.

This interface is fulfilled by EntityTrait, and it is recommended that classes implementing EntityInterface make use of that trait to ensure proper configuration.

## Namespace

Google \ Cloud \ Datastore

## Methods 

### get

Return all entity data as an array.

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### set

Set the entity body.

**Parameter**  
---  
**Name** | **Description**  
`entity` |  `array`   
The new entity body.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### key

Return the Datastore key, or null if no key is present.

**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)|null` |   
  
### cursor

Fetch the cursor

This is only set when the entity was obtained from a query result. It can be used to manually paginate results.

**Returns**  
---  
**Type** | **Description**  
`string|null` |   
  
### baseVersion

Fetch the baseVersion

This is only set when the entity was obtained from a query result. It is used for concurrency control internally.

**Returns**  
---  
**Type** | **Description**  
`string|null` |   
  
### populatedByService

Indicate whether the entity was created as the result of an API call.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setExcludeFromIndexes

A list of entity properties to exclude from datastore indexes.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `array`   
A list of properties to exclude from indexes.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### excludedProperties

Return a list of properties excluded from datastore indexes.

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### meanings

Return a list of meaning values.

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### static::build

Create an instance of the entity class.

This factory method allows the implementor to define the means by which the key, entity data and entity options are managed within the entity implementation. This method is called by the Google Cloud PHP client to create entities.

**Parameters**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Key)|null`   
[optional] The Entity's Key, defining its unique identifier. **Defaults to** `null`.  
`entity` |  `array`   
[optional] The entity body. **Defaults to** `[]`.  
`options` |  `array`   
Configuration Options  
`↳ cursor` |  `string`   
Set only when the entity is obtained by a query result. If set, the entity cursor can be retrieved from [EntityInterface::cursor()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface#_Google_Cloud_Datastore_EntityInterface__cursor__).  
`↳ baseVersion` |  `string`   
Set only when the entity is obtained by a query result. If set, the entity cursor can be retrieved from [EntityInterface::baseVersion()](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface#_Google_Cloud_Datastore_EntityInterface__baseVersion__).  
`↳ excludeFromIndexes` |  `array`   
A list of entity keys to exclude from datastore indexes.  
`↳ meanings` |  `array`   
A list of meaning values for entity properties.  
`↳ populatedByService` |  `bool`   
Indicates whether the entity was created as the result of a service request.  
  
### static::mappings

Defines embedded entity mappings.

Embedded entities are converted to instances of [Entity](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/Entity), or to associative arrays by default. By providing mappings, you can define the types to use in your application.

Types must implement [EntityInterface](https://docs.cloud.google.com/php/docs/reference/cloud-datastore/latest/EntityInterface).

**Returns**  
---  
**Type** | **Description**  
`array` | An associative array, where the key is the property name, and the value is the fully-qualified name of a PHP class implementing {@see \Google\Cloud\Datastore\EntityInterface}.  
  
## Constants 

### EXCLUDE_FROM_INDEXES
    
    
    Value: '___GOOGLECLOUDPHP___EXCLUDEFROMINDEXES___'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
