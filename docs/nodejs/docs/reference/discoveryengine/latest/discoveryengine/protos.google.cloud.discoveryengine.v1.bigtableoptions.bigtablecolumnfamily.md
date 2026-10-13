---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.bigtablecolumnfamily
title: Class protos.google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumnFamily (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:02:46.466072+00:00
---

# Class protos.google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumnFamily (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.bigtablecolumnfamily

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumnFamily (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a BigtableColumnFamily.

## Implements

[protos.google.cloud.discoveryengine.v1.BigtableOptions.IBigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.ibigtablecolumnfamily)

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.discoveryengine.v1.BigtableOptions.IBigtableColumnFamily);

Constructs a new BigtableColumnFamily.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.ibigtablecolumnfamily)`   
Properties to set  
  
## Properties 

### columns
    
    
    public columns: google.cloud.discoveryengine.v1.BigtableOptions.IBigtableColumn[];

BigtableColumnFamily columns.

### encoding
    
    
    public encoding: (google.cloud.discoveryengine.v1.BigtableOptions.Encoding|keyof typeof google.cloud.discoveryengine.v1.BigtableOptions.Encoding);

BigtableColumnFamily encoding.

### fieldName
    
    
    public fieldName: string;

BigtableColumnFamily fieldName.

### type
    
    
    public type: (google.cloud.discoveryengine.v1.BigtableOptions.Type|keyof typeof google.cloud.discoveryengine.v1.BigtableOptions.Type);

BigtableColumnFamily type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.discoveryengine.v1.BigtableOptions.IBigtableColumnFamily): google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumnFamily;

Creates a new BigtableColumnFamily instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.ibigtablecolumnfamily)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.bigtablecolumnfamily)` | BigtableColumnFamily instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumnFamily;

Decodes a BigtableColumnFamily message from the specified reader or buffer.

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
`[BigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.bigtablecolumnfamily)` | BigtableColumnFamily  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumnFamily;

Decodes a BigtableColumnFamily message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.bigtablecolumnfamily)` | BigtableColumnFamily  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.discoveryengine.v1.BigtableOptions.IBigtableColumnFamily, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BigtableColumnFamily message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.ibigtablecolumnfamily)`   
BigtableColumnFamily message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.discoveryengine.v1.BigtableOptions.IBigtableColumnFamily, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BigtableColumnFamily message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.ibigtablecolumnfamily)`   
BigtableColumnFamily message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumnFamily;

Creates a BigtableColumnFamily message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.bigtablecolumnfamily)` | BigtableColumnFamily  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BigtableColumnFamily

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

Converts this BigtableColumnFamily to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumnFamily, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BigtableColumnFamily message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BigtableColumnFamily](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.bigtableoptions.bigtablecolumnfamily)`   
BigtableColumnFamily  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BigtableColumnFamily message.

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
