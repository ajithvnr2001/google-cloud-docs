---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partnerlinkservice-class
title: Class protos.google.ads.datamanager.v1.PartnerLinkService (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:34.231351+00:00
---

# Class protos.google.ads.datamanager.v1.PartnerLinkService (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partnerlinkservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.PartnerLinkService (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a PartnerLinkService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.datamanager.v1.PartnerLinkService

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new PartnerLinkService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): PartnerLinkService;

Creates new PartnerLinkService service using the specified rpc implementation.

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
`[PartnerLinkService](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partnerlinkservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createPartnerLink(request, callback)
    
    
    public createPartnerLink(request: google.ads.datamanager.v1.ICreatePartnerLinkRequest, callback: google.ads.datamanager.v1.PartnerLinkService.CreatePartnerLinkCallback): void;

Calls CreatePartnerLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icreatepartnerlinkrequest)`   
CreatePartnerLinkRequest message or plain object  
`callback` |  `[CreatePartnerLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and PartnerLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPartnerLink(request)
    
    
    public createPartnerLink(request: google.ads.datamanager.v1.ICreatePartnerLinkRequest): Promise<google.ads.datamanager.v1.PartnerLink>;

Calls CreatePartnerLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icreatepartnerlinkrequest)`   
CreatePartnerLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.PartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partnerlink)>` | Promise  
  
### deletePartnerLink(request, callback)
    
    
    public deletePartnerLink(request: google.ads.datamanager.v1.IDeletePartnerLinkRequest, callback: google.ads.datamanager.v1.PartnerLinkService.DeletePartnerLinkCallback): void;

Calls DeletePartnerLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ideletepartnerlinkrequest)`   
DeletePartnerLinkRequest message or plain object  
`callback` |  `[DeletePartnerLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePartnerLink(request)
    
    
    public deletePartnerLink(request: google.ads.datamanager.v1.IDeletePartnerLinkRequest): Promise<google.protobuf.Empty>;

Calls DeletePartnerLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePartnerLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ideletepartnerlinkrequest)`   
DeletePartnerLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.protobuf.empty)>` | Promise  
  
### searchPartnerLinks(request, callback)
    
    
    public searchPartnerLinks(request: google.ads.datamanager.v1.ISearchPartnerLinksRequest, callback: google.ads.datamanager.v1.PartnerLinkService.SearchPartnerLinksCallback): void;

Calls SearchPartnerLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchPartnerLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.isearchpartnerlinksrequest)`   
SearchPartnerLinksRequest message or plain object  
`callback` |  `[SearchPartnerLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchPartnerLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchPartnerLinks(request)
    
    
    public searchPartnerLinks(request: google.ads.datamanager.v1.ISearchPartnerLinksRequest): Promise<google.ads.datamanager.v1.SearchPartnerLinksResponse>;

Calls SearchPartnerLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchPartnerLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.isearchpartnerlinksrequest)`   
SearchPartnerLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.SearchPartnerLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.searchpartnerlinksresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
