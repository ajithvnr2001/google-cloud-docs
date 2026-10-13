---
url: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.gitfilesource-class
title: Class protos.google.devtools.cloudbuild.v1.GitFileSource (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:35.137553+00:00
---

# Class protos.google.devtools.cloudbuild.v1.GitFileSource (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.gitfilesource-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devtools.cloudbuild.v1.GitFileSource (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.6.0  5.5.0  5.1.0  4.8.0  4.7.0  4.1.1  4.0.0  3.6.0  3.3.0  3.2.0  3.1.2  2.6.0  2.5.0  2.4.0  2.3.2  2.2.7 

Represents a GitFileSource.

## Implements

[protos.google.devtools.cloudbuild.v1.IGitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.igitfilesource)

## Package

[@google-cloud/cloudbuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devtools.cloudbuild.v1.IGitFileSource);

Constructs a new GitFileSource.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.igitfilesource)`   
Properties to set  
  
## Properties 

### enterpriseConfig
    
    
    public enterpriseConfig?: "githubEnterpriseConfig";

GitFileSource enterpriseConfig.

### githubEnterpriseConfig
    
    
    public githubEnterpriseConfig?: (string|null);

GitFileSource githubEnterpriseConfig.

### path
    
    
    public path: string;

GitFileSource path.

### repository
    
    
    public repository?: (string|null);

GitFileSource repository.

### repoType
    
    
    public repoType: (google.devtools.cloudbuild.v1.GitFileSource.RepoType|keyof typeof google.devtools.cloudbuild.v1.GitFileSource.RepoType);

GitFileSource repoType.

### revision
    
    
    public revision: string;

GitFileSource revision.

### source
    
    
    public source?: "repository";

GitFileSource source.

### uri
    
    
    public uri: string;

GitFileSource uri.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devtools.cloudbuild.v1.IGitFileSource): google.devtools.cloudbuild.v1.GitFileSource;

Creates a new GitFileSource instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.igitfilesource)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.gitfilesource-class)` | GitFileSource instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devtools.cloudbuild.v1.GitFileSource;

Decodes a GitFileSource message from the specified reader or buffer.

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
`[GitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.gitfilesource-class)` | GitFileSource  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devtools.cloudbuild.v1.GitFileSource;

Decodes a GitFileSource message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.gitfilesource-class)` | GitFileSource  
  
### encode(message, writer)
    
    
    public static encode(message: google.devtools.cloudbuild.v1.IGitFileSource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GitFileSource message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.igitfilesource)`   
GitFileSource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devtools.cloudbuild.v1.IGitFileSource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GitFileSource message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.igitfilesource)`   
GitFileSource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devtools.cloudbuild.v1.GitFileSource;

Creates a GitFileSource message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.gitfilesource-class)` | GitFileSource  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GitFileSource

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

Converts this GitFileSource to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devtools.cloudbuild.v1.GitFileSource, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GitFileSource message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GitFileSource](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.gitfilesource-class)`   
GitFileSource  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GitFileSource message.

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
