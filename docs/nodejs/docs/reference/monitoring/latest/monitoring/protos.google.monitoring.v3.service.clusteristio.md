---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.clusteristio
title: Class protos.google.monitoring.v3.Service.ClusterIstio (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:50.139426+00:00
---

# Class protos.google.monitoring.v3.Service.ClusterIstio (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.clusteristio

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.Service.ClusterIstio (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents a ClusterIstio.

## Implements

[protos.google.monitoring.v3.Service.IClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.iclusteristio)

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.v3.Service.IClusterIstio);

Constructs a new ClusterIstio.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.iclusteristio)`   
Properties to set  
  
## Properties 

### clusterName
    
    
    public clusterName: string;

ClusterIstio clusterName.

### location
    
    
    public location: string;

ClusterIstio location.

### serviceName
    
    
    public serviceName: string;

ClusterIstio serviceName.

### serviceNamespace
    
    
    public serviceNamespace: string;

ClusterIstio serviceNamespace.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.v3.Service.IClusterIstio): google.monitoring.v3.Service.ClusterIstio;

Creates a new ClusterIstio instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.iclusteristio)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.clusteristio)` | ClusterIstio instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.v3.Service.ClusterIstio;

Decodes a ClusterIstio message from the specified reader or buffer.

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
`[ClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.clusteristio)` | ClusterIstio  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.v3.Service.ClusterIstio;

Decodes a ClusterIstio message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.clusteristio)` | ClusterIstio  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.v3.Service.IClusterIstio, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClusterIstio message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.iclusteristio)`   
ClusterIstio message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.v3.Service.IClusterIstio, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClusterIstio message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.iclusteristio)`   
ClusterIstio message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.v3.Service.ClusterIstio;

Creates a ClusterIstio message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.clusteristio)` | ClusterIstio  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ClusterIstio

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

Converts this ClusterIstio to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.v3.Service.ClusterIstio, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ClusterIstio message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ClusterIstio](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.service.clusteristio)`   
ClusterIstio  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ClusterIstio message.

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
