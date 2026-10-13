---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.httprequest
title: Class protos.google.api.servicecontrol.v1.HttpRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:42.287779+00:00
---

# Class protos.google.api.servicecontrol.v1.HttpRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.httprequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.servicecontrol.v1.HttpRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  4.4.0  3.3.0  3.2.0  2.3.0  2.2.0  2.1.2  2.0.3  1.4.0  1.3.0  1.2.1  1.1.4 

Represents a HttpRequest.

## Implements

[protos.google.api.servicecontrol.v1.IHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.ihttprequest)

## Package

[@google-cloud/service-control](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.servicecontrol.v1.IHttpRequest);

Constructs a new HttpRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.ihttprequest)`   
Properties to set  
  
## Properties 

### cacheFillBytes
    
    
    public cacheFillBytes: (number|Long|string);

HttpRequest cacheFillBytes.

### cacheHit
    
    
    public cacheHit: boolean;

HttpRequest cacheHit.

### cacheLookup
    
    
    public cacheLookup: boolean;

HttpRequest cacheLookup.

### cacheValidatedWithOriginServer
    
    
    public cacheValidatedWithOriginServer: boolean;

HttpRequest cacheValidatedWithOriginServer.

### latency
    
    
    public latency?: (google.protobuf.IDuration|null);

HttpRequest latency.

### protocol
    
    
    public protocol: string;

HttpRequest protocol.

### referer
    
    
    public referer: string;

HttpRequest referer.

### remoteIp
    
    
    public remoteIp: string;

HttpRequest remoteIp.

### requestMethod
    
    
    public requestMethod: string;

HttpRequest requestMethod.

### requestSize
    
    
    public requestSize: (number|Long|string);

HttpRequest requestSize.

### requestUrl
    
    
    public requestUrl: string;

HttpRequest requestUrl.

### responseSize
    
    
    public responseSize: (number|Long|string);

HttpRequest responseSize.

### serverIp
    
    
    public serverIp: string;

HttpRequest serverIp.

### status
    
    
    public status: number;

HttpRequest status.

### userAgent
    
    
    public userAgent: string;

HttpRequest userAgent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.servicecontrol.v1.IHttpRequest): google.api.servicecontrol.v1.HttpRequest;

Creates a new HttpRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.ihttprequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.httprequest)` | HttpRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.servicecontrol.v1.HttpRequest;

Decodes a HttpRequest message from the specified reader or buffer.

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
`[HttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.httprequest)` | HttpRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.servicecontrol.v1.HttpRequest;

Decodes a HttpRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.httprequest)` | HttpRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.servicecontrol.v1.IHttpRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HttpRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.ihttprequest)`   
HttpRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.servicecontrol.v1.IHttpRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HttpRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.ihttprequest)`   
HttpRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.servicecontrol.v1.HttpRequest;

Creates a HttpRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.httprequest)` | HttpRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for HttpRequest

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

Converts this HttpRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.servicecontrol.v1.HttpRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a HttpRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[HttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.httprequest)`   
HttpRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a HttpRequest message.

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
