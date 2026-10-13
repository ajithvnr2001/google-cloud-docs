---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authprovider
title: Class protos.google.api.AuthProvider (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:11.118560+00:00
---

# Class protos.google.api.AuthProvider (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authprovider

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.AuthProvider (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.3.0  2.2.2  2.1.2  1.2.1  1.1.4 

Represents an AuthProvider.

## Implements

[protos.google.api.IAuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthprovider)

## Package

[@google-cloud/service-usage](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IAuthProvider);

Constructs a new AuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthprovider)`   
Properties to set  
  
## Properties 

### audiences
    
    
    public audiences: string;

AuthProvider audiences.

### authorizationUrl
    
    
    public authorizationUrl: string;

AuthProvider authorizationUrl.

### id
    
    
    public id: string;

AuthProvider id.

### issuer
    
    
    public issuer: string;

AuthProvider issuer.

### jwksUri
    
    
    public jwksUri: string;

AuthProvider jwksUri.

### jwtLocations
    
    
    public jwtLocations: google.api.IJwtLocation[];

AuthProvider jwtLocations.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IAuthProvider): google.api.AuthProvider;

Creates a new AuthProvider instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthprovider)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authprovider)` | AuthProvider instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.AuthProvider;

Decodes an AuthProvider message from the specified reader or buffer.

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
`[AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authprovider)` | AuthProvider  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.AuthProvider;

Decodes an AuthProvider message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authprovider)` | AuthProvider  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IAuthProvider, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AuthProvider message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthprovider)`   
AuthProvider message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IAuthProvider, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AuthProvider message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.iauthprovider)`   
AuthProvider message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.AuthProvider;

Creates an AuthProvider message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authprovider)` | AuthProvider  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AuthProvider

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

Converts this AuthProvider to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.AuthProvider, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AuthProvider message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AuthProvider](https://docs.cloud.google.com/nodejs/docs/reference/service-usage/latest/service-usage/protos.google.api.authprovider)`   
AuthProvider  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AuthProvider message.

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
