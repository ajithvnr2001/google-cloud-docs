---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.activitylevelrollupbyactivityleveltype
title: Class protos.google.devicesandservices.health.v4.ActivityLevelRollupValue.ActivityLevelRollupByActivityLevelType (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:05.152327+00:00
---

# Class protos.google.devicesandservices.health.v4.ActivityLevelRollupValue.ActivityLevelRollupByActivityLevelType (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.activitylevelrollupbyactivityleveltype

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.ActivityLevelRollupValue.ActivityLevelRollupByActivityLevelType (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an ActivityLevelRollupByActivityLevelType.

## Implements

[protos.google.devicesandservices.health.v4.ActivityLevelRollupValue.IActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.iactivitylevelrollupbyactivityleveltype)

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devicesandservices.health.v4.ActivityLevelRollupValue.IActivityLevelRollupByActivityLevelType);

Constructs a new ActivityLevelRollupByActivityLevelType.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.iactivitylevelrollupbyactivityleveltype)`   
Properties to set  
  
## Properties 

### activityLevelType
    
    
    public activityLevelType: (google.devicesandservices.health.v4.ActivityLevel.ActivityLevelType|keyof typeof google.devicesandservices.health.v4.ActivityLevel.ActivityLevelType);

ActivityLevelRollupByActivityLevelType activityLevelType.

### totalDuration
    
    
    public totalDuration?: (google.protobuf.IDuration|null);

ActivityLevelRollupByActivityLevelType totalDuration.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devicesandservices.health.v4.ActivityLevelRollupValue.IActivityLevelRollupByActivityLevelType): google.devicesandservices.health.v4.ActivityLevelRollupValue.ActivityLevelRollupByActivityLevelType;

Creates a new ActivityLevelRollupByActivityLevelType instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.iactivitylevelrollupbyactivityleveltype)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.activitylevelrollupbyactivityleveltype)` | ActivityLevelRollupByActivityLevelType instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devicesandservices.health.v4.ActivityLevelRollupValue.ActivityLevelRollupByActivityLevelType;

Decodes an ActivityLevelRollupByActivityLevelType message from the specified reader or buffer.

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
`[ActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.activitylevelrollupbyactivityleveltype)` | ActivityLevelRollupByActivityLevelType  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devicesandservices.health.v4.ActivityLevelRollupValue.ActivityLevelRollupByActivityLevelType;

Decodes an ActivityLevelRollupByActivityLevelType message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.activitylevelrollupbyactivityleveltype)` | ActivityLevelRollupByActivityLevelType  
  
### encode(message, writer)
    
    
    public static encode(message: google.devicesandservices.health.v4.ActivityLevelRollupValue.IActivityLevelRollupByActivityLevelType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ActivityLevelRollupByActivityLevelType message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.iactivitylevelrollupbyactivityleveltype)`   
ActivityLevelRollupByActivityLevelType message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devicesandservices.health.v4.ActivityLevelRollupValue.IActivityLevelRollupByActivityLevelType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ActivityLevelRollupByActivityLevelType message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.iactivitylevelrollupbyactivityleveltype)`   
ActivityLevelRollupByActivityLevelType message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devicesandservices.health.v4.ActivityLevelRollupValue.ActivityLevelRollupByActivityLevelType;

Creates an ActivityLevelRollupByActivityLevelType message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.activitylevelrollupbyactivityleveltype)` | ActivityLevelRollupByActivityLevelType  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ActivityLevelRollupByActivityLevelType

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

Converts this ActivityLevelRollupByActivityLevelType to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devicesandservices.health.v4.ActivityLevelRollupValue.ActivityLevelRollupByActivityLevelType, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ActivityLevelRollupByActivityLevelType message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ActivityLevelRollupByActivityLevelType](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.activitylevelrollupvalue.activitylevelrollupbyactivityleveltype)`   
ActivityLevelRollupByActivityLevelType  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ActivityLevelRollupByActivityLevelType message.

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
