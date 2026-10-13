---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accessmetricheader
title: Class protos.google.analytics.admin.v1beta.AccessMetricHeader (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:44.023870+00:00
---

# Class protos.google.analytics.admin.v1beta.AccessMetricHeader (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accessmetricheader

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1beta.AccessMetricHeader (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents an AccessMetricHeader.

## Implements

[protos.google.analytics.admin.v1beta.IAccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccessmetricheader)

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.admin.v1beta.IAccessMetricHeader);

Constructs a new AccessMetricHeader.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccessmetricheader)`   
Properties to set  
  
## Properties 

### metricName
    
    
    public metricName: string;

AccessMetricHeader metricName.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.admin.v1beta.IAccessMetricHeader): google.analytics.admin.v1beta.AccessMetricHeader;

Creates a new AccessMetricHeader instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccessmetricheader)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accessmetricheader)` | AccessMetricHeader instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.admin.v1beta.AccessMetricHeader;

Decodes an AccessMetricHeader message from the specified reader or buffer.

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
`[AccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accessmetricheader)` | AccessMetricHeader  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.admin.v1beta.AccessMetricHeader;

Decodes an AccessMetricHeader message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accessmetricheader)` | AccessMetricHeader  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.admin.v1beta.IAccessMetricHeader, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AccessMetricHeader message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccessmetricheader)`   
AccessMetricHeader message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.admin.v1beta.IAccessMetricHeader, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AccessMetricHeader message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccessmetricheader)`   
AccessMetricHeader message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.admin.v1beta.AccessMetricHeader;

Creates an AccessMetricHeader message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accessmetricheader)` | AccessMetricHeader  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AccessMetricHeader

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

Converts this AccessMetricHeader to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.admin.v1beta.AccessMetricHeader, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AccessMetricHeader message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AccessMetricHeader](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accessmetricheader)`   
AccessMetricHeader  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AccessMetricHeader message.

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
