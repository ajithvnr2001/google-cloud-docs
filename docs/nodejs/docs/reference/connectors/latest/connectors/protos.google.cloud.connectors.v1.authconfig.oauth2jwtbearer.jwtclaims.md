---
url: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.jwtclaims
title: Class protos.google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.JwtClaims (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:24.450496+00:00
---

# Class protos.google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.JwtClaims (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.jwtclaims

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.JwtClaims (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a JwtClaims.

## Implements

[protos.google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.IJwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.ijwtclaims)

## Package

[@google-cloud/connectors](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.IJwtClaims);

Constructs a new JwtClaims.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.ijwtclaims)`   
Properties to set  
  
## Properties 

### audience
    
    
    public audience: string;

JwtClaims audience.

### issuer
    
    
    public issuer: string;

JwtClaims issuer.

### subject
    
    
    public subject: string;

JwtClaims subject.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.IJwtClaims): google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.JwtClaims;

Creates a new JwtClaims instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.ijwtclaims)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[JwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.jwtclaims)` | JwtClaims instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.JwtClaims;

Decodes a JwtClaims message from the specified reader or buffer.

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
`[JwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.jwtclaims)` | JwtClaims  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.JwtClaims;

Decodes a JwtClaims message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[JwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.jwtclaims)` | JwtClaims  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.IJwtClaims, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified JwtClaims message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.ijwtclaims)`   
JwtClaims message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.IJwtClaims, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified JwtClaims message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.ijwtclaims)`   
JwtClaims message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.JwtClaims;

Creates a JwtClaims message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[JwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.jwtclaims)` | JwtClaims  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for JwtClaims

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

Converts this JwtClaims to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.connectors.v1.AuthConfig.Oauth2JwtBearer.JwtClaims, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a JwtClaims message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[JwtClaims](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.authconfig.oauth2jwtbearer.jwtclaims)`   
JwtClaims  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a JwtClaims message.

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
