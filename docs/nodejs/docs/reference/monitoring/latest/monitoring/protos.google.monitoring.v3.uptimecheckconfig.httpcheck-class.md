---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.httpcheck-class
title: Class protos.google.monitoring.v3.UptimeCheckConfig.HttpCheck (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:58.926049+00:00
---

# Class protos.google.monitoring.v3.UptimeCheckConfig.HttpCheck (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.httpcheck-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.UptimeCheckConfig.HttpCheck (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents a HttpCheck.

## Implements

[protos.google.monitoring.v3.UptimeCheckConfig.IHttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.ihttpcheck)

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.v3.UptimeCheckConfig.IHttpCheck);

Constructs a new HttpCheck.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.ihttpcheck)`   
Properties to set  
  
## Properties 

### acceptedResponseStatusCodes
    
    
    public acceptedResponseStatusCodes: google.monitoring.v3.UptimeCheckConfig.HttpCheck.IResponseStatusCode[];

HttpCheck acceptedResponseStatusCodes.

### authInfo
    
    
    public authInfo?: (google.monitoring.v3.UptimeCheckConfig.HttpCheck.IBasicAuthentication|null);

HttpCheck authInfo.

### authMethod
    
    
    public authMethod?: "serviceAgentAuthentication";

HttpCheck authMethod.

### body
    
    
    public body: (Uint8Array|Buffer|string);

HttpCheck body.

### contentType
    
    
    public contentType: (google.monitoring.v3.UptimeCheckConfig.HttpCheck.ContentType|keyof typeof google.monitoring.v3.UptimeCheckConfig.HttpCheck.ContentType);

HttpCheck contentType.

### customContentType
    
    
    public customContentType: string;

HttpCheck customContentType.

### headers
    
    
    public headers: { [k: string]: string };

HttpCheck headers.

### maskHeaders
    
    
    public maskHeaders: boolean;

HttpCheck maskHeaders.

### path
    
    
    public path: string;

HttpCheck path.

### pingConfig
    
    
    public pingConfig?: (google.monitoring.v3.UptimeCheckConfig.IPingConfig|null);

HttpCheck pingConfig.

### port
    
    
    public port: number;

HttpCheck port.

### requestMethod
    
    
    public requestMethod: (google.monitoring.v3.UptimeCheckConfig.HttpCheck.RequestMethod|keyof typeof google.monitoring.v3.UptimeCheckConfig.HttpCheck.RequestMethod);

HttpCheck requestMethod.

### serviceAgentAuthentication
    
    
    public serviceAgentAuthentication?: (google.monitoring.v3.UptimeCheckConfig.HttpCheck.IServiceAgentAuthentication|null);

HttpCheck serviceAgentAuthentication.

### useSsl
    
    
    public useSsl: boolean;

HttpCheck useSsl.

### validateSsl
    
    
    public validateSsl: boolean;

HttpCheck validateSsl.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.v3.UptimeCheckConfig.IHttpCheck): google.monitoring.v3.UptimeCheckConfig.HttpCheck;

Creates a new HttpCheck instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.ihttpcheck)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[HttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.httpcheck-class)` | HttpCheck instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.v3.UptimeCheckConfig.HttpCheck;

Decodes a HttpCheck message from the specified reader or buffer.

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
`[HttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.httpcheck-class)` | HttpCheck  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.v3.UptimeCheckConfig.HttpCheck;

Decodes a HttpCheck message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[HttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.httpcheck-class)` | HttpCheck  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.v3.UptimeCheckConfig.IHttpCheck, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HttpCheck message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.ihttpcheck)`   
HttpCheck message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.v3.UptimeCheckConfig.IHttpCheck, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HttpCheck message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.ihttpcheck)`   
HttpCheck message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.v3.UptimeCheckConfig.HttpCheck;

Creates a HttpCheck message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[HttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.httpcheck-class)` | HttpCheck  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for HttpCheck

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

Converts this HttpCheck to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.v3.UptimeCheckConfig.HttpCheck, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a HttpCheck message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[HttpCheck](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.httpcheck-class)`   
HttpCheck  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a HttpCheck message.

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
