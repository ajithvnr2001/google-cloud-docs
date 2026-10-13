---
url: https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse-class
title: Class protos.google.cloud.contactcenterinsights.v1.QueryMetricsResponse (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:43.271788+00:00
---

# Class protos.google.cloud.contactcenterinsights.v1.QueryMetricsResponse (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.contactcenterinsights.v1.QueryMetricsResponse (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.0.1  4.1.3  3.9.0  3.8.0  3.7.0  3.6.0  3.3.0  3.1.0  2.7.0  2.6.0  2.4.1  2.3.0  2.1.2  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.2 

Represents a QueryMetricsResponse.

## Implements

[protos.google.cloud.contactcenterinsights.v1.IQueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iquerymetricsresponse)

## Package

[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.contactcenterinsights.v1.IQueryMetricsResponse);

Constructs a new QueryMetricsResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IQueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iquerymetricsresponse)`   
Properties to set  
  
## Properties 

### location
    
    
    public location: string;

QueryMetricsResponse location.

### macroAverageSlice
    
    
    public macroAverageSlice?: (google.cloud.contactcenterinsights.v1.QueryMetricsResponse.ISlice|null);

QueryMetricsResponse macroAverageSlice.

### slices
    
    
    public slices: google.cloud.contactcenterinsights.v1.QueryMetricsResponse.ISlice[];

QueryMetricsResponse slices.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

QueryMetricsResponse updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.contactcenterinsights.v1.IQueryMetricsResponse): google.cloud.contactcenterinsights.v1.QueryMetricsResponse;

Creates a new QueryMetricsResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IQueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iquerymetricsresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[QueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse-class)` | QueryMetricsResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.contactcenterinsights.v1.QueryMetricsResponse;

Decodes a QueryMetricsResponse message from the specified reader or buffer.

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
`[QueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse-class)` | QueryMetricsResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.contactcenterinsights.v1.QueryMetricsResponse;

Decodes a QueryMetricsResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[QueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse-class)` | QueryMetricsResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.contactcenterinsights.v1.IQueryMetricsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified QueryMetricsResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IQueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iquerymetricsresponse)`   
QueryMetricsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.contactcenterinsights.v1.IQueryMetricsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified QueryMetricsResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IQueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iquerymetricsresponse)`   
QueryMetricsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.contactcenterinsights.v1.QueryMetricsResponse;

Creates a QueryMetricsResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[QueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse-class)` | QueryMetricsResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for QueryMetricsResponse

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

Converts this QueryMetricsResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.contactcenterinsights.v1.QueryMetricsResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a QueryMetricsResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[QueryMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse-class)`   
QueryMetricsResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a QueryMetricsResponse message.

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
