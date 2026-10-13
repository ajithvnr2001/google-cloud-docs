---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table/
title: BigQuery Client - Class Table (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:48.774360+00:00
---

# BigQuery Client - Class Table (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class Table (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class Table.

[Tables](https://cloud.google.com/bigquery/docs/tables) are a standard two-dimensional table with individual records organized in rows, and a data type assigned to each column (also called a field).

## Namespace

Google \ Cloud \ BigQuery

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `Connection\ConnectionInterface`   
Represents a connection to BigQuery. This object is created by BigQueryClient, and should not be instantiated outside of this client.  
`id` |  `string`   
The table's id.  
`datasetId` |  `string`   
The dataset's id.  
`projectId` |  `string`   
The project's id.  
`mapper` |  `[ValueMapper](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ValueMapper)`   
Maps values between PHP and BigQuery.  
`info` |  `array`   
[optional] The table's metadata.  
`location` |  `string|null`   
[optional] A default geographic location, used when no table metadata exists.  
  
### exists

Check whether or not the table exists.

Example:
    
    
    if ($table->exists()) {
        echo 'Table exists!';
    }
    

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### delete

See also:

  * [Tables delete API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/delete)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
  
### update

See also:

  * [Tables patch API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/patch)
  * [Patch (Partial Update)](https://cloud.google.com/bigquery/docs/api-performance#patch)



**Parameters**  
---  
**Name** | **Description**  
`metadata` |  `array`   
The available options for metadata are outlined at the [Table Resource API docs](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables)  
`options` |  `array`   
[optional] Configuration options.  
  
### rows

See also:

  * [Tabledata list API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/list)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ maxResults` |  `int`   
Maximum number of results to return per page.  
`↳ resultLimit` |  `int`   
Limit the number of results returned in total. **Defaults to** `0` (return all results).  
`↳ pageToken` |  `string`   
A previously-returned page token used to resume the loading of results from a specific point.  
`↳ startIndex` |  `int`   
Zero-based index of the starting row.  
`↳ formatOptions.useInt64Timestamp` |  `boolean`   
Optional. Output timestamp as usec int64. Default is true.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iterator\ItemIterator](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iterator.ItemIterator.html)<array>` |   
  
### runJob

See also:

  * [Jobs insert API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert)



**Parameters**  
---  
**Name** | **Description**  
`config` |  `[JobConfigurationInterface](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/JobConfigurationInterface)`   
The job configuration.  
`options` |  `array`   
Configuration options.  
`↳ maxRetries` |  `int`   
The number of times to retry, checking if the job has completed. **Defaults to** `100`.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job)` |   
  
### startJob

See also:

  * [Jobs insert API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert)



**Parameters**  
---  
**Name** | **Description**  
`config` |  `[JobConfigurationInterface](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/JobConfigurationInterface)`   
The job configuration.  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job)` |   
  
### copy

See also:

  * [Jobs insert API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert)



**Parameters**  
---  
**Name** | **Description**  
`destination` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table)`   
The destination table.  
`options` |  `array`   
Configuration options.  
`↳ configuration` |  `array`   
Job configuration. Please see the [API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfiguration) for the available options. | **Properties**  
---  
**Name** | **Description**  
`copy` | `array`  
Copy job configuration. Please see the [documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationtablecopy) for the available options.  
**Returns**  
---  
**Type** | **Description**  
`[CopyJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/CopyJobConfiguration)` |   
  
### extract

See also:

  * [Jobs insert API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert)



**Parameters**  
---  
**Name** | **Description**  
`destination` |  `string|Google\Cloud\Storage\StorageObject`   
The destination object. May be a Google\Cloud\Storage\StorageObject or a URI pointing to a Google Cloud Storage object in the format of `gs://{bucket-name}/{object-name}`.  
`options` |  `array`   
Configuration options.  
`↳ configuration` |  `array`   
Job configuration. Please see the [API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfiguration) for the available options. | **Properties**  
---  
**Name** | **Description**  
`extract` | `array`  
Extract job configuration. Please see the [documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationextract) for the available options.  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
### load

See also:

  * [Jobs insert API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert)



**Parameters**  
---  
**Name** | **Description**  
`data` |  `string|resource|Psr\Http\Message\StreamInterface`   
The data to load.  
`options` |  `array`   
Configuration options.  
`↳ configuration` |  `array`   
Job configuration. Please see the [API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfiguration) for the available options. | **Properties**  
---  
**Name** | **Description**  
`load` | `array`  
Load job configuration. Please see the [documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationload) for the available options.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### loadFromStorage

See also:

  * [Jobs insert API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert)



**Parameters**  
---  
**Name** | **Description**  
`object` |  `string|Google\Cloud\Storage\StorageObject`   
The object to load data from. May be a Google\Cloud\Storage\StorageObject or a URI pointing to a Google Cloud Storage object in the format of `gs://{bucket-name}/{object-name}`.  
`options` |  `array`   
Configuration options.  
`↳ configuration` |  `array`   
Job configuration. Please see the [API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfiguration) for the available options. | **Properties**  
---  
**Name** | **Description**  
`load` | `array`  
Load job configuration. Please see the [documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationload) for the available options.  
**Returns**  
---  
**Type** | **Description**  
`[LoadJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/LoadJobConfiguration)` |   
  
### insertRow

See also:

  * [Tabledata insertAll API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/insertAll)
  * [Streaming data into BigQuery.](https://cloud.google.com/bigquery/streaming-data-into-bigquery)



**Parameters**  
---  
**Name** | **Description**  
`row` |  `array`   
Key/value set of data matching the table's schema.  
`options` |  `array`   
Please see [Table::insertRows()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table#_Google_Cloud_BigQuery_Table__insertRows__) for the other available configuration options.  
`↳ insertId` |  `string`   
Used to [ensure data consistency](https://cloud.google.com/bigquery/streaming-data-into-bigquery#dataconsistency).  
**Returns**  
---  
**Type** | **Description**  
`[InsertResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/InsertResponse)` |   
  
### insertRows

See also:

  * [Tabledata insertAll API Documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/insertAll)
  * [Streaming data into BigQuery.](https://cloud.google.com/bigquery/streaming-data-into-bigquery)



**Parameters**  
---  
**Name** | **Description**  
`rows` |  `array`   
The rows to insert. Each item in the array must contain a `data` key which is to hold a key/value array with data matching the schema of the table. Optionally, one may also provide an `insertId` key which will be used to [ensure data consistency](https://cloud.google.com/bigquery/streaming-data-into-bigquery#dataconsistency).  
`options` |  `array`   
Configuration options.  
`↳ autoCreate` |  `bool`   
Whether or not to attempt to automatically create the table in the case it does not exist. Please note, it will be required to provide a schema through $tableMetadata['schema'] in the case the table does not already exist. **Defaults to** `false`.  
`↳ tableMetadata` |  `array`   
Metadata to apply to table to be created. The full set of metadata are outlined at the [Table Resource API docs](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables). Only applies when `autoCreate` is `true`.  
`↳ maxRetries` |  `int`   
The maximum number of times to attempt creating the table in the case of failure. Please note, each retry attempt may take up to two minutes. Only applies when `autoCreate` is `true`. **Defaults to** `100`.  
`↳ skipInvalidRows` |  `bool`   
Insert all valid rows of a request, even if invalid rows exist. The default value is `false`, which causes the entire request to fail if any invalid rows exist. **Defaults to** `false`.  
`↳ ignoreUnknownValues` |  `bool`   
Accept rows that contain values that do not match the schema. The unknown values are ignored. The default value is `false`, which treats unknown values as errors. **Defaults to** `false`.  
`↳ templateSuffix` |  `string`   
If specified, treats the destination table as a base template, and inserts the rows into an instance table named "{destination}{templateSuffix}". BigQuery will manage creation of the instance table, using the schema of the base template table. See [Creating tables automatically using template tables](https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables) for considerations when working with templates tables.  
**Returns**  
---  
**Type** | **Description**  
`[InsertResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/InsertResponse)` |   
  
### info

See also:

  * [Tables resource documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ selectedFields` |  `string`   
List of table schema fields to return (comma-separated). If unspecified, all fields are returned.  
`↳ view` |  `string`   
Specifies the view that determines which table information is returned. Acceptable values are defined in [TableMetadataView](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/TableMetadataView). By default, basic table information and storage statistics (STORAGE_STATS) are returned. **Note:** If metadata is already cached, $options will be ignored. Use [Table::reload()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table#_Google_Cloud_BigQuery_Table__reload__) to force a refresh with specific options. More information: <https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/get#query-parameters>  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### reload

See also:

  * [Tables get API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/get)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ selectedFields` |  `string`   
List of table schema fields to return (comma-separated). If unspecified, all fields are returned.  
`↳ view` |  `string`   
Specifies the view that determines which table information is returned. Acceptable values are defined in [TableMetadataView](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/TableMetadataView). By default, basic table information and storage statistics (STORAGE_STATS) are returned. More information: <https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/get#query-parameters>  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### id

Retrieves the table's ID.

Example:
    
    
    echo $table->id();
    

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### identity

Retrieves the table's identity.

An identity provides a description of a nested resource.

Example:
    
    
    echo $table->identity()['projectId'];
    

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### iam

See also:

  * [BigQuery Table Access Control Documentation](https://cloud.google.com/bigquery/docs/table-access-controls-intro)
  * [Get Table IAM Policy](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/getIamPolicy)
  * [Set Table IAM Policy](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/setIamPolicy)
  * [Test Table Permissions](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/testIamPermissions)



**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iam\Iam](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iam.Iam.html)` |   
  
## Constants 

### MAX_RETRIES
    
    
    Value: 100

### INSERT_CREATE_MAX_DELAY_MICROSECONDS
    
    
    Value: 60000000

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
