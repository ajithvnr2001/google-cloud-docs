---
url: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset
title: Class protos.google.cloud.datalabeling.v1beta1.AnnotatedDataset (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:51.133527+00:00
---

# Class protos.google.cloud.datalabeling.v1beta1.AnnotatedDataset (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datalabeling.v1beta1.AnnotatedDataset (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.2.2  3.1.1  2.3.0  2.2.7 

Represents an AnnotatedDataset.

## Implements

[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset)

## Package

[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datalabeling.v1beta1.IAnnotatedDataset);

Constructs a new AnnotatedDataset.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset)`   
Properties to set  
  
## Properties 

### annotationSource
    
    
    public annotationSource: (google.cloud.datalabeling.v1beta1.AnnotationSource|keyof typeof google.cloud.datalabeling.v1beta1.AnnotationSource);

AnnotatedDataset annotationSource.

### annotationType
    
    
    public annotationType: (google.cloud.datalabeling.v1beta1.AnnotationType|keyof typeof google.cloud.datalabeling.v1beta1.AnnotationType);

AnnotatedDataset annotationType.

### blockingResources
    
    
    public blockingResources: string[];

AnnotatedDataset blockingResources.

### completedExampleCount
    
    
    public completedExampleCount: (number|Long|string);

AnnotatedDataset completedExampleCount.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AnnotatedDataset createTime.

### description
    
    
    public description: string;

AnnotatedDataset description.

### displayName
    
    
    public displayName: string;

AnnotatedDataset displayName.

### exampleCount
    
    
    public exampleCount: (number|Long|string);

AnnotatedDataset exampleCount.

### labelStats
    
    
    public labelStats?: (google.cloud.datalabeling.v1beta1.ILabelStats|null);

AnnotatedDataset labelStats.

### metadata
    
    
    public metadata?: (google.cloud.datalabeling.v1beta1.IAnnotatedDatasetMetadata|null);

AnnotatedDataset metadata.

### name
    
    
    public name: string;

AnnotatedDataset name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datalabeling.v1beta1.IAnnotatedDataset): google.cloud.datalabeling.v1beta1.AnnotatedDataset;

Creates a new AnnotatedDataset instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset)` | AnnotatedDataset instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datalabeling.v1beta1.AnnotatedDataset;

Decodes an AnnotatedDataset message from the specified reader or buffer.

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
`[AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset)` | AnnotatedDataset  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datalabeling.v1beta1.AnnotatedDataset;

Decodes an AnnotatedDataset message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset)` | AnnotatedDataset  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datalabeling.v1beta1.IAnnotatedDataset, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnnotatedDataset message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset)`   
AnnotatedDataset message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datalabeling.v1beta1.IAnnotatedDataset, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnnotatedDataset message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset)`   
AnnotatedDataset message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datalabeling.v1beta1.AnnotatedDataset;

Creates an AnnotatedDataset message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset)` | AnnotatedDataset  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AnnotatedDataset

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

Converts this AnnotatedDataset to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datalabeling.v1beta1.AnnotatedDataset, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AnnotatedDataset message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset)`   
AnnotatedDataset  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AnnotatedDataset message.

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
