---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataasset-class
title: Class protos.google.cloud.dataplex.v1.DataAsset (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:33.551567+00:00
---

# Class protos.google.cloud.dataplex.v1.DataAsset (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataasset-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.DataAsset (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a DataAsset.

## Implements

[protos.google.cloud.dataplex.v1.IDataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataasset)

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataplex.v1.IDataAsset);

Constructs a new DataAsset.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataasset)`   
Properties to set  
  
## Properties 

### accessGroupConfigs
    
    
    public accessGroupConfigs: { [k: string]: google.cloud.dataplex.v1.DataAsset.IAccessGroupConfig };

DataAsset accessGroupConfigs.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

DataAsset createTime.

### etag
    
    
    public etag: string;

DataAsset etag.

### labels
    
    
    public labels: { [k: string]: string };

DataAsset labels.

### name
    
    
    public name: string;

DataAsset name.

### resource
    
    
    public resource: string;

DataAsset resource.

### uid
    
    
    public uid: string;

DataAsset uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

DataAsset updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataplex.v1.IDataAsset): google.cloud.dataplex.v1.DataAsset;

Creates a new DataAsset instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataasset)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataasset-class)` | DataAsset instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataplex.v1.DataAsset;

Decodes a DataAsset message from the specified reader or buffer.

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
`[DataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataasset-class)` | DataAsset  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataplex.v1.DataAsset;

Decodes a DataAsset message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataasset-class)` | DataAsset  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataplex.v1.IDataAsset, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataAsset message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataasset)`   
DataAsset message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataplex.v1.IDataAsset, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataAsset message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataasset)`   
DataAsset message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataplex.v1.DataAsset;

Creates a DataAsset message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataasset-class)` | DataAsset  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DataAsset

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

Converts this DataAsset to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataplex.v1.DataAsset, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DataAsset message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DataAsset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataasset-class)`   
DataAsset  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DataAsset message.

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
