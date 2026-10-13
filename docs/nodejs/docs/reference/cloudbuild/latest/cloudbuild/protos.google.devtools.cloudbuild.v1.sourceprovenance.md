---
url: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.sourceprovenance
title: Class protos.google.devtools.cloudbuild.v1.SourceProvenance (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:41.162119+00:00
---

# Class protos.google.devtools.cloudbuild.v1.SourceProvenance (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.sourceprovenance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devtools.cloudbuild.v1.SourceProvenance (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.6.0  5.5.0  5.1.0  4.8.0  4.7.0  4.1.1  4.0.0  3.6.0  3.3.0  3.2.0  3.1.2  2.6.0  2.5.0  2.4.0  2.3.2  2.2.7 

Represents a SourceProvenance.

## Implements

[protos.google.devtools.cloudbuild.v1.ISourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.isourceprovenance)

## Package

[@google-cloud/cloudbuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devtools.cloudbuild.v1.ISourceProvenance);

Constructs a new SourceProvenance.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.isourceprovenance)`   
Properties to set  
  
## Properties 

### fileHashes
    
    
    public fileHashes: { [k: string]: google.devtools.cloudbuild.v1.IFileHashes };

SourceProvenance fileHashes.

### resolvedConnectedRepository
    
    
    public resolvedConnectedRepository?: (google.devtools.cloudbuild.v1.IConnectedRepository|null);

SourceProvenance resolvedConnectedRepository.

### resolvedGitSource
    
    
    public resolvedGitSource?: (google.devtools.cloudbuild.v1.IGitSource|null);

SourceProvenance resolvedGitSource.

### resolvedRepoSource
    
    
    public resolvedRepoSource?: (google.devtools.cloudbuild.v1.IRepoSource|null);

SourceProvenance resolvedRepoSource.

### resolvedStorageSource
    
    
    public resolvedStorageSource?: (google.devtools.cloudbuild.v1.IStorageSource|null);

SourceProvenance resolvedStorageSource.

### resolvedStorageSourceManifest
    
    
    public resolvedStorageSourceManifest?: (google.devtools.cloudbuild.v1.IStorageSourceManifest|null);

SourceProvenance resolvedStorageSourceManifest.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devtools.cloudbuild.v1.ISourceProvenance): google.devtools.cloudbuild.v1.SourceProvenance;

Creates a new SourceProvenance instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.isourceprovenance)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.sourceprovenance)` | SourceProvenance instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devtools.cloudbuild.v1.SourceProvenance;

Decodes a SourceProvenance message from the specified reader or buffer.

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
`[SourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.sourceprovenance)` | SourceProvenance  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devtools.cloudbuild.v1.SourceProvenance;

Decodes a SourceProvenance message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.sourceprovenance)` | SourceProvenance  
  
### encode(message, writer)
    
    
    public static encode(message: google.devtools.cloudbuild.v1.ISourceProvenance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SourceProvenance message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.isourceprovenance)`   
SourceProvenance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devtools.cloudbuild.v1.ISourceProvenance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SourceProvenance message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.isourceprovenance)`   
SourceProvenance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devtools.cloudbuild.v1.SourceProvenance;

Creates a SourceProvenance message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.sourceprovenance)` | SourceProvenance  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SourceProvenance

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

Converts this SourceProvenance to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devtools.cloudbuild.v1.SourceProvenance, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SourceProvenance message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SourceProvenance](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.sourceprovenance)`   
SourceProvenance  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SourceProvenance message.

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
