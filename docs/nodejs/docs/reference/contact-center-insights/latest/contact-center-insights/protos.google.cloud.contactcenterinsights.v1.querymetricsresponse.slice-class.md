---
url: https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.slice-class
title: Class protos.google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:54.144407+00:00
---

# Class protos.google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.slice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.0.1  4.1.3  3.9.0  3.8.0  3.7.0  3.6.0  3.3.0  3.1.0  2.7.0  2.6.0  2.4.1  2.3.0  2.1.2  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.2 

Represents a Slice.

## Implements

[protos.google.cloud.contactcenterinsights.v1.QueryMetricsResponse.ISlice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.islice)

## Package

[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.contactcenterinsights.v1.QueryMetricsResponse.ISlice);

Constructs a new Slice.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISlice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.islice)`   
Properties to set  
  
## Properties 

### dimensions
    
    
    public dimensions: google.cloud.contactcenterinsights.v1.IDimension[];

Slice dimensions.

### timeSeries
    
    
    public timeSeries?: (google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice.ITimeSeries|null);

Slice timeSeries.

### total
    
    
    public total?: (google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice.IDataPoint|null);

Slice total.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.contactcenterinsights.v1.QueryMetricsResponse.ISlice): google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice;

Creates a new Slice instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISlice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.islice)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Slice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.slice-class)` | Slice instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice;

Decodes a Slice message from the specified reader or buffer.

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
`[Slice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.slice-class)` | Slice  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice;

Decodes a Slice message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Slice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.slice-class)` | Slice  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.contactcenterinsights.v1.QueryMetricsResponse.ISlice, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Slice message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISlice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.islice)`   
Slice message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.contactcenterinsights.v1.QueryMetricsResponse.ISlice, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Slice message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISlice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.islice)`   
Slice message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice;

Creates a Slice message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Slice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.slice-class)` | Slice  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Slice

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

Converts this Slice to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.contactcenterinsights.v1.QueryMetricsResponse.Slice, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Slice message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Slice](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.querymetricsresponse.slice-class)`   
Slice  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Slice message.

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
