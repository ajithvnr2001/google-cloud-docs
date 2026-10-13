---
url: https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.publishing
title: Class protos.google.api.Publishing (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:35.332503+00:00
---

# Class protos.google.api.Publishing (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.publishing

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.Publishing (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.1 (latest)  0.1.0 

Represents a Publishing.

## Implements

[protos.google.api.IPublishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.ipublishing)

## Package

[@google-cloud/configmanagement](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IPublishing);

Constructs a new Publishing.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPublishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.ipublishing)`   
Properties to set  
  
## Properties 

### apiShortName
    
    
    public apiShortName: string;

Publishing apiShortName.

### codeownerGithubTeams
    
    
    public codeownerGithubTeams: string[];

Publishing codeownerGithubTeams.

### docTagPrefix
    
    
    public docTagPrefix: string;

Publishing docTagPrefix.

### documentationUri
    
    
    public documentationUri: string;

Publishing documentationUri.

### githubLabel
    
    
    public githubLabel: string;

Publishing githubLabel.

### librarySettings
    
    
    public librarySettings: google.api.IClientLibrarySettings[];

Publishing librarySettings.

### methodSettings
    
    
    public methodSettings: google.api.IMethodSettings[];

Publishing methodSettings.

### newIssueUri
    
    
    public newIssueUri: string;

Publishing newIssueUri.

### organization
    
    
    public organization: (google.api.ClientLibraryOrganization|keyof typeof google.api.ClientLibraryOrganization);

Publishing organization.

### protoReferenceDocumentationUri
    
    
    public protoReferenceDocumentationUri: string;

Publishing protoReferenceDocumentationUri.

### restReferenceDocumentationUri
    
    
    public restReferenceDocumentationUri: string;

Publishing restReferenceDocumentationUri.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IPublishing): google.api.Publishing;

Creates a new Publishing instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPublishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.ipublishing)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Publishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.publishing)` | Publishing instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.Publishing;

Decodes a Publishing message from the specified reader or buffer.

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
`[Publishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.publishing)` | Publishing  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.Publishing;

Decodes a Publishing message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Publishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.publishing)` | Publishing  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IPublishing, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Publishing message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPublishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.ipublishing)`   
Publishing message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IPublishing, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Publishing message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPublishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.ipublishing)`   
Publishing message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.Publishing;

Creates a Publishing message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Publishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.publishing)` | Publishing  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Publishing

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

Converts this Publishing to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.Publishing, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Publishing message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Publishing](https://docs.cloud.google.com/nodejs/docs/reference/configmanagement/latest/configmanagement/protos.google.api.publishing)`   
Publishing  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Publishing message.

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
