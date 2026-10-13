---
url: https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.resourcestatus
title: Class protos.google.cloud.telcoautomation.v1.ResourceStatus (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:56.273775+00:00
---

# Class protos.google.cloud.telcoautomation.v1.ResourceStatus (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.resourcestatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.telcoautomation.v1.ResourceStatus (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.1.0 

Represents a ResourceStatus.

## Implements

[protos.google.cloud.telcoautomation.v1.IResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.iresourcestatus)

## Package

[@google-cloud/telcoautomation](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.telcoautomation.v1.IResourceStatus);

Constructs a new ResourceStatus.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.iresourcestatus)`   
Properties to set  
  
## Properties 

### group
    
    
    public group: string;

ResourceStatus group.

### kind
    
    
    public kind: string;

ResourceStatus kind.

### name
    
    
    public name: string;

ResourceStatus name.

### nfDeployStatus
    
    
    public nfDeployStatus?: (google.cloud.telcoautomation.v1.INFDeployStatus|null);

ResourceStatus nfDeployStatus.

### resourceNamespace
    
    
    public resourceNamespace: string;

ResourceStatus resourceNamespace.

### resourceType
    
    
    public resourceType: (google.cloud.telcoautomation.v1.ResourceType|keyof typeof google.cloud.telcoautomation.v1.ResourceType);

ResourceStatus resourceType.

### status
    
    
    public status: (google.cloud.telcoautomation.v1.Status|keyof typeof google.cloud.telcoautomation.v1.Status);

ResourceStatus status.

### version
    
    
    public version: string;

ResourceStatus version.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.telcoautomation.v1.IResourceStatus): google.cloud.telcoautomation.v1.ResourceStatus;

Creates a new ResourceStatus instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.iresourcestatus)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.resourcestatus)` | ResourceStatus instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.telcoautomation.v1.ResourceStatus;

Decodes a ResourceStatus message from the specified reader or buffer.

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
`[ResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.resourcestatus)` | ResourceStatus  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.telcoautomation.v1.ResourceStatus;

Decodes a ResourceStatus message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.resourcestatus)` | ResourceStatus  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.telcoautomation.v1.IResourceStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ResourceStatus message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.iresourcestatus)`   
ResourceStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.telcoautomation.v1.IResourceStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ResourceStatus message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.iresourcestatus)`   
ResourceStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.telcoautomation.v1.ResourceStatus;

Creates a ResourceStatus message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.resourcestatus)` | ResourceStatus  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ResourceStatus

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

Converts this ResourceStatus to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.telcoautomation.v1.ResourceStatus, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ResourceStatus message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ResourceStatus](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1.resourcestatus)`   
ResourceStatus  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ResourceStatus message.

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
