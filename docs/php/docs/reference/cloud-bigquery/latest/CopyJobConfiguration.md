---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/CopyJobConfiguration/
title: BigQuery Client - Class CopyJobConfiguration (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:29.951468+00:00
---

# BigQuery Client - Class CopyJobConfiguration (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/CopyJobConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class CopyJobConfiguration (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class CopyJobConfiguration.

Represents a configuration for a copy job. For more information on the available settings please see the [Jobs configuration API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job).

Example:
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    $bigQuery = new BigQueryClient();
    $sourceTable = $bigQuery->dataset('my_dataset')
        ->table('my_source_table');
    $destinationTable = $bigQuery->dataset('my_dataset')
        ->table('my_destination_table');
    
    $copyJobConfig = $sourceTable->copy($destinationTable);
    

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
  
### createDisposition

Set whether the job is allowed to create new tables. Creation, truncation and append actions occur as one atomic update upon job completion.

Example:
    
    
    $copyJobConfig->createDisposition('CREATE_NEVER');
    

**Parameter**  
---  
**Name** | **Description**  
`createDisposition` |  `string`   
The create disposition. Acceptable values include `"CREATED_IF_NEEDED"`, `"CREATE_NEVER"`. **Defaults to** `"CREATE_IF_NEEDED"`.  
**Returns**  
---  
**Type** | **Description**  
`[CopyJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/CopyJobConfiguration)` |   
  
### destinationEncryptionConfiguration

Sets the custom encryption configuration (e.g., Cloud KMS keys).

Example:
    
    
    $copyJobConfig->destinationEncryptionConfiguration([
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
`[CopyJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/CopyJobConfiguration)` |   
  
### destinationTable

Sets the destination table.

Example:
    
    
    $table = $bigQuery->dataset('my_dataset')
        ->table('my_table');
    $copyJobConfig->destinationTable($table);
    

**Parameter**  
---  
**Name** | **Description**  
`destinationTable` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table)`   
The destination table.  
**Returns**  
---  
**Type** | **Description**  
`[CopyJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/CopyJobConfiguration)` |   
  
### sourceTable

Sets the source table to copy.

Example:
    
    
    $table = $bigQuery->dataset('my_dataset')
        ->table('source_table');
    $copyJobConfig->sourceTable($table);
    

**Parameter**  
---  
**Name** | **Description**  
`sourceTable` |  `[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Table)`   
The destination table.  
**Returns**  
---  
**Type** | **Description**  
`[CopyJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/CopyJobConfiguration)` |   
  
### writeDisposition

Sets the action that occurs if the destination table already exists. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion.

Example:
    
    
    $copyJobConfig->writeDisposition('WRITE_TRUNCATE');
    

**Parameter**  
---  
**Name** | **Description**  
`writeDisposition` |  `string`   
The write disposition. Acceptable values include `"WRITE_TRUNCATE"`, `"WRITE_APPEND"`, `"WRITE_EMPTY"`. _Defaults to_ * `"WRITE_EMPTY"`.  
**Returns**  
---  
**Type** | **Description**  
`[CopyJobConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/CopyJobConfiguration)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
