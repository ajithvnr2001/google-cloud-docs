---
url: https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.caseexpression
title: Class protos.google.analytics.data.v1beta.DimensionExpression.CaseExpression (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:24.158685+00:00
---

# Class protos.google.analytics.data.v1beta.DimensionExpression.CaseExpression (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.caseexpression

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.data.v1beta.DimensionExpression.CaseExpression (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.2.0  7.1.0  6.1.0  6.0.0  4.12.0  4.11.0  4.9.0  4.8.0  4.6.0  4.5.0  3.2.1 

Represents a CaseExpression.

## Implements

[protos.google.analytics.data.v1beta.DimensionExpression.ICaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.icaseexpression)

## Package

[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.data.v1beta.DimensionExpression.ICaseExpression);

Constructs a new CaseExpression.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.icaseexpression)`   
Properties to set  
  
## Properties 

### dimensionName
    
    
    public dimensionName: string;

CaseExpression dimensionName.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.data.v1beta.DimensionExpression.ICaseExpression): google.analytics.data.v1beta.DimensionExpression.CaseExpression;

Creates a new CaseExpression instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.icaseexpression)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.caseexpression)` | CaseExpression instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.data.v1beta.DimensionExpression.CaseExpression;

Decodes a CaseExpression message from the specified reader or buffer.

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
`[CaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.caseexpression)` | CaseExpression  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.data.v1beta.DimensionExpression.CaseExpression;

Decodes a CaseExpression message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.caseexpression)` | CaseExpression  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.data.v1beta.DimensionExpression.ICaseExpression, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CaseExpression message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.icaseexpression)`   
CaseExpression message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.data.v1beta.DimensionExpression.ICaseExpression, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CaseExpression message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.icaseexpression)`   
CaseExpression message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.data.v1beta.DimensionExpression.CaseExpression;

Creates a CaseExpression message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.caseexpression)` | CaseExpression  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CaseExpression

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

Converts this CaseExpression to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.data.v1beta.DimensionExpression.CaseExpression, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CaseExpression message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CaseExpression](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.dimensionexpression.caseexpression)`   
CaseExpression  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CaseExpression message.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
