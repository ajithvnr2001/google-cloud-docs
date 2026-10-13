---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.fieldfilter
title: Class protos.google.ads.admanager.v1.ReportDefinition.Filter.FieldFilter (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:54.081456+00:00
---

# Class protos.google.ads.admanager.v1.ReportDefinition.Filter.FieldFilter (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.fieldfilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.ReportDefinition.Filter.FieldFilter (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents a FieldFilter.

## Implements

[protos.google.ads.admanager.v1.ReportDefinition.Filter.IFieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.ifieldfilter)

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.admanager.v1.ReportDefinition.Filter.IFieldFilter);

Constructs a new FieldFilter.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.ifieldfilter)`   
Properties to set  
  
## Properties 

### field
    
    
    public field?: (google.ads.admanager.v1.ReportDefinition.IField|null);

FieldFilter field.

### metricValueType
    
    
    public metricValueType?: (google.ads.admanager.v1.ReportDefinition.MetricValueType|keyof typeof google.ads.admanager.v1.ReportDefinition.MetricValueType|null);

FieldFilter metricValueType.

### operation
    
    
    public operation: (google.ads.admanager.v1.ReportDefinition.Filter.Operation|keyof typeof google.ads.admanager.v1.ReportDefinition.Filter.Operation);

FieldFilter operation.

### slice
    
    
    public slice?: (google.ads.admanager.v1.ReportDefinition.ISlice|null);

FieldFilter slice.

### timePeriodIndex
    
    
    public timePeriodIndex?: (number|null);

FieldFilter timePeriodIndex.

### values
    
    
    public values: google.ads.admanager.v1.IReportValue[];

FieldFilter values.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.admanager.v1.ReportDefinition.Filter.IFieldFilter): google.ads.admanager.v1.ReportDefinition.Filter.FieldFilter;

Creates a new FieldFilter instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.ifieldfilter)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.fieldfilter)` | FieldFilter instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.admanager.v1.ReportDefinition.Filter.FieldFilter;

Decodes a FieldFilter message from the specified reader or buffer.

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
`[FieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.fieldfilter)` | FieldFilter  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.admanager.v1.ReportDefinition.Filter.FieldFilter;

Decodes a FieldFilter message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.fieldfilter)` | FieldFilter  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.admanager.v1.ReportDefinition.Filter.IFieldFilter, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldFilter message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.ifieldfilter)`   
FieldFilter message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.admanager.v1.ReportDefinition.Filter.IFieldFilter, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldFilter message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.ifieldfilter)`   
FieldFilter message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.admanager.v1.ReportDefinition.Filter.FieldFilter;

Creates a FieldFilter message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.fieldfilter)` | FieldFilter  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FieldFilter

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

Converts this FieldFilter to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.admanager.v1.ReportDefinition.Filter.FieldFilter, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FieldFilter message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FieldFilter](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.reportdefinition.filter.fieldfilter)`   
FieldFilter  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FieldFilter message.

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
