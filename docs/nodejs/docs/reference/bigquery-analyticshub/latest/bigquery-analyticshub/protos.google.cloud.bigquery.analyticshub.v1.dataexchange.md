---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange
title: Class protos.google.cloud.bigquery.analyticshub.v1.DataExchange (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:07.788190+00:00
---

# Class protos.google.cloud.bigquery.analyticshub.v1.DataExchange (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.analyticshub.v1.DataExchange (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.2.0  1.6.0  1.1.0  0.2.2  0.1.2 

Represents a DataExchange.

## Implements

[protos.google.cloud.bigquery.analyticshub.v1.IDataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.idataexchange)

## Package

[@google-cloud/bigquery-analyticshub](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.bigquery.analyticshub.v1.IDataExchange);

Constructs a new DataExchange.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.idataexchange)`   
Properties to set  
  
## Properties 

### description
    
    
    public description: string;

DataExchange description.

### discoveryType
    
    
    public discoveryType?: (google.cloud.bigquery.analyticshub.v1.DiscoveryType|keyof typeof google.cloud.bigquery.analyticshub.v1.DiscoveryType|null);

DataExchange discoveryType.

### displayName
    
    
    public displayName: string;

DataExchange displayName.

### documentation
    
    
    public documentation: string;

DataExchange documentation.

### icon
    
    
    public icon: (Uint8Array|Buffer|string);

DataExchange icon.

### listingCount
    
    
    public listingCount: number;

DataExchange listingCount.

### logLinkedDatasetQueryUserEmail
    
    
    public logLinkedDatasetQueryUserEmail?: (boolean|null);

DataExchange logLinkedDatasetQueryUserEmail.

### name
    
    
    public name: string;

DataExchange name.

### primaryContact
    
    
    public primaryContact: string;

DataExchange primaryContact.

### sharingEnvironmentConfig
    
    
    public sharingEnvironmentConfig?: (google.cloud.bigquery.analyticshub.v1.ISharingEnvironmentConfig|null);

DataExchange sharingEnvironmentConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.bigquery.analyticshub.v1.IDataExchange): google.cloud.bigquery.analyticshub.v1.DataExchange;

Creates a new DataExchange instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.idataexchange)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange)` | DataExchange instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.bigquery.analyticshub.v1.DataExchange;

Decodes a DataExchange message from the specified reader or buffer.

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
`[DataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange)` | DataExchange  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.bigquery.analyticshub.v1.DataExchange;

Decodes a DataExchange message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange)` | DataExchange  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.bigquery.analyticshub.v1.IDataExchange, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataExchange message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.idataexchange)`   
DataExchange message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.bigquery.analyticshub.v1.IDataExchange, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DataExchange message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.idataexchange)`   
DataExchange message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.bigquery.analyticshub.v1.DataExchange;

Creates a DataExchange message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange)` | DataExchange  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DataExchange

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

Converts this DataExchange to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.bigquery.analyticshub.v1.DataExchange, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DataExchange message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange)`   
DataExchange  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DataExchange message.

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
