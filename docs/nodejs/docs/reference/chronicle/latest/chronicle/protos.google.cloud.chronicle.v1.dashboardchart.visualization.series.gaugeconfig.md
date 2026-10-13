---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.gaugeconfig
title: Class protos.google.cloud.chronicle.v1.DashboardChart.Visualization.Series.GaugeConfig (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:39.207905+00:00
---

# Class protos.google.cloud.chronicle.v1.DashboardChart.Visualization.Series.GaugeConfig (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.gaugeconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.DashboardChart.Visualization.Series.GaugeConfig (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a GaugeConfig.

## Implements

[protos.google.cloud.chronicle.v1.DashboardChart.Visualization.Series.IGaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.igaugeconfig)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.chronicle.v1.DashboardChart.Visualization.Series.IGaugeConfig);

Constructs a new GaugeConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.igaugeconfig)`   
Properties to set  
  
## Properties 

### baseValue
    
    
    public baseValue?: (google.cloud.chronicle.v1.DashboardChart.Visualization.Series.IGaugeValue|null);

GaugeConfig baseValue.

### limitValue
    
    
    public limitValue?: (google.cloud.chronicle.v1.DashboardChart.Visualization.Series.IGaugeValue|null);

GaugeConfig limitValue.

### thresholdValues
    
    
    public thresholdValues: google.cloud.chronicle.v1.DashboardChart.Visualization.Series.IGaugeValue[];

GaugeConfig thresholdValues.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.chronicle.v1.DashboardChart.Visualization.Series.IGaugeConfig): google.cloud.chronicle.v1.DashboardChart.Visualization.Series.GaugeConfig;

Creates a new GaugeConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.igaugeconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.gaugeconfig)` | GaugeConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.chronicle.v1.DashboardChart.Visualization.Series.GaugeConfig;

Decodes a GaugeConfig message from the specified reader or buffer.

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
`[GaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.gaugeconfig)` | GaugeConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.chronicle.v1.DashboardChart.Visualization.Series.GaugeConfig;

Decodes a GaugeConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.gaugeconfig)` | GaugeConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.chronicle.v1.DashboardChart.Visualization.Series.IGaugeConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GaugeConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.igaugeconfig)`   
GaugeConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.chronicle.v1.DashboardChart.Visualization.Series.IGaugeConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GaugeConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.igaugeconfig)`   
GaugeConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.chronicle.v1.DashboardChart.Visualization.Series.GaugeConfig;

Creates a GaugeConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.gaugeconfig)` | GaugeConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GaugeConfig

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

Converts this GaugeConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.chronicle.v1.DashboardChart.Visualization.Series.GaugeConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GaugeConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GaugeConfig](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.visualization.series.gaugeconfig)`   
GaugeConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GaugeConfig message.

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
