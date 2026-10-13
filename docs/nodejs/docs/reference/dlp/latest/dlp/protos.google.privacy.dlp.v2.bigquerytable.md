---
url: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bigquerytable
title: Class protos.google.privacy.dlp.v2.BigQueryTable (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:17.790481+00:00
---

# Class protos.google.privacy.dlp.v2.BigQueryTable (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bigquerytable

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.privacy.dlp.v2.BigQueryTable (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.6.0  6.2.0  6.1.0  5.13.0  5.11.0  5.10.0  5.7.0  5.5.0  5.3.0  5.0.0  4.4.2  4.2.0  4.1.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.8 

Represents a BigQueryTable.

## Implements

[protos.google.privacy.dlp.v2.IBigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ibigquerytable)

## Package

[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.privacy.dlp.v2.IBigQueryTable);

Constructs a new BigQueryTable.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ibigquerytable)`   
Properties to set  
  
## Properties 

### datasetId
    
    
    public datasetId: string;

BigQueryTable datasetId.

### projectId
    
    
    public projectId: string;

BigQueryTable projectId.

### tableId
    
    
    public tableId: string;

BigQueryTable tableId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.privacy.dlp.v2.IBigQueryTable): google.privacy.dlp.v2.BigQueryTable;

Creates a new BigQueryTable instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ibigquerytable)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bigquerytable)` | BigQueryTable instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.privacy.dlp.v2.BigQueryTable;

Decodes a BigQueryTable message from the specified reader or buffer.

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
`[BigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bigquerytable)` | BigQueryTable  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.privacy.dlp.v2.BigQueryTable;

Decodes a BigQueryTable message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bigquerytable)` | BigQueryTable  
  
### encode(message, writer)
    
    
    public static encode(message: google.privacy.dlp.v2.IBigQueryTable, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BigQueryTable message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ibigquerytable)`   
BigQueryTable message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.privacy.dlp.v2.IBigQueryTable, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BigQueryTable message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ibigquerytable)`   
BigQueryTable message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.privacy.dlp.v2.BigQueryTable;

Creates a BigQueryTable message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bigquerytable)` | BigQueryTable  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BigQueryTable

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

Converts this BigQueryTable to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.privacy.dlp.v2.BigQueryTable, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BigQueryTable message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BigQueryTable](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bigquerytable)`   
BigQueryTable  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BigQueryTable message.

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
