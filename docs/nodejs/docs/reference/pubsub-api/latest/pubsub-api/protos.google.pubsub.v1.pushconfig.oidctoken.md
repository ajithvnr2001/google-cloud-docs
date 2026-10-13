---
url: https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.oidctoken
title: Class protos.google.pubsub.v1.PushConfig.OidcToken (0.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:15.182270+00:00
---

# Class protos.google.pubsub.v1.PushConfig.OidcToken (0.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.oidctoken

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.pubsub.v1.PushConfig.OidcToken (0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.1 

Represents an OidcToken.

## Implements

[protos.google.pubsub.v1.PushConfig.IOidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.ioidctoken)

## Package

[@google-cloud/pubsub-api](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.pubsub.v1.PushConfig.IOidcToken);

Constructs a new OidcToken.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.ioidctoken)`   
Properties to set  
  
## Properties 

### audience
    
    
    public audience: string;

OidcToken audience.

### serviceAccountEmail
    
    
    public serviceAccountEmail: string;

OidcToken serviceAccountEmail.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.pubsub.v1.PushConfig.IOidcToken): google.pubsub.v1.PushConfig.OidcToken;

Creates a new OidcToken instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.ioidctoken)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.oidctoken)` | OidcToken instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.pubsub.v1.PushConfig.OidcToken;

Decodes an OidcToken message from the specified reader or buffer.

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
`[OidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.oidctoken)` | OidcToken  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.pubsub.v1.PushConfig.OidcToken;

Decodes an OidcToken message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.oidctoken)` | OidcToken  
  
### encode(message, writer)
    
    
    public static encode(message: google.pubsub.v1.PushConfig.IOidcToken, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OidcToken message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.ioidctoken)`   
OidcToken message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.pubsub.v1.PushConfig.IOidcToken, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OidcToken message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.ioidctoken)`   
OidcToken message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.pubsub.v1.PushConfig.OidcToken;

Creates an OidcToken message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.oidctoken)` | OidcToken  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OidcToken

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

Converts this OidcToken to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.pubsub.v1.PushConfig.OidcToken, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OidcToken message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OidcToken](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pushconfig.oidctoken)`   
OidcToken  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OidcToken message.

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
