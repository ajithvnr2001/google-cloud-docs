---
url: https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.entry
title: Class protos.google.cloud.datacatalog.v1.Entry (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:26.341025+00:00
---

# Class protos.google.cloud.datacatalog.v1.Entry (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.entry

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datacatalog.v1.Entry (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  4.7.0  4.6.0  4.5.0  4.1.1  3.3.1  3.2.1  2.5.0  2.4.2  2.3.4 

Represents an Entry.

## Implements

[protos.google.cloud.datacatalog.v1.IEntry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ientry)

## Package

[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datacatalog.v1.IEntry);

Constructs a new Entry.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEntry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ientry)`   
Properties to set  
  
## Properties 

### bigqueryDateShardedSpec
    
    
    public bigqueryDateShardedSpec?: (google.cloud.datacatalog.v1.IBigQueryDateShardedSpec|null);

Entry bigqueryDateShardedSpec.

### bigqueryTableSpec
    
    
    public bigqueryTableSpec?: (google.cloud.datacatalog.v1.IBigQueryTableSpec|null);

Entry bigqueryTableSpec.

### businessContext
    
    
    public businessContext?: (google.cloud.datacatalog.v1.IBusinessContext|null);

Entry businessContext.

### cloudBigtableSystemSpec
    
    
    public cloudBigtableSystemSpec?: (google.cloud.datacatalog.v1.ICloudBigtableSystemSpec|null);

Entry cloudBigtableSystemSpec.

### databaseTableSpec
    
    
    public databaseTableSpec?: (google.cloud.datacatalog.v1.IDatabaseTableSpec|null);

Entry databaseTableSpec.

### datasetSpec
    
    
    public datasetSpec?: (google.cloud.datacatalog.v1.IDatasetSpec|null);

Entry datasetSpec.

### dataSource
    
    
    public dataSource?: (google.cloud.datacatalog.v1.IDataSource|null);

Entry dataSource.

### dataSourceConnectionSpec
    
    
    public dataSourceConnectionSpec?: (google.cloud.datacatalog.v1.IDataSourceConnectionSpec|null);

Entry dataSourceConnectionSpec.

### description
    
    
    public description: string;

Entry description.

### displayName
    
    
    public displayName: string;

Entry displayName.

### entryType
    
    
    public entryType?: ("type"|"userSpecifiedType");

Entry entryType.

### featureOnlineStoreSpec
    
    
    public featureOnlineStoreSpec?: (google.cloud.datacatalog.v1.IFeatureOnlineStoreSpec|null);

Entry featureOnlineStoreSpec.

### filesetSpec
    
    
    public filesetSpec?: (google.cloud.datacatalog.v1.IFilesetSpec|null);

Entry filesetSpec.

### fullyQualifiedName
    
    
    public fullyQualifiedName: string;

Entry fullyQualifiedName.

### gcsFilesetSpec
    
    
    public gcsFilesetSpec?: (google.cloud.datacatalog.v1.IGcsFilesetSpec|null);

Entry gcsFilesetSpec.

### integratedSystem
    
    
    public integratedSystem?: (google.cloud.datacatalog.v1.IntegratedSystem|keyof typeof google.cloud.datacatalog.v1.IntegratedSystem|null);

Entry integratedSystem.

### labels
    
    
    public labels: { [k: string]: string };

Entry labels.

### linkedResource
    
    
    public linkedResource: string;

Entry linkedResource.

### lookerSystemSpec
    
    
    public lookerSystemSpec?: (google.cloud.datacatalog.v1.ILookerSystemSpec|null);

Entry lookerSystemSpec.

### modelSpec
    
    
    public modelSpec?: (google.cloud.datacatalog.v1.IModelSpec|null);

Entry modelSpec.

### name
    
    
    public name: string;

Entry name.

### personalDetails
    
    
    public personalDetails?: (google.cloud.datacatalog.v1.IPersonalDetails|null);

Entry personalDetails.

### routineSpec
    
    
    public routineSpec?: (google.cloud.datacatalog.v1.IRoutineSpec|null);

Entry routineSpec.

### schema
    
    
    public schema?: (google.cloud.datacatalog.v1.ISchema|null);

Entry schema.

### serviceSpec
    
    
    public serviceSpec?: (google.cloud.datacatalog.v1.IServiceSpec|null);

Entry serviceSpec.

### sourceSystemTimestamps
    
    
    public sourceSystemTimestamps?: (google.cloud.datacatalog.v1.ISystemTimestamps|null);

Entry sourceSystemTimestamps.

### spec
    
    
    public spec?: ("databaseTableSpec"|"dataSourceConnectionSpec"|"routineSpec"|"datasetSpec"|"filesetSpec"|"serviceSpec"|"modelSpec"|"featureOnlineStoreSpec");

Entry spec.

### sqlDatabaseSystemSpec
    
    
    public sqlDatabaseSystemSpec?: (google.cloud.datacatalog.v1.ISqlDatabaseSystemSpec|null);

Entry sqlDatabaseSystemSpec.

### system
    
    
    public system?: ("integratedSystem"|"userSpecifiedSystem");

Entry system.

### systemSpec
    
    
    public systemSpec?: ("sqlDatabaseSystemSpec"|"lookerSystemSpec"|"cloudBigtableSystemSpec");

Entry systemSpec.

### type
    
    
    public type?: (google.cloud.datacatalog.v1.EntryType|keyof typeof google.cloud.datacatalog.v1.EntryType|null);

Entry type.

### typeSpec
    
    
    public typeSpec?: ("gcsFilesetSpec"|"bigqueryTableSpec"|"bigqueryDateShardedSpec");

Entry typeSpec.

### usageSignal
    
    
    public usageSignal?: (google.cloud.datacatalog.v1.IUsageSignal|null);

Entry usageSignal.

### userSpecifiedSystem
    
    
    public userSpecifiedSystem?: (string|null);

Entry userSpecifiedSystem.

### userSpecifiedType
    
    
    public userSpecifiedType?: (string|null);

Entry userSpecifiedType.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datacatalog.v1.IEntry): google.cloud.datacatalog.v1.Entry;

Creates a new Entry instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEntry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ientry)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.entry)` | Entry instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datacatalog.v1.Entry;

Decodes an Entry message from the specified reader or buffer.

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
`[Entry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.entry)` | Entry  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datacatalog.v1.Entry;

Decodes an Entry message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.entry)` | Entry  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datacatalog.v1.IEntry, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Entry message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEntry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ientry)`   
Entry message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datacatalog.v1.IEntry, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Entry message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEntry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ientry)`   
Entry message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datacatalog.v1.Entry;

Creates an Entry message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.entry)` | Entry  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Entry

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

Converts this Entry to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datacatalog.v1.Entry, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Entry message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Entry](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.entry)`   
Entry  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Entry message.

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
