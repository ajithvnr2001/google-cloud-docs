---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.sourceinstanceproperties-class
title: Class protos.google.cloud.compute.v1.SourceInstanceProperties (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:59.627726+00:00
---

# Class protos.google.cloud.compute.v1.SourceInstanceProperties (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.sourceinstanceproperties-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1.SourceInstanceProperties (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a SourceInstanceProperties.

## Implements

[protos.google.cloud.compute.v1.ISourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isourceinstanceproperties)

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.compute.v1.ISourceInstanceProperties);

Constructs a new SourceInstanceProperties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isourceinstanceproperties)`   
Properties to set  
  
## Properties 

### canIpForward
    
    
    public canIpForward?: (boolean|null);

SourceInstanceProperties canIpForward.

### deletionProtection
    
    
    public deletionProtection?: (boolean|null);

SourceInstanceProperties deletionProtection.

### description
    
    
    public description?: (string|null);

SourceInstanceProperties description.

### disks
    
    
    public disks: google.cloud.compute.v1.ISavedAttachedDisk[];

SourceInstanceProperties disks.

### guestAccelerators
    
    
    public guestAccelerators: google.cloud.compute.v1.IAcceleratorConfig[];

SourceInstanceProperties guestAccelerators.

### keyRevocationActionType
    
    
    public keyRevocationActionType?: (string|null);

SourceInstanceProperties keyRevocationActionType.

### labels
    
    
    public labels: { [k: string]: string };

SourceInstanceProperties labels.

### machineType
    
    
    public machineType?: (string|null);

SourceInstanceProperties machineType.

### metadata
    
    
    public metadata?: (google.cloud.compute.v1.IMetadata|null);

SourceInstanceProperties metadata.

### minCpuPlatform
    
    
    public minCpuPlatform?: (string|null);

SourceInstanceProperties minCpuPlatform.

### networkInterfaces
    
    
    public networkInterfaces: google.cloud.compute.v1.INetworkInterface[];

SourceInstanceProperties networkInterfaces.

### postKeyRevocationActionType
    
    
    public postKeyRevocationActionType?: (string|null);

SourceInstanceProperties postKeyRevocationActionType.

### scheduling
    
    
    public scheduling?: (google.cloud.compute.v1.IScheduling|null);

SourceInstanceProperties scheduling.

### serviceAccounts
    
    
    public serviceAccounts: google.cloud.compute.v1.IServiceAccount[];

SourceInstanceProperties serviceAccounts.

### tags
    
    
    public tags?: (google.cloud.compute.v1.ITags|null);

SourceInstanceProperties tags.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.compute.v1.ISourceInstanceProperties): google.cloud.compute.v1.SourceInstanceProperties;

Creates a new SourceInstanceProperties instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isourceinstanceproperties)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.sourceinstanceproperties-class)` | SourceInstanceProperties instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.compute.v1.SourceInstanceProperties;

Decodes a SourceInstanceProperties message from the specified reader or buffer.

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
`[SourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.sourceinstanceproperties-class)` | SourceInstanceProperties  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.compute.v1.SourceInstanceProperties;

Decodes a SourceInstanceProperties message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.sourceinstanceproperties-class)` | SourceInstanceProperties  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.compute.v1.ISourceInstanceProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SourceInstanceProperties message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isourceinstanceproperties)`   
SourceInstanceProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.compute.v1.ISourceInstanceProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SourceInstanceProperties message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isourceinstanceproperties)`   
SourceInstanceProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.compute.v1.SourceInstanceProperties;

Creates a SourceInstanceProperties message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.sourceinstanceproperties-class)` | SourceInstanceProperties  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SourceInstanceProperties

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

Converts this SourceInstanceProperties to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.compute.v1.SourceInstanceProperties, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SourceInstanceProperties message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SourceInstanceProperties](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.sourceinstanceproperties-class)`   
SourceInstanceProperties  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SourceInstanceProperties message.

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
