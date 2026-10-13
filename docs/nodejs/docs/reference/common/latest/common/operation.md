---
url: https://docs.cloud.google.com/nodejs/docs/reference/common/latest/common/operation/
title: Class Operation (8.0.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:17.668729+00:00
---

# Class Operation (8.0.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/common/latest/common/operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Operation (8.0.2) Stay organized with collections  Save and categorize content based on your preferences. 

8.0.2 (latest)  8.0.1  6.1.0  6.0.1  5.0.2  4.0.3  3.10.0  3.9.0  3.8.1  3.7.4 

## Inheritance

ServiceObject<T> > Operation

## Package

[@google-cloud/common](https://docs.cloud.google.com/nodejs/docs/reference/common/latest/overview.html)

## Constructors 

### (constructor)(config)
    
    
    constructor(config: ServiceObjectConfig);

An Operation object allows you to interact with APIs that take longer to process things.

module:common/operation

**Parameter**  
---  
**Name** | **Description**  
`config` |  `[ServiceObjectConfig](https://docs.cloud.google.com/nodejs/docs/reference/common/latest/common/serviceobjectconfig)`   
Configuration object.  
  
## Properties 

### completeListeners
    
    
    completeListeners: number;

### hasActiveListeners
    
    
    hasActiveListeners: boolean;

## Methods 

### listenForEvents_()
    
    
    protected listenForEvents_(): void;

Begin listening for events on the operation. This method keeps track of how many "complete" listeners are registered and removed, making sure polling is handled automatically.

As long as there is one active "complete" listener, the connection is open. When there are no more listeners, the polling stops.

**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### poll_(callback)
    
    
    protected poll_(callback: MetadataCallback): void;

Poll for a status update. Returns null for an incomplete status, and metadata for a complete status.

**Parameter**  
---  
**Name** | **Description**  
`callback` |  `[MetadataCallback](https://docs.cloud.google.com/nodejs/docs/reference/common/latest/overview.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### promise()
    
    
    promise(): Promise<unknown>;

Wraps the `complete` and `error` events in a Promise.

{Promise}

**Returns**  
---  
**Type** | **Description**  
`Promise<unknown>` |   
  
### startPolling_()
    
    
    protected startPolling_(): Promise<void>;

Poll `getMetadata` to check the operation's status. This runs a loop to ping the API on an interval.

Note: This method is automatically called once a "complete" event handler is registered on the operation.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
