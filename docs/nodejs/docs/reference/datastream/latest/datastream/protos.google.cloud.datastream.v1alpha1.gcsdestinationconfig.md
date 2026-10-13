---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.gcsdestinationconfig
title: Class protos.google.cloud.datastream.v1alpha1.GcsDestinationConfig (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:41.604465+00:00
---

# Class protos.google.cloud.datastream.v1alpha1.GcsDestinationConfig (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.gcsdestinationconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datastream.v1alpha1.GcsDestinationConfig (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.0.1  3.4.0  3.3.0  3.1.0  2.2.2  2.1.2  1.1.0  1.0.0  0.2.0 

Represents a GcsDestinationConfig.

## Implements

[protos.google.cloud.datastream.v1alpha1.IGcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igcsdestinationconfig)

## Package

[@google-cloud/datastream](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datastream.v1alpha1.IGcsDestinationConfig);

Constructs a new GcsDestinationConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igcsdestinationconfig)`   
Properties to set  
  
## Properties 

### avroFileFormat
    
    
    public avroFileFormat?: (google.cloud.datastream.v1alpha1.IAvroFileFormat|null);

GcsDestinationConfig avroFileFormat.

### fileFormat
    
    
    public fileFormat?: ("avroFileFormat"|"jsonFileFormat");

GcsDestinationConfig fileFormat.

### fileRotationInterval
    
    
    public fileRotationInterval?: (google.protobuf.IDuration|null);

GcsDestinationConfig fileRotationInterval.

### fileRotationMb
    
    
    public fileRotationMb: number;

GcsDestinationConfig fileRotationMb.

### gcsFileFormat
    
    
    public gcsFileFormat: (google.cloud.datastream.v1alpha1.GcsFileFormat|keyof typeof google.cloud.datastream.v1alpha1.GcsFileFormat);

GcsDestinationConfig gcsFileFormat.

### jsonFileFormat
    
    
    public jsonFileFormat?: (google.cloud.datastream.v1alpha1.IJsonFileFormat|null);

GcsDestinationConfig jsonFileFormat.

### path
    
    
    public path: string;

GcsDestinationConfig path.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datastream.v1alpha1.IGcsDestinationConfig): google.cloud.datastream.v1alpha1.GcsDestinationConfig;

Creates a new GcsDestinationConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igcsdestinationconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.gcsdestinationconfig)` | GcsDestinationConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datastream.v1alpha1.GcsDestinationConfig;

Decodes a GcsDestinationConfig message from the specified reader or buffer.

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
`[GcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.gcsdestinationconfig)` | GcsDestinationConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datastream.v1alpha1.GcsDestinationConfig;

Decodes a GcsDestinationConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.gcsdestinationconfig)` | GcsDestinationConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datastream.v1alpha1.IGcsDestinationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GcsDestinationConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igcsdestinationconfig)`   
GcsDestinationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datastream.v1alpha1.IGcsDestinationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GcsDestinationConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igcsdestinationconfig)`   
GcsDestinationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datastream.v1alpha1.GcsDestinationConfig;

Creates a GcsDestinationConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.gcsdestinationconfig)` | GcsDestinationConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GcsDestinationConfig

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

Converts this GcsDestinationConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datastream.v1alpha1.GcsDestinationConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GcsDestinationConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GcsDestinationConfig](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.gcsdestinationconfig)`   
GcsDestinationConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GcsDestinationConfig message.

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
