---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.lintingservice-class
title: Class protos.google.cloud.apihub.v1.LintingService (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:03.161561+00:00
---

# Class protos.google.cloud.apihub.v1.LintingService (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.lintingservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.LintingService (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a LintingService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apihub.v1.LintingService

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new LintingService service.

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

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): LintingService;

Creates new LintingService service using the specified rpc implementation.

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
`[LintingService](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.lintingservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getStyleGuide(request, callback)
    
    
    public getStyleGuide(request: google.cloud.apihub.v1.IGetStyleGuideRequest, callback: google.cloud.apihub.v1.LintingService.GetStyleGuideCallback): void;

Calls GetStyleGuide.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStyleGuideRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetstyleguiderequest)`   
GetStyleGuideRequest message or plain object  
`callback` |  `[GetStyleGuideCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and StyleGuide  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStyleGuide(request)
    
    
    public getStyleGuide(request: google.cloud.apihub.v1.IGetStyleGuideRequest): Promise<google.cloud.apihub.v1.StyleGuide>;

Calls GetStyleGuide.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetStyleGuideRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetstyleguiderequest)`   
GetStyleGuideRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.StyleGuide](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.styleguide)>` | Promise  
  
### getStyleGuideContents(request, callback)
    
    
    public getStyleGuideContents(request: google.cloud.apihub.v1.IGetStyleGuideContentsRequest, callback: google.cloud.apihub.v1.LintingService.GetStyleGuideContentsCallback): void;

Calls GetStyleGuideContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStyleGuideContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetstyleguidecontentsrequest)`   
GetStyleGuideContentsRequest message or plain object  
`callback` |  `[GetStyleGuideContentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and StyleGuideContents  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStyleGuideContents(request)
    
    
    public getStyleGuideContents(request: google.cloud.apihub.v1.IGetStyleGuideContentsRequest): Promise<google.cloud.apihub.v1.StyleGuideContents>;

Calls GetStyleGuideContents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetStyleGuideContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igetstyleguidecontentsrequest)`   
GetStyleGuideContentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.StyleGuideContents](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.styleguidecontents)>` | Promise  
  
### lintSpec(request, callback)
    
    
    public lintSpec(request: google.cloud.apihub.v1.ILintSpecRequest, callback: google.cloud.apihub.v1.LintingService.LintSpecCallback): void;

Calls LintSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILintSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilintspecrequest)`   
LintSpecRequest message or plain object  
`callback` |  `[LintSpecCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lintSpec(request)
    
    
    public lintSpec(request: google.cloud.apihub.v1.ILintSpecRequest): Promise<google.protobuf.Empty>;

Calls LintSpec.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILintSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilintspecrequest)`   
LintSpecRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.protobuf.empty)>` | Promise  
  
### updateStyleGuide(request, callback)
    
    
    public updateStyleGuide(request: google.cloud.apihub.v1.IUpdateStyleGuideRequest, callback: google.cloud.apihub.v1.LintingService.UpdateStyleGuideCallback): void;

Calls UpdateStyleGuide.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateStyleGuideRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatestyleguiderequest)`   
UpdateStyleGuideRequest message or plain object  
`callback` |  `[UpdateStyleGuideCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and StyleGuide  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateStyleGuide(request)
    
    
    public updateStyleGuide(request: google.cloud.apihub.v1.IUpdateStyleGuideRequest): Promise<google.cloud.apihub.v1.StyleGuide>;

Calls UpdateStyleGuide.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateStyleGuideRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatestyleguiderequest)`   
UpdateStyleGuideRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.StyleGuide](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.styleguide)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
