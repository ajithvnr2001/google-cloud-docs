---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.statisticaltimeseriesfilter-class
title: Class protos.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:22.414700+00:00
---

# Class protos.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.statisticaltimeseriesfilter-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  4.2.0  2.9.2  2.8.0  2.6.1  2.5.1  2.4.2  2.3.4 

Represents a StatisticalTimeSeriesFilter.

## Implements

[protos.google.monitoring.dashboard.v1.IStatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.istatisticaltimeseriesfilter)

## Package

[@google-cloud/monitoring-dashboards](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.dashboard.v1.IStatisticalTimeSeriesFilter);

Constructs a new StatisticalTimeSeriesFilter.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.istatisticaltimeseriesfilter)`   
Properties to set  
  
## Properties 

### numTimeSeries
    
    
    public numTimeSeries: number;

StatisticalTimeSeriesFilter numTimeSeries.

### rankingMethod
    
    
    public rankingMethod: (google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter.Method|keyof typeof google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter.Method);

StatisticalTimeSeriesFilter rankingMethod.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.dashboard.v1.IStatisticalTimeSeriesFilter): google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter;

Creates a new StatisticalTimeSeriesFilter instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.istatisticaltimeseriesfilter)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[StatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.statisticaltimeseriesfilter-class)` | StatisticalTimeSeriesFilter instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter;

Decodes a StatisticalTimeSeriesFilter message from the specified reader or buffer.

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
`[StatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.statisticaltimeseriesfilter-class)` | StatisticalTimeSeriesFilter  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter;

Decodes a StatisticalTimeSeriesFilter message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[StatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.statisticaltimeseriesfilter-class)` | StatisticalTimeSeriesFilter  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.dashboard.v1.IStatisticalTimeSeriesFilter, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StatisticalTimeSeriesFilter message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.istatisticaltimeseriesfilter)`   
StatisticalTimeSeriesFilter message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.dashboard.v1.IStatisticalTimeSeriesFilter, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StatisticalTimeSeriesFilter message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.istatisticaltimeseriesfilter)`   
StatisticalTimeSeriesFilter message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter;

Creates a StatisticalTimeSeriesFilter message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[StatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.statisticaltimeseriesfilter-class)` | StatisticalTimeSeriesFilter  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for StatisticalTimeSeriesFilter

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

Converts this StatisticalTimeSeriesFilter to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.dashboard.v1.StatisticalTimeSeriesFilter, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a StatisticalTimeSeriesFilter message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[StatisticalTimeSeriesFilter](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.statisticaltimeseriesfilter-class)`   
StatisticalTimeSeriesFilter  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a StatisticalTimeSeriesFilter message.

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
