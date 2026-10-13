---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardfilter
title: Class protos.google.cloud.chronicle.v1.DashboardFilter (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:32.488829+00:00
---

# Class protos.google.cloud.chronicle.v1.DashboardFilter (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardfilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.DashboardFilter (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a DashboardFilter.

## Implements

[protos.google.cloud.chronicle.v1.IDashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.idashboardfilter)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.chronicle.v1.IDashboardFilter);

Constructs a new DashboardFilter.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.idashboardfilter)`   
Properties to set  
  
## Properties 

### advancedFilterConfig
    
    
    public advancedFilterConfig?: (google.cloud.chronicle.v1.IAdvancedFilterConfig|null);

DashboardFilter advancedFilterConfig.

### chartIds
    
    
    public chartIds: string[];

DashboardFilter chartIds.

### dataSource
    
    
    public dataSource: (google.cloud.chronicle.v1.DataSource|keyof typeof google.cloud.chronicle.v1.DataSource);

DashboardFilter dataSource.

### displayName
    
    
    public displayName: string;

DashboardFilter displayName.

### fieldPath
    
    
    public fieldPath: string;

DashboardFilter fieldPath.

### filterOperatorAndFieldValues
    
    
    public filterOperatorAndFieldValues: google.cloud.chronicle.v1.IFilterOperatorAndValues[];

DashboardFilter filterOperatorAndFieldValues.

### id
    
    
    public id: string;

DashboardFilter id.

### isMandatory
    
    
    public isMandatory: boolean;

DashboardFilter isMandatory.

### isStandardTimeRangeFilter
    
    
    public isStandardTimeRangeFilter: boolean;

DashboardFilter isStandardTimeRangeFilter.

### isStandardTimeRangeFilterEnabled
    
    
    public isStandardTimeRangeFilterEnabled?: (boolean|null);

DashboardFilter isStandardTimeRangeFilterEnabled.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.chronicle.v1.IDashboardFilter): google.cloud.chronicle.v1.DashboardFilter;

Creates a new DashboardFilter instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.idashboardfilter)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardfilter)` | DashboardFilter instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.chronicle.v1.DashboardFilter;

Decodes a DashboardFilter message from the specified reader or buffer.

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
`[DashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardfilter)` | DashboardFilter  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.chronicle.v1.DashboardFilter;

Decodes a DashboardFilter message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardfilter)` | DashboardFilter  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.chronicle.v1.IDashboardFilter, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DashboardFilter message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.idashboardfilter)`   
DashboardFilter message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.chronicle.v1.IDashboardFilter, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DashboardFilter message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.idashboardfilter)`   
DashboardFilter message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.chronicle.v1.DashboardFilter;

Creates a DashboardFilter message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardfilter)` | DashboardFilter  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DashboardFilter

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

Converts this DashboardFilter to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.chronicle.v1.DashboardFilter, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DashboardFilter message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DashboardFilter](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardfilter)`   
DashboardFilter  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DashboardFilter message.

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
