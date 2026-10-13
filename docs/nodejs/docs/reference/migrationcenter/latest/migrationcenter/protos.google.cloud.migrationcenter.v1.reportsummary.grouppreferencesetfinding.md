---
url: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.grouppreferencesetfinding
title: Class protos.google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFinding (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:27:56.072093+00:00
---

# Class protos.google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFinding (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.grouppreferencesetfinding

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFinding (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0 

Represents a GroupPreferenceSetFinding.

## Implements

[protos.google.cloud.migrationcenter.v1.ReportSummary.IGroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.igrouppreferencesetfinding)

## Package

[@google-cloud/migrationcenter](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.migrationcenter.v1.ReportSummary.IGroupPreferenceSetFinding);

Constructs a new GroupPreferenceSetFinding.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.igrouppreferencesetfinding)`   
Properties to set  
  
## Properties 

### computeEngineFinding
    
    
    public computeEngineFinding?: (google.cloud.migrationcenter.v1.ReportSummary.IComputeEngineFinding|null);

GroupPreferenceSetFinding computeEngineFinding.

### description
    
    
    public description: string;

GroupPreferenceSetFinding description.

### displayName
    
    
    public displayName: string;

GroupPreferenceSetFinding displayName.

### machinePreferences
    
    
    public machinePreferences?: (google.cloud.migrationcenter.v1.IVirtualMachinePreferences|null);

GroupPreferenceSetFinding machinePreferences.

### monthlyCostCompute
    
    
    public monthlyCostCompute?: (google.type.IMoney|null);

GroupPreferenceSetFinding monthlyCostCompute.

### monthlyCostNetworkEgress
    
    
    public monthlyCostNetworkEgress?: (google.type.IMoney|null);

GroupPreferenceSetFinding monthlyCostNetworkEgress.

### monthlyCostOsLicense
    
    
    public monthlyCostOsLicense?: (google.type.IMoney|null);

GroupPreferenceSetFinding monthlyCostOsLicense.

### monthlyCostOther
    
    
    public monthlyCostOther?: (google.type.IMoney|null);

GroupPreferenceSetFinding monthlyCostOther.

### monthlyCostStorage
    
    
    public monthlyCostStorage?: (google.type.IMoney|null);

GroupPreferenceSetFinding monthlyCostStorage.

### monthlyCostTotal
    
    
    public monthlyCostTotal?: (google.type.IMoney|null);

GroupPreferenceSetFinding monthlyCostTotal.

### soleTenantFinding
    
    
    public soleTenantFinding?: (google.cloud.migrationcenter.v1.ReportSummary.ISoleTenantFinding|null);

GroupPreferenceSetFinding soleTenantFinding.

### vmwareEngineFinding
    
    
    public vmwareEngineFinding?: (google.cloud.migrationcenter.v1.ReportSummary.IVmwareEngineFinding|null);

GroupPreferenceSetFinding vmwareEngineFinding.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.migrationcenter.v1.ReportSummary.IGroupPreferenceSetFinding): google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFinding;

Creates a new GroupPreferenceSetFinding instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.igrouppreferencesetfinding)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.grouppreferencesetfinding)` | GroupPreferenceSetFinding instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFinding;

Decodes a GroupPreferenceSetFinding message from the specified reader or buffer.

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
`[GroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.grouppreferencesetfinding)` | GroupPreferenceSetFinding  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFinding;

Decodes a GroupPreferenceSetFinding message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.grouppreferencesetfinding)` | GroupPreferenceSetFinding  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.migrationcenter.v1.ReportSummary.IGroupPreferenceSetFinding, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GroupPreferenceSetFinding message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.igrouppreferencesetfinding)`   
GroupPreferenceSetFinding message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.migrationcenter.v1.ReportSummary.IGroupPreferenceSetFinding, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GroupPreferenceSetFinding message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.igrouppreferencesetfinding)`   
GroupPreferenceSetFinding message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFinding;

Creates a GroupPreferenceSetFinding message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.grouppreferencesetfinding)` | GroupPreferenceSetFinding  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GroupPreferenceSetFinding

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

Converts this GroupPreferenceSetFinding to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.migrationcenter.v1.ReportSummary.GroupPreferenceSetFinding, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GroupPreferenceSetFinding message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GroupPreferenceSetFinding](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.reportsummary.grouppreferencesetfinding)`   
GroupPreferenceSetFinding  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GroupPreferenceSetFinding message.

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
