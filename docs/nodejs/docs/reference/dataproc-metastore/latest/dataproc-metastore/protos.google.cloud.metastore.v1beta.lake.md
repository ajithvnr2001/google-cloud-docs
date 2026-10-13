---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.lake
title: Class protos.google.cloud.metastore.v1beta.Lake (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:43.284539+00:00
---

# Class protos.google.cloud.metastore.v1beta.Lake (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.lake

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.metastore.v1beta.Lake (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.0  4.1.0  3.5.0  3.4.1  3.1.2  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.6 

Represents a Lake.

## Implements

[protos.google.cloud.metastore.v1beta.ILake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ilake)

## Package

[@google-cloud/dataproc-metastore](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.metastore.v1beta.ILake);

Constructs a new Lake.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ilake)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

Lake name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.metastore.v1beta.ILake): google.cloud.metastore.v1beta.Lake;

Creates a new Lake instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ilake)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Lake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.lake)` | Lake instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.metastore.v1beta.Lake;

Decodes a Lake message from the specified reader or buffer.

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
`[Lake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.lake)` | Lake  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.metastore.v1beta.Lake;

Decodes a Lake message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Lake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.lake)` | Lake  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.metastore.v1beta.ILake, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Lake message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ilake)`   
Lake message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.metastore.v1beta.ILake, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Lake message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ilake)`   
Lake message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.metastore.v1beta.Lake;

Creates a Lake message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Lake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.lake)` | Lake  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Lake

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

Converts this Lake to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.metastore.v1beta.Lake, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Lake message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Lake](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.lake)`   
Lake  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Lake message.

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
