---
url: https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.accesssummary
title: Class protos.google.cloud.agentidentity.v1.AccessSummary (0.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:11.153748+00:00
---

# Class protos.google.cloud.agentidentity.v1.AccessSummary (0.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.accesssummary

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.agentidentity.v1.AccessSummary (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an AccessSummary.

## Implements

[protos.google.cloud.agentidentity.v1.IAccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iaccesssummary)

## Package

[@google-cloud/agentidentity](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.agentidentity.v1.IAccessSummary);

Constructs a new AccessSummary.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iaccesssummary)`   
Properties to set  
  
## Properties 

### authProvider
    
    
    public authProvider: string;

AccessSummary authProvider.

### authProviderType
    
    
    public authProviderType: (google.cloud.agentidentity.v1.AuthProviderType|keyof typeof google.cloud.agentidentity.v1.AuthProviderType);

AccessSummary authProviderType.

### firstAccessTime
    
    
    public firstAccessTime?: (google.protobuf.ITimestamp|null);

AccessSummary firstAccessTime.

### labels
    
    
    public labels: { [k: string]: string };

AccessSummary labels.

### lastAccessTime
    
    
    public lastAccessTime?: (google.protobuf.ITimestamp|null);

AccessSummary lastAccessTime.

### name
    
    
    public name: string;

AccessSummary name.

### purgeTime
    
    
    public purgeTime?: (google.protobuf.ITimestamp|null);

AccessSummary purgeTime.

### scopes
    
    
    public scopes: string[];

AccessSummary scopes.

### tokenUrl
    
    
    public tokenUrl: string;

AccessSummary tokenUrl.

### userId
    
    
    public userId: string;

AccessSummary userId.

### workloadId
    
    
    public workloadId: string;

AccessSummary workloadId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.agentidentity.v1.IAccessSummary): google.cloud.agentidentity.v1.AccessSummary;

Creates a new AccessSummary instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iaccesssummary)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.accesssummary)` | AccessSummary instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.agentidentity.v1.AccessSummary;

Decodes an AccessSummary message from the specified reader or buffer.

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
`[AccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.accesssummary)` | AccessSummary  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.agentidentity.v1.AccessSummary;

Decodes an AccessSummary message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.accesssummary)` | AccessSummary  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.agentidentity.v1.IAccessSummary, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AccessSummary message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iaccesssummary)`   
AccessSummary message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.agentidentity.v1.IAccessSummary, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AccessSummary message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.iaccesssummary)`   
AccessSummary message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.agentidentity.v1.AccessSummary;

Creates an AccessSummary message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.accesssummary)` | AccessSummary  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AccessSummary

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

Converts this AccessSummary to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.agentidentity.v1.AccessSummary, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AccessSummary message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AccessSummary](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1.accesssummary)`   
AccessSummary  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AccessSummary message.

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

Last updated 2026-08-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-12 UTC."],[],[]] 
