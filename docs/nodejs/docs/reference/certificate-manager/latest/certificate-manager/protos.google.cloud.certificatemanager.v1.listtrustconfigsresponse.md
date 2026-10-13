---
url: https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listtrustconfigsresponse
title: Class protos.google.cloud.certificatemanager.v1.ListTrustConfigsResponse (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:18.308140+00:00
---

# Class protos.google.cloud.certificatemanager.v1.ListTrustConfigsResponse (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listtrustconfigsresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.certificatemanager.v1.ListTrustConfigsResponse (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.3  0.7.2  0.6.2  0.5.0  0.1.0 

Represents a ListTrustConfigsResponse.

## Implements

[protos.google.cloud.certificatemanager.v1.IListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilisttrustconfigsresponse)

## Package

[@google-cloud/certificate-manager](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.certificatemanager.v1.IListTrustConfigsResponse);

Constructs a new ListTrustConfigsResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilisttrustconfigsresponse)`   
Properties to set  
  
## Properties 

### nextPageToken
    
    
    public nextPageToken: string;

ListTrustConfigsResponse nextPageToken.

### trustConfigs
    
    
    public trustConfigs: google.cloud.certificatemanager.v1.ITrustConfig[];

ListTrustConfigsResponse trustConfigs.

### unreachable
    
    
    public unreachable: string[];

ListTrustConfigsResponse unreachable.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.certificatemanager.v1.IListTrustConfigsResponse): google.cloud.certificatemanager.v1.ListTrustConfigsResponse;

Creates a new ListTrustConfigsResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilisttrustconfigsresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listtrustconfigsresponse)` | ListTrustConfigsResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.certificatemanager.v1.ListTrustConfigsResponse;

Decodes a ListTrustConfigsResponse message from the specified reader or buffer.

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
`[ListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listtrustconfigsresponse)` | ListTrustConfigsResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.certificatemanager.v1.ListTrustConfigsResponse;

Decodes a ListTrustConfigsResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listtrustconfigsresponse)` | ListTrustConfigsResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.certificatemanager.v1.IListTrustConfigsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListTrustConfigsResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilisttrustconfigsresponse)`   
ListTrustConfigsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.certificatemanager.v1.IListTrustConfigsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListTrustConfigsResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilisttrustconfigsresponse)`   
ListTrustConfigsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.certificatemanager.v1.ListTrustConfigsResponse;

Creates a ListTrustConfigsResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listtrustconfigsresponse)` | ListTrustConfigsResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListTrustConfigsResponse

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

Converts this ListTrustConfigsResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.certificatemanager.v1.ListTrustConfigsResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListTrustConfigsResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listtrustconfigsresponse)`   
ListTrustConfigsResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListTrustConfigsResponse message.

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
