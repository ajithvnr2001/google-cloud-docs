---
url: https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.apideployment
title: Class protos.google.cloud.apigeeregistry.v1.ApiDeployment (3.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:13.277795+00:00
---

# Class protos.google.cloud.apigeeregistry.v1.ApiDeployment (3.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.apideployment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apigeeregistry.v1.ApiDeployment (3.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.0.1 (latest)  1.0.1  0.2.1  0.1.0 

Represents an ApiDeployment.

## Implements

[protos.google.cloud.apigeeregistry.v1.IApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.iapideployment)

## Package

[@google-cloud/apigee-registry](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apigeeregistry.v1.IApiDeployment);

Constructs a new ApiDeployment.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.iapideployment)`   
Properties to set  
  
## Properties 

### accessGuidance
    
    
    public accessGuidance: string;

ApiDeployment accessGuidance.

### annotations
    
    
    public annotations: { [k: string]: string };

ApiDeployment annotations.

### apiSpecRevision
    
    
    public apiSpecRevision: string;

ApiDeployment apiSpecRevision.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

ApiDeployment createTime.

### description
    
    
    public description: string;

ApiDeployment description.

### displayName
    
    
    public displayName: string;

ApiDeployment displayName.

### endpointUri
    
    
    public endpointUri: string;

ApiDeployment endpointUri.

### externalChannelUri
    
    
    public externalChannelUri: string;

ApiDeployment externalChannelUri.

### intendedAudience
    
    
    public intendedAudience: string;

ApiDeployment intendedAudience.

### labels
    
    
    public labels: { [k: string]: string };

ApiDeployment labels.

### name
    
    
    public name: string;

ApiDeployment name.

### revisionCreateTime
    
    
    public revisionCreateTime?: (google.protobuf.ITimestamp|null);

ApiDeployment revisionCreateTime.

### revisionId
    
    
    public revisionId: string;

ApiDeployment revisionId.

### revisionUpdateTime
    
    
    public revisionUpdateTime?: (google.protobuf.ITimestamp|null);

ApiDeployment revisionUpdateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apigeeregistry.v1.IApiDeployment): google.cloud.apigeeregistry.v1.ApiDeployment;

Creates a new ApiDeployment instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.iapideployment)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.apideployment)` | ApiDeployment instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apigeeregistry.v1.ApiDeployment;

Decodes an ApiDeployment message from the specified reader or buffer.

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
`[ApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.apideployment)` | ApiDeployment  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apigeeregistry.v1.ApiDeployment;

Decodes an ApiDeployment message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.apideployment)` | ApiDeployment  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apigeeregistry.v1.IApiDeployment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ApiDeployment message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.iapideployment)`   
ApiDeployment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apigeeregistry.v1.IApiDeployment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ApiDeployment message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.iapideployment)`   
ApiDeployment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apigeeregistry.v1.ApiDeployment;

Creates an ApiDeployment message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.apideployment)` | ApiDeployment  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ApiDeployment

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

Converts this ApiDeployment to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apigeeregistry.v1.ApiDeployment, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ApiDeployment message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ApiDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.apideployment)`   
ApiDeployment  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ApiDeployment message.

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
