---
url: https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.buildmetadata
title: Class protos.grafeas.v1.InTotoSlsaProvenanceV1.BuildMetadata (7.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:25.608962+00:00
---

# Class protos.grafeas.v1.InTotoSlsaProvenanceV1.BuildMetadata (7.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.buildmetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.grafeas.v1.InTotoSlsaProvenanceV1.BuildMetadata (7.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.0.1 (latest)  6.0.1  5.5.0  4.5.0  4.2.2  4.1.2  3.6.1  3.5.0  3.4.6 

Represents a BuildMetadata.

## Implements

[protos.grafeas.v1.InTotoSlsaProvenanceV1.IBuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.ibuildmetadata)

## Package

[@google-cloud/grafeas](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: grafeas.v1.InTotoSlsaProvenanceV1.IBuildMetadata);

Constructs a new BuildMetadata.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.ibuildmetadata)`   
Properties to set  
  
## Properties 

### finishedOn
    
    
    public finishedOn?: (google.protobuf.ITimestamp|null);

BuildMetadata finishedOn.

### invocationId
    
    
    public invocationId: string;

BuildMetadata invocationId.

### startedOn
    
    
    public startedOn?: (google.protobuf.ITimestamp|null);

BuildMetadata startedOn.

## Methods 

### create(properties)
    
    
    public static create(properties?: grafeas.v1.InTotoSlsaProvenanceV1.IBuildMetadata): grafeas.v1.InTotoSlsaProvenanceV1.BuildMetadata;

Creates a new BuildMetadata instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.ibuildmetadata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.buildmetadata)` | BuildMetadata instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): grafeas.v1.InTotoSlsaProvenanceV1.BuildMetadata;

Decodes a BuildMetadata message from the specified reader or buffer.

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
`[BuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.buildmetadata)` | BuildMetadata  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): grafeas.v1.InTotoSlsaProvenanceV1.BuildMetadata;

Decodes a BuildMetadata message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.buildmetadata)` | BuildMetadata  
  
### encode(message, writer)
    
    
    public static encode(message: grafeas.v1.InTotoSlsaProvenanceV1.IBuildMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BuildMetadata message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.ibuildmetadata)`   
BuildMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: grafeas.v1.InTotoSlsaProvenanceV1.IBuildMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BuildMetadata message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.ibuildmetadata)`   
BuildMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): grafeas.v1.InTotoSlsaProvenanceV1.BuildMetadata;

Creates a BuildMetadata message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.buildmetadata)` | BuildMetadata  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BuildMetadata

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

Converts this BuildMetadata to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: grafeas.v1.InTotoSlsaProvenanceV1.BuildMetadata, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BuildMetadata message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BuildMetadata](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.intotoslsaprovenancev1.buildmetadata)`   
BuildMetadata  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BuildMetadata message.

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
