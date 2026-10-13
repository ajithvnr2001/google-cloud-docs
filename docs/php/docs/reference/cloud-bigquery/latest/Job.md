---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job/
title: BigQuery Client - Class Job (1.39.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:47.651717+00:00
---

# BigQuery Client - Class Job (1.39.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  BigQuery Client - Class Job (1.39.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.39.3 (latest)  1.38.0  1.37.0  1.36.0  1.35.2  1.34.7  1.33.1  1.32.0  1.31.1  1.30.3  1.29.0  1.28.3  1.27.0  1.26.1  1.25.1  1.24.2  1.23.10 

Reference documentation and code samples for the BigQuery Client class Job.

[Jobs](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job) are objects that manage asynchronous tasks such as running queries, loading data, and exporting data.

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
The job's ID.  
`projectId` |  `string`   
The project's ID.  
`mapper` |  `[ValueMapper](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/ValueMapper)`   
Maps values between PHP and BigQuery.  
`info` |  `array`   
[optional] The job's metadata.  
`location` |  `string|null`   
[optional] A default geographic location, used when no job metadata exists.  
  
### exists

Check whether or not the job exists.

Example:
    
    
    echo $job->exists();
    

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### cancel

See also:

  * [Jobs cancel API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/cancel)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
  
### queryResults

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
`↳ initialTimeoutMs` |  `int`   
How long, in milliseconds, to wait for query results to become available before timing out. **Defaults to** `0` milliseconds (0 seconds). Please note that this option is used only for the initial call to get query results. To control the timeout for any subsequent calls while polling for query results to complete, please see the `$timeoutMs` option.  
`↳ timeoutMs` |  `int`   
How long, in milliseconds, each API call will wait for query results to become available before timing out. Depending on whether the $maxRetries has been exceeded, the results will be polled again after the timeout has been reached. **Defaults to** `10000` milliseconds (10 seconds). Please note that this option is used when iterating on the returned class, and will not apply immediately upon calling of this method.  
`↳ maxRetries` |  `int`   
The number of times to poll the Job status, until the job is complete. By default, will poll indefinitely. Please note that this option is used when iterating on the returned class, and will not block immediately upon calling of this method.  
`↳ returnRawResults` |  `bool`   
Returns the raw data types returned from BigQuery without converting their values into native PHP types or the custom type classes supported by this library. Default is false  
`↳ formatOptions.useInt64Timestamp` |  `boolean`   
Optional. Output timestamp as usec int64. Default is false.  
**Returns**  
---  
**Type** | **Description**  
`[QueryResults](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/QueryResults)` |   
  
### waitUntilComplete

Blocks until the job is complete.

Example:
    
    
    $job->waitUntilComplete();
    

**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ maxRetries` |  `int`   
The number of times to poll the Job status, until the job is complete. By default, will poll indefinitely.  
  
### isComplete

Checks the job's completeness.

Useful in combination with [Job::reload()](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/Job#_Google_Cloud_BigQuery_Job__reload__) to poll for job status.

Example:
    
    
    $isComplete = $job->isComplete();
    
    while (!$isComplete) {
        sleep(1); // let's wait for a moment...
        $job->reload();
        $isComplete = $job->isComplete();
    }
    
    echo 'Query complete!';
    

**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### info

See also:

  * [Jobs resource documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### reload

See also:

  * [Jobs get API documentation.](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get)



**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] Configuration options.  
**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### id

Retrieves the job's ID.

Example:
    
    
    echo $job->id();
    

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### identity

Retrieves the job's identity.

An identity provides a description of a nested resource.

Example:
    
    
    echo $job->identity()['projectId'];
    

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
## Constants 

### MAX_RETRIES
    
    
    Value: PHP_INT_MAX

### DONE
    
    
    Value: 'DONE'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
