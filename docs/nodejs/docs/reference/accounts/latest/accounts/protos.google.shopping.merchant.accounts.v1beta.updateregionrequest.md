---
url: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.updateregionrequest
title: Class protos.google.shopping.merchant.accounts.v1beta.UpdateRegionRequest (4.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:25.363814+00:00
---

# Class protos.google.shopping.merchant.accounts.v1beta.UpdateRegionRequest (4.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.updateregionrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.accounts.v1beta.UpdateRegionRequest (4.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.1 (latest)  3.2.0  2.2.0  1.0.0 

Represents an UpdateRegionRequest.

## Implements

[protos.google.shopping.merchant.accounts.v1beta.IUpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateregionrequest)

## Package

[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.accounts.v1beta.IUpdateRegionRequest);

Constructs a new UpdateRegionRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateregionrequest)`   
Properties to set  
  
## Properties 

### region
    
    
    public region?: (google.shopping.merchant.accounts.v1beta.IRegion|null);

UpdateRegionRequest region.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateRegionRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.accounts.v1beta.IUpdateRegionRequest): google.shopping.merchant.accounts.v1beta.UpdateRegionRequest;

Creates a new UpdateRegionRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateregionrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.updateregionrequest)` | UpdateRegionRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.accounts.v1beta.UpdateRegionRequest;

Decodes an UpdateRegionRequest message from the specified reader or buffer.

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
`[UpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.updateregionrequest)` | UpdateRegionRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.accounts.v1beta.UpdateRegionRequest;

Decodes an UpdateRegionRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.updateregionrequest)` | UpdateRegionRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.accounts.v1beta.IUpdateRegionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateRegionRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateregionrequest)`   
UpdateRegionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.accounts.v1beta.IUpdateRegionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateRegionRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.iupdateregionrequest)`   
UpdateRegionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.accounts.v1beta.UpdateRegionRequest;

Creates an UpdateRegionRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.updateregionrequest)` | UpdateRegionRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateRegionRequest

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

Converts this UpdateRegionRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.accounts.v1beta.UpdateRegionRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateRegionRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateRegionRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.updateregionrequest)`   
UpdateRegionRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateRegionRequest message.

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
