---
url: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.volume
title: Class protos.google.cloud.run.v2.Volume (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:11.392098+00:00
---

# Class protos.google.cloud.run.v2.Volume (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.volume

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.run.v2.Volume (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.3.0  3.2.0  2.1.0  1.5.0  1.0.2  0.5.0  0.4.2  0.2.3 

Represents a Volume.

## Implements

[protos.google.cloud.run.v2.IVolume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ivolume)

## Package

[@google-cloud/run](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.run.v2.IVolume);

Constructs a new Volume.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVolume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ivolume)`   
Properties to set  
  
## Properties 

### cloudSqlInstance
    
    
    public cloudSqlInstance?: (google.cloud.run.v2.ICloudSqlInstance|null);

Volume cloudSqlInstance.

### emptyDir
    
    
    public emptyDir?: (google.cloud.run.v2.IEmptyDirVolumeSource|null);

Volume emptyDir.

### gcs
    
    
    public gcs?: (google.cloud.run.v2.IGCSVolumeSource|null);

Volume gcs.

### name
    
    
    public name: string;

Volume name.

### nfs
    
    
    public nfs?: (google.cloud.run.v2.INFSVolumeSource|null);

Volume nfs.

### secret
    
    
    public secret?: (google.cloud.run.v2.ISecretVolumeSource|null);

Volume secret.

### volumeType
    
    
    public volumeType?: ("secret"|"cloudSqlInstance"|"emptyDir"|"nfs"|"gcs");

Volume volumeType.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.run.v2.IVolume): google.cloud.run.v2.Volume;

Creates a new Volume instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVolume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ivolume)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Volume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.volume)` | Volume instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.run.v2.Volume;

Decodes a Volume message from the specified reader or buffer.

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
`[Volume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.volume)` | Volume  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.run.v2.Volume;

Decodes a Volume message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Volume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.volume)` | Volume  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.run.v2.IVolume, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Volume message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVolume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ivolume)`   
Volume message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.run.v2.IVolume, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Volume message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVolume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ivolume)`   
Volume message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.run.v2.Volume;

Creates a Volume message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Volume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.volume)` | Volume  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Volume

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

Converts this Volume to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.run.v2.Volume, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Volume message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Volume](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.volume)`   
Volume  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Volume message.

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
