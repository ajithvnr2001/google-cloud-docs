---
url: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.yumrepository
title: Class protos.google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepository (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:16.173819+00:00
---

# Class protos.google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepository (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.yumrepository

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepository (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.2.2  2.1.2  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.6 

Represents a YumRepository.

## Implements

[protos.google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.IYumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.iyumrepository)

## Package

[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.IYumRepository);

Constructs a new YumRepository.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IYumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.iyumrepository)`   
Properties to set  
  
## Properties 

### baseUrl
    
    
    public baseUrl: string;

YumRepository baseUrl.

### displayName
    
    
    public displayName: string;

YumRepository displayName.

### gpgKeys
    
    
    public gpgKeys: string[];

YumRepository gpgKeys.

### id
    
    
    public id: string;

YumRepository id.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.IYumRepository): google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepository;

Creates a new YumRepository instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IYumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.iyumrepository)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[YumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.yumrepository)` | YumRepository instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepository;

Decodes a YumRepository message from the specified reader or buffer.

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
`[YumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.yumrepository)` | YumRepository  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepository;

Decodes a YumRepository message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[YumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.yumrepository)` | YumRepository  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.IYumRepository, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified YumRepository message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IYumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.iyumrepository)`   
YumRepository message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.IYumRepository, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified YumRepository message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IYumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.iyumrepository)`   
YumRepository message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepository;

Creates a YumRepository message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[YumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.yumrepository)` | YumRepository  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for YumRepository

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

Converts this YumRepository to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.osconfig.v1alpha.OSPolicy.Resource.RepositoryResource.YumRepository, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a YumRepository message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[YumRepository](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicy.resource.repositoryresource.yumrepository)`   
YumRepository  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a YumRepository message.

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
