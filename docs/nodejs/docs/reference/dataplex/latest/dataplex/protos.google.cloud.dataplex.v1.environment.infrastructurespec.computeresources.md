---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.computeresources
title: Class protos.google.cloud.dataplex.v1.Environment.InfrastructureSpec.ComputeResources (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:26.518157+00:00
---

# Class protos.google.cloud.dataplex.v1.Environment.InfrastructureSpec.ComputeResources (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.computeresources

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.Environment.InfrastructureSpec.ComputeResources (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a ComputeResources.

## Implements

[protos.google.cloud.dataplex.v1.Environment.InfrastructureSpec.IComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.icomputeresources)

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataplex.v1.Environment.InfrastructureSpec.IComputeResources);

Constructs a new ComputeResources.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.icomputeresources)`   
Properties to set  
  
## Properties 

### diskSizeGb
    
    
    public diskSizeGb: number;

ComputeResources diskSizeGb.

### maxNodeCount
    
    
    public maxNodeCount: number;

ComputeResources maxNodeCount.

### nodeCount
    
    
    public nodeCount: number;

ComputeResources nodeCount.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataplex.v1.Environment.InfrastructureSpec.IComputeResources): google.cloud.dataplex.v1.Environment.InfrastructureSpec.ComputeResources;

Creates a new ComputeResources instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.icomputeresources)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.computeresources)` | ComputeResources instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataplex.v1.Environment.InfrastructureSpec.ComputeResources;

Decodes a ComputeResources message from the specified reader or buffer.

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
`[ComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.computeresources)` | ComputeResources  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataplex.v1.Environment.InfrastructureSpec.ComputeResources;

Decodes a ComputeResources message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.computeresources)` | ComputeResources  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataplex.v1.Environment.InfrastructureSpec.IComputeResources, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ComputeResources message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.icomputeresources)`   
ComputeResources message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataplex.v1.Environment.InfrastructureSpec.IComputeResources, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ComputeResources message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.icomputeresources)`   
ComputeResources message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataplex.v1.Environment.InfrastructureSpec.ComputeResources;

Creates a ComputeResources message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.computeresources)` | ComputeResources  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ComputeResources

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

Converts this ComputeResources to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataplex.v1.Environment.InfrastructureSpec.ComputeResources, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ComputeResources message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ComputeResources](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.environment.infrastructurespec.computeresources)`   
ComputeResources  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ComputeResources message.

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
