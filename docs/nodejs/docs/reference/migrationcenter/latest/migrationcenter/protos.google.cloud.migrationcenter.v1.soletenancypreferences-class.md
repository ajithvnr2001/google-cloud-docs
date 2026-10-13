---
url: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.soletenancypreferences-class
title: Class protos.google.cloud.migrationcenter.v1.SoleTenancyPreferences (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:36.212280+00:00
---

# Class protos.google.cloud.migrationcenter.v1.SoleTenancyPreferences (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.soletenancypreferences-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.migrationcenter.v1.SoleTenancyPreferences (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0 

Represents a SoleTenancyPreferences.

## Implements

[protos.google.cloud.migrationcenter.v1.ISoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.isoletenancypreferences)

## Package

[@google-cloud/migrationcenter](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.migrationcenter.v1.ISoleTenancyPreferences);

Constructs a new SoleTenancyPreferences.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.isoletenancypreferences)`   
Properties to set  
  
## Properties 

### commitmentPlan
    
    
    public commitmentPlan: (google.cloud.migrationcenter.v1.SoleTenancyPreferences.CommitmentPlan|keyof typeof google.cloud.migrationcenter.v1.SoleTenancyPreferences.CommitmentPlan);

SoleTenancyPreferences commitmentPlan.

### cpuOvercommitRatio
    
    
    public cpuOvercommitRatio: number;

SoleTenancyPreferences cpuOvercommitRatio.

### hostMaintenancePolicy
    
    
    public hostMaintenancePolicy: (google.cloud.migrationcenter.v1.SoleTenancyPreferences.HostMaintenancePolicy|keyof typeof google.cloud.migrationcenter.v1.SoleTenancyPreferences.HostMaintenancePolicy);

SoleTenancyPreferences hostMaintenancePolicy.

### nodeTypes
    
    
    public nodeTypes: google.cloud.migrationcenter.v1.ISoleTenantNodeType[];

SoleTenancyPreferences nodeTypes.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.migrationcenter.v1.ISoleTenancyPreferences): google.cloud.migrationcenter.v1.SoleTenancyPreferences;

Creates a new SoleTenancyPreferences instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.isoletenancypreferences)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.soletenancypreferences-class)` | SoleTenancyPreferences instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.migrationcenter.v1.SoleTenancyPreferences;

Decodes a SoleTenancyPreferences message from the specified reader or buffer.

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
`[SoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.soletenancypreferences-class)` | SoleTenancyPreferences  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.migrationcenter.v1.SoleTenancyPreferences;

Decodes a SoleTenancyPreferences message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.soletenancypreferences-class)` | SoleTenancyPreferences  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.migrationcenter.v1.ISoleTenancyPreferences, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SoleTenancyPreferences message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.isoletenancypreferences)`   
SoleTenancyPreferences message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.migrationcenter.v1.ISoleTenancyPreferences, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SoleTenancyPreferences message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.isoletenancypreferences)`   
SoleTenancyPreferences message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.migrationcenter.v1.SoleTenancyPreferences;

Creates a SoleTenancyPreferences message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.soletenancypreferences-class)` | SoleTenancyPreferences  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SoleTenancyPreferences

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

Converts this SoleTenancyPreferences to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.migrationcenter.v1.SoleTenancyPreferences, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SoleTenancyPreferences message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SoleTenancyPreferences](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.soletenancypreferences-class)`   
SoleTenancyPreferences  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SoleTenancyPreferences message.

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
