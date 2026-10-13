---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.condition-class
title: Class protos.google.monitoring.v3.AlertPolicy.Condition (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:49.856671+00:00
---

# Class protos.google.monitoring.v3.AlertPolicy.Condition (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.condition-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.AlertPolicy.Condition (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents a Condition.

## Implements

[protos.google.monitoring.v3.AlertPolicy.ICondition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.icondition)

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.v3.AlertPolicy.ICondition);

Constructs a new Condition.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICondition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.icondition)`   
Properties to set  
  
## Properties 

### condition
    
    
    public condition?: ("conditionThreshold"|"conditionAbsent"|"conditionMatchedLog"|"conditionMonitoringQueryLanguage"|"conditionPrometheusQueryLanguage"|"conditionSql");

Condition condition.

### conditionAbsent
    
    
    public conditionAbsent?: (google.monitoring.v3.AlertPolicy.Condition.IMetricAbsence|null);

Condition conditionAbsent.

### conditionMatchedLog
    
    
    public conditionMatchedLog?: (google.monitoring.v3.AlertPolicy.Condition.ILogMatch|null);

Condition conditionMatchedLog.

### conditionMonitoringQueryLanguage
    
    
    public conditionMonitoringQueryLanguage?: (google.monitoring.v3.AlertPolicy.Condition.IMonitoringQueryLanguageCondition|null);

Condition conditionMonitoringQueryLanguage.

### conditionPrometheusQueryLanguage
    
    
    public conditionPrometheusQueryLanguage?: (google.monitoring.v3.AlertPolicy.Condition.IPrometheusQueryLanguageCondition|null);

Condition conditionPrometheusQueryLanguage.

### conditionSql
    
    
    public conditionSql?: (google.monitoring.v3.AlertPolicy.Condition.ISqlCondition|null);

Condition conditionSql.

### conditionThreshold
    
    
    public conditionThreshold?: (google.monitoring.v3.AlertPolicy.Condition.IMetricThreshold|null);

Condition conditionThreshold.

### displayName
    
    
    public displayName: string;

Condition displayName.

### name
    
    
    public name: string;

Condition name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.v3.AlertPolicy.ICondition): google.monitoring.v3.AlertPolicy.Condition;

Creates a new Condition instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICondition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.icondition)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Condition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.condition-class)` | Condition instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.v3.AlertPolicy.Condition;

Decodes a Condition message from the specified reader or buffer.

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
`[Condition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.condition-class)` | Condition  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.v3.AlertPolicy.Condition;

Decodes a Condition message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Condition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.condition-class)` | Condition  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.v3.AlertPolicy.ICondition, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Condition message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICondition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.icondition)`   
Condition message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.v3.AlertPolicy.ICondition, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Condition message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICondition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.icondition)`   
Condition message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.v3.AlertPolicy.Condition;

Creates a Condition message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Condition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.condition-class)` | Condition  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Condition

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

Converts this Condition to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.v3.AlertPolicy.Condition, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Condition message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Condition](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.condition-class)`   
Condition  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Condition message.

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
