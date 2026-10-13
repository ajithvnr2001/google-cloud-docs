---
url: https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.generatecredentialsrequest-class
title: Class protos.google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:06.809381+00:00
---

# Class protos.google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.generatecredentialsrequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.0  5.0.1  4.0.0  3.2.0  2.1.2  2.0.5  1.1.0  1.0.3 

Represents a GenerateCredentialsRequest.

## Implements

[protos.google.cloud.gkeconnect.gateway.v1beta1.IGenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.igeneratecredentialsrequest)

## Package

[@google-cloud/gke-connect-gateway](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkeconnect.gateway.v1beta1.IGenerateCredentialsRequest);

Constructs a new GenerateCredentialsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.igeneratecredentialsrequest)`   
Properties to set  
  
## Properties 

### forceUseAgent
    
    
    public forceUseAgent: boolean;

GenerateCredentialsRequest forceUseAgent.

### kubernetesNamespace
    
    
    public kubernetesNamespace: string;

GenerateCredentialsRequest kubernetesNamespace.

### name
    
    
    public name: string;

GenerateCredentialsRequest name.

### operatingSystem
    
    
    public operatingSystem: (google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest.OperatingSystem|keyof typeof google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest.OperatingSystem);

GenerateCredentialsRequest operatingSystem.

### version
    
    
    public version: string;

GenerateCredentialsRequest version.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkeconnect.gateway.v1beta1.IGenerateCredentialsRequest): google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest;

Creates a new GenerateCredentialsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.igeneratecredentialsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.generatecredentialsrequest-class)` | GenerateCredentialsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest;

Decodes a GenerateCredentialsRequest message from the specified reader or buffer.

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
`[GenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.generatecredentialsrequest-class)` | GenerateCredentialsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest;

Decodes a GenerateCredentialsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.generatecredentialsrequest-class)` | GenerateCredentialsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkeconnect.gateway.v1beta1.IGenerateCredentialsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerateCredentialsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.igeneratecredentialsrequest)`   
GenerateCredentialsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkeconnect.gateway.v1beta1.IGenerateCredentialsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerateCredentialsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.igeneratecredentialsrequest)`   
GenerateCredentialsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest;

Creates a GenerateCredentialsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.generatecredentialsrequest-class)` | GenerateCredentialsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GenerateCredentialsRequest

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

Converts this GenerateCredentialsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GenerateCredentialsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GenerateCredentialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-connect-gateway/latest/gke-connect-gateway/protos.google.cloud.gkeconnect.gateway.v1beta1.generatecredentialsrequest-class)`   
GenerateCredentialsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GenerateCredentialsRequest message.

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
