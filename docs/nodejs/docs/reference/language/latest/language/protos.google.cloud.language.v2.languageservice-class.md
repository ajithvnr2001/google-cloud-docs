---
url: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.languageservice-class
title: Class protos.google.cloud.language.v2.LanguageService (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:05.010976+00:00
---

# Class protos.google.cloud.language.v2.LanguageService (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.languageservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.language.v2.LanguageService (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.1.0  6.5.0  5.2.2  5.1.2  5.0.2  4.3.2  4.2.9 

Represents a LanguageService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.language.v2.LanguageService

## Package

[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new LanguageService service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### analyzeEntities(request, callback)
    
    
    public analyzeEntities(request: google.cloud.language.v2.IAnalyzeEntitiesRequest, callback: google.cloud.language.v2.LanguageService.AnalyzeEntitiesCallback): void;

Calls AnalyzeEntities.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.ianalyzeentitiesrequest)`   
AnalyzeEntitiesRequest message or plain object  
`callback` |  `[AnalyzeEntitiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)`   
Node-style callback called with the error, if any, and AnalyzeEntitiesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeEntities(request)
    
    
    public analyzeEntities(request: google.cloud.language.v2.IAnalyzeEntitiesRequest): Promise<google.cloud.language.v2.AnalyzeEntitiesResponse>;

Calls AnalyzeEntities.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.ianalyzeentitiesrequest)`   
AnalyzeEntitiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.language.v2.AnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.analyzeentitiesresponse)>` | Promise  
  
### analyzeSentiment(request, callback)
    
    
    public analyzeSentiment(request: google.cloud.language.v2.IAnalyzeSentimentRequest, callback: google.cloud.language.v2.LanguageService.AnalyzeSentimentCallback): void;

Calls AnalyzeSentiment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeSentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.ianalyzesentimentrequest)`   
AnalyzeSentimentRequest message or plain object  
`callback` |  `[AnalyzeSentimentCallback](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)`   
Node-style callback called with the error, if any, and AnalyzeSentimentResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeSentiment(request)
    
    
    public analyzeSentiment(request: google.cloud.language.v2.IAnalyzeSentimentRequest): Promise<google.cloud.language.v2.AnalyzeSentimentResponse>;

Calls AnalyzeSentiment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeSentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.ianalyzesentimentrequest)`   
AnalyzeSentimentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.language.v2.AnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.analyzesentimentresponse)>` | Promise  
  
### annotateText(request, callback)
    
    
    public annotateText(request: google.cloud.language.v2.IAnnotateTextRequest, callback: google.cloud.language.v2.LanguageService.AnnotateTextCallback): void;

Calls AnnotateText.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.iannotatetextrequest)`   
AnnotateTextRequest message or plain object  
`callback` |  `[AnnotateTextCallback](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)`   
Node-style callback called with the error, if any, and AnnotateTextResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### annotateText(request)
    
    
    public annotateText(request: google.cloud.language.v2.IAnnotateTextRequest): Promise<google.cloud.language.v2.AnnotateTextResponse>;

Calls AnnotateText.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.iannotatetextrequest)`   
AnnotateTextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.language.v2.AnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.annotatetextresponse)>` | Promise  
  
### classifyText(request, callback)
    
    
    public classifyText(request: google.cloud.language.v2.IClassifyTextRequest, callback: google.cloud.language.v2.LanguageService.ClassifyTextCallback): void;

Calls ClassifyText.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IClassifyTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.iclassifytextrequest)`   
ClassifyTextRequest message or plain object  
`callback` |  `[ClassifyTextCallback](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)`   
Node-style callback called with the error, if any, and ClassifyTextResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### classifyText(request)
    
    
    public classifyText(request: google.cloud.language.v2.IClassifyTextRequest): Promise<google.cloud.language.v2.ClassifyTextResponse>;

Calls ClassifyText.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IClassifyTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.iclassifytextrequest)`   
ClassifyTextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.language.v2.ClassifyTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.classifytextresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): LanguageService;

Creates new LanguageService service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[LanguageService](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.languageservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### moderateText(request, callback)
    
    
    public moderateText(request: google.cloud.language.v2.IModerateTextRequest, callback: google.cloud.language.v2.LanguageService.ModerateTextCallback): void;

Calls ModerateText.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IModerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.imoderatetextrequest)`   
ModerateTextRequest message or plain object  
`callback` |  `[ModerateTextCallback](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)`   
Node-style callback called with the error, if any, and ModerateTextResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moderateText(request)
    
    
    public moderateText(request: google.cloud.language.v2.IModerateTextRequest): Promise<google.cloud.language.v2.ModerateTextResponse>;

Calls ModerateText.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IModerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.imoderatetextrequest)`   
ModerateTextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.language.v2.ModerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.moderatetextresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
