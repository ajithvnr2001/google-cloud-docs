---
url: https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.breakdown-class
title: Class protos.google.shopping.merchant.issueresolution.v1beta.Breakdown (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:43.914676+00:00
---

# Class protos.google.shopping.merchant.issueresolution.v1beta.Breakdown (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.breakdown-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.issueresolution.v1beta.Breakdown (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.4.0 

Represents a Breakdown.

## Implements

[protos.google.shopping.merchant.issueresolution.v1beta.IBreakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.ibreakdown)

## Package

[@google-shopping/issueresolution](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.issueresolution.v1beta.IBreakdown);

Constructs a new Breakdown.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBreakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.ibreakdown)`   
Properties to set  
  
## Properties 

### details
    
    
    public details: string[];

Breakdown details.

### regions
    
    
    public regions: google.shopping.merchant.issueresolution.v1beta.Breakdown.IRegion[];

Breakdown regions.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.issueresolution.v1beta.IBreakdown): google.shopping.merchant.issueresolution.v1beta.Breakdown;

Creates a new Breakdown instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBreakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.ibreakdown)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Breakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.breakdown-class)` | Breakdown instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.issueresolution.v1beta.Breakdown;

Decodes a Breakdown message from the specified reader or buffer.

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
`[Breakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.breakdown-class)` | Breakdown  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.issueresolution.v1beta.Breakdown;

Decodes a Breakdown message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Breakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.breakdown-class)` | Breakdown  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.issueresolution.v1beta.IBreakdown, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Breakdown message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBreakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.ibreakdown)`   
Breakdown message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.issueresolution.v1beta.IBreakdown, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Breakdown message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBreakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.ibreakdown)`   
Breakdown message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.issueresolution.v1beta.Breakdown;

Creates a Breakdown message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Breakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.breakdown-class)` | Breakdown  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Breakdown

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

Converts this Breakdown to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.issueresolution.v1beta.Breakdown, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Breakdown message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Breakdown](https://docs.cloud.google.com/nodejs/docs/reference/issueresolution/latest/issueresolution/protos.google.shopping.merchant.issueresolution.v1beta.breakdown-class)`   
Breakdown  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Breakdown message.

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
