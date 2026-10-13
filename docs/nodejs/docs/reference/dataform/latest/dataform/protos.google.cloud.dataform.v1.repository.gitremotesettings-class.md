---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.gitremotesettings-class
title: Class protos.google.cloud.dataform.v1.Repository.GitRemoteSettings (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:26.341240+00:00
---

# Class protos.google.cloud.dataform.v1.Repository.GitRemoteSettings (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.gitremotesettings-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataform.v1.Repository.GitRemoteSettings (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Represents a GitRemoteSettings.

## Implements

[protos.google.cloud.dataform.v1.Repository.IGitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.igitremotesettings)

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataform.v1.Repository.IGitRemoteSettings);

Constructs a new GitRemoteSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.igitremotesettings)`   
Properties to set  
  
## Properties 

### authenticationTokenSecretVersion
    
    
    public authenticationTokenSecretVersion: string;

GitRemoteSettings authenticationTokenSecretVersion.

### defaultBranch
    
    
    public defaultBranch: string;

GitRemoteSettings defaultBranch.

### effectiveDefaultBranch
    
    
    public effectiveDefaultBranch: string;

GitRemoteSettings effectiveDefaultBranch.

### gitRepositoryLink
    
    
    public gitRepositoryLink?: (string|null);

GitRemoteSettings gitRepositoryLink.

### sshAuthenticationConfig
    
    
    public sshAuthenticationConfig?: (google.cloud.dataform.v1.Repository.GitRemoteSettings.ISshAuthenticationConfig|null);

GitRemoteSettings sshAuthenticationConfig.

### tokenStatus
    
    
    public tokenStatus: (google.cloud.dataform.v1.Repository.GitRemoteSettings.TokenStatus|keyof typeof google.cloud.dataform.v1.Repository.GitRemoteSettings.TokenStatus);

GitRemoteSettings tokenStatus.

### url
    
    
    public url: string;

GitRemoteSettings url.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataform.v1.Repository.IGitRemoteSettings): google.cloud.dataform.v1.Repository.GitRemoteSettings;

Creates a new GitRemoteSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.igitremotesettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.gitremotesettings-class)` | GitRemoteSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataform.v1.Repository.GitRemoteSettings;

Decodes a GitRemoteSettings message from the specified reader or buffer.

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
`[GitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.gitremotesettings-class)` | GitRemoteSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataform.v1.Repository.GitRemoteSettings;

Decodes a GitRemoteSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.gitremotesettings-class)` | GitRemoteSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataform.v1.Repository.IGitRemoteSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GitRemoteSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.igitremotesettings)`   
GitRemoteSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataform.v1.Repository.IGitRemoteSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GitRemoteSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.igitremotesettings)`   
GitRemoteSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataform.v1.Repository.GitRemoteSettings;

Creates a GitRemoteSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.gitremotesettings-class)` | GitRemoteSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GitRemoteSettings

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

Converts this GitRemoteSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataform.v1.Repository.GitRemoteSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GitRemoteSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GitRemoteSettings](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.repository.gitremotesettings-class)`   
GitRemoteSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GitRemoteSettings message.

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
