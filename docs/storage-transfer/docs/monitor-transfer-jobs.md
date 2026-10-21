---
url: https://docs.cloud.google.com/storage-transfer/docs/monitor-transfer-jobs/
title: Monitor transfer jobs \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:41.685271+00:00
---

# Monitor transfer jobs  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/monitor-transfer-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Monitor transfer jobs Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring automatically collects and stores information for your Storage Transfer Service jobs. You can use Cloud Monitoring to chart and monitor a range of metrics:

  * The number of found objects and bytes
  * The number of copied objects and bytes
  * The number of deleted objects and bytes
  * The number of errors, and the associated error codes



Cloud Monitoring is automatically enabled for Storage Transfer Service. There's no charge for the collection of data or to view metrics in the Google Cloud console. API calls may incur charges; see [Cloud Monitoring pricing](https://docs.cloud.google.com/monitoring#section-7) for pricing details.

## Required IAM role

You must have the Monitoring Viewer (`roles/monitoring.viewer`) role, or equivalent permissions, to view metrics in Cloud Monitoring.

Learn how to [grant an IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

## View metrics

Cloud Monitoring metrics are available from two locations in the Google Cloud console:

  * The Storage Transfer Service job details page displays metrics for a specific transfer job. In addition to the metrics listed below, it computes the bandwidth of bytes copies and the rate of objects copied.

  * The Cloud Monitoring page can display metrics for a single transfer job, multiple jobs, or all jobs in a project. It provides multiple chart options and customizations.




### View metrics on the job details page

To view a specific job's metrics:

  1. Go to the **Transfer jobs** page in the Google Cloud console. 

[Go to Transfer jobs](https://console.cloud.google.com/transfer/jobs)

  2. Click on the job for which to view metrics. The **Job details** page appears.

  3. Click the **Monitoring** tab. The default dashboard is displayed.




### View metrics in Cloud Monitoring

To view Storage Transfer Service metrics in Cloud Monitoring, do the following:

  1. Go to the **Metrics Explorer** page in the Google Cloud console.

[Go to Monitoring: Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer/)

  2. Follow the instructions in [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) to select and display your metrics.




## Resource details

Monitored resource name: `storage_transfer_job`

Resource field / Target field  | REST resource and field used to populate this field | Description   
---|---|---  
project_id  | TransferJob.project_id  | The identifier of the project associated with this resource  
job_id  | TransferJob.name  | The globally unique name of the transfer  
location  | Will always be set to `global` since transfer jobs are not associated with a region or location | The location of the transfer job   
  
## Metric details

All Storage Transfer Service metrics are [_delta_ metrics](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types#metric-kinds). They measure the change since the metric was last recorded. For example, metrics measuring request counts are delta metrics; each value records how many requests were received since the last data point was recorded.

Data is sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds.

Metric names all begin with `storagetransfer.googleapis.com/transferjob/`. For example, `storagetransfer.googleapis.com/transferjob/found_bytes_count`.

Metric name | Labels | Description  
---|---|---  
found_bytes_count | 
    
    
    origin=[source | sink]

|  Number of bytes found that are scheduled to be transferred or deleted, excluding any that are filtered based on [ object conditions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#ObjectConditions) or because they already exist at the destination. See [ TransferOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#transferoptions) for information about overwriting data in the sink. Corresponding [ `TransferCounters`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#transfercounters): bytesFoundFromSource, bytesFoundOnlyFromSink  
found_objects_count  | 
    
    
    origin=[source | sink]

|  Number of objects found that are scheduled to be transferred or deleted, excluding any that are filtered based on object conditions or skipped due to sync. Corresponding [ `TransferCounters`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#transfercounters): objectsFoundFromSource, objectsFoundOnlyFromSink  
copied_bytes_count  | 
    
    
    status=[succeeded | skipped | failed]

|  Number of bytes copied. Corresponding [ `TransferCounters`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#transfercounters): bytesCopiedToSink, bytesFromSourceSkippedBySync, bytesFromSourceFailed The value of `copied_bytes_count` with status `succeeded` does not always match the `bytesCopiedToSink` counter, as the metric also counts successfully copied bytes that are discarded in the case of a failure. For example, if Storage Transfer Service copies 100 bytes of an object that is deleted mid-way through transfer, the 100 bytes copied are recorded under `copied_bytes_count` with status `succeeded`. The full object's bytes are also recorded under `copied_bytes_count` with status `failed`.   
copied_objects_count | 
    
    
    status=[succeeded | skipped | failed]

|  Number of objects copied. Corresponding [ `TransferCounters`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#transfercounters): objectsCopiedToSink, objectsFromSourceSkippedBySync, objectsFromSourceFailed  
deleted_bytes_count  | 
    
    
    origin=[source | sink]
    status=[succeeded | failed]

|  Number of bytes deleted. Storage Transfer Service can be configured to delete data at the source and/or the destination. See [ TransferOptions](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#transferoptions) for information about configuring delete behavior. Corresponding [ `TransferCounters`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#transfercounters): bytesDeletedFromSource, bytesDeletedFromSink, bytesFromSourceFailed, bytesFailedToDeleteFromSink Note: this counter is the sum of `deleted_bytes_count:status=failed,origin=source` and `copied_bytes_count:status=failed`.  
deleted_objects_count  | 
    
    
    origin=[source | sink]
    status=[succeeded | failed]

|  Number of objects deleted. Corresponding [ `TransferCounters`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#transfercounters): objectsDeletedFromSource, objectsDeletedFromSink, objectsFromSourceFailed, objectsFailedToDeleteFromSink Note: this counter is the sum of `deleted_objects_count:status=failed,origin=source` and `copied_objects_count:status=failed`.  
error_count  | 
    
    
    code=[error code](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#code)

|  The number of errors as reported in [ ErrorSummary](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#errorsummary).  
object_replication_count | 
    
    
    status=[succeeded | failed]
    destination_bucket=[string]
    source_bucket=[string]

| The number of objects replicated using [cross-bucket replication](https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication).  
replication_latency | 
    
    
    destination_bucket=[string]
    source_bucket=[string]

| Time in milliseconds for the object to be replicated using [cross-bucket replication](https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication).   
replication_start_latency | 
    
    
    destination_bucket=[string]
    source_bucket=[string]

| Time in milliseconds for the object to be picked up for [cross-bucket replication](https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
