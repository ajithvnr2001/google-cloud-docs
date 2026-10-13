---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataqualityrule-class
title: Class protos.google.cloud.dataplex.v1.DataQualityRule (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:39.098770+00:00
---

# Class protos.google.cloud.dataplex.v1.DataQualityRule (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataqualityrule-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.DataQualityRule (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a DataQualityRule.

## Implements

[protos.google.cloud.dataplex.v1.IDataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataqualityrule)

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataplex.v1.IDataQualityRule);

Constructs a new DataQualityRule.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataqualityrule)`   
Properties to set  
  
## Properties 

### attributes
    
    
    public attributes: { [k: string]: string };

DataQualityRule attributes.

### column
    
    
    public column: string;

DataQualityRule column.

### debugQueries
    
    
    public debugQueries: google.cloud.dataplex.v1.DataQualityRule.IDebugQuery[];

DataQualityRule debugQueries.

### description
    
    
    public description: string;

DataQualityRule description.

### dimension
    
    
    public dimension: string;

DataQualityRule dimension.

### ignoreNull
    
    
    public ignoreNull: boolean;

DataQualityRule ignoreNull.

### name
    
    
    public name: string;

DataQualityRule name.

### nonNullExpectation
    
    
    public nonNullExpectation?: (google.cloud.dataplex.v1.DataQualityRule.INonNullExpectation|null);

DataQualityRule nonNullExpectation.

### rangeExpectation
    
    
    public rangeExpectation?: (google.cloud.dataplex.v1.DataQualityRule.IRangeExpectation|null);

DataQualityRule rangeExpectation.

### regexExpectation
    
    
    public regexExpectation?: (google.cloud.dataplex.v1.DataQualityRule.IRegexExpectation|null);

DataQualityRule regexExpectation.

### rowConditionExpectation
    
    
    public rowConditionExpectation?: (google.cloud.dataplex.v1.DataQualityRule.IRowConditionExpectation|null);

DataQualityRule rowConditionExpectation.

### ruleSource
    
    
    public ruleSource?: (google.cloud.dataplex.v1.DataQualityRule.IRuleSource|null);

DataQualityRule ruleSource.

### ruleType
    
    
    public ruleType?: ("rangeExpectation"|"nonNullExpectation"|"setExpectation"|"regexExpectation"|"uniquenessExpectation"|"statisticRangeExpectation"|"rowConditionExpectation"|"tableConditionExpectation"|"sqlAssertion"|"templateReference");

DataQualityRule ruleType.

### setExpectation
    
    
    public setExpectation?: (google.cloud.dataplex.v1.DataQualityRule.ISetExpectation|null);

DataQualityRule setExpectation.

### sqlAssertion
    
    
    public sqlAssertion?: (google.cloud.dataplex.v1.DataQualityRule.ISqlAssertion|null);

DataQualityRule sqlAssertion.

### statisticRangeExpectation
    
    
    public statisticRangeExpectation?: (google.cloud.dataplex.v1.DataQualityRule.IStatisticRangeExpectation|null);

DataQualityRule statisticRangeExpectation.

### suspended
    
    
    public suspended: boolean;

DataQualityRule suspended.

### tableConditionExpectation
    
    
    public tableConditionExpectation?: (google.cloud.dataplex.v1.DataQualityRule.ITableConditionExpectation|null);

DataQualityRule tableConditionExpectation.

### templateReference
    
    
    public templateReference?: (google.cloud.dataplex.v1.DataQualityRule.ITemplateReference|null);

DataQualityRule templateReference.

### threshold
    
    
    public threshold: number;

DataQualityRule threshold.

### uniquenessExpectation
    
    
    public uniquenessExpectation?: (google.cloud.dataplex.v1.DataQualityRule.IUniquenessExpectation|null);

DataQualityRule uniquenessExpectation.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataplex.v1.IDataQualityRule): google.cloud.dataplex.v1.DataQualityRule;

Creates a new DataQualityRule instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataqualityrule)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataqualityrule-class)` | DataQualityRule instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataplex.v1.DataQualityRule;

Decodes a DataQualityRule message from the specified reader or buffer.

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
`[DataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataqualityrule-class)` | DataQualityRule  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataplex.v1.DataQualityRule;

Decodes a DataQualityRule message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataqualityrule-class)` | DataQualityRule  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataplex.v1.IDataQualityRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataQualityRule message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataqualityrule)`   
DataQualityRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataplex.v1.IDataQualityRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataQualityRule message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataqualityrule)`   
DataQualityRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataplex.v1.DataQualityRule;

Creates a DataQualityRule message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataqualityrule-class)` | DataQualityRule  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DataQualityRule

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

Converts this DataQualityRule to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataplex.v1.DataQualityRule, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DataQualityRule message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DataQualityRule](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataqualityrule-class)`   
DataQualityRule  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DataQualityRule message.

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
