---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanjob-class
title: Class protos.google.cloud.dataplex.v1.DataScanJob (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:41.220365+00:00
---

# Class protos.google.cloud.dataplex.v1.DataScanJob (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanjob-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.DataScanJob (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a DataScanJob.

## Implements

[protos.google.cloud.dataplex.v1.IDataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idatascanjob)

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataplex.v1.IDataScanJob);

Constructs a new DataScanJob.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idatascanjob)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

DataScanJob createTime.

### dataDiscoveryResult
    
    
    public dataDiscoveryResult?: (google.cloud.dataplex.v1.IDataDiscoveryResult|null);

DataScanJob dataDiscoveryResult.

### dataDiscoverySpec
    
    
    public dataDiscoverySpec?: (google.cloud.dataplex.v1.IDataDiscoverySpec|null);

DataScanJob dataDiscoverySpec.

### dataDocumentationResult
    
    
    public dataDocumentationResult?: (google.cloud.dataplex.v1.IDataDocumentationResult|null);

DataScanJob dataDocumentationResult.

### dataDocumentationSpec
    
    
    public dataDocumentationSpec?: (google.cloud.dataplex.v1.IDataDocumentationSpec|null);

DataScanJob dataDocumentationSpec.

### dataProfileResult
    
    
    public dataProfileResult?: (google.cloud.dataplex.v1.IDataProfileResult|null);

DataScanJob dataProfileResult.

### dataProfileSpec
    
    
    public dataProfileSpec?: (google.cloud.dataplex.v1.IDataProfileSpec|null);

DataScanJob dataProfileSpec.

### dataQualityResult
    
    
    public dataQualityResult?: (google.cloud.dataplex.v1.IDataQualityResult|null);

DataScanJob dataQualityResult.

### dataQualitySpec
    
    
    public dataQualitySpec?: (google.cloud.dataplex.v1.IDataQualitySpec|null);

DataScanJob dataQualitySpec.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

DataScanJob endTime.

### message
    
    
    public message: string;

DataScanJob message.

### name
    
    
    public name: string;

DataScanJob name.

### partialFailureMessage
    
    
    public partialFailureMessage: string;

DataScanJob partialFailureMessage.

### result
    
    
    public result?: ("dataQualityResult"|"dataProfileResult"|"dataDiscoveryResult"|"dataDocumentationResult");

DataScanJob result.

### spec
    
    
    public spec?: ("dataQualitySpec"|"dataProfileSpec"|"dataDiscoverySpec"|"dataDocumentationSpec");

DataScanJob spec.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

DataScanJob startTime.

### state
    
    
    public state: (google.cloud.dataplex.v1.DataScanJob.State|keyof typeof google.cloud.dataplex.v1.DataScanJob.State);

DataScanJob state.

### type
    
    
    public type: (google.cloud.dataplex.v1.DataScanType|keyof typeof google.cloud.dataplex.v1.DataScanType);

DataScanJob type.

### uid
    
    
    public uid: string;

DataScanJob uid.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataplex.v1.IDataScanJob): google.cloud.dataplex.v1.DataScanJob;

Creates a new DataScanJob instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idatascanjob)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanjob-class)` | DataScanJob instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataplex.v1.DataScanJob;

Decodes a DataScanJob message from the specified reader or buffer.

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
`[DataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanjob-class)` | DataScanJob  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataplex.v1.DataScanJob;

Decodes a DataScanJob message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanjob-class)` | DataScanJob  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataplex.v1.IDataScanJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataScanJob message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idatascanjob)`   
DataScanJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataplex.v1.IDataScanJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataScanJob message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idatascanjob)`   
DataScanJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataplex.v1.DataScanJob;

Creates a DataScanJob message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanjob-class)` | DataScanJob  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DataScanJob

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

Converts this DataScanJob to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataplex.v1.DataScanJob, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DataScanJob message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DataScanJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.datascanjob-class)`   
DataScanJob  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DataScanJob message.

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
