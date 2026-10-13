---
url: https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.methoddetails
title: Class protos.google.shopping.merchant.quota.v1.MethodDetails (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:51.845011+00:00
---

# Class protos.google.shopping.merchant.quota.v1.MethodDetails (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.methoddetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.quota.v1.MethodDetails (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.9.0  0.4.0  0.3.1  0.1.1 

Represents a MethodDetails.

## Implements

[protos.google.shopping.merchant.quota.v1.IMethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.imethoddetails)

## Package

[@google-shopping/quota](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.quota.v1.IMethodDetails);

Constructs a new MethodDetails.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.imethoddetails)`   
Properties to set  
  
## Properties 

### method
    
    
    public method: string;

MethodDetails method.

### path
    
    
    public path: string;

MethodDetails path.

### subapi
    
    
    public subapi: string;

MethodDetails subapi.

### version
    
    
    public version: string;

MethodDetails version.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.quota.v1.IMethodDetails): google.shopping.merchant.quota.v1.MethodDetails;

Creates a new MethodDetails instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.imethoddetails)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.methoddetails)` | MethodDetails instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.quota.v1.MethodDetails;

Decodes a MethodDetails message from the specified reader or buffer.

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
`[MethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.methoddetails)` | MethodDetails  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.quota.v1.MethodDetails;

Decodes a MethodDetails message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.methoddetails)` | MethodDetails  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.quota.v1.IMethodDetails, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MethodDetails message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.imethoddetails)`   
MethodDetails message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.quota.v1.IMethodDetails, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MethodDetails message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.imethoddetails)`   
MethodDetails message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.quota.v1.MethodDetails;

Creates a MethodDetails message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.methoddetails)` | MethodDetails  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MethodDetails

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

Converts this MethodDetails to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.quota.v1.MethodDetails, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MethodDetails message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MethodDetails](https://docs.cloud.google.com/nodejs/docs/reference/quota/latest/quota/protos.google.shopping.merchant.quota.v1.methoddetails)`   
MethodDetails  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MethodDetails message.

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
