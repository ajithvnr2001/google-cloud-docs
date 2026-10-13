---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.discoveredapiobservation-class
title: Class protos.google.cloud.apihub.v1.DiscoveredApiObservation (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:54.600229+00:00
---

# Class protos.google.cloud.apihub.v1.DiscoveredApiObservation (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.discoveredapiobservation-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.DiscoveredApiObservation (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DiscoveredApiObservation.

## Implements

[protos.google.cloud.apihub.v1.IDiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.idiscoveredapiobservation)

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apihub.v1.IDiscoveredApiObservation);

Constructs a new DiscoveredApiObservation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.idiscoveredapiobservation)`   
Properties to set  
  
## Properties 

### apiOperationCount
    
    
    public apiOperationCount: (number|Long|string);

DiscoveredApiObservation apiOperationCount.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

DiscoveredApiObservation createTime.

### hostname
    
    
    public hostname: string;

DiscoveredApiObservation hostname.

### knownOperationsCount
    
    
    public knownOperationsCount: (number|Long|string);

DiscoveredApiObservation knownOperationsCount.

### lastEventDetectedTime
    
    
    public lastEventDetectedTime?: (google.protobuf.ITimestamp|null);

DiscoveredApiObservation lastEventDetectedTime.

### name
    
    
    public name: string;

DiscoveredApiObservation name.

### origin
    
    
    public origin: string;

DiscoveredApiObservation origin.

### serverIps
    
    
    public serverIps: string[];

DiscoveredApiObservation serverIps.

### sourceLocations
    
    
    public sourceLocations: string[];

DiscoveredApiObservation sourceLocations.

### sourceMetadata
    
    
    public sourceMetadata?: (google.cloud.apihub.v1.ISourceMetadata|null);

DiscoveredApiObservation sourceMetadata.

### sourceTypes
    
    
    public sourceTypes: google.cloud.apihub.v1.DiscoveredApiObservation.SourceType[];

DiscoveredApiObservation sourceTypes.

### style
    
    
    public style: (google.cloud.apihub.v1.DiscoveredApiObservation.Style|keyof typeof google.cloud.apihub.v1.DiscoveredApiObservation.Style);

DiscoveredApiObservation style.

### unknownOperationsCount
    
    
    public unknownOperationsCount: (number|Long|string);

DiscoveredApiObservation unknownOperationsCount.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

DiscoveredApiObservation updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apihub.v1.IDiscoveredApiObservation): google.cloud.apihub.v1.DiscoveredApiObservation;

Creates a new DiscoveredApiObservation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.idiscoveredapiobservation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.discoveredapiobservation-class)` | DiscoveredApiObservation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apihub.v1.DiscoveredApiObservation;

Decodes a DiscoveredApiObservation message from the specified reader or buffer.

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
`[DiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.discoveredapiobservation-class)` | DiscoveredApiObservation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apihub.v1.DiscoveredApiObservation;

Decodes a DiscoveredApiObservation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.discoveredapiobservation-class)` | DiscoveredApiObservation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apihub.v1.IDiscoveredApiObservation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DiscoveredApiObservation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.idiscoveredapiobservation)`   
DiscoveredApiObservation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apihub.v1.IDiscoveredApiObservation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DiscoveredApiObservation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.idiscoveredapiobservation)`   
DiscoveredApiObservation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apihub.v1.DiscoveredApiObservation;

Creates a DiscoveredApiObservation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.discoveredapiobservation-class)` | DiscoveredApiObservation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DiscoveredApiObservation

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

Converts this DiscoveredApiObservation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apihub.v1.DiscoveredApiObservation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DiscoveredApiObservation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DiscoveredApiObservation](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.discoveredapiobservation-class)`   
DiscoveredApiObservation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DiscoveredApiObservation message.

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
