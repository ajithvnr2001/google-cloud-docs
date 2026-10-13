---
url: https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.listmavenartifactsrequest
title: Class protos.google.devtools.artifactregistry.v1.ListMavenArtifactsRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:25.394228+00:00
---

# Class protos.google.devtools.artifactregistry.v1.ListMavenArtifactsRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.listmavenartifactsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devtools.artifactregistry.v1.ListMavenArtifactsRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.7.0  4.6.0  4.4.0  4.2.0  3.1.1  2.2.2  2.1.0  2.0.2  1.3.0  1.2.3  1.1.0  1.0.7 

Represents a ListMavenArtifactsRequest.

## Implements

[protos.google.devtools.artifactregistry.v1.IListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.ilistmavenartifactsrequest)

## Package

[@google-cloud/artifact-registry](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devtools.artifactregistry.v1.IListMavenArtifactsRequest);

Constructs a new ListMavenArtifactsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.ilistmavenartifactsrequest)`   
Properties to set  
  
## Properties 

### pageSize
    
    
    public pageSize: number;

ListMavenArtifactsRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListMavenArtifactsRequest pageToken.

### parent
    
    
    public parent: string;

ListMavenArtifactsRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devtools.artifactregistry.v1.IListMavenArtifactsRequest): google.devtools.artifactregistry.v1.ListMavenArtifactsRequest;

Creates a new ListMavenArtifactsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.ilistmavenartifactsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.listmavenartifactsrequest)` | ListMavenArtifactsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devtools.artifactregistry.v1.ListMavenArtifactsRequest;

Decodes a ListMavenArtifactsRequest message from the specified reader or buffer.

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
`[ListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.listmavenartifactsrequest)` | ListMavenArtifactsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devtools.artifactregistry.v1.ListMavenArtifactsRequest;

Decodes a ListMavenArtifactsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.listmavenartifactsrequest)` | ListMavenArtifactsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.devtools.artifactregistry.v1.IListMavenArtifactsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListMavenArtifactsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.ilistmavenartifactsrequest)`   
ListMavenArtifactsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devtools.artifactregistry.v1.IListMavenArtifactsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListMavenArtifactsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.ilistmavenartifactsrequest)`   
ListMavenArtifactsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devtools.artifactregistry.v1.ListMavenArtifactsRequest;

Creates a ListMavenArtifactsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.listmavenartifactsrequest)` | ListMavenArtifactsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListMavenArtifactsRequest

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

Converts this ListMavenArtifactsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devtools.artifactregistry.v1.ListMavenArtifactsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListMavenArtifactsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListMavenArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/artifact-registry/latest/artifact-registry/protos.google.devtools.artifactregistry.v1.listmavenartifactsrequest)`   
ListMavenArtifactsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListMavenArtifactsRequest message.

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
