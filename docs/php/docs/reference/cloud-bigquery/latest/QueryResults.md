---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryResults/
title: BigQuery Client - Class QueryResults (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:49.008615+00:00
---

# BigQuery Client - Class QueryResults (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryResults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class QueryResults (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class QueryResults.

QueryResults represent the result of a BigQuery SQL query. Read more at the [Query Response API Documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#response-body)

This class should be not instantiated directly, but as a result of calling [BigQueryClient::runQuery()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient#_Google_Cloud_BigQuery_BigQueryClient__runQuery__) or [Job::queryResults()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job#_Google_Cloud_BigQuery_Job__queryResults__).

## Namespace

Google \ Cloud \ BigQuery

## Implements

\IteratorAggregate

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `Connection\ConnectionInterface`   
Represents a connection to BigQuery. This object is created by BigQueryClient, and should not be instantiated outside of this client.  
`jobId` |  `string`   
The job's ID.  
`projectId` |  `string`   
The project's ID.  
`info` |  `array`   
The query result's metadata.  
`mapper` |  `[ValueMapper](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ValueMapper)`   
Maps values between PHP and BigQuery.  
`job` |  `[Job](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job)`   
The job from which the query results originated.  
`queryResultsOptions` |  `array`   
Default options to be used for calls to get query results. See [documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/getQueryResults#query-parameters) for available options.  
  
### rows

Retrieves the rows associated with the query and merges them together with the table's schema.

Refer to the table below for a guide on how BigQuery types are mapped as they come back from the API.

**PHP Type** | **BigQuery Data Type**  
---|---  
`\DateTimeInterface` | `DATETIME`  
[Bytes](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Bytes) | `BYTES`  
[Date](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Date) | `DATE`  
[Google\Cloud\Core\Int64](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Int64.html) | `INTEGER`  
[Time](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Time) | `TIME`  
[Timestamp](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Timestamp) | `TIMESTAMP`  
Associative Array | `RECORD`  
Non-Associative Array | `RECORD` (Repeated)  
`float` | `FLOAT`  
`int` | `INTEGER`  
`string` | `STRING`  
`bool` | `BOOLEAN`  
  
Example:
    
    
    $rows = $queryResults->rows();
    
    foreach ($rows as $row) {
        echo $row['name'] . PHP_EOL;
    }
    

**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options. Please note, these options will inherit the values set by either [BigQueryClient::runQuery()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient#_Google_Cloud_BigQuery_BigQueryClient__runQuery__) or [Job::queryResults()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job#_Google_Cloud_BigQuery_Job__queryResults__).  
`↳ maxResults` |  `int`   
Maximum number of results to read per page.  
`↳ startIndex` |  `int`   
Zero-based index of the starting row.  
`↳ timeoutMs` |  `int`   
How long, in milliseconds, each API call will wait for query results to become available before timing out. Depending on whether the $maxRetries has been exceeded, the results will be polled again after the timeout has been reached. **Defaults to** `10000` milliseconds (10 seconds).  
`↳ maxRetries` |  `int`   
The number of times to poll the Job status, until the job is complete. By default, will poll indefinitely.  
`↳ returnRawResults` |  `bool`   
Returns the raw data types returned from BigQuery without converting their values into native PHP types or the custom type classes supported by this library. Default is false.  
`↳ formatOptions.useInt64Timestamp` |  `boolean`   
Optional. Output timestamp as usec int64. Default is false.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iterator\ItemIterator](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iterator.ItemIterator.html)` |   
  
### waitUntilComplete

Blocks until the query is complete.

Example:
    
    
    $queryResults->waitUntilComplete();
    

**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options. Please note, these options will inherit the values set by either [BigQueryClient::runQuery()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient#_Google_Cloud_BigQuery_BigQueryClient__runQuery__) or [Job::queryResults()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job#_Google_Cloud_BigQuery_Job__queryResults__).  
`↳ maxResults` |  `int`   
Maximum number of results to read per page.  
`↳ startIndex` |  `int`   
Zero-based index of the starting row.  
`↳ timeoutMs` |  `int`   
How long, in milliseconds, each API call will wait for query results to become available before timing out. Depending on whether the $maxRetries has been exceeded, the results will be polled again after the timeout has been reached. **Defaults to** `10000` milliseconds (10 seconds).  
`↳ maxRetries` |  `int`   
The number of times to poll the Job status, until the job is complete. By default, will poll indefinitely.  
`↳ formatOptions.useInt64Timestamp` |  `boolean`   
Optional. Output timestamp as usec int64. Default is false.  
  
### info

See also:

  * [Jobs getQueryResults API response documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/getQueryResults#response-body)



**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### reload

See also:

  * [Jobs getQueryResults API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/getQueryResults)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ maxResults` |  `int`   
Maximum number of results to read per page.  
`↳ startIndex` |  `int`   
Zero-based index of the starting row.  
`↳ timeoutMs` |  `int`   
How long to wait for the query to complete, in milliseconds. **Defaults to** `10000` milliseconds (10 seconds).  
`↳ formatOptions.useInt64Timestamp` |  `boolean`   
Optional. Output timestamp as usec int64. Default is false.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### identity

Retrieves the query result's identity.

An identity provides a description of a nested resource.

Example:
    
    
    echo $queryResults->identity()['projectId'];
    

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### isComplete

Checks the job's completeness.

Useful in combination with [QueryResults::reload()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryResults#_Google_Cloud_BigQuery_QueryResults__reload__) to poll for query status.

Example:
    
    
    $isComplete = $queryResults->isComplete();
    
    while (!$isComplete) {
        sleep(1); // let's wait for a moment...
        $queryResults->reload();
        $isComplete = $queryResults->isComplete();
    }
    
    echo 'Query complete!';
    

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### job

Returns a reference to the job.

The [Job](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job) instance is used to fetch the query results. This is especially useful when attempting to access job statistics after calling [BigQueryClient::runQuery()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient#_Google_Cloud_BigQuery_BigQueryClient__runQuery__).

Example:
    
    
    $job = $queryResults->job();
    

**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job)` |   
  
### getIterator

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iterator\ItemIterator](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iterator.ItemIterator.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
