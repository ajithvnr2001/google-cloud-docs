---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.datasource-class
title: Class protos.google.cloud.bigquery.datatransfer.v1.DataSource (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:41.886814+00:00
---

# Class protos.google.cloud.bigquery.datatransfer.v1.DataSource (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.datasource-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.datatransfer.v1.DataSource (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.2  4.4.0  4.2.1  3.2.2  3.1.5  2.3.0  2.2.7 

Represents a DataSource.

## Implements

[protos.google.cloud.bigquery.datatransfer.v1.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.idatasource)

## Package

[@google-cloud/bigquery-data-transfer](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.bigquery.datatransfer.v1.IDataSource);

Constructs a new DataSource.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.idatasource)`   
Properties to set  
  
## Properties 

### authorizationType
    
    
    public authorizationType: (google.cloud.bigquery.datatransfer.v1.DataSource.AuthorizationType|keyof typeof google.cloud.bigquery.datatransfer.v1.DataSource.AuthorizationType);

DataSource authorizationType.

### clientId
    
    
    public clientId: string;

DataSource clientId.

### dataRefreshType
    
    
    public dataRefreshType: (google.cloud.bigquery.datatransfer.v1.DataSource.DataRefreshType|keyof typeof google.cloud.bigquery.datatransfer.v1.DataSource.DataRefreshType);

DataSource dataRefreshType.

### dataSourceId
    
    
    public dataSourceId: string;

DataSource dataSourceId.

### defaultDataRefreshWindowDays
    
    
    public defaultDataRefreshWindowDays: number;

DataSource defaultDataRefreshWindowDays.

### defaultSchedule
    
    
    public defaultSchedule: string;

DataSource defaultSchedule.

### description
    
    
    public description: string;

DataSource description.

### displayName
    
    
    public displayName: string;

DataSource displayName.

### helpUrl
    
    
    public helpUrl: string;

DataSource helpUrl.

### manualRunsDisabled
    
    
    public manualRunsDisabled: boolean;

DataSource manualRunsDisabled.

### minimumScheduleInterval
    
    
    public minimumScheduleInterval?: (google.protobuf.IDuration|null);

DataSource minimumScheduleInterval.

### name
    
    
    public name: string;

DataSource name.

### parameters
    
    
    public parameters: google.cloud.bigquery.datatransfer.v1.IDataSourceParameter[];

DataSource parameters.

### scopes
    
    
    public scopes: string[];

DataSource scopes.

### supportsCustomSchedule
    
    
    public supportsCustomSchedule: boolean;

DataSource supportsCustomSchedule.

### supportsMultipleTransfers
    
    
    public supportsMultipleTransfers: boolean;

DataSource supportsMultipleTransfers.

### transferType
    
    
    public transferType: (google.cloud.bigquery.datatransfer.v1.TransferType|keyof typeof google.cloud.bigquery.datatransfer.v1.TransferType);

DataSource transferType.

### updateDeadlineSeconds
    
    
    public updateDeadlineSeconds: number;

DataSource updateDeadlineSeconds.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.bigquery.datatransfer.v1.IDataSource): google.cloud.bigquery.datatransfer.v1.DataSource;

Creates a new DataSource instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.idatasource)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.datasource-class)` | DataSource instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.bigquery.datatransfer.v1.DataSource;

Decodes a DataSource message from the specified reader or buffer.

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
`[DataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.datasource-class)` | DataSource  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.bigquery.datatransfer.v1.DataSource;

Decodes a DataSource message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.datasource-class)` | DataSource  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.bigquery.datatransfer.v1.IDataSource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataSource message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.idatasource)`   
DataSource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.bigquery.datatransfer.v1.IDataSource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataSource message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.idatasource)`   
DataSource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.bigquery.datatransfer.v1.DataSource;

Creates a DataSource message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.datasource-class)` | DataSource  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DataSource

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

Converts this DataSource to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.bigquery.datatransfer.v1.DataSource, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DataSource message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DataSource](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-transfer/latest/bigquery-data-transfer/protos.google.cloud.bigquery.datatransfer.v1.datasource-class)`   
DataSource  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DataSource message.

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
