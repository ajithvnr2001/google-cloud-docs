---
url: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.createinstructionmetadata
title: Class protos.google.cloud.datalabeling.v1beta1.CreateInstructionMetadata (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:50.514450+00:00
---

# Class protos.google.cloud.datalabeling.v1beta1.CreateInstructionMetadata (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.createinstructionmetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datalabeling.v1beta1.CreateInstructionMetadata (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.2.2  3.1.1  2.3.0  2.2.7 

Represents a CreateInstructionMetadata.

## Implements

[protos.google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionmetadata)

## Package

[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata);

Constructs a new CreateInstructionMetadata.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionmetadata)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

CreateInstructionMetadata createTime.

### instruction
    
    
    public instruction: string;

CreateInstructionMetadata instruction.

### partialFailures
    
    
    public partialFailures: google.rpc.IStatus[];

CreateInstructionMetadata partialFailures.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata): google.cloud.datalabeling.v1beta1.CreateInstructionMetadata;

Creates a new CreateInstructionMetadata instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionmetadata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.createinstructionmetadata)` | CreateInstructionMetadata instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datalabeling.v1beta1.CreateInstructionMetadata;

Decodes a CreateInstructionMetadata message from the specified reader or buffer.

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
`[CreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.createinstructionmetadata)` | CreateInstructionMetadata  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datalabeling.v1beta1.CreateInstructionMetadata;

Decodes a CreateInstructionMetadata message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.createinstructionmetadata)` | CreateInstructionMetadata  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateInstructionMetadata message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionmetadata)`   
CreateInstructionMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateInstructionMetadata message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionmetadata)`   
CreateInstructionMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datalabeling.v1beta1.CreateInstructionMetadata;

Creates a CreateInstructionMetadata message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.createinstructionmetadata)` | CreateInstructionMetadata  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateInstructionMetadata

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

Converts this CreateInstructionMetadata to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datalabeling.v1beta1.CreateInstructionMetadata, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateInstructionMetadata message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.createinstructionmetadata)`   
CreateInstructionMetadata  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateInstructionMetadata message.

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
