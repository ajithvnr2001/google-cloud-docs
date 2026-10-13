---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.drilldown-class
title: Class protos.google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:26.632705+00:00
---

# Class protos.google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.drilldown-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a DrillDown.

## Implements

[protos.google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.IDrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.idrilldown)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.IDrillDown);

Constructs a new DrillDown.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.idrilldown)`   
Properties to set  
  
## Properties 

### customSettings
    
    
    public customSettings?: (google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown.ICustomDrillDownSettings|null);

DrillDown customSettings.

### defaultSettings
    
    
    public defaultSettings?: (google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown.IDefaultDrillDownSettings|null);

DrillDown defaultSettings.

### displayName
    
    
    public displayName: string;

DrillDown displayName.

### id
    
    
    public id: string;

DrillDown id.

### settings
    
    
    public settings?: ("defaultSettings"|"customSettings");

DrillDown settings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.IDrillDown): google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown;

Creates a new DrillDown instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.idrilldown)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.drilldown-class)` | DrillDown instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown;

Decodes a DrillDown message from the specified reader or buffer.

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
`[DrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.drilldown-class)` | DrillDown  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown;

Decodes a DrillDown message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.drilldown-class)` | DrillDown  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.IDrillDown, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DrillDown message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.idrilldown)`   
DrillDown message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.IDrillDown, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DrillDown message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.idrilldown)`   
DrillDown message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown;

Creates a DrillDown message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.drilldown-class)` | DrillDown  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DrillDown

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

Converts this DrillDown to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.chronicle.v1.DashboardChart.DrillDownConfig.DrillDown, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DrillDown message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DrillDown](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart.drilldownconfig.drilldown-class)`   
DrillDown  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DrillDown message.

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
