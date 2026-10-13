---
url: https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.resource
title: Class protos.google.cloud.securitycenter.v1.Resource (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:53.982138+00:00
---

# Class protos.google.cloud.securitycenter.v1.Resource (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.resource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.securitycenter.v1.Resource (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.0.1  9.5.0  9.4.0  9.3.0  8.12.0  8.11.0  8.10.0  8.9.0  8.7.0  8.5.0  8.4.0  8.3.0  8.1.0  8.0.0  7.4.0  7.2.1  7.0.0  6.3.1  6.2.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.1  5.4.1  5.3.5 

Represents a Resource.

## Implements

[protos.google.cloud.securitycenter.v1.IResource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.iresource)

## Package

[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.securitycenter.v1.IResource);

Constructs a new Resource.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IResource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.iresource)`   
Properties to set  
  
## Properties 

### awsMetadata
    
    
    public awsMetadata?: (google.cloud.securitycenter.v1.IAwsMetadata|null);

Resource awsMetadata.

### azureMetadata
    
    
    public azureMetadata?: (google.cloud.securitycenter.v1.IAzureMetadata|null);

Resource azureMetadata.

### cloudProvider
    
    
    public cloudProvider: (google.cloud.securitycenter.v1.CloudProvider|keyof typeof google.cloud.securitycenter.v1.CloudProvider);

Resource cloudProvider.

### cloudProviderMetadata
    
    
    public cloudProviderMetadata?: ("awsMetadata"|"azureMetadata");

Resource cloudProviderMetadata.

### displayName
    
    
    public displayName: string;

Resource displayName.

### folders
    
    
    public folders: google.cloud.securitycenter.v1.IFolder[];

Resource folders.

### location
    
    
    public location: string;

Resource location.

### name
    
    
    public name: string;

Resource name.

### organization
    
    
    public organization: string;

Resource organization.

### parent
    
    
    public parent: string;

Resource parent.

### parentDisplayName
    
    
    public parentDisplayName: string;

Resource parentDisplayName.

### project
    
    
    public project: string;

Resource project.

### projectDisplayName
    
    
    public projectDisplayName: string;

Resource projectDisplayName.

### resourcePath
    
    
    public resourcePath?: (google.cloud.securitycenter.v1.IResourcePath|null);

Resource resourcePath.

### resourcePathString
    
    
    public resourcePathString: string;

Resource resourcePathString.

### service
    
    
    public service: string;

Resource service.

### type
    
    
    public type: string;

Resource type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.securitycenter.v1.IResource): google.cloud.securitycenter.v1.Resource;

Creates a new Resource instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IResource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.iresource)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Resource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.resource)` | Resource instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.securitycenter.v1.Resource;

Decodes a Resource message from the specified reader or buffer.

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
`[Resource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.resource)` | Resource  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.securitycenter.v1.Resource;

Decodes a Resource message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Resource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.resource)` | Resource  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.securitycenter.v1.IResource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Resource message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IResource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.iresource)`   
Resource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.securitycenter.v1.IResource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Resource message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IResource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.iresource)`   
Resource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.securitycenter.v1.Resource;

Creates a Resource message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Resource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.resource)` | Resource  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Resource

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

Converts this Resource to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.securitycenter.v1.Resource, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Resource message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Resource](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v1.resource)`   
Resource  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Resource message.

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
