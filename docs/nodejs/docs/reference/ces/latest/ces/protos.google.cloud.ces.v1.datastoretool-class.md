---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.datastoretool-class
title: Class protos.google.cloud.ces.v1.DataStoreTool (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:09.204532+00:00
---

# Class protos.google.cloud.ces.v1.DataStoreTool (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.datastoretool-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.DataStoreTool (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents a DataStoreTool.

## Implements

[protos.google.cloud.ces.v1.IDataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.idatastoretool)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IDataStoreTool);

Constructs a new DataStoreTool.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.idatastoretool)`   
Properties to set  
  
## Properties 

### boostSpecs
    
    
    public boostSpecs: google.cloud.ces.v1.DataStoreTool.IBoostSpecs[];

DataStoreTool boostSpecs.

### dataStoreSource
    
    
    public dataStoreSource?: (google.cloud.ces.v1.DataStoreTool.IDataStoreSource|null);

DataStoreTool dataStoreSource.

### description
    
    
    public description: string;

DataStoreTool description.

### engineSource
    
    
    public engineSource?: (google.cloud.ces.v1.DataStoreTool.IEngineSource|null);

DataStoreTool engineSource.

### filterParameterBehavior
    
    
    public filterParameterBehavior: (google.cloud.ces.v1.DataStoreTool.FilterParameterBehavior|keyof typeof google.cloud.ces.v1.DataStoreTool.FilterParameterBehavior);

DataStoreTool filterParameterBehavior.

### modalityConfigs
    
    
    public modalityConfigs: google.cloud.ces.v1.DataStoreTool.IModalityConfig[];

DataStoreTool modalityConfigs.

### name
    
    
    public name: string;

DataStoreTool name.

### searchSource
    
    
    public searchSource?: ("dataStoreSource"|"engineSource");

DataStoreTool searchSource.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IDataStoreTool): google.cloud.ces.v1.DataStoreTool;

Creates a new DataStoreTool instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.idatastoretool)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.datastoretool-class)` | DataStoreTool instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.DataStoreTool;

Decodes a DataStoreTool message from the specified reader or buffer.

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
`[DataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.datastoretool-class)` | DataStoreTool  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.DataStoreTool;

Decodes a DataStoreTool message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.datastoretool-class)` | DataStoreTool  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IDataStoreTool, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataStoreTool message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.idatastoretool)`   
DataStoreTool message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IDataStoreTool, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataStoreTool message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.idatastoretool)`   
DataStoreTool message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.DataStoreTool;

Creates a DataStoreTool message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.datastoretool-class)` | DataStoreTool  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DataStoreTool

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

Converts this DataStoreTool to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.DataStoreTool, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DataStoreTool message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DataStoreTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.datastoretool-class)`   
DataStoreTool  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DataStoreTool message.

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
