---
url: https://docs.cloud.google.com/static/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application
title: Class protos.google.ads.admanager.v1.Application (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:47.732135+00:00
---

# Class protos.google.ads.admanager.v1.Application (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/static/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.Application (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an Application.

## Implements

[protos.google.ads.admanager.v1.IApplication](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iapplication)

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.admanager.v1.IApplication);

Constructs a new Application.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApplication](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iapplication)`   
Properties to set  
  
## Properties 

### applicationCode
    
    
    public applicationCode?: (string|null);

Application applicationCode.

### approvalStatus
    
    
    public approvalStatus?: (google.ads.admanager.v1.ApplicationApprovalStatusEnum.ApplicationApprovalStatus|keyof typeof google.ads.admanager.v1.ApplicationApprovalStatusEnum.ApplicationApprovalStatus|null);

Application approvalStatus.

### appStoreDisplayName
    
    
    public appStoreDisplayName?: (string|null);

Application appStoreDisplayName.

### appStoreId
    
    
    public appStoreId?: (string|null);

Application appStoreId.

### appStores
    
    
    public appStores: google.ads.admanager.v1.ApplicationStoreEnum.ApplicationStore[];

Application appStores.

### archived
    
    
    public archived?: (boolean|null);

Application archived.

### developer
    
    
    public developer?: (string|null);

Application developer.

### displayName
    
    
    public displayName?: (string|null);

Application displayName.

### downloadUrl
    
    
    public downloadUrl?: (string|null);

Application downloadUrl.

### free
    
    
    public free?: (boolean|null);

Application free.

### name
    
    
    public name: string;

Application name.

### platform
    
    
    public platform?: (google.ads.admanager.v1.ApplicationPlatformEnum.ApplicationPlatform|keyof typeof google.ads.admanager.v1.ApplicationPlatformEnum.ApplicationPlatform|null);

Application platform.

### webviewClaimingStatus
    
    
    public webviewClaimingStatus?: (google.ads.admanager.v1.WebviewClaimingStatusEnum.WebviewClaimingStatus|keyof typeof google.ads.admanager.v1.WebviewClaimingStatusEnum.WebviewClaimingStatus|null);

Application webviewClaimingStatus.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.admanager.v1.IApplication): google.ads.admanager.v1.Application;

Creates a new Application instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApplication](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iapplication)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application)` | Application instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.admanager.v1.Application;

Decodes an Application message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application)` | Application  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.admanager.v1.Application;

Decodes an Application message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application)` | Application  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.admanager.v1.IApplication, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Application message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApplication](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iapplication)`   
Application message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.admanager.v1.IApplication, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Application message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApplication](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iapplication)`   
Application message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.admanager.v1.Application;

Creates an Application message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application)` | Application  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Application

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this Application to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.admanager.v1.Application, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Application message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Application](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.application)`   
Application  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Application message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
