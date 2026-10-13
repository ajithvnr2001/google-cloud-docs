---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent
title: Class protos.google.cloud.geminidataanalytics.v1.DataAgent (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:34.892976+00:00
---

# Class protos.google.cloud.geminidataanalytics.v1.DataAgent (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.geminidataanalytics.v1.DataAgent (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Represents a DataAgent.

## Implements

[protos.google.cloud.geminidataanalytics.v1.IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.idataagent)

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.geminidataanalytics.v1.IDataAgent);

Constructs a new DataAgent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.idataagent)`   
Properties to set  
  
## Properties 

### bigqueryAgentAnalyticsEnabled
    
    
    public bigqueryAgentAnalyticsEnabled?: (boolean|null);

DataAgent bigqueryAgentAnalyticsEnabled.

### bigqueryAgentAnalyticsTable
    
    
    public bigqueryAgentAnalyticsTable?: (google.cloud.geminidataanalytics.v1.IBigQueryTableReference|null);

DataAgent bigqueryAgentAnalyticsTable.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

DataAgent createTime.

### dataAnalyticsAgent
    
    
    public dataAnalyticsAgent?: (google.cloud.geminidataanalytics.v1.IDataAnalyticsAgent|null);

DataAgent dataAnalyticsAgent.

### deleteTime
    
    
    public deleteTime?: (google.protobuf.ITimestamp|null);

DataAgent deleteTime.

### description
    
    
    public description: string;

DataAgent description.

### displayName
    
    
    public displayName: string;

DataAgent displayName.

### kmsKey
    
    
    public kmsKey?: (string|null);

DataAgent kmsKey.

### labels
    
    
    public labels: { [k: string]: string };

DataAgent labels.

### name
    
    
    public name: string;

DataAgent name.

### purgeTime
    
    
    public purgeTime?: (google.protobuf.ITimestamp|null);

DataAgent purgeTime.

### type
    
    
    public type?: "dataAnalyticsAgent";

DataAgent type.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

DataAgent updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.geminidataanalytics.v1.IDataAgent): google.cloud.geminidataanalytics.v1.DataAgent;

Creates a new DataAgent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.idataagent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent)` | DataAgent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.geminidataanalytics.v1.DataAgent;

Decodes a DataAgent message from the specified reader or buffer.

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
`[DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent)` | DataAgent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.geminidataanalytics.v1.DataAgent;

Decodes a DataAgent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent)` | DataAgent  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.geminidataanalytics.v1.IDataAgent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataAgent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.idataagent)`   
DataAgent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.geminidataanalytics.v1.IDataAgent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataAgent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.idataagent)`   
DataAgent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.geminidataanalytics.v1.DataAgent;

Creates a DataAgent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent)` | DataAgent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DataAgent

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

Converts this DataAgent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.geminidataanalytics.v1.DataAgent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DataAgent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent)`   
DataAgent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DataAgent message.

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
