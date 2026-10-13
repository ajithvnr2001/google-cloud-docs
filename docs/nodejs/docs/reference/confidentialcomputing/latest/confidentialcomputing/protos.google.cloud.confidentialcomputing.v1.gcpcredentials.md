---
url: https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.gcpcredentials
title: Class protos.google.cloud.confidentialcomputing.v1.GcpCredentials (3.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:37.244005+00:00
---

# Class protos.google.cloud.confidentialcomputing.v1.GcpCredentials (3.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.gcpcredentials

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.confidentialcomputing.v1.GcpCredentials (3.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.1 (latest)  2.3.0  1.8.0  1.7.0  1.2.0  0.1.0 

Represents a GcpCredentials.

## Implements

[protos.google.cloud.confidentialcomputing.v1.IGcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.igcpcredentials)

## Package

[@google-cloud/confidentialcomputing](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.confidentialcomputing.v1.IGcpCredentials);

Constructs a new GcpCredentials.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.igcpcredentials)`   
Properties to set  
  
## Properties 

### serviceAccountIdTokens
    
    
    public serviceAccountIdTokens: string[];

GcpCredentials serviceAccountIdTokens.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.confidentialcomputing.v1.IGcpCredentials): google.cloud.confidentialcomputing.v1.GcpCredentials;

Creates a new GcpCredentials instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.igcpcredentials)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.gcpcredentials)` | GcpCredentials instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.confidentialcomputing.v1.GcpCredentials;

Decodes a GcpCredentials message from the specified reader or buffer.

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
`[GcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.gcpcredentials)` | GcpCredentials  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.confidentialcomputing.v1.GcpCredentials;

Decodes a GcpCredentials message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.gcpcredentials)` | GcpCredentials  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.confidentialcomputing.v1.IGcpCredentials, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GcpCredentials message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.igcpcredentials)`   
GcpCredentials message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.confidentialcomputing.v1.IGcpCredentials, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GcpCredentials message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.igcpcredentials)`   
GcpCredentials message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.confidentialcomputing.v1.GcpCredentials;

Creates a GcpCredentials message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.gcpcredentials)` | GcpCredentials  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GcpCredentials

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

Converts this GcpCredentials to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.confidentialcomputing.v1.GcpCredentials, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GcpCredentials message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GcpCredentials](https://docs.cloud.google.com/nodejs/docs/reference/confidentialcomputing/latest/confidentialcomputing/protos.google.cloud.confidentialcomputing.v1.gcpcredentials)`   
GcpCredentials  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GcpCredentials message.

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
