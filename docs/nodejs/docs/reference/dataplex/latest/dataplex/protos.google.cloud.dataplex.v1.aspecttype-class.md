---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.aspecttype-class
title: Class protos.google.cloud.dataplex.v1.AspectType (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:20.322078+00:00
---

# Class protos.google.cloud.dataplex.v1.AspectType (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.aspecttype-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.AspectType (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents an AspectType.

## Implements

[protos.google.cloud.dataplex.v1.IAspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaspecttype)

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataplex.v1.IAspectType);

Constructs a new AspectType.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaspecttype)`   
Properties to set  
  
## Properties 

### authorization
    
    
    public authorization?: (google.cloud.dataplex.v1.AspectType.IAuthorization|null);

AspectType authorization.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AspectType createTime.

### dataClassification
    
    
    public dataClassification: (google.cloud.dataplex.v1.AspectType.DataClassification|keyof typeof google.cloud.dataplex.v1.AspectType.DataClassification);

AspectType dataClassification.

### description
    
    
    public description: string;

AspectType description.

### displayName
    
    
    public displayName: string;

AspectType displayName.

### etag
    
    
    public etag: string;

AspectType etag.

### labels
    
    
    public labels: { [k: string]: string };

AspectType labels.

### metadataTemplate
    
    
    public metadataTemplate?: (google.cloud.dataplex.v1.AspectType.IMetadataTemplate|null);

AspectType metadataTemplate.

### name
    
    
    public name: string;

AspectType name.

### transferStatus
    
    
    public transferStatus: (google.cloud.dataplex.v1.TransferStatus|keyof typeof google.cloud.dataplex.v1.TransferStatus);

AspectType transferStatus.

### uid
    
    
    public uid: string;

AspectType uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

AspectType updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataplex.v1.IAspectType): google.cloud.dataplex.v1.AspectType;

Creates a new AspectType instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaspecttype)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.aspecttype-class)` | AspectType instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataplex.v1.AspectType;

Decodes an AspectType message from the specified reader or buffer.

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
`[AspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.aspecttype-class)` | AspectType  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataplex.v1.AspectType;

Decodes an AspectType message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.aspecttype-class)` | AspectType  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataplex.v1.IAspectType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AspectType message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaspecttype)`   
AspectType message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataplex.v1.IAspectType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AspectType message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaspecttype)`   
AspectType message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataplex.v1.AspectType;

Creates an AspectType message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.aspecttype-class)` | AspectType  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AspectType

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

Converts this AspectType to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataplex.v1.AspectType, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AspectType message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.aspecttype-class)`   
AspectType  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AspectType message.

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
