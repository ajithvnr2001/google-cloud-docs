---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcedescriptor
title: Class protos.google.api.MonitoredResourceDescriptor (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:15.301032+00:00
---

# Class protos.google.api.MonitoredResourceDescriptor (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcedescriptor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.MonitoredResourceDescriptor (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  4.2.0  2.9.2  2.8.0  2.6.1  2.5.1  2.4.2  2.3.4 

Represents a MonitoredResourceDescriptor.

## Implements

[protos.google.api.IMonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcedescriptor)

## Package

[@google-cloud/monitoring-dashboards](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IMonitoredResourceDescriptor);

Constructs a new MonitoredResourceDescriptor.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcedescriptor)`   
Properties to set  
  
## Properties 

### description
    
    
    public description: string;

MonitoredResourceDescriptor description.

### displayName
    
    
    public displayName: string;

MonitoredResourceDescriptor displayName.

### labels
    
    
    public labels: google.api.ILabelDescriptor[];

MonitoredResourceDescriptor labels.

### launchStage
    
    
    public launchStage: (google.api.LaunchStage|keyof typeof google.api.LaunchStage);

MonitoredResourceDescriptor launchStage.

### name
    
    
    public name: string;

MonitoredResourceDescriptor name.

### type
    
    
    public type: string;

MonitoredResourceDescriptor type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IMonitoredResourceDescriptor): google.api.MonitoredResourceDescriptor;

Creates a new MonitoredResourceDescriptor instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcedescriptor)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcedescriptor)` | MonitoredResourceDescriptor instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.MonitoredResourceDescriptor;

Decodes a MonitoredResourceDescriptor message from the specified reader or buffer.

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
`[MonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcedescriptor)` | MonitoredResourceDescriptor  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.MonitoredResourceDescriptor;

Decodes a MonitoredResourceDescriptor message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcedescriptor)` | MonitoredResourceDescriptor  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IMonitoredResourceDescriptor, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MonitoredResourceDescriptor message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcedescriptor)`   
MonitoredResourceDescriptor message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IMonitoredResourceDescriptor, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MonitoredResourceDescriptor message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.imonitoredresourcedescriptor)`   
MonitoredResourceDescriptor message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.MonitoredResourceDescriptor;

Creates a MonitoredResourceDescriptor message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcedescriptor)` | MonitoredResourceDescriptor  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MonitoredResourceDescriptor

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

Converts this MonitoredResourceDescriptor to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.MonitoredResourceDescriptor, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MonitoredResourceDescriptor message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MonitoredResourceDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.api.monitoredresourcedescriptor)`   
MonitoredResourceDescriptor  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MonitoredResourceDescriptor message.

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
