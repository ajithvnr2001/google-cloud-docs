---
url: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.restrictallowedresourcesresponse
title: Class protos.google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:13.092286+00:00
---

# Class protos.google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.restrictallowedresourcesresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.6.2  3.5.0  3.4.1  3.2.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.6 

Represents a RestrictAllowedResourcesResponse.

## Implements

[protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesresponse)

## Package

[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse);

Constructs a new RestrictAllowedResourcesResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesresponse)`   
Properties to set  
  
## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse): google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse;

Creates a new RestrictAllowedResourcesResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.restrictallowedresourcesresponse)` | RestrictAllowedResourcesResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse;

Decodes a RestrictAllowedResourcesResponse message from the specified reader or buffer.

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
`[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.restrictallowedresourcesresponse)` | RestrictAllowedResourcesResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse;

Decodes a RestrictAllowedResourcesResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.restrictallowedresourcesresponse)` | RestrictAllowedResourcesResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RestrictAllowedResourcesResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesresponse)`   
RestrictAllowedResourcesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RestrictAllowedResourcesResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesresponse)`   
RestrictAllowedResourcesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse;

Creates a RestrictAllowedResourcesResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.restrictallowedresourcesresponse)` | RestrictAllowedResourcesResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RestrictAllowedResourcesResponse

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

Converts this RestrictAllowedResourcesResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RestrictAllowedResourcesResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.restrictallowedresourcesresponse)`   
RestrictAllowedResourcesResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RestrictAllowedResourcesResponse message.

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
