---
url: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelproperties
title: Class protos.google.cloud.apptopology.v1.LabelProperties (0.3.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:01:03.773556+00:00
---

# Class protos.google.cloud.apptopology.v1.LabelProperties (0.3.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelproperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apptopology.v1.LabelProperties (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.0 

Represents a LabelProperties.

## Implements

[protos.google.cloud.apptopology.v1.ILabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelproperties)

## Package

[@google-cloud/apptopology](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apptopology.v1.ILabelProperties);

Constructs a new LabelProperties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelproperties)`   
Properties to set  
  
## Properties 

### description
    
    
    public description: string;

LabelProperties description.

### label
    
    
    public label: string;

LabelProperties label.

### properties
    
    
    public properties: google.cloud.apptopology.v1.IProperty[];

LabelProperties properties.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apptopology.v1.ILabelProperties): google.cloud.apptopology.v1.LabelProperties;

Creates a new LabelProperties instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelproperties)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelproperties)` | LabelProperties instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apptopology.v1.LabelProperties;

Decodes a LabelProperties message from the specified reader or buffer.

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
`[LabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelproperties)` | LabelProperties  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apptopology.v1.LabelProperties;

Decodes a LabelProperties message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelproperties)` | LabelProperties  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apptopology.v1.ILabelProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LabelProperties message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelproperties)`   
LabelProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apptopology.v1.ILabelProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LabelProperties message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilabelproperties)`   
LabelProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apptopology.v1.LabelProperties;

Creates a LabelProperties message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelproperties)` | LabelProperties  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LabelProperties

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

Converts this LabelProperties to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apptopology.v1.LabelProperties, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LabelProperties message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LabelProperties](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.labelproperties)`   
LabelProperties  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LabelProperties message.

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
