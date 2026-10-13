---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.apiauthentication
title: Class protos.google.cloud.ces.v1.ApiAuthentication (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:05:54.111257+00:00
---

# Class protos.google.cloud.ces.v1.ApiAuthentication (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.apiauthentication

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.ApiAuthentication (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an ApiAuthentication.

## Implements

[protos.google.cloud.ces.v1.IApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapiauthentication)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IApiAuthentication);

Constructs a new ApiAuthentication.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapiauthentication)`   
Properties to set  
  
## Properties 

### apiKeyConfig
    
    
    public apiKeyConfig?: (google.cloud.ces.v1.IApiKeyConfig|null);

ApiAuthentication apiKeyConfig.

### authConfig
    
    
    public authConfig?: ("apiKeyConfig"|"oauthConfig"|"serviceAgentIdTokenAuthConfig"|"serviceAccountAuthConfig"|"bearerTokenConfig");

ApiAuthentication authConfig.

### bearerTokenConfig
    
    
    public bearerTokenConfig?: (google.cloud.ces.v1.IBearerTokenConfig|null);

ApiAuthentication bearerTokenConfig.

### oauthConfig
    
    
    public oauthConfig?: (google.cloud.ces.v1.IOAuthConfig|null);

ApiAuthentication oauthConfig.

### serviceAccountAuthConfig
    
    
    public serviceAccountAuthConfig?: (google.cloud.ces.v1.IServiceAccountAuthConfig|null);

ApiAuthentication serviceAccountAuthConfig.

### serviceAgentIdTokenAuthConfig
    
    
    public serviceAgentIdTokenAuthConfig?: (google.cloud.ces.v1.IServiceAgentIdTokenAuthConfig|null);

ApiAuthentication serviceAgentIdTokenAuthConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IApiAuthentication): google.cloud.ces.v1.ApiAuthentication;

Creates a new ApiAuthentication instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapiauthentication)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.apiauthentication)` | ApiAuthentication instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.ApiAuthentication;

Decodes an ApiAuthentication message from the specified reader or buffer.

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
`[ApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.apiauthentication)` | ApiAuthentication  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.ApiAuthentication;

Decodes an ApiAuthentication message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.apiauthentication)` | ApiAuthentication  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IApiAuthentication, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ApiAuthentication message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapiauthentication)`   
ApiAuthentication message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IApiAuthentication, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ApiAuthentication message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iapiauthentication)`   
ApiAuthentication message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.ApiAuthentication;

Creates an ApiAuthentication message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.apiauthentication)` | ApiAuthentication  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ApiAuthentication

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

Converts this ApiAuthentication to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.ApiAuthentication, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ApiAuthentication message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ApiAuthentication](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.apiauthentication)`   
ApiAuthentication  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ApiAuthentication message.

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
