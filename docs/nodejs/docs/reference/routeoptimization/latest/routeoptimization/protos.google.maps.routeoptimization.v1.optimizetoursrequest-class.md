---
url: https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursrequest-class
title: Class protos.google.maps.routeoptimization.v1.OptimizeToursRequest (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:20.700289+00:00
---

# Class protos.google.maps.routeoptimization.v1.OptimizeToursRequest (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursrequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.routeoptimization.v1.OptimizeToursRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.3.0  0.2.0  0.1.0 

Represents an OptimizeToursRequest.

## Implements

[protos.google.maps.routeoptimization.v1.IOptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.ioptimizetoursrequest)

## Package

[@googlemaps/routeoptimization](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.routeoptimization.v1.IOptimizeToursRequest);

Constructs a new OptimizeToursRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.ioptimizetoursrequest)`   
Properties to set  
  
## Properties 

### allowLargeDeadlineDespiteInterruptionRisk
    
    
    public allowLargeDeadlineDespiteInterruptionRisk: boolean;

OptimizeToursRequest allowLargeDeadlineDespiteInterruptionRisk.

### considerRoadTraffic
    
    
    public considerRoadTraffic: boolean;

OptimizeToursRequest considerRoadTraffic.

### geodesicMetersPerSecond
    
    
    public geodesicMetersPerSecond?: (number|null);

OptimizeToursRequest geodesicMetersPerSecond.

### injectedFirstSolutionRoutes
    
    
    public injectedFirstSolutionRoutes: google.maps.routeoptimization.v1.IShipmentRoute[];

OptimizeToursRequest injectedFirstSolutionRoutes.

### injectedSolutionConstraint
    
    
    public injectedSolutionConstraint?: (google.maps.routeoptimization.v1.IInjectedSolutionConstraint|null);

OptimizeToursRequest injectedSolutionConstraint.

### interpretInjectedSolutionsUsingLabels
    
    
    public interpretInjectedSolutionsUsingLabels: boolean;

OptimizeToursRequest interpretInjectedSolutionsUsingLabels.

### label
    
    
    public label: string;

OptimizeToursRequest label.

### maxValidationErrors
    
    
    public maxValidationErrors?: (number|null);

OptimizeToursRequest maxValidationErrors.

### model
    
    
    public model?: (google.maps.routeoptimization.v1.IShipmentModel|null);

OptimizeToursRequest model.

### parent
    
    
    public parent: string;

OptimizeToursRequest parent.

### populatePolylines
    
    
    public populatePolylines: boolean;

OptimizeToursRequest populatePolylines.

### populateTransitionPolylines
    
    
    public populateTransitionPolylines: boolean;

OptimizeToursRequest populateTransitionPolylines.

### refreshDetailsRoutes
    
    
    public refreshDetailsRoutes: google.maps.routeoptimization.v1.IShipmentRoute[];

OptimizeToursRequest refreshDetailsRoutes.

### searchMode
    
    
    public searchMode: (google.maps.routeoptimization.v1.OptimizeToursRequest.SearchMode|keyof typeof google.maps.routeoptimization.v1.OptimizeToursRequest.SearchMode);

OptimizeToursRequest searchMode.

### solvingMode
    
    
    public solvingMode: (google.maps.routeoptimization.v1.OptimizeToursRequest.SolvingMode|keyof typeof google.maps.routeoptimization.v1.OptimizeToursRequest.SolvingMode);

OptimizeToursRequest solvingMode.

### timeout
    
    
    public timeout?: (google.protobuf.IDuration|null);

OptimizeToursRequest timeout.

### useGeodesicDistances
    
    
    public useGeodesicDistances: boolean;

OptimizeToursRequest useGeodesicDistances.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.routeoptimization.v1.IOptimizeToursRequest): google.maps.routeoptimization.v1.OptimizeToursRequest;

Creates a new OptimizeToursRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.ioptimizetoursrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursrequest-class)` | OptimizeToursRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.routeoptimization.v1.OptimizeToursRequest;

Decodes an OptimizeToursRequest message from the specified reader or buffer.

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
`[OptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursrequest-class)` | OptimizeToursRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.routeoptimization.v1.OptimizeToursRequest;

Decodes an OptimizeToursRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursrequest-class)` | OptimizeToursRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.routeoptimization.v1.IOptimizeToursRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OptimizeToursRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.ioptimizetoursrequest)`   
OptimizeToursRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.routeoptimization.v1.IOptimizeToursRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OptimizeToursRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.ioptimizetoursrequest)`   
OptimizeToursRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.routeoptimization.v1.OptimizeToursRequest;

Creates an OptimizeToursRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursrequest-class)` | OptimizeToursRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OptimizeToursRequest

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

Converts this OptimizeToursRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.routeoptimization.v1.OptimizeToursRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OptimizeToursRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OptimizeToursRequest](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursrequest-class)`   
OptimizeToursRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OptimizeToursRequest message.

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
