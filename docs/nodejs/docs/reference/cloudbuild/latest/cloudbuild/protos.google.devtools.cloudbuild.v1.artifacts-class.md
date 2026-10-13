---
url: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.artifacts-class
title: Class protos.google.devtools.cloudbuild.v1.Artifacts (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:19.339506+00:00
---

# Class protos.google.devtools.cloudbuild.v1.Artifacts (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.artifacts-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devtools.cloudbuild.v1.Artifacts (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.6.0  5.5.0  5.1.0  4.8.0  4.7.0  4.1.1  4.0.0  3.6.0  3.3.0  3.2.0  3.1.2  2.6.0  2.5.0  2.4.0  2.3.2  2.2.7 

Represents an Artifacts.

## Implements

[protos.google.devtools.cloudbuild.v1.IArtifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.iartifacts)

## Package

[@google-cloud/cloudbuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devtools.cloudbuild.v1.IArtifacts);

Constructs a new Artifacts.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IArtifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.iartifacts)`   
Properties to set  
  
## Properties 

### goModules
    
    
    public goModules: google.devtools.cloudbuild.v1.Artifacts.IGoModule[];

Artifacts goModules.

### images
    
    
    public images: string[];

Artifacts images.

### mavenArtifacts
    
    
    public mavenArtifacts: google.devtools.cloudbuild.v1.Artifacts.IMavenArtifact[];

Artifacts mavenArtifacts.

### npmPackages
    
    
    public npmPackages: google.devtools.cloudbuild.v1.Artifacts.INpmPackage[];

Artifacts npmPackages.

### objects
    
    
    public objects?: (google.devtools.cloudbuild.v1.Artifacts.IArtifactObjects|null);

Artifacts objects.

### pythonPackages
    
    
    public pythonPackages: google.devtools.cloudbuild.v1.Artifacts.IPythonPackage[];

Artifacts pythonPackages.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devtools.cloudbuild.v1.IArtifacts): google.devtools.cloudbuild.v1.Artifacts;

Creates a new Artifacts instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IArtifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.iartifacts)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.artifacts-class)` | Artifacts instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devtools.cloudbuild.v1.Artifacts;

Decodes an Artifacts message from the specified reader or buffer.

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
`[Artifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.artifacts-class)` | Artifacts  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devtools.cloudbuild.v1.Artifacts;

Decodes an Artifacts message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.artifacts-class)` | Artifacts  
  
### encode(message, writer)
    
    
    public static encode(message: google.devtools.cloudbuild.v1.IArtifacts, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Artifacts message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IArtifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.iartifacts)`   
Artifacts message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devtools.cloudbuild.v1.IArtifacts, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Artifacts message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IArtifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.iartifacts)`   
Artifacts message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devtools.cloudbuild.v1.Artifacts;

Creates an Artifacts message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.artifacts-class)` | Artifacts  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Artifacts

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

Converts this Artifacts to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devtools.cloudbuild.v1.Artifacts, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Artifacts message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Artifacts](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.artifacts-class)`   
Artifacts  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Artifacts message.

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
