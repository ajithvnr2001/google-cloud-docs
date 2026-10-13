---
url: https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.getbillingaccountrequest
title: Class protos.google.cloud.billing.v1.GetBillingAccountRequest (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:34.876838+00:00
---

# Class protos.google.cloud.billing.v1.GetBillingAccountRequest (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.getbillingaccountrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.billing.v1.GetBillingAccountRequest (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  4.6.0  4.2.0  4.1.0  4.0.0  3.3.2  3.1.3  2.4.0  2.3.0  2.2.7 

Represents a GetBillingAccountRequest.

## Implements

[protos.google.cloud.billing.v1.IGetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.igetbillingaccountrequest)

## Package

[@google-cloud/billing](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.billing.v1.IGetBillingAccountRequest);

Constructs a new GetBillingAccountRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.igetbillingaccountrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

GetBillingAccountRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.billing.v1.IGetBillingAccountRequest): google.cloud.billing.v1.GetBillingAccountRequest;

Creates a new GetBillingAccountRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.igetbillingaccountrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.getbillingaccountrequest)` | GetBillingAccountRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.billing.v1.GetBillingAccountRequest;

Decodes a GetBillingAccountRequest message from the specified reader or buffer.

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
`[GetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.getbillingaccountrequest)` | GetBillingAccountRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.billing.v1.GetBillingAccountRequest;

Decodes a GetBillingAccountRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.getbillingaccountrequest)` | GetBillingAccountRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.billing.v1.IGetBillingAccountRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetBillingAccountRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.igetbillingaccountrequest)`   
GetBillingAccountRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.billing.v1.IGetBillingAccountRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetBillingAccountRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.igetbillingaccountrequest)`   
GetBillingAccountRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.billing.v1.GetBillingAccountRequest;

Creates a GetBillingAccountRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.getbillingaccountrequest)` | GetBillingAccountRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GetBillingAccountRequest

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

Converts this GetBillingAccountRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.billing.v1.GetBillingAccountRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GetBillingAccountRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GetBillingAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing/latest/billing/protos.google.cloud.billing.v1.getbillingaccountrequest)`   
GetBillingAccountRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GetBillingAccountRequest message.

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
