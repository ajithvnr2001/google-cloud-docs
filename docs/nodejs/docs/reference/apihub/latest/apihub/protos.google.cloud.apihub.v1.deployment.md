---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment
title: Class protos.google.cloud.apihub.v1.Deployment (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:53.810209+00:00
---

# Class protos.google.cloud.apihub.v1.Deployment (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.Deployment (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Deployment.

## Implements

[protos.google.cloud.apihub.v1.IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideployment)

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apihub.v1.IDeployment);

Constructs a new Deployment.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideployment)`   
Properties to set  
  
## Properties 

### apiVersions
    
    
    public apiVersions: string[];

Deployment apiVersions.

### attributes
    
    
    public attributes: { [k: string]: google.cloud.apihub.v1.IAttributeValues };

Deployment attributes.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Deployment createTime.

### deploymentType
    
    
    public deploymentType?: (google.cloud.apihub.v1.IAttributeValues|null);

Deployment deploymentType.

### description
    
    
    public description: string;

Deployment description.

### displayName
    
    
    public displayName: string;

Deployment displayName.

### documentation
    
    
    public documentation?: (google.cloud.apihub.v1.IDocumentation|null);

Deployment documentation.

### endpoints
    
    
    public endpoints: string[];

Deployment endpoints.

### environment
    
    
    public environment?: (google.cloud.apihub.v1.IAttributeValues|null);

Deployment environment.

### managementUrl
    
    
    public managementUrl?: (google.cloud.apihub.v1.IAttributeValues|null);

Deployment managementUrl.

### name
    
    
    public name: string;

Deployment name.

### resourceUri
    
    
    public resourceUri: string;

Deployment resourceUri.

### slo
    
    
    public slo?: (google.cloud.apihub.v1.IAttributeValues|null);

Deployment slo.

### sourceEnvironment
    
    
    public sourceEnvironment: string;

Deployment sourceEnvironment.

### sourceMetadata
    
    
    public sourceMetadata: google.cloud.apihub.v1.ISourceMetadata[];

Deployment sourceMetadata.

### sourceProject
    
    
    public sourceProject: string;

Deployment sourceProject.

### sourceUri
    
    
    public sourceUri?: (google.cloud.apihub.v1.IAttributeValues|null);

Deployment sourceUri.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Deployment updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apihub.v1.IDeployment): google.cloud.apihub.v1.Deployment;

Creates a new Deployment instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideployment)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment)` | Deployment instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apihub.v1.Deployment;

Decodes a Deployment message from the specified reader or buffer.

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
`[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment)` | Deployment  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apihub.v1.Deployment;

Decodes a Deployment message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment)` | Deployment  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apihub.v1.IDeployment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Deployment message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideployment)`   
Deployment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apihub.v1.IDeployment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Deployment message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ideployment)`   
Deployment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apihub.v1.Deployment;

Creates a Deployment message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment)` | Deployment  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Deployment

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

Converts this Deployment to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apihub.v1.Deployment, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Deployment message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.deployment)`   
Deployment  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Deployment message.

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
