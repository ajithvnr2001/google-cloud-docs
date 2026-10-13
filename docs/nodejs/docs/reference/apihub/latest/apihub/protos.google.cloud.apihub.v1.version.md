---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version
title: Class protos.google.cloud.apihub.v1.Version (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:54.018793+00:00
---

# Class protos.google.cloud.apihub.v1.Version (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.Version (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Version.

## Implements

[protos.google.cloud.apihub.v1.IVersion](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iversion)

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apihub.v1.IVersion);

Constructs a new Version.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVersion](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iversion)`   
Properties to set  
  
## Properties 

### accreditation
    
    
    public accreditation?: (google.cloud.apihub.v1.IAttributeValues|null);

Version accreditation.

### apiOperations
    
    
    public apiOperations: string[];

Version apiOperations.

### attributes
    
    
    public attributes: { [k: string]: google.cloud.apihub.v1.IAttributeValues };

Version attributes.

### compliance
    
    
    public compliance?: (google.cloud.apihub.v1.IAttributeValues|null);

Version compliance.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Version createTime.

### definitions
    
    
    public definitions: string[];

Version definitions.

### deployments
    
    
    public deployments: string[];

Version deployments.

### description
    
    
    public description: string;

Version description.

### displayName
    
    
    public displayName: string;

Version displayName.

### documentation
    
    
    public documentation?: (google.cloud.apihub.v1.IDocumentation|null);

Version documentation.

### lifecycle
    
    
    public lifecycle?: (google.cloud.apihub.v1.IAttributeValues|null);

Version lifecycle.

### name
    
    
    public name: string;

Version name.

### selectedDeployment
    
    
    public selectedDeployment: string;

Version selectedDeployment.

### sourceMetadata
    
    
    public sourceMetadata: google.cloud.apihub.v1.ISourceMetadata[];

Version sourceMetadata.

### specs
    
    
    public specs: string[];

Version specs.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Version updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apihub.v1.IVersion): google.cloud.apihub.v1.Version;

Creates a new Version instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVersion](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iversion)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version)` | Version instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apihub.v1.Version;

Decodes a Version message from the specified reader or buffer.

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
`[Version](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version)` | Version  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apihub.v1.Version;

Decodes a Version message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version)` | Version  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apihub.v1.IVersion, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Version message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVersion](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iversion)`   
Version message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apihub.v1.IVersion, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Version message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVersion](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iversion)`   
Version message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apihub.v1.Version;

Creates a Version message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version)` | Version  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Version

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

Converts this Version to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apihub.v1.Version, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Version message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Version](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.version)`   
Version  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Version message.

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
