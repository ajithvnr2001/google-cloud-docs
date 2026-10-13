---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration/
title: BigQuery Client - Class QueryJobConfiguration (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:48.459865+00:00
---

# BigQuery Client - Class QueryJobConfiguration (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class QueryJobConfiguration (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class QueryJobConfiguration.

Represents a configuration for a query job. For more information on the available settings please see the [Jobs configuration API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job).

Example:
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    $bigQuery = new BigQueryClient();
    $query = $bigQuery->query('SELECT commit FROM `bigquery-public-data.github_repos.commits` LIMIT 100');
    

## Namespace

Google \ Cloud \ BigQuery

## Implements

[JobConfigurationInterface](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/JobConfigurationInterface)

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`mapper` |  `[ValueMapper](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ValueMapper)`   
Maps values between PHP and BigQuery.  
`projectId` |  `string`   
The project's ID.  
`config` |  `array`   
A set of configuration options for a job.  
`location` |  `string|null`   
The geographic location in which the job is executed.  
  
### allowLargeResults

Sets whether or not the query can produce arbitrarily large result tables at a slight cost in performance.

Only applies to queries performed with legacy SQL dialect and requires a [QueryJobConfiguration::destinationTable()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration#_Google_Cloud_BigQuery_QueryJobConfiguration__destinationTable__) to be set.

Example:
    
    
    $query->allowLargeResults(true);
    

**Parameter**  
---  
**Name** | **Description**  
`allowLargeResults` |  `bool`   
Whether or not to allow large result sets.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
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
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### createDisposition

Sets whether the job is allowed to create new tables.

Example:
    
    
    $query->createDisposition('CREATE_NEVER');
    

**Parameter**  
---  
**Name** | **Description**  
`createDisposition` |  `string`   
The create disposition. Acceptable values include `"CREATE_IF_NEEDED"`, `"CREATE_NEVER"`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### defaultDataset

Sets the default dataset to use for unqualified table names in the query.

Example:
    
    
    $dataset = $bigQuery->dataset('my_dataset');
    $query->defaultDataset($dataset);
    

**Parameter**  
---  
**Name** | **Description**  
`defaultDataset` |  `[Dataset](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Dataset)`   
The default dataset.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### destinationEncryptionConfiguration

Sets the custom encryption configuration (e.g., Cloud KMS keys).

Example:
    
    
    $query->destinationEncryptionConfiguration([
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
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### destinationTable

Sets the table where the query results should be stored. If not set, a new table will be created to store the results. This property must be set for large results that exceed the maximum response size.

Example:
    
    
    $table = $bigQuery->dataset('my_dataset')
        ->table('my_table');
    $query->destinationTable($table);
    

**Parameter**  
---  
**Name** | **Description**  
`destinationTable` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table)`   
The destination table.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### flattenResults

Sets whether or not to flatten all nested and repeated fields in the query results.

Only applies to queries performed with legacy SQL dialect. [QueryJobConfiguration::allowLargeResults()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration#_Google_Cloud_BigQuery_QueryJobConfiguration__allowLargeResults__) must be true if this is set to false.

Example:
    
    
    $query->useLegacySql(true)
        ->flattenResults(true);
    

**Parameter**  
---  
**Name** | **Description**  
`flattenResults` |  `bool`   
Whether or not to flatten results.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### maximumBillingTier

Sets the billing tier limit for this job. Queries that have resource usage beyond this tier will fail (without incurring a charge). If unspecified, this will be set to your project default.

Example:
    
    
    $query->maximumBillingTier(1);
    

**Parameter**  
---  
**Name** | **Description**  
`maximumBillingTier` |  `int`   
The maximum billing tier.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### maximumBytesBilled

Sets a bytes billed limit for this job. Queries that will have bytes billed beyond this limit will fail (without incurring a charge). If unspecified, this will be set to your project default.

Example:
    
    
    $query->maximumBytesBilled(3000);
    

**Parameter**  
---  
**Name** | **Description**  
`maximumBytesBilled` |  `int`   
The maximum allowable bytes to bill.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### parameters

Sets parameters to be used on the query. Only available for standard SQL queries.

For examples of usage please see [BigQueryClient::runQuery()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient#_Google_Cloud_BigQuery_BigQueryClient__runQuery__).

**Parameter**  
---  
**Name** | **Description**  
`parameters` |  `array`   
Parameters to use on the query. When providing a non-associative array positional parameters (`?`) will be used. When providing an associative array named parameters will be used (`@name`).  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### setParamTypes

Sets the parameter types for positional parameters.

Note, that this is of high importance when an empty array can be passed as a positional parameter, as we have no way of guessing the data type of the array contents.
    
    
    $queryStr = 'SELECT * FROM `bigquery-public-data.github_repos.commits` ' .
        'WHERE author.time_sec IN UNNEST (?) AND message IN UNNEST (?) AND committer.name = ? LIMIT 10';
    
    $queryJobConfig = $bigQuery->query("")
      ->parameters([[], ["abc", "def"], "John"])
      ->setParamTypes(['INT64']);
    

In the above example, the first array will have a type of INT64 while the next one will have a type of STRING (even though the second array type is not supplied).

For named params, we can simply call:
    
    
    $queryJobConfig = $bigQuery->query("")
      ->parameters(['times' => [], 'messages' => ["abc", "def"]])
      ->setParamTypes(['times' => 'INT64']);
    

**Parameter**  
---  
**Name** | **Description**  
`userTypes` |  `array`   
The user supplied types for the positional parameters. This overrides the guessed types that the ValueMapper got from the toParameter method call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### priority

Sets a priority for the query.

Example:
    
    
    $query->priority('BATCH');
    

**Parameter**  
---  
**Name** | **Description**  
`priority` |  `string`   
The priority. Acceptable values include `"INTERACTIVE"`, `"BATCH"`. **Defaults to** `"INTERACTIVE"`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### query

Sets the SQL query.

Example:
    
    
    $query->query(
        'SELECT commit FROM `bigquery-public-data.github_repos.commits` LIMIT 100'
    );
    

**Parameter**  
---  
**Name** | **Description**  
`query` |  `string`   
SQL query text to execute.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### schemaUpdateOptions

Sets options to allow the schema of the destination table to be updated as a side effect of the query job. Schema update options are supported in two cases: when writeDisposition is `"WRITE_APPEND"`; when writeDisposition is `"WRITE_TRUNCATE"` and the destination table is a partition of a table, specified by partition decorators. For normal tables, `"WRITE_TRUNCATE"` will always overwrite the schema.

Example:
    
    
    $query->schemaUpdateOptions([
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
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### tableDefinitions

Sets table definitions for querying an external data source outside of BigQuery. Describes the data format, location and other properties of the data source.

Example:
    
    
    $query->tableDefinitions([
        'autodetect' => true,
        'sourceUris' => [
            'gs://my_bucket/table.json'
        ]
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`tableDefinitions` |  `array`   
The table definitions.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### timePartitioning

Sets time-based partitioning for the destination table.

Only one of timePartitioning and rangePartitioning should be specified.

Example:
    
    
    $query->timePartitioning([
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
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### rangePartitioning

Sets range partitioning specification for the destination table.

Only one of timePartitioning and rangePartitioning should be specified.

Example:
    
    
    $query->rangePartitioning([
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
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### useLegacySql

Sets whether or not to use legacy SQL dialect. When not set, defaults to false in this client.

Example:
    
    
    $query->useLegacySql(true);
    

**Parameter**  
---  
**Name** | **Description**  
`useLegacySql` |  `bool`   
Whether or not to use legacy SQL dialect.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### useQueryCache

See also:

  * [Using cached results](https://cloud.google.com/bigquery/docs/cached-results)



**Parameter**  
---  
**Name** | **Description**  
`useQueryCache` |  `bool`   
Whether or not to use the query cache.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### userDefinedFunctionResources

Sets user-defined function resources used in the query.

Example:
    
    
    $query->userDefinedFunctionResources([
        ['resourceUri' => 'gs://my_bucket/code_path']
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`userDefinedFunctionResources` |  `array`   
User-defined function resources used in the query. This is to be formatted as a list of sub-arrays containing either a key `resourceUri` or `inlineCode`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### writeDisposition

Sets the action that occurs if the destination table already exists. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion.

Example:
    
    
    $query->writeDisposition('WRITE_TRUNCATE');
    

**Parameter**  
---  
**Name** | **Description**  
`writeDisposition` |  `string`   
The write disposition. Acceptable values include `"WRITE_TRUNCATE"`, `"WRITE_APPEND"`, `"WRITE_EMPTY"`. _Defaults to_ * `"WRITE_EMPTY"`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryJobConfiguration)` |   
  
### isStateless

Returns true if the current configuration is compatible with the stateless query API.

False if not

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### toQueryRequest

Returns an array representation of a QueryRequest: [QueryRequest](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#QueryRequest)

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
