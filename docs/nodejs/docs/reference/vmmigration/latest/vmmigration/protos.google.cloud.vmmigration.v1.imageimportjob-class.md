---
url: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imageimportjob-class
title: Class protos.google.cloud.vmmigration.v1.ImageImportJob (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:52.401224+00:00
---

# Class protos.google.cloud.vmmigration.v1.ImageImportJob (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imageimportjob-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.vmmigration.v1.ImageImportJob (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  3.0.2  2.3.2  2.2.1  2.1.0  1.0.0  0.2.0 

Represents an ImageImportJob.

## Implements

[protos.google.cloud.vmmigration.v1.IImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iimageimportjob)

## Package

[@google-cloud/vmmigration](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.vmmigration.v1.IImageImportJob);

Constructs a new ImageImportJob.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iimageimportjob)`   
Properties to set  
  
## Properties 

### cloudStorageUri
    
    
    public cloudStorageUri?: (string|null);

ImageImportJob cloudStorageUri.

### createdResources
    
    
    public createdResources: string[];

ImageImportJob createdResources.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

ImageImportJob createTime.

### diskImageTargetDetails
    
    
    public diskImageTargetDetails?: (google.cloud.vmmigration.v1.IDiskImageTargetDetails|null);

ImageImportJob diskImageTargetDetails.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

ImageImportJob endTime.

### errors
    
    
    public errors: google.rpc.IStatus[];

ImageImportJob errors.

### machineImageTargetDetails
    
    
    public machineImageTargetDetails?: (google.cloud.vmmigration.v1.IMachineImageTargetDetails|null);

ImageImportJob machineImageTargetDetails.

### name
    
    
    public name: string;

ImageImportJob name.

### source
    
    
    public source?: "cloudStorageUri";

ImageImportJob source.

### state
    
    
    public state: (google.cloud.vmmigration.v1.ImageImportJob.State|keyof typeof google.cloud.vmmigration.v1.ImageImportJob.State);

ImageImportJob state.

### steps
    
    
    public steps: google.cloud.vmmigration.v1.IImageImportStep[];

ImageImportJob steps.

### targetDetails
    
    
    public targetDetails?: ("diskImageTargetDetails"|"machineImageTargetDetails");

ImageImportJob targetDetails.

### warnings
    
    
    public warnings: google.cloud.vmmigration.v1.IMigrationWarning[];

ImageImportJob warnings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.vmmigration.v1.IImageImportJob): google.cloud.vmmigration.v1.ImageImportJob;

Creates a new ImageImportJob instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iimageimportjob)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imageimportjob-class)` | ImageImportJob instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.vmmigration.v1.ImageImportJob;

Decodes an ImageImportJob message from the specified reader or buffer.

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
`[ImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imageimportjob-class)` | ImageImportJob  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.vmmigration.v1.ImageImportJob;

Decodes an ImageImportJob message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imageimportjob-class)` | ImageImportJob  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.vmmigration.v1.IImageImportJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImageImportJob message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iimageimportjob)`   
ImageImportJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.vmmigration.v1.IImageImportJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImageImportJob message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iimageimportjob)`   
ImageImportJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.vmmigration.v1.ImageImportJob;

Creates an ImageImportJob message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imageimportjob-class)` | ImageImportJob  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ImageImportJob

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

Converts this ImageImportJob to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.vmmigration.v1.ImageImportJob, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ImageImportJob message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ImageImportJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imageimportjob-class)`   
ImageImportJob  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ImageImportJob message.

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
