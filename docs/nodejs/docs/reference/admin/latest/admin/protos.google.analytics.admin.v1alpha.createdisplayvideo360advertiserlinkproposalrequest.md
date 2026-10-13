---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.createdisplayvideo360advertiserlinkproposalrequest
title: Class protos.google.analytics.admin.v1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:42:30.251254+00:00
---

# Class protos.google.analytics.admin.v1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.createdisplayvideo360advertiserlinkproposalrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents a CreateDisplayVideo360AdvertiserLinkProposalRequest.

## Implements

[protos.google.analytics.admin.v1alpha.ICreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedisplayvideo360advertiserlinkproposalrequest)

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.admin.v1alpha.ICreateDisplayVideo360AdvertiserLinkProposalRequest);

Constructs a new CreateDisplayVideo360AdvertiserLinkProposalRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedisplayvideo360advertiserlinkproposalrequest)`   
Properties to set  
  
## Properties 

### displayVideo_360AdvertiserLinkProposal
    
    
    public displayVideo_360AdvertiserLinkProposal?: (google.analytics.admin.v1alpha.IDisplayVideo360AdvertiserLinkProposal|null);

CreateDisplayVideo360AdvertiserLinkProposalRequest displayVideo_360AdvertiserLinkProposal.

### parent
    
    
    public parent: string;

CreateDisplayVideo360AdvertiserLinkProposalRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.admin.v1alpha.ICreateDisplayVideo360AdvertiserLinkProposalRequest): google.analytics.admin.v1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest;

Creates a new CreateDisplayVideo360AdvertiserLinkProposalRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedisplayvideo360advertiserlinkproposalrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.createdisplayvideo360advertiserlinkproposalrequest)` | CreateDisplayVideo360AdvertiserLinkProposalRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.admin.v1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest;

Decodes a CreateDisplayVideo360AdvertiserLinkProposalRequest message from the specified reader or buffer.

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
`[CreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.createdisplayvideo360advertiserlinkproposalrequest)` | CreateDisplayVideo360AdvertiserLinkProposalRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.admin.v1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest;

Decodes a CreateDisplayVideo360AdvertiserLinkProposalRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.createdisplayvideo360advertiserlinkproposalrequest)` | CreateDisplayVideo360AdvertiserLinkProposalRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.admin.v1alpha.ICreateDisplayVideo360AdvertiserLinkProposalRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateDisplayVideo360AdvertiserLinkProposalRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedisplayvideo360advertiserlinkproposalrequest)`   
CreateDisplayVideo360AdvertiserLinkProposalRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.admin.v1alpha.ICreateDisplayVideo360AdvertiserLinkProposalRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateDisplayVideo360AdvertiserLinkProposalRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedisplayvideo360advertiserlinkproposalrequest)`   
CreateDisplayVideo360AdvertiserLinkProposalRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.admin.v1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest;

Creates a CreateDisplayVideo360AdvertiserLinkProposalRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.createdisplayvideo360advertiserlinkproposalrequest)` | CreateDisplayVideo360AdvertiserLinkProposalRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateDisplayVideo360AdvertiserLinkProposalRequest

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

Converts this CreateDisplayVideo360AdvertiserLinkProposalRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.admin.v1alpha.CreateDisplayVideo360AdvertiserLinkProposalRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateDisplayVideo360AdvertiserLinkProposalRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.createdisplayvideo360advertiserlinkproposalrequest)`   
CreateDisplayVideo360AdvertiserLinkProposalRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateDisplayVideo360AdvertiserLinkProposalRequest message.

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
