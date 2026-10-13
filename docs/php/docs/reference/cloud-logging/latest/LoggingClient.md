---
url: https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/LoggingClient/
title: Stackdriver Logging Client - Class LoggingClient (2.2.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:41.829523+00:00
---

# Stackdriver Logging Client - Class LoggingClient (2.2.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/LoggingClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Stackdriver Logging Client - Class LoggingClient (2.2.3) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.3 (latest)  2.1.0  2.0.0  1.34.5  1.33.0  1.32.3  1.31.3  1.30.3  1.29.0  1.28.5  1.27.1  1.26.0  1.25.5  1.24.10 

Reference documentation and code samples for the Stackdriver Logging Client class LoggingClient.

Google Stackdriver Logging allows you to store, search, analyze, monitor, and alert on log data and events from Google Cloud Platform and Amazon Web Services. Find more information at the [Google Stackdriver Logging docs](https://cloud.google.com/logging/docs/).

This client supports transport over [REST](https://cloud.google.com/logging/docs/api/reference/rest/) or gRPC.

In order to enable gRPC support please make sure to install and enable the gRPC extension through PECL:
    
    
    $ pecl install grpc
    

NOTE: Support for gRPC is currently at an Alpha quality level, meaning it is still a work in progress and is more likely to get backwards-incompatible updates.

When using gRPC in production environments, it is highly recommended that you make use of the Protobuf PHP extension for improved performance. Protobuf can be installed via [PECL](https://pecl.php.net).
    
    
    $ pecl install protobuf
    

Example:
    
    
    use Google\Cloud\Logging\LoggingClient;
    
    $logging = new LoggingClient();
    

## Namespace

Google \ Cloud \ Logging

## Methods 

### __construct

Create a Logging client.

**Parameter**  
---  
**Name** | **Description**  
`config` |  `array`   
  
  
### createSink

See also:

  * [projects.sinks create API documentation.](https://cloud.google.com/logging/docs/api/reference/rest/v2/projects.sinks/create)



**Parameters**  
---  
**Name** | **Description**  
`name` |  `string`   
The name of the sink.  
`destination` |  `string`   
The export destination. Please see [Exporting Logs With Sinks](https://cloud.google.com/logging/docs/api/tasks/exporting-logs#about_sinks) for more information and examples.  
`options` |  `array`   
Configuration options.  
`↳ filter` |  `string`   
An [advanced logs filter](https://cloud.google.com/logging/docs/view/advanced_filters).  
**Returns**  
---  
**Type** | **Description**  
`[Sink](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Sink)` |   
  
### sink

Lazily instantiates a sink. There are no network requests made at this point. To see the operations that can be performed on a sink please see [Sink](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Sink).

Example:
    
    
    $sink = $logging->sink('my-sink');
    echo $sink->name();
    

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The name of the sink.  
**Returns**  
---  
**Type** | **Description**  
`[Sink](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Sink)` |   
  
### sinks

See also:

  * [projects.sinks list API documentation.](https://cloud.google.com/logging/docs/api/reference/rest/v2/projects.sinks/list)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ pageSize` |  `int`   
The maximum number of results to return per request.  
`↳ resultLimit` |  `int`   
Limit the number of results returned in total. **Defaults to** `0` (return all results).  
`↳ pageToken` |  `string`   
A previously-returned page token used to resume the loading of results from a specific point.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iterator\ItemIterator](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iterator.ItemIterator.html)<[Sink](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Sink)>` |   
  
### createMetric

See also:

  * [projects.metrics create API documentation.](https://cloud.google.com/logging/docs/api/reference/rest/v2/projects.metrics/create)



**Parameters**  
---  
**Name** | **Description**  
`name` |  `string`   
The name of the metric.  
`filter` |  `string`   
An [advanced logs filter](https://cloud.google.com/logging/docs/view/advanced_filters).  
`options` |  `array`   
Configuration Options.  
`↳ description` |  `string`   
A description of the metric.  
**Returns**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Metric)` |   
  
### metric

Lazily instantiates a metric. There are no network requests made at this point. To see the operations that can be performed on a metric please see [Metric](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Metric).

Example:
    
    
    $metric = $logging->metric('my-metric');
    echo $metric->name();
    

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The name of the metric.  
**Returns**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Metric)` |   
  
### metrics

See also:

  * [projects.metrics list API documentation.](https://cloud.google.com/logging/docs/api/reference/rest/v2/projects.metrics/list)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ pageSize` |  `int`   
The maximum number of results to return per request.  
`↳ resultLimit` |  `int`   
Limit the number of results returned in total. **Defaults to** `0` (return all results).  
`↳ pageToken` |  `string`   
A previously-returned page token used to resume the loading of results from a specific point.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iterator\ItemIterator](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iterator.ItemIterator.html)<[Metric](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Metric)>` |   
  
### entries

See also:

  * [Entries list API documentation.](https://cloud.google.com/logging/docs/api/reference/rest/v2/entries/list)



**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Configuration options.  
`↳ projectIds` |  `string[]`   
A list of projectIds to fetch entries from in addition to entries found in the project bound to this client.  
`↳ resourceNames` |  `string[]`   
One or more cloud resources from which to retrieve log entries. Projects listed in projectIds are added to this list. Example: "projects/my-project-1A", "projects/1234567890".  
`↳ filter` |  `string`   
An [advanced logs filter](https://cloud.google.com/logging/docs/view/advanced_filters).  
`↳ orderBy` |  `string`   
How the results should be sorted. Presently, the only permitted values are `timestamp asc` and `timestamp desc`. **Defaults to** `"timestamp asc"`.  
`↳ pageSize` |  `int`   
The maximum number of results to return per request.  
`↳ resultLimit` |  `int`   
Limit the number of results returned in total. **Defaults to** `0` (return all results).  
`↳ pageToken` |  `string`   
A previously-returned page token used to resume the loading of results from a specific point.  
**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Core\Iterator\ItemIterator](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Iterator.ItemIterator.html)<[Entry](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Entry)>` |   
  
### psrLogger

Fetches a logger which will write log entries to Stackdriver Logging and implements the PSR-3 specification.

Example:
    
    
    $psrLogger = $logging->psrLogger('my-log');
    
    
    
    // Write entries with background batching.
    $psrLogger = $logging->psrLogger('my-log', [
        'batchEnabled' => true
    ]);
    

**Parameters**  
---  
**Name** | **Description**  
`name` |  `string`   
The name of the log to write entries to.  
`options` |  `array`   
Configuration options.  
`↳ messageKey` |  `string`   
The key in the `jsonPayload` used to contain the logged message. **Defaults to** `message`.  
`↳ resource` |  `array`   
The [monitored resource](https://cloud.google.com/logging/docs/api/reference/rest/v2/MonitoredResource) to associate log entries with. **Defaults to** type global.  
`↳ labels` |  `array`   
A set of user-defined (key, value) data that provides additional information about the log entry.  
`↳ metadataProvider` |  `[Google\Cloud\Core\Report\MetadataProviderInterface](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Report.MetadataProviderInterface.html)`   
**Defaults to** An automatically chosen provider, based on detected environment settings.  
`↳ batchEnabled` |  `bool`   
Determines whether or not to use background batching. **Defaults to** `false`.  
`↳ debugOutput` |  `bool`   
Whether or not to output debug information. Please note debug output currently only applies in CLI based applications. **Defaults to** `false`. Applies only when `batchEnabled` is set to `true`.  
`↳ debugOutputResource` |  `resource`   
A resource to output debug output to. Applies only when `batchEnabled` is set to `true`.  
`↳ batchOptions` |  `array`   
A set of options for a BatchJob. [Google\Cloud\Core\Batch\BatchJob::__construct()](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchJob.html#_Google_Cloud_Core_Batch_BatchJob____construct__) for more details. **Defaults to** ['batchSize' => 1000, 'callPeriod' => 2.0, 'numWorkers' => 2]. Applies only when `batchEnabled` is set to `true`. Note that this option is currently considered **experimental** and is subject to change.  
`↳ clientConfig` |  `array`   
Configuration options for the Logging client used to handle processing of batch items. For valid options please see [LoggingClient::__construct()](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/LoggingClient#_Google_Cloud_Logging_LoggingClient____construct__). **Defaults to** the options provided to the current client. Applies only when `batchEnabled` is set to `true`.  
`↳ batchRunner` |  `[Google\Cloud\Core\Batch\BatchRunner](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchRunner.html)`   
A BatchRunner object. Mainly used for the tests to inject a mock. **Defaults to** a newly created BatchRunner. Applies only when `batchEnabled` is set to `true`.  
`↳ closureSerializer` |  `[Google\Cloud\Core\Batch\ClosureSerializerInterface](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.ClosureSerializerInterface.html)`   
An implementation responsible for serializing closures used in the `$clientConfig`. This is especially important when using the batch daemon. **Defaults to** Google\Cloud\Core\Batch\OpisClosureSerializer if the `opis/closure` library is installed.  
**Returns**  
---  
**Type** | **Description**  
`[PsrLogger](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/PsrLogger)` |   
  
### logger

Fetches a logger which will write log entries to Stackdriver Logging.

Example:
    
    
    $logger = $logging->logger('my-log');
    

**Parameters**  
---  
**Name** | **Description**  
`name` |  `string`   
The name of the log to write entries to.  
`options` |  `array`   
Configuration options.  
`↳ resource` |  `array`   
The [monitored resource](https://cloud.google.com/logging/docs/api/reference/rest/v2/MonitoredResource) to associate log entries with. **Defaults to** type global.  
`↳ labels` |  `array`   
A set of user-defined (key, value) data that provides additional information about the log entry.  
**Returns**  
---  
**Type** | **Description**  
`[Logger](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/Logger)` |   
  
### static::psrBatchLogger

Create a PsrLogger with batching enabled.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `string`   
The name of the log to write entries to.  
`options` |  `array`   
Configuration options.  
`↳ apiEndpoint` |  `string`   
A hostname with optional port to use in place of the service's default endpoint.  
`↳ messageKey` |  `string`   
The key in the `jsonPayload` used to contain the logged message. **Defaults to** `message`.  
`↳ resource` |  `array`   
The [monitored resource](https://cloud.google.com/logging/docs/api/reference/rest/v2/MonitoredResource) to associate log entries with. **Defaults to** type global.  
`↳ labels` |  `array`   
A set of user-defined (key, value) data that provides additional information about the log entry.  
`↳ metadataProvider` |  `[Google\Cloud\Core\Report\MetadataProviderInterface](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Report.MetadataProviderInterface.html)`   
**Defaults to** An automatically chosen provider, based on detected environment settings.  
`↳ debugOutput` |  `bool`   
Whether or not to output debug information. Please note debug output currently only applies in CLI based applications. **Defaults to** `false`.  
`↳ batchOptions` |  `array`   
A set of options for a BatchJob. [Google\Cloud\Core\Batch\BatchJob::__construct()](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchJob.html#_Google_Cloud_Core_Batch_BatchJob____construct__) for more details. **Defaults to** ['batchSize' => 1000, 'callPeriod' => 2.0, 'numWorkers' => 2].  
`↳ clientConfig` |  `array`   
Configuration options for the Logging client used to handle processing of batch items. For valid options please see [LoggingClient::__construct()](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/LoggingClient#_Google_Cloud_Logging_LoggingClient____construct__).  
`↳ batchRunner` |  `[Google\Cloud\Core\Batch\BatchRunner](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchRunner.html)`   
A BatchRunner object. Mainly used for the tests to inject a mock. **Defaults to** a newly created BatchRunner.  
`↳ closureSerializer` |  `[Google\Cloud\Core\Batch\ClosureSerializerInterface](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.ClosureSerializerInterface.html)`   
An implementation responsible for serializing closures used in the `$clientConfig`. This is especially important when using the batch daemon. **Defaults to** Google\Cloud\Core\Batch\OpisClosureSerializer if the `opis/closure` library is installed.  
**Returns**  
---  
**Type** | **Description**  
`[PsrLogger](https://docs.cloud.google.com/php/docs/reference/cloud-logging/latest/PsrLogger)` |   
  
## Constants 

### FULL_CONTROL_SCOPE
    
    
    Value: 'https://www.googleapis.com/auth/logging.admin'

### READ_ONLY_SCOPE
    
    
    Value: 'https://www.googleapis.com/auth/logging.read'

### WRITE_ONLY_SCOPE
    
    
    Value: 'https://www.googleapis.com/auth/logging.write'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
