---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.action-class
title: Class protos.google.cloud.dataplex.v1.Action (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:18.802055+00:00
---

# Class protos.google.cloud.dataplex.v1.Action (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.action-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.Action (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents an Action.

## Implements

[protos.google.cloud.dataplex.v1.IAction](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaction)

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataplex.v1.IAction);

Constructs a new Action.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAction](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaction)`   
Properties to set  
  
## Properties 

### asset
    
    
    public asset: string;

Action asset.

### category
    
    
    public category: (google.cloud.dataplex.v1.Action.Category|keyof typeof google.cloud.dataplex.v1.Action.Category);

Action category.

### dataLocations
    
    
    public dataLocations: string[];

Action dataLocations.

### details
    
    
    public details?: ("invalidDataFormat"|"incompatibleDataSchema"|"invalidDataPartition"|"missingData"|"missingResource"|"unauthorizedResource"|"failedSecurityPolicyApply"|"invalidDataOrganization");

Action details.

### detectTime
    
    
    public detectTime?: (google.protobuf.ITimestamp|null);

Action detectTime.

### failedSecurityPolicyApply
    
    
    public failedSecurityPolicyApply?: (google.cloud.dataplex.v1.Action.IFailedSecurityPolicyApply|null);

Action failedSecurityPolicyApply.

### incompatibleDataSchema
    
    
    public incompatibleDataSchema?: (google.cloud.dataplex.v1.Action.IIncompatibleDataSchema|null);

Action incompatibleDataSchema.

### invalidDataFormat
    
    
    public invalidDataFormat?: (google.cloud.dataplex.v1.Action.IInvalidDataFormat|null);

Action invalidDataFormat.

### invalidDataOrganization
    
    
    public invalidDataOrganization?: (google.cloud.dataplex.v1.Action.IInvalidDataOrganization|null);

Action invalidDataOrganization.

### invalidDataPartition
    
    
    public invalidDataPartition?: (google.cloud.dataplex.v1.Action.IInvalidDataPartition|null);

Action invalidDataPartition.

### issue
    
    
    public issue: string;

Action issue.

### lake
    
    
    public lake: string;

Action lake.

### missingData
    
    
    public missingData?: (google.cloud.dataplex.v1.Action.IMissingData|null);

Action missingData.

### missingResource
    
    
    public missingResource?: (google.cloud.dataplex.v1.Action.IMissingResource|null);

Action missingResource.

### name
    
    
    public name: string;

Action name.

### unauthorizedResource
    
    
    public unauthorizedResource?: (google.cloud.dataplex.v1.Action.IUnauthorizedResource|null);

Action unauthorizedResource.

### zone
    
    
    public zone: string;

Action zone.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataplex.v1.IAction): google.cloud.dataplex.v1.Action;

Creates a new Action instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAction](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaction)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Action](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.action-class)` | Action instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataplex.v1.Action;

Decodes an Action message from the specified reader or buffer.

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
`[Action](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.action-class)` | Action  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataplex.v1.Action;

Decodes an Action message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Action](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.action-class)` | Action  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataplex.v1.IAction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Action message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAction](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaction)`   
Action message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataplex.v1.IAction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Action message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAction](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iaction)`   
Action message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataplex.v1.Action;

Creates an Action message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Action](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.action-class)` | Action  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Action

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

Converts this Action to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataplex.v1.Action, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Action message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Action](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.action-class)`   
Action  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Action message.

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
