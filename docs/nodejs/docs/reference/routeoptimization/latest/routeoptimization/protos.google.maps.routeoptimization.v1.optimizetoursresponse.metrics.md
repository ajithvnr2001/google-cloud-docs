---
url: https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.metrics
title: Class protos.google.maps.routeoptimization.v1.OptimizeToursResponse.Metrics (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:20.563632+00:00
---

# Class protos.google.maps.routeoptimization.v1.OptimizeToursResponse.Metrics (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.metrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.routeoptimization.v1.OptimizeToursResponse.Metrics (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.3.0  0.2.0  0.1.0 

Represents a Metrics.

## Implements

[protos.google.maps.routeoptimization.v1.OptimizeToursResponse.IMetrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.imetrics)

## Package

[@googlemaps/routeoptimization](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.routeoptimization.v1.OptimizeToursResponse.IMetrics);

Constructs a new Metrics.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMetrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.imetrics)`   
Properties to set  
  
## Properties 

### aggregatedRouteMetrics
    
    
    public aggregatedRouteMetrics?: (google.maps.routeoptimization.v1.IAggregatedMetrics|null);

Metrics aggregatedRouteMetrics.

### costs
    
    
    public costs: { [k: string]: number };

Metrics costs.

### earliestVehicleStartTime
    
    
    public earliestVehicleStartTime?: (google.protobuf.ITimestamp|null);

Metrics earliestVehicleStartTime.

### latestVehicleEndTime
    
    
    public latestVehicleEndTime?: (google.protobuf.ITimestamp|null);

Metrics latestVehicleEndTime.

### skippedMandatoryShipmentCount
    
    
    public skippedMandatoryShipmentCount: number;

Metrics skippedMandatoryShipmentCount.

### totalCost
    
    
    public totalCost: number;

Metrics totalCost.

### usedVehicleCount
    
    
    public usedVehicleCount: number;

Metrics usedVehicleCount.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.routeoptimization.v1.OptimizeToursResponse.IMetrics): google.maps.routeoptimization.v1.OptimizeToursResponse.Metrics;

Creates a new Metrics instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMetrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.imetrics)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Metrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.metrics)` | Metrics instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.routeoptimization.v1.OptimizeToursResponse.Metrics;

Decodes a Metrics message from the specified reader or buffer.

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
`[Metrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.metrics)` | Metrics  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.routeoptimization.v1.OptimizeToursResponse.Metrics;

Decodes a Metrics message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Metrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.metrics)` | Metrics  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.routeoptimization.v1.OptimizeToursResponse.IMetrics, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Metrics message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMetrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.imetrics)`   
Metrics message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.routeoptimization.v1.OptimizeToursResponse.IMetrics, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Metrics message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMetrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.imetrics)`   
Metrics message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.routeoptimization.v1.OptimizeToursResponse.Metrics;

Creates a Metrics message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Metrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.metrics)` | Metrics  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Metrics

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

Converts this Metrics to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.routeoptimization.v1.OptimizeToursResponse.Metrics, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Metrics message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Metrics](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursresponse.metrics)`   
Metrics  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Metrics message.

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
