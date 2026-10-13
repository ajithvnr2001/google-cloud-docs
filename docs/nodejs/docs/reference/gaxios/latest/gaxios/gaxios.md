---
url: https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxios/
title: Class Gaxios (6.5.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:46.077612+00:00
---

# Class Gaxios (6.5.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxios/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Gaxios (6.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 6.5.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxios/)
  * [ 6.4.0 ](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/6.4.0/gaxios/gaxios/)
  * [ 6.3.0 ](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/6.3.0/gaxios/gaxios/)
  * [ 6.2.0 ](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/6.2.0/gaxios/gaxios/)
  * [ 6.1.1 ](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/6.1.1/gaxios/gaxios/)
  * [ 6.0.4 ](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/6.0.4/gaxios/gaxios/)



## Package

[gaxios](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/overview.html)

## Constructors 

### (constructor)(defaults)
    
    
    constructor(defaults?: GaxiosOptions);

The Gaxios class is responsible for making HTTP requests.

**Parameter**  
---  
**Name** | **Description**  
`defaults` |  `[GaxiosOptions](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxiosoptions)`   
The default set of options to be used for this instance.  
  
## Properties 

### agentCache
    
    
    protected agentCache: Map<string | URL, Agent | ((parsedUrl: URL) => Agent)>;

### defaults
    
    
    defaults: GaxiosOptions;

Default HTTP options that will be used for every HTTP request.

## Methods 

### _request(opts)
    
    
    protected _request<T = any>(opts?: GaxiosOptions): GaxiosPromise<T>;

Internal, retryable version of the `request` method.

**Parameter**  
---  
**Name** | **Description**  
`opts` |  `[GaxiosOptions](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxiosoptions)`   
Set of HTTP options that will be used for this HTTP request.  
**Returns**  
---  
**Type** | **Description**  
`[GaxiosPromise](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/overview.html)<T>` |   
**Type Parameter**  
---  
**Name** | **Description**  
`T` |   
  
### request(opts)
    
    
    request<T = any>(opts?: GaxiosOptions): GaxiosPromise<T>;

Perform an HTTP request with the given options.

**Parameter**  
---  
**Name** | **Description**  
`opts` |  `[GaxiosOptions](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/gaxios/gaxiosoptions)`   
Set of HTTP options that will be used for this HTTP request.  
**Returns**  
---  
**Type** | **Description**  
`[GaxiosPromise](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/overview.html)<T>` |   
**Type Parameter**  
---  
**Name** | **Description**  
`T` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
