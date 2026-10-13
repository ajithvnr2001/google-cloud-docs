---
url: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables
title: REST Resource: hive.v1.projects.catalogs.databases.tables \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:54.709023+00:00
---

# REST Resource: hive.v1.projects.catalogs.databases.tables  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/lakehouse/docs/quotas)



#  REST Resource: hive.v1.projects.catalogs.databases.tables Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: HiveTable
    * JSON representation
  * StorageDescriptor
    * JSON representation
  * FieldSchema
    * JSON representation
  * SerdeInfo
    * JSON representation
  * SerdeType
  * Order
    * JSON representation
  * SkewedInfo
    * JSON representation
  * SkewedColumnValue
    * JSON representation
  * SkewedKeyValuesLocation
    * JSON representation
  * Methods



## Resource: HiveTable

Stores the hive table information. It includes the table name, schema (column names and types), data location, storage format, serde info, etc. This message closely matches the Table object in the IMetastoreClient

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "storageDescriptor": {
        object ([StorageDescriptor](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#StorageDescriptor))
      },
      "createTime": string,
      "partitionKeys": [
        {
          object ([FieldSchema](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#FieldSchema))
        }
      ],
      "parameters": {
        string: string,
        ...
      },
      "viewOriginalText": string,
      "viewExpandedText": string,
      "tableType": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name. Format: projects/{project_id_or_number}/catalogs/{catalogId}/databases/{databaseId}/tables/{tableId}  
`description` |  `string` Optional. Description of the table. The maximum length is 4000 characters.  
`storageDescriptor` |  `object (`[StorageDescriptor](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#StorageDescriptor)`)` Required. Storage descriptor of the table.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the table.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`partitionKeys[]` |  `object (`[FieldSchema](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#FieldSchema)`)` Optional. The partition keys of the table.  
`parameters` |  `map (key: string, value: string)` Optional. Stores the properties associated with the table. The maximum size is 4MiB.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`viewOriginalText` |  `string` Optional. The original view text. Empty for non-view. The maximum size is 16MiB.  
`viewExpandedText` |  `string` Optional. The expanded view text. Empty for non-view. The maximum size is 16MiB.  
`tableType` |  `string` Output only. The type of the table. This is EXTERNAL for BigLake hive tables.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The update time of the table.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## StorageDescriptor

Contains information about the physical storage of the table data.

JSON representation  
---  
      
    
    {
      "columns": [
        {
          object ([FieldSchema](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#FieldSchema))
        }
      ],
      "locationUri": string,
      "inputFormat": string,
      "outputFormat": string,
      "serdeInfo": {
        object ([SerdeInfo](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SerdeInfo))
      },
      "bucketCols": [
        string
      ],
      "sortCols": [
        {
          object ([Order](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#Order))
        }
      ],
      "parameters": {
        string: string,
        ...
      },
      "skewedInfo": {
        object ([SkewedInfo](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SkewedInfo))
      },
      "compressed": boolean,
      "numBuckets": integer,
      "storedAsSubDirs": boolean
    }  
  
Fields  
---  
`columns[]` |  `object (`[FieldSchema](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#FieldSchema)`)` Required. Specifies the columns of the table.  
`locationUri` |  `string` Optional. The Cloud storage uri where the table is located. Defaults to `<database_location_uri>/<table_name>`. The maximum length is 4000 characters.  
`inputFormat` |  `string` Optional. The fully qualified Java class name of the input format. The maximum length is 4000 characters.  
`outputFormat` |  `string` Optional. The fully qualified Java class name of the output format. The maximum length is 4000 characters.  
`serdeInfo` |  `object (`[SerdeInfo](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SerdeInfo)`)` Optional. Serialization and deserialization information.  
`bucketCols[]` |  `string` Optional. Reducer grouping columns and clustering columns and bucketing columns  
`sortCols[]` |  `object (`[Order](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#Order)`)` Optional. Sort order of the data in each bucket  
`parameters` |  `map (key: string, value: string)` Optional. Key-value pairs for the storage descriptor. The maximum size is 10Kib.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`skewedInfo` |  `object (`[SkewedInfo](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SkewedInfo)`)` Optional. Table data skew information.  
`compressed` |  `boolean` Optional. Whether the table is compressed.  
`numBuckets` |  `integer` Optional. The number of buckets in the table.  
`storedAsSubDirs` |  `boolean` Optional. Whether the table is stored as sub directories.  
  
## FieldSchema

Field schema information.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "comment": string
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the field. The maximum length is 767 characters.  
`type` |  `string` Required. Type of the field. The maximum length is 128 characters.  
`comment` |  `string` Optional. Comment of the field. The maximum length is 256 characters.  
  
## SerdeInfo

Serialization and deserialization information.

JSON representation  
---  
      
    
    {
      "name": string,
      "serializationLib": string,
      "description": string,
      "parameters": {
        string: string,
        ...
      },
      "serializerClass": string,
      "deserializerClass": string,
      "serdeType": enum ([SerdeType](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SerdeType))
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the SerDe. Table name by default. The maximum length is 128 characters.  
`serializationLib` |  `string` Required. The fully qualified Java class name of the serialization library. The maximum length is 4000 characters.  
`description` |  `string` Optional. Description of the serde. The maximum length is 4000 characters.  
`parameters` |  `map (key: string, value: string)` Optional. Parameters of the serde. The maximum size is 10Kib.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`serializerClass` |  `string` Optional. The fully qualified Java class name of the serializer. The maximum length is 4000 characters.  
`deserializerClass` |  `string` Optional. The fully qualified Java class name of the deserializer. The maximum length is 4000 characters.  
`serdeType` |  `enum (`[SerdeType](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SerdeType)`)` Optional. The serde type.  
  
## SerdeType

The serde types.

Enums  
---  
`SERDE_TYPE_UNSPECIFIED` | The serde type is not specified.  
`HIVE` | Hive.  
`SCHEMA_REGISTRY` | Schema registry.  
  
## Order

Sort order of the stored data per column.

JSON representation  
---  
      
    
    {
      "col": string,
      "order": integer
    }  
  
Fields  
---  
`col` |  `string` Required. The column name. The maximum length is 767 characters.  
`order` |  `integer` Required. Defines the sort order of the column. Ascending if 1, descending if 0.  
  
## SkewedInfo

Stores all the information about skewed table.

JSON representation  
---  
      
    
    {
      "skewedColNames": [
        string
      ],
      "skewedColValues": [
        {
          object ([SkewedColumnValue](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SkewedColumnValue))
        }
      ],
      "skewedKeyValuesLocations": [
        {
          object ([SkewedKeyValuesLocation](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SkewedKeyValuesLocation))
        }
      ]
    }  
  
Fields  
---  
`skewedColNames[]` |  `string` Required. The column names that are skewed. The maximum length is 256 characters per column name.  
`skewedColValues[]` |  `object (`[SkewedColumnValue](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SkewedColumnValue)`)` Required. The skewed column values.  
`skewedKeyValuesLocations[]` |  `object (`[SkewedKeyValuesLocation](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables#SkewedKeyValuesLocation)`)` Required. The skewed key values locations.  
  
## SkewedColumnValue

The skewed column values.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ]
    }  
  
Fields  
---  
`values[]` |  `string` Required. The skewed column values. The maximum length is 256 characters per value.  
  
## SkewedKeyValuesLocation

The skewed key values and their corresponding location.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ],
      "location": string
    }  
  
Fields  
---  
`values[]` |  `string` Required. The skewed column values. The maximum length is 256 characters per value.  
`location` |  `string` Required. The location of the skewed column values. The maximum length is 4000 characters.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables/create)`

|  Creates a new hive table.  
  
### `[delete](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables/delete)`

|  Deletes an existing table specified by the table name.  
  
### `[get](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables/get)`

|  Gets the table specified by the resource name.  
  
### `[list](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables/list)`

|  List all hive tables in a specified project under the hive catalog and database.  
  
### `[patch](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases.tables/patch)`

|  Updates an existing table specified by the table name.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
