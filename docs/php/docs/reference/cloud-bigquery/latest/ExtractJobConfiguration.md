---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration/
title: BigQuery Client - Class ExtractJobConfiguration (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:47.437802+00:00
---

# BigQuery Client - Class ExtractJobConfiguration (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class ExtractJobConfiguration (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class ExtractJobConfiguration.

Represents a configuration for an extract job. For more information on the available settings please see the [Jobs configuration API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job).

Example:
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    $bigQuery = new BigQueryClient();
    $table = $bigQuery->dataset('my_dataset')
        ->table('my_table');
    $extractJobConfig = $table->extract('gs://my_bucket/target.csv');
    

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
  
### compression

Sets the compression type to use for exported files.

Not applicable when extracting models.

Example:
    
    
    $extractJobConfig->compression('GZIP');
    

**Parameter**  
---  
**Name** | **Description**  
`compression` |  `string`   
The compression type. Acceptable values include `"GZIP"`, `"NONE"`. **Defaults to** `"NONE"`.  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
### destinationFormat

Sets the exported file format. Tables with nested or repeated fields cannot be exported as CSV.

Example:
    
    
    $extractJobConfig->destinationFormat('NEWLINE_DELIMITED_JSON');
    

**Parameter**  
---  
**Name** | **Description**  
`destinationFormat` |  `string`   
The exported file format. Acceptable values for tables include `CSV`, `NEWLINE_DELIMITED_JSON`, `AVRO`. For models, acceptable values include `ML_TF_SAVED_MODEL` and `ML_XGBOOST_BOOSTER`. **Defaults to** `CSV` for tables, or `ML_TF_SAVED_MODEL` for models.  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
### destinationUris

Sets a list of fully-qualified Google Cloud Storage URIs where the extracted table should be written.

Example:
    
    
    $extractJobConfig->destinationUris([
        'gs://my_bucket/destination.csv'
    ]);
    

**Parameter**  
---  
**Name** | **Description**  
`destinationUris` |  `array`   
The destination URIs.  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
### fieldDelimiter

Sets the delimiter to use between fields in the exported data.

Not applicable when extracting models.

Example:
    
    
    $extractJobConfig->fieldDelimiter(',');
    

**Parameter**  
---  
**Name** | **Description**  
`fieldDelimiter` |  `string`   
The field delimiter. **Defaults to** `","`.  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
### printHeader

Sets whether or not to print out a header row in the results.

Not applicable when extracting models.

Example:
    
    
    $extractJobConfig->printHeader(false);
    

**Parameter**  
---  
**Name** | **Description**  
`printHeader` |  `bool`   
Whether or not to print out a header row. _Defaults to_ * `true`.  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
### sourceTable

Sets a reference to the table being exported.

Cannot be used in the same job as [ExtractJobConfiguration::sourceModel()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration#_Google_Cloud_BigQuery_ExtractJobConfiguration__sourceModel__).

Example:
    
    
    $table = $bigQuery->dataset('my_dataset')
        ->table('my_table');
    $extractJobConfig->sourceTable($table);
    

**Parameter**  
---  
**Name** | **Description**  
`sourceTable` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table)`   
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
### sourceModel

Sets a reference to the model being exported.

Cannot be used in the same job as [ExtractJobConfiguration::sourceTable()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration#_Google_Cloud_BigQuery_ExtractJobConfiguration__sourceTable__).

Example:
    
    
    $model = $bigQuery->dataset('my_dataset')
        ->model('my_model');
    $extractJobConfig->sourceModel($model);
    

**Parameter**  
---  
**Name** | **Description**  
`sourceModel` |  `[Model](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Model)`   
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
### useAvroLogicalTypes

Sets whether to use logical types when extracting to AVRO format.

If destinationFormat is set to "AVRO", this flag indicates whether to enable extracting applicable column types (such as TIMESTAMP) to their corresponding AVRO logical types (timestamp-micros), instead of only using their raw types (avro-long).

Not applicable when extracting models.

Example:
    
    
    $extractJobConfig->useAvroLogicalTypes(true);
    

**Parameter**  
---  
**Name** | **Description**  
`useAvroLogicalTypes` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`[ExtractJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ExtractJobConfiguration)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
