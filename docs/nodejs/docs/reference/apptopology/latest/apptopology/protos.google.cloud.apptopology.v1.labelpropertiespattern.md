---
url: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelpropertiespattern
title: Class protos.google.cloud.apptopology.v1.LabelPropertiesPattern (0.3.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:01:03.905097+00:00
---

# Class protos.google.cloud.apptopology.v1.LabelPropertiesPattern (0.3.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelpropertiespattern

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apptopology.v1.LabelPropertiesPattern (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.0 

Represents a LabelPropertiesPattern.

## Implements

[protos.google.cloud.apptopology.v1.ILabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelpropertiespattern)

## Package

[@google-cloud/apptopology](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apptopology.v1.ILabelPropertiesPattern);

Constructs a new LabelPropertiesPattern.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelpropertiespattern)`   
Properties to set  
  
## Properties 

### labelMatcherExpr
    
    
    public labelMatcherExpr: string;

LabelPropertiesPattern labelMatcherExpr.

### propertyMatcherExpr
    
    
    public propertyMatcherExpr: string;

LabelPropertiesPattern propertyMatcherExpr.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apptopology.v1.ILabelPropertiesPattern): google.cloud.apptopology.v1.LabelPropertiesPattern;

Creates a new LabelPropertiesPattern instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelpropertiespattern)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelpropertiespattern)` | LabelPropertiesPattern instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apptopology.v1.LabelPropertiesPattern;

Decodes a LabelPropertiesPattern message from the specified reader or buffer.

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
`[LabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelpropertiespattern)` | LabelPropertiesPattern  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apptopology.v1.LabelPropertiesPattern;

Decodes a LabelPropertiesPattern message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelpropertiespattern)` | LabelPropertiesPattern  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apptopology.v1.ILabelPropertiesPattern, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LabelPropertiesPattern message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelpropertiespattern)`   
LabelPropertiesPattern message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apptopology.v1.ILabelPropertiesPattern, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LabelPropertiesPattern message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelpropertiespattern)`   
LabelPropertiesPattern message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apptopology.v1.LabelPropertiesPattern;

Creates a LabelPropertiesPattern message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelpropertiespattern)` | LabelPropertiesPattern  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LabelPropertiesPattern

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

Converts this LabelPropertiesPattern to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apptopology.v1.LabelPropertiesPattern, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LabelPropertiesPattern message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LabelPropertiesPattern](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelpropertiespattern)`   
LabelPropertiesPattern  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LabelPropertiesPattern message.

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
