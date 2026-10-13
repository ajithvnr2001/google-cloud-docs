---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.acknowledgeuserdatacollectionresponse
title: Class protos.google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:54.548373+00:00
---

# Class protos.google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.acknowledgeuserdatacollectionresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents an AcknowledgeUserDataCollectionResponse.

## Implements

[protos.google.analytics.admin.v1alpha.IAcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iacknowledgeuserdatacollectionresponse)

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.admin.v1alpha.IAcknowledgeUserDataCollectionResponse);

Constructs a new AcknowledgeUserDataCollectionResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iacknowledgeuserdatacollectionresponse)`   
Properties to set  
  
## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.admin.v1alpha.IAcknowledgeUserDataCollectionResponse): google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse;

Creates a new AcknowledgeUserDataCollectionResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iacknowledgeuserdatacollectionresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.acknowledgeuserdatacollectionresponse)` | AcknowledgeUserDataCollectionResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse;

Decodes an AcknowledgeUserDataCollectionResponse message from the specified reader or buffer.

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
`[AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.acknowledgeuserdatacollectionresponse)` | AcknowledgeUserDataCollectionResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse;

Decodes an AcknowledgeUserDataCollectionResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.acknowledgeuserdatacollectionresponse)` | AcknowledgeUserDataCollectionResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.admin.v1alpha.IAcknowledgeUserDataCollectionResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AcknowledgeUserDataCollectionResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iacknowledgeuserdatacollectionresponse)`   
AcknowledgeUserDataCollectionResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.admin.v1alpha.IAcknowledgeUserDataCollectionResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AcknowledgeUserDataCollectionResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iacknowledgeuserdatacollectionresponse)`   
AcknowledgeUserDataCollectionResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse;

Creates an AcknowledgeUserDataCollectionResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.acknowledgeuserdatacollectionresponse)` | AcknowledgeUserDataCollectionResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AcknowledgeUserDataCollectionResponse

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

Converts this AcknowledgeUserDataCollectionResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AcknowledgeUserDataCollectionResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.acknowledgeuserdatacollectionresponse)`   
AcknowledgeUserDataCollectionResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AcknowledgeUserDataCollectionResponse message.

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
