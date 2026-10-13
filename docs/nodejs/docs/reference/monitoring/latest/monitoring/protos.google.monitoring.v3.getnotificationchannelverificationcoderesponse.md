---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.getnotificationchannelverificationcoderesponse
title: Class protos.google.monitoring.v3.GetNotificationChannelVerificationCodeResponse (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:57.059583+00:00
---

# Class protos.google.monitoring.v3.GetNotificationChannelVerificationCodeResponse (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.getnotificationchannelverificationcoderesponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.GetNotificationChannelVerificationCodeResponse (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents a GetNotificationChannelVerificationCodeResponse.

## Implements

[protos.google.monitoring.v3.IGetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.igetnotificationchannelverificationcoderesponse)

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.v3.IGetNotificationChannelVerificationCodeResponse);

Constructs a new GetNotificationChannelVerificationCodeResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.igetnotificationchannelverificationcoderesponse)`   
Properties to set  
  
## Properties 

### code
    
    
    public code: string;

GetNotificationChannelVerificationCodeResponse code.

### expireTime
    
    
    public expireTime?: (google.protobuf.ITimestamp|null);

GetNotificationChannelVerificationCodeResponse expireTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.v3.IGetNotificationChannelVerificationCodeResponse): google.monitoring.v3.GetNotificationChannelVerificationCodeResponse;

Creates a new GetNotificationChannelVerificationCodeResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.igetnotificationchannelverificationcoderesponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.getnotificationchannelverificationcoderesponse)` | GetNotificationChannelVerificationCodeResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.v3.GetNotificationChannelVerificationCodeResponse;

Decodes a GetNotificationChannelVerificationCodeResponse message from the specified reader or buffer.

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
`[GetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.getnotificationchannelverificationcoderesponse)` | GetNotificationChannelVerificationCodeResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.v3.GetNotificationChannelVerificationCodeResponse;

Decodes a GetNotificationChannelVerificationCodeResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.getnotificationchannelverificationcoderesponse)` | GetNotificationChannelVerificationCodeResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.v3.IGetNotificationChannelVerificationCodeResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetNotificationChannelVerificationCodeResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.igetnotificationchannelverificationcoderesponse)`   
GetNotificationChannelVerificationCodeResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.v3.IGetNotificationChannelVerificationCodeResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetNotificationChannelVerificationCodeResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.igetnotificationchannelverificationcoderesponse)`   
GetNotificationChannelVerificationCodeResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.v3.GetNotificationChannelVerificationCodeResponse;

Creates a GetNotificationChannelVerificationCodeResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.getnotificationchannelverificationcoderesponse)` | GetNotificationChannelVerificationCodeResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GetNotificationChannelVerificationCodeResponse

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

Converts this GetNotificationChannelVerificationCodeResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.v3.GetNotificationChannelVerificationCodeResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GetNotificationChannelVerificationCodeResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.getnotificationchannelverificationcoderesponse)`   
GetNotificationChannelVerificationCodeResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GetNotificationChannelVerificationCodeResponse message.

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
