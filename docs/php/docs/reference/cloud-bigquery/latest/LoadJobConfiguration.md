---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration/
title: BigQuery Client - Class LoadJobConfiguration (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:48.286239+00:00
---

# BigQuery Client - Class LoadJobConfiguration (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class LoadJobConfiguration (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class LoadJobConfiguration.

Represents a configuration for a load job. For more information on the available settings please see the [Jobs configuration API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job).

Example:
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    $bigQuery = new BigQueryClient();
    $table = $bigQuery->dataset('my_dataset')
        ->table('my_table');
    $loadJobConfig = $table->load(fopen('/path/to/my/data.csv', 'r'));
    

## Namespace

Google \ Cloud \ BigQuery

## Implements

[JobConfigurationInterface](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/JobConfigurationInterface)

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`projectId` |  `string`   
The project's ID.  
`config` |  `array`   
A set of configuration options for a job.  
`location` |  `string|null`   
The geographic location in which the job is executed.  
  
### allowJaggedRows

Sets whether to accept rows that are missing trailing optional columns.

The missing values are treated as nulls. If false, records with missing trailing columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. Only applicable to CSV, ignored for other formats.

Example:
    
    
    $loadJobConfig->allowJaggedRows(true);
    

**Parameter**  
---  
**Name** | **Description**  
`allowJaggedRows` |  `bool`   
Whether or not to allow jagged rows. _Defaults to_ * `false`.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### allowQuotedNewlines

Sets whether quoted data sections that contain newline characters in a CSV file are allowed.

Example:
    
    
    $loadJobConfig->allowQuotedNewlines(true);
    

**Parameter**  
---  
**Name** | **Description**  
`allowQuotedNewlines` |  `bool`   
Whether or not to allow quoted new lines. **Defaults to** `false`.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### autodetect

Sets whether we should automatically infer the options and schema for CSV and JSON sources.

Example:
    
    
    $loadJobConfig->autodetect(true);
    

**Parameter**  
---  
**Name** | **Description**  
`autodetect` |  `bool`   
Whether or not to autodetect options and schema.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### clustering

See also:

  * [Introduction to Clustered Tables](https://cloud.google.com/bigquery/docs/clustered-tables)



**Parameter**  
---  
**Name** | **Description**  
`clustering` |  `array`   
Clustering specification for the table.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### createDisposition

Set whether the job is allowed to create new tables. Creation, truncation and append actions occur as one atomic update upon job completion.

Example:
    
    
    $loadJobConfig->createDisposition('CREATE_NEVER');
    

**Parameter**  
---  
**Name** | **Description**  
`createDisposition` |  `string`   
The create disposition. Acceptable values include `"CREATED_IF_NEEDED"`, `"CREATE_NEVER"`. **Defaults to** `"CREATE_IF_NEEDED"`.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### destinationEncryptionConfiguration

Sets the custom encryption configuration (e.g., Cloud KMS keys).

Example:
    
    
    $loadJobConfig->destinationEncryptionConfiguration([
        'kmsKeyName' => 'my_key'
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`configuration` |  `array`   
Custom encryption configuration.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### data

The data to be loaded into the table.

Example:
    
    
    $loadJobConfig->data(fopen('/path/to/my/data.csv', 'r'));
    

**Parameter**  
---  
**Name** | **Description**  
`data` |  `string|resource|Psr\Http\Message\StreamInterface`   
The data to be loaded into the table.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### destinationTable

Sets the destination table to load the data into.

Example:
    
    
    $table = $bigQuery->dataset('my_dataset')
        ->table('my_table');
    $loadJobConfig->destinationTable($table);
    

**Parameter**  
---  
**Name** | **Description**  
`destinationTable` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table)`   
The destination table.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### encoding

Sets the character encoding of the data. BigQuery decodes the data after the raw, binary data has been split using the values of the quote and fieldDelimiter properties.

Example:
    
    
    $loadJobConfig->encoding('UTF-8');
    

**Parameter**  
---  
**Name** | **Description**  
`encoding` |  `string`   
The encoding type. Acceptable values include `"UTF-8"`, `"ISO-8859-1"`. **Defaults to** `"UTF-8"`.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### fieldDelimiter

Sets the separator for fields in a CSV file. The separator can be any ISO-8859-1 single-byte character. To use a character in the range 128-255, you must encode the character as UTF8. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. BigQuery also supports the escape sequence "\t" to specify a tab separator.

Example:
    
    
    $loadJobConfig->fieldDelimiter('\t');
    

**Parameter**  
---  
**Name** | **Description**  
`fieldDelimiter` |  `string`   
The field delimiter. **Defaults to** `","`.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### ignoreUnknownValues

Sets whether values that are not represented in the table schema should be allowed. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result.

The sourceFormat property determines what BigQuery treats as an extra value:

  * CSV: Trailing columns.
  * JSON: Named values that don't match any column names.



Example:
    
    
    $loadJobConfig->ignoreUnknownValues(true);
    

**Parameter**  
---  
**Name** | **Description**  
`ignoreUnknownValues` |  `bool`   
Whether or not to ignore unknown values. _Defaults to_ * `false`.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### maxBadRecords

Sets the maximum number of bad records that BigQuery can ignore when running the job. If the number of bad records exceeds this value, an invalid error is returned in the job result.

Example:
    
    
    $loadJobConfig->maxBadRecords(10);
    

**Parameter**  
---  
**Name** | **Description**  
`maxBadRecords` |  `int`   
The maximum number of bad records. _Defaults to_ * `0` (requires all records to be valid).  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### nullMarker

Sets a string that represents a null value in a CSV file. For example, if you specify "\N", BigQuery interprets "\N" as a null value when loading a CSV file. The default value is the empty string. If you set this property to a custom value, BigQuery throws an error if an empty string is present for all data types except for STRING and BYTE. For STRING and BYTE columns, BigQuery interprets the empty string as an empty value.

Example:
    
    
    $loadJobConfig->nullMarker('\N');
    

**Parameter**  
---  
**Name** | **Description**  
`nullMarker` |  `string`   
The null marker.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### projectionFields

Sets a list of projection fields. If sourceFormat is set to "DATASTORE_BACKUP", indicates which entity properties to load into BigQuery from a Cloud Datastore backup. Property names are case sensitive and must be top-level properties. If no properties are specified, BigQuery loads all properties. If any named property isn't found in the Cloud Datastore backup, an invalid error is returned in the job result.

Example:
    
    
    $loadJobConfig->projectionFields([
        'field_name'
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`projectionFields` |  `array`   
The projection fields.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### quote

Sets the value that is used to quote data sections in a CSV file.

BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true.

Example:
    
    
    $loadJobConfig->quote('"');
    

**Parameter**  
---  
**Name** | **Description**  
`quote` |  `string`   
The quote value. **Defaults to** `"""` (double quotes).  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### schema

Sets the schema for the destination table. The schema can be omitted if the destination table already exists, or if you're loading data from Google Cloud Datastore.

Example:
    
    
    $loadJobConfig->schema([
        'fields' => [
            [
                'name' => 'col1',
                'type' => 'STRING',
            ],
            [
                'name' => 'col2',
                'type' => 'BOOL',
            ]
        ]
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`schema` |  `array`   
The table schema.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### schemaUpdateOptions

Sets options to allow the schema of the destination table to be updated as a side effect of the query job. Schema update options are supported in two cases: when writeDisposition is `"WRITE_APPEND"`; when writeDisposition is `"WRITE_TRUNCATE"` and the destination table is a partition of a table, specified by partition decorators. For normal tables, `"WRITE_TRUNCATE"` will always overwrite the schema.

Example:
    
    
    $loadJobConfig->schemaUpdateOptions([
        'ALLOW_FIELD_ADDITION'
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`schemaUpdateOptions` |  `array`   
Schema update options. Acceptable values include `"ALLOW_FIELD_ADDITION"` (allow adding a nullable field to the schema), `"ALLOW_FIELD_RELAXATION"` (allow relaxing a required field in the original schema to nullable).  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### skipLeadingRows

Sets the number of rows at the top of a CSV file that BigQuery will skip when loading the data. This property is useful if you have header rows in the file that should be skipped.

Example:
    
    
    $loadJobConfig->skipLeadingRows(10);
    

**Parameter**  
---  
**Name** | **Description**  
`skipLeadingRows` |  `int`   
The number of rows to skip. _Defaults to_ * `0`.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### sourceFormat

Sets the format of the data files.

Example:
    
    
    $loadJobConfig->sourceFormat('NEWLINE_DELIMITED_JSON');
    

**Parameter**  
---  
**Name** | **Description**  
`sourceFormat` |  `string`   
The source format. Acceptable values include `"CSV"`, `"DATASTORE_BACKUP"`, `"NEWLINE_DELIMITED_JSON"`, `"AVRO"`, `"PARQUET"`, `"ORC"`. **Defaults to** `"CSV"`.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### sourceUris

Sets the fully-qualified URIs that point to your data in Google Cloud.

  * For Google Cloud Storage URIs: Each URI can contain one '*' wildcard character and it must come after the 'bucket' name.
  * For Google Cloud Bigtable URIs: Exactly one URI can be specified and it has be a fully specified and valid HTTPS URL for a Google Cloud Bigtable table.
  * For Google Cloud Datastore backups: Exactly one URI can be specified. Also, the '*' wildcard character is not allowed.



Example:
    
    
    $loadJobConfig->sourceUris([
        'gs://my_bucket/source.csv'
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`sourceUris` |  `array`   
The source URIs.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### timePartitioning

Sets time-based partitioning for the destination table.

Only one of timePartitioning and rangePartitioning should be specified.

Example:
    
    
    $loadJobConfig->timePartitioning([
        'type' => 'DAY'
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`timePartitioning` |  `array`   
Time-based partitioning configuration.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### rangePartitioning

Sets range partitioning specification for the destination table.

Only one of timePartitioning and rangePartitioning should be specified.

Example:
    
    
    $loadJobConfig->rangePartitioning([
        'field' => 'myInt',
        'range' => [
            'start' => '0',
            'end' => '1000',
            'interval' => '100'
        ]
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`rangePartitioning` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### writeDisposition

Sets the action that occurs if the destination table already exists. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion.

Example:
    
    
    $loadJobConfig->writeDisposition('WRITE_TRUNCATE');
    

**Parameter**  
---  
**Name** | **Description**  
`writeDisposition` |  `string`   
The write disposition. Acceptable values include `"WRITE_TRUNCATE"`, `"WRITE_APPEND"`, `"WRITE_EMPTY"`. _Defaults to_ * `"WRITE_APPEND"`.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### useAvroLogicalTypes

Sets whether to use logical types when loading from AVRO format.

If sourceFormat is set to "AVRO", indicates whether to enable interpreting logical types into their corresponding types (ie. TIMESTAMP), instead of only using their raw types (ie. INTEGER).

Example:
    
    
    $loadJobConfig->useAvroLogicalTypes(true);
    

**Parameter**  
---  
**Name** | **Description**  
`useAvroLogicalTypes` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### hivePartitioningOptions

See also:

  * [HivePartitoningOptions](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#HivePartitioningOptions)



**Parameter**  
---  
**Name** | **Description**  
`hivePartitioningOptions` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### createSession

Decide whether to create a new session with a random id.

The created session id is returned as part of the SessionInfo within the query statistics.

Example:
    
    
    $loadJobConfig->createSession(true);
    

**Parameter**  
---  
**Name** | **Description**  
`createSession` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### connectionProperties

Sets connection properties for the load job.

Example:
    
    
    $loadJobConfig->connectionProperties([
        'key' => 'session_id',
        'value' => 'sessionId'
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`connectionProperties` |  `array`   
  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### referenceFileSchemaUri

Sets the reference for external table schema.

It is enabled for AVRO, PARQUET and ORC format.

Example:
    
    
    $loadJobConfig->referenceFileSchemaUri('gs://bucket/source.parquet');
    

**Parameter**  
---  
**Name** | **Description**  
`referenceFileSchemaUri` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### columnNameCharacterMap

Character map supported for column names in CSV/Parquet loads.

Defaults to STRICT and can be overridden by Project Config Service. Using this option with unsupporting load formats will result in an error.

Example:
    
    
    $loadJobConfig->columnNameCharacterMap('V2');
    

**Parameter**  
---  
**Name** | **Description**  
`columnNameCharacterMap` |  `string`   
The column name character map. Acceptable values include "COLUMN_NAME_CHARACTER_MAP_UNSPECIFIED", "STRICT", "V1", "V2".  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### copyFilesOnly

[Experimental] Configures the load job to copy files directly to the destination BigLake managed table, bypassing file content reading and rewriting. Copying files only is supported when all the following are true:

  * `source_uris` are located in the same Cloud Storage location as the destination table's `storage_uri` location.

  * `source_format` is `PARQUET`.

  * `destination_table` is an existing BigLake managed table. The table's schema does not have flexible column names. The table's columns do not have type parameters other than precision and scale.
  * No options other than the above are specified.



Example:
    
    
    $loadJobConfig->copyFilesOnly(true);
    

**Parameter**  
---  
**Name** | **Description**  
`copyFilesOnly` |  `bool`   
Whether to copy files only.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### dateFormat

Date format used for parsing DATE values.

Example:
    
    
    $loadJobConfig->dateFormat('YYYY-MM-DD');
    

**Parameter**  
---  
**Name** | **Description**  
`dateFormat` |  `string`   
The date format string.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### datetimeFormat

Date format used for parsing DATETIME values.

Example:
    
    
    $loadJobConfig->datetimeFormat('YYYY-MM-DD HH24:MI:SS');
    

**Parameter**  
---  
**Name** | **Description**  
`datetimeFormat` |  `string`   
The datetime format string.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### decimalTargetTypes

Defines the list of possible SQL data types to which the source decimal values are converted. This list and the precision and the scale parameters of the decimal field determine the target type. In the order of NUMERIC, BIGNUMERIC, and STRING, a type is picked if it is in the specified list and if it supports the precision and the scale. STRING supports all precision and scale values. If none of the listed types supports the precision and the scale, the type supporting the widest range in the specified list is picked, and if a value exceeds the supported range when reading the data, an error will be thrown. Example: Suppose the value of this field is ["NUMERIC", "BIGNUMERIC"]. If (precision,scale) is:

  * (38,9) -> NUMERIC;
  * (39,9) -> BIGNUMERIC (NUMERIC cannot hold 30 integer digits);
  * (38,10) -> BIGNUMERIC (NUMERIC cannot hold 10 fractional digits);
  * (76,38) -> BIGNUMERIC;
  * (77,38) -> BIGNUMERIC (error if value exceeds supported range).



This field cannot contain duplicate types. The order of the types in this field is ignored. For example, ["BIGNUMERIC", "NUMERIC"] is the same as ["NUMERIC", "BIGNUMERIC"] and NUMERIC always takes precedence over BIGNUMERIC. Defaults to ["NUMERIC", "STRING"] for ORC and ["NUMERIC"] for the other file formats.

Example:
    
    
    $loadJobConfig->decimalTargetTypes(['NUMERIC', 'BIGNUMERIC']);
    

**Parameter**  
---  
**Name** | **Description**  
`decimalTargetTypes` |  `string[]`   
An array of target decimal types. Acceptable values include "DECIMAL_TARGET_TYPE_UNSPECIFIED", "NUMERIC", "BIGNUMERIC", "STRING".  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### destinationTableProperties

See also:

  * [DestinationTableProperties](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#destinationtableproperties)



**Parameter**  
---  
**Name** | **Description**  
`destinationTableProperties` |  `array`   
Properties for the destination table.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### fileSetSpecType

Specifies how source URIs are interpreted for constructing the file set to load. By default, source URIs are expanded against the underlying storage. You can also specify manifest files to control how the file set is constructed. This option is only applicable to object storage systems.

Example:
    
    
    $loadJobConfig->fileSetSpecType('FILE_SET_SPEC_TYPE_NEW_LINE_DELIMITED_MANIFEST');
    

**Parameter**  
---  
**Name** | **Description**  
`fileSetSpecType` |  `string`   
The file set specification type. Acceptable values include "FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH", "FILE_SET_SPEC_TYPE_NEW_LINE_DELIMITED_MANIFEST".  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### jsonExtension

Load option to be used together with source_format newline-delimited JSON to indicate that a variant of JSON is being loaded.

To load newline-delimited GeoJSON, specify GEOJSON (and source_format must be set to NEWLINE_DELIMITED_JSON).

Example:
    
    
    $loadJobConfig->jsonExtension('GEOJSON');
    

**Parameter**  
---  
**Name** | **Description**  
`jsonExtension` |  `string`   
The JSON extension type. Acceptable values include "JSON_EXTENSION_UNSPECIFIED", "GEOJSON".  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### nullMarkers

A list of strings represented as SQL NULL value in a CSV file.

null_marker and null_markers can't be set at the same time. If null_marker is set, null_markers has to be not set. If null_markers is set, null_marker has to be not set. If both null_marker and null_markers are set at the same time, a user error would be thrown. Any strings listed in null_markers, including empty string would be interpreted as SQL NULL. This applies to all column types.

Example:
    
    
    $loadJobConfig->nullMarkers(['\\N', 'NULL']);
    

**Parameter**  
---  
**Name** | **Description**  
`nullMarkers` |  `string[]`   
An array of strings to be interpreted as NULL.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### parquetOptions

See also:

  * [ParquetOptions](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#ParquetOptions)



Example: `$loadJobConfig->parquetOptions([ 'enumAsString' => true ]);`

**Parameter**  
---  
**Name** | **Description**  
`parquetOptions` |  `array`   
Additional Parquet options.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### preserveAsciiControlCharacters

When sourceFormat is set to "CSV", this indicates whether the embedded ASCII control characters (the first 32 characters in the ASCII-table, from '\x00' to '\x1F') are preserved.

Example:
    
    
    $loadJobConfig->preserveAsciiControlCharacters(true);
    

**Parameter**  
---  
**Name** | **Description**  
`preserveAsciiControlCharacters` |  `bool`   
Whether to preserve ASCII control characters.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### sourceColumnMatch

Controls the strategy used to match loaded columns to the schema.

If not set, a sensible default is chosen based on how the schema is provided. If autodetect is used, then columns are matched by name. Otherwise, columns are matched by position. This is done to keep the behavior backward-compatible.

Example:
    
    
    $loadJobConfig->sourceColumnMatch('NAME');
    

**Parameter**  
---  
**Name** | **Description**  
`sourceColumnMatch` |  `string`   
The column match strategy. Acceptable values include "SOURCE_COLUMN_MATCH_UNSPECIFIED", "POSITION", "NAME".  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### timeFormat

Date format used for parsing TIME values.

Example:
    
    
    $loadJobConfig->timeFormat('HH24:MI:SS');
    

**Parameter**  
---  
**Name** | **Description**  
`timeFormat` |  `string`   
The time format string.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### timeZone

Default time zone that will apply when parsing timestamp values that have no specific time zone.

Example:
    
    
    $loadJobConfig->timeZone('America/Los_Angeles');
    

**Parameter**  
---  
**Name** | **Description**  
`timeZone` |  `string`   
The default time zone string.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### timestampFormat

Date format used for parsing TIMESTAMP values.

Example:
    
    
    $loadJobConfig->timestampFormat('YYYY-MM-DD HH24:MI:SS.FF3 TZH');
    

**Parameter**  
---  
**Name** | **Description**  
`timestampFormat` |  `string`   
The timestamp format string.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
