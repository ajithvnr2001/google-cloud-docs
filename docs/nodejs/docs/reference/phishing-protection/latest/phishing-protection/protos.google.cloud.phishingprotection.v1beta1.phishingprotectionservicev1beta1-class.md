---
url: https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.phishingprotectionservicev1beta1-class
title: Class protos.google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1 (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:47.003180+00:00
---

# Class protos.google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1 (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.phishingprotectionservicev1beta1-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1 (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.0  5.0.1  3.0.8  2.5.0  2.4.7 

Represents a PhishingProtectionServiceV1Beta1

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1

## Package

[@google-cloud/phishing-protection](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new PhishingProtectionServiceV1Beta1 service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): PhishingProtectionServiceV1Beta1;

Creates new PhishingProtectionServiceV1Beta1 service using the specified rpc implementation.

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
`[PhishingProtectionServiceV1Beta1](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.phishingprotectionservicev1beta1-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### reportPhishing(request, callback)
    
    
    public reportPhishing(request: google.cloud.phishingprotection.v1beta1.IReportPhishingRequest, callback: google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1.ReportPhishingCallback): void;

Calls ReportPhishing.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReportPhishingRequest](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingrequest)`   
ReportPhishingRequest message or plain object  
`callback` |  `[ReportPhishingCallback](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/overview.html)`   
Node-style callback called with the error, if any, and ReportPhishingResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### reportPhishing(request)
    
    
    public reportPhishing(request: google.cloud.phishingprotection.v1beta1.IReportPhishingRequest): Promise<google.cloud.phishingprotection.v1beta1.ReportPhishingResponse>;

Calls ReportPhishing.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReportPhishingRequest](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingrequest)`   
ReportPhishingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.phishingprotection.v1beta1.ReportPhishingResponse](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.reportphishingresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
