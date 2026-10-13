---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcemetadata
title: Class protos.google.api.MonitoredResourceMetadata (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:02.434398+00:00
---

# Class protos.google.api.MonitoredResourceMetadata (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcemetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.MonitoredResourceMetadata (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  4.2.0  2.9.2  2.8.0  2.6.1  2.5.1  2.4.2  2.3.4 

Represents a MonitoredResourceMetadata.

## Implements

[protos.google.api.IMonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcemetadata)

## Package

[@google-cloud/monitoring-dashboards](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IMonitoredResourceMetadata);

Constructs a new MonitoredResourceMetadata.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcemetadata)`   
Properties to set  
  
## Properties 

### systemLabels
    
    
    public systemLabels?: (google.protobuf.IStruct|null);

MonitoredResourceMetadata systemLabels.

### userLabels
    
    
    public userLabels: { [k: string]: string };

MonitoredResourceMetadata userLabels.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IMonitoredResourceMetadata): google.api.MonitoredResourceMetadata;

Creates a new MonitoredResourceMetadata instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcemetadata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcemetadata)` | MonitoredResourceMetadata instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.MonitoredResourceMetadata;

Decodes a MonitoredResourceMetadata message from the specified reader or buffer.

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
`[MonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcemetadata)` | MonitoredResourceMetadata  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.MonitoredResourceMetadata;

Decodes a MonitoredResourceMetadata message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcemetadata)` | MonitoredResourceMetadata  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IMonitoredResourceMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MonitoredResourceMetadata message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcemetadata)`   
MonitoredResourceMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IMonitoredResourceMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MonitoredResourceMetadata message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcemetadata)`   
MonitoredResourceMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.MonitoredResourceMetadata;

Creates a MonitoredResourceMetadata message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcemetadata)` | MonitoredResourceMetadata  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MonitoredResourceMetadata

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

Converts this MonitoredResourceMetadata to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.MonitoredResourceMetadata, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MonitoredResourceMetadata message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MonitoredResourceMetadata](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcemetadata)`   
MonitoredResourceMetadata  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MonitoredResourceMetadata message.

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
