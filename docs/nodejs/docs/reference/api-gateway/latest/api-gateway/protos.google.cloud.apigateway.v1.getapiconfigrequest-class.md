---
url: https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.getapiconfigrequest-class
title: Class protos.google.cloud.apigateway.v1.GetApiConfigRequest (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:56.199087+00:00
---

# Class protos.google.cloud.apigateway.v1.GetApiConfigRequest (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.getapiconfigrequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apigateway.v1.GetApiConfigRequest (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  4.3.0  2.2.2  2.1.2  1.2.1  1.1.6 

Represents a GetApiConfigRequest.

## Implements

[protos.google.cloud.apigateway.v1.IGetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.igetapiconfigrequest)

## Package

[@google-cloud/api-gateway](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apigateway.v1.IGetApiConfigRequest);

Constructs a new GetApiConfigRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.igetapiconfigrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

GetApiConfigRequest name.

### view
    
    
    public view: (google.cloud.apigateway.v1.GetApiConfigRequest.ConfigView|keyof typeof google.cloud.apigateway.v1.GetApiConfigRequest.ConfigView);

GetApiConfigRequest view.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apigateway.v1.IGetApiConfigRequest): google.cloud.apigateway.v1.GetApiConfigRequest;

Creates a new GetApiConfigRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.igetapiconfigrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.getapiconfigrequest-class)` | GetApiConfigRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apigateway.v1.GetApiConfigRequest;

Decodes a GetApiConfigRequest message from the specified reader or buffer.

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
`[GetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.getapiconfigrequest-class)` | GetApiConfigRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apigateway.v1.GetApiConfigRequest;

Decodes a GetApiConfigRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.getapiconfigrequest-class)` | GetApiConfigRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apigateway.v1.IGetApiConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetApiConfigRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.igetapiconfigrequest)`   
GetApiConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apigateway.v1.IGetApiConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetApiConfigRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.igetapiconfigrequest)`   
GetApiConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apigateway.v1.GetApiConfigRequest;

Creates a GetApiConfigRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.getapiconfigrequest-class)` | GetApiConfigRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GetApiConfigRequest

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

Converts this GetApiConfigRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apigateway.v1.GetApiConfigRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GetApiConfigRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GetApiConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/api-gateway/latest/api-gateway/protos.google.cloud.apigateway.v1.getapiconfigrequest-class)`   
GetApiConfigRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GetApiConfigRequest message.

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
