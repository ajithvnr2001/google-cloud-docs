---
url: https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.listapideploymentrevisionsrequest
title: Class protos.google.cloud.apigeeregistry.v1.ListApiDeploymentRevisionsRequest (3.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:06.685664+00:00
---

# Class protos.google.cloud.apigeeregistry.v1.ListApiDeploymentRevisionsRequest (3.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.listapideploymentrevisionsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apigeeregistry.v1.ListApiDeploymentRevisionsRequest (3.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.0.1 (latest)  1.0.1  0.2.1  0.1.0 

Represents a ListApiDeploymentRevisionsRequest.

## Implements

[protos.google.cloud.apigeeregistry.v1.IListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.ilistapideploymentrevisionsrequest)

## Package

[@google-cloud/apigee-registry](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apigeeregistry.v1.IListApiDeploymentRevisionsRequest);

Constructs a new ListApiDeploymentRevisionsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.ilistapideploymentrevisionsrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

ListApiDeploymentRevisionsRequest name.

### pageSize
    
    
    public pageSize: number;

ListApiDeploymentRevisionsRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListApiDeploymentRevisionsRequest pageToken.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apigeeregistry.v1.IListApiDeploymentRevisionsRequest): google.cloud.apigeeregistry.v1.ListApiDeploymentRevisionsRequest;

Creates a new ListApiDeploymentRevisionsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.ilistapideploymentrevisionsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.listapideploymentrevisionsrequest)` | ListApiDeploymentRevisionsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apigeeregistry.v1.ListApiDeploymentRevisionsRequest;

Decodes a ListApiDeploymentRevisionsRequest message from the specified reader or buffer.

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
`[ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.listapideploymentrevisionsrequest)` | ListApiDeploymentRevisionsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apigeeregistry.v1.ListApiDeploymentRevisionsRequest;

Decodes a ListApiDeploymentRevisionsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.listapideploymentrevisionsrequest)` | ListApiDeploymentRevisionsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apigeeregistry.v1.IListApiDeploymentRevisionsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListApiDeploymentRevisionsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.ilistapideploymentrevisionsrequest)`   
ListApiDeploymentRevisionsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apigeeregistry.v1.IListApiDeploymentRevisionsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListApiDeploymentRevisionsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.ilistapideploymentrevisionsrequest)`   
ListApiDeploymentRevisionsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apigeeregistry.v1.ListApiDeploymentRevisionsRequest;

Creates a ListApiDeploymentRevisionsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.listapideploymentrevisionsrequest)` | ListApiDeploymentRevisionsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListApiDeploymentRevisionsRequest

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

Converts this ListApiDeploymentRevisionsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apigeeregistry.v1.ListApiDeploymentRevisionsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListApiDeploymentRevisionsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListApiDeploymentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apigee-registry/latest/apigee-registry/protos.google.cloud.apigeeregistry.v1.listapideploymentrevisionsrequest)`   
ListApiDeploymentRevisionsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListApiDeploymentRevisionsRequest message.

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
