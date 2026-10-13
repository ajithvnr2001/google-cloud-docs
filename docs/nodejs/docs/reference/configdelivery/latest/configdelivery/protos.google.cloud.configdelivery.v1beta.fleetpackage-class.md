---
url: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackage-class
title: Class protos.google.cloud.configdelivery.v1beta.FleetPackage (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:47.388822+00:00
---

# Class protos.google.cloud.configdelivery.v1beta.FleetPackage (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackage-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.configdelivery.v1beta.FleetPackage (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a FleetPackage.

## Implements

[protos.google.cloud.configdelivery.v1beta.IFleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackage)

## Package

[@google-cloud/configdelivery](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.configdelivery.v1beta.IFleetPackage);

Constructs a new FleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackage)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

FleetPackage createTime.

### deletionPropagationPolicy
    
    
    public deletionPropagationPolicy: (google.cloud.configdelivery.v1beta.DeletionPropagationPolicy|keyof typeof google.cloud.configdelivery.v1beta.DeletionPropagationPolicy);

FleetPackage deletionPropagationPolicy.

### info
    
    
    public info?: (google.cloud.configdelivery.v1beta.IFleetPackageInfo|null);

FleetPackage info.

### labels
    
    
    public labels: { [k: string]: string };

FleetPackage labels.

### name
    
    
    public name: string;

FleetPackage name.

### resourceBundleSelector
    
    
    public resourceBundleSelector?: (google.cloud.configdelivery.v1beta.FleetPackage.IResourceBundleSelector|null);

FleetPackage resourceBundleSelector.

### rolloutStrategy
    
    
    public rolloutStrategy?: (google.cloud.configdelivery.v1beta.IRolloutStrategy|null);

FleetPackage rolloutStrategy.

### state
    
    
    public state: (google.cloud.configdelivery.v1beta.FleetPackage.State|keyof typeof google.cloud.configdelivery.v1beta.FleetPackage.State);

FleetPackage state.

### target
    
    
    public target?: (google.cloud.configdelivery.v1beta.FleetPackage.ITarget|null);

FleetPackage target.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

FleetPackage updateTime.

### variantSelector
    
    
    public variantSelector?: (google.cloud.configdelivery.v1beta.FleetPackage.IVariantSelector|null);

FleetPackage variantSelector.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.configdelivery.v1beta.IFleetPackage): google.cloud.configdelivery.v1beta.FleetPackage;

Creates a new FleetPackage instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackage)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackage-class)` | FleetPackage instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.configdelivery.v1beta.FleetPackage;

Decodes a FleetPackage message from the specified reader or buffer.

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
`[FleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackage-class)` | FleetPackage  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.configdelivery.v1beta.FleetPackage;

Decodes a FleetPackage message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackage-class)` | FleetPackage  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.configdelivery.v1beta.IFleetPackage, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FleetPackage message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackage)`   
FleetPackage message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.configdelivery.v1beta.IFleetPackage, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FleetPackage message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackage)`   
FleetPackage message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.configdelivery.v1beta.FleetPackage;

Creates a FleetPackage message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackage-class)` | FleetPackage  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FleetPackage

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

Converts this FleetPackage to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.configdelivery.v1beta.FleetPackage, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FleetPackage message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FleetPackage](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackage-class)`   
FleetPackage  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FleetPackage message.

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
