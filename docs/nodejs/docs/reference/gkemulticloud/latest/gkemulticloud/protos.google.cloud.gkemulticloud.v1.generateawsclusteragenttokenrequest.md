---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateawsclusteragenttokenrequest
title: Class protos.google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenRequest (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:51.618683+00:00
---

# Class protos.google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenRequest (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateawsclusteragenttokenrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenRequest (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

Represents a GenerateAwsClusterAgentTokenRequest.

## Implements

[protos.google.cloud.gkemulticloud.v1.IGenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateawsclusteragenttokenrequest)

## Package

[@google-cloud/gkemulticloud](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkemulticloud.v1.IGenerateAwsClusterAgentTokenRequest);

Constructs a new GenerateAwsClusterAgentTokenRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateawsclusteragenttokenrequest)`   
Properties to set  
  
## Properties 

### audience
    
    
    public audience: string;

GenerateAwsClusterAgentTokenRequest audience.

### awsCluster
    
    
    public awsCluster: string;

GenerateAwsClusterAgentTokenRequest awsCluster.

### grantType
    
    
    public grantType: string;

GenerateAwsClusterAgentTokenRequest grantType.

### nodePoolId
    
    
    public nodePoolId: string;

GenerateAwsClusterAgentTokenRequest nodePoolId.

### options
    
    
    public options: string;

GenerateAwsClusterAgentTokenRequest options.

### requestedTokenType
    
    
    public requestedTokenType: string;

GenerateAwsClusterAgentTokenRequest requestedTokenType.

### scope
    
    
    public scope: string;

GenerateAwsClusterAgentTokenRequest scope.

### subjectToken
    
    
    public subjectToken: string;

GenerateAwsClusterAgentTokenRequest subjectToken.

### subjectTokenType
    
    
    public subjectTokenType: string;

GenerateAwsClusterAgentTokenRequest subjectTokenType.

### version
    
    
    public version: string;

GenerateAwsClusterAgentTokenRequest version.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkemulticloud.v1.IGenerateAwsClusterAgentTokenRequest): google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenRequest;

Creates a new GenerateAwsClusterAgentTokenRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateawsclusteragenttokenrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateawsclusteragenttokenrequest)` | GenerateAwsClusterAgentTokenRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenRequest;

Decodes a GenerateAwsClusterAgentTokenRequest message from the specified reader or buffer.

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
`[GenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateawsclusteragenttokenrequest)` | GenerateAwsClusterAgentTokenRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenRequest;

Decodes a GenerateAwsClusterAgentTokenRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateawsclusteragenttokenrequest)` | GenerateAwsClusterAgentTokenRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkemulticloud.v1.IGenerateAwsClusterAgentTokenRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerateAwsClusterAgentTokenRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateawsclusteragenttokenrequest)`   
GenerateAwsClusterAgentTokenRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkemulticloud.v1.IGenerateAwsClusterAgentTokenRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerateAwsClusterAgentTokenRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.igenerateawsclusteragenttokenrequest)`   
GenerateAwsClusterAgentTokenRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenRequest;

Creates a GenerateAwsClusterAgentTokenRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateawsclusteragenttokenrequest)` | GenerateAwsClusterAgentTokenRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GenerateAwsClusterAgentTokenRequest

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

Converts this GenerateAwsClusterAgentTokenRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GenerateAwsClusterAgentTokenRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GenerateAwsClusterAgentTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.generateawsclusteragenttokenrequest)`   
GenerateAwsClusterAgentTokenRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GenerateAwsClusterAgentTokenRequest message.

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
