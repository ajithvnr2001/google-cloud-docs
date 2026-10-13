---
url: https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/google-cloud-kvstore/kvstore/
title: Class KVStore (10.0.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:11.138875+00:00
---

# Class KVStore (10.0.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/google-cloud-kvstore/kvstore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class KVStore (10.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 10.0.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/google-cloud-kvstore/kvstore/)
  * [ 9.0.1 ](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/9.0.1/google-cloud-kvstore/kvstore/)
  * [ 8.0.2 ](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/8.0.2/google-cloud-kvstore/kvstore/)



## Package

[google-cloud-kvstore](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)

## Constructors 

### (constructor)(dataset)
    
    
    constructor(dataset: DataSet);

Constructs a new instance of the `KVStore` class

**Parameter**  
---  
**Name** | **Description**  
`dataset` |  `[DataSet](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/google-cloud-kvstore/dataset)`   
  
  
## Properties 

### dataset
    
    
    dataset: DataSet;

## Methods 

### delete(key)
    
    
    delete(key: Key): Promise<void>;

**Parameter**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<void>` |   
  
### delete(key, callback)
    
    
    delete(key: Key, callback: DeleteCallback): void;

**Parameters**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(key)
    
    
    get(key: Key): Promise<Entity>;

**Parameter**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[Entity](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/google-cloud-kvstore/entity)>` |   
  
### get(key, callback)
    
    
    get(key: Key, callback: GetCallback): void;

**Parameters**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### set(key, value)
    
    
    set(key: Key, value: Value): Promise<void>;

**Parameters**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
`value` |  `[Value](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<void>` |   
  
### set(key, value, callback)
    
    
    set(key: Key, value: Value, callback: SetCallback): void;

**Parameters**  
---  
**Name** | **Description**  
`key` |  `[Key](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
`value` |  `[Value](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
`callback` |  `[SetCallback](https://docs.cloud.google.com/nodejs/docs/reference/google-cloud-kvstore/latest/overview.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
