---
url: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJob
title: Class CopyJob (3.46.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:12.992450+00:00
---

# Class CopyJob (3.46.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CopyJob (3.46.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.46.1 (latest)  3.46.0  3.45.2  3.44.0  3.43.0  3.42.3  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.31.0  3.30.0  3.29.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.1  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.2  3.16.0  3.15.0  3.14.1  3.13.0  3.12.0  3.11.4  3.4.0  3.3.6  3.2.0  3.1.0  3.0.1  2.34.4  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.27.1  2.26.0  2.25.2  2.24.1  2.23.3  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.0  1.28.2  1.27.2  1.26.1  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0 
    
    
    CopyJob(job_id, sources, destination, client, job_config=None)

Asynchronous job: copy data into a table from other tables.

## Parameters  
  
---  
**Name** | **Description**  
`job_id` |  `str`   
the job's ID, within the project belonging to `client`.  
`sources` |  `List[[google.cloud.bigquery.table.TableReference](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.TableReference)]`   
Table from which data is to be loaded.  
`destination` |  `[google.cloud.bigquery.table.TableReference](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.TableReference)`   
Table into which data is to be loaded.  
`client` |  `[google.cloud.bigquery.client.Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client)`   
A client which holds credentials and project configuration for the dataset (which requires a project).  
`job_config` |  `Optional[[google.cloud.bigquery.job.CopyJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJobConfig)]`   
Extra configuration options for the copy job.  
  
## Properties 

### configuration

The configuration for this copy job.

### create_disposition

See [create_disposition](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJobConfig).

### created

Datetime at which the job was created.

**Returns**  
---  
**Type** | **Description**  
`Optional[datetime.datetime]` | the creation time (None until set from the server).  
  
### destination

[google.cloud.bigquery.table.TableReference](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.TableReference): Table into which data is to be loaded.

### destination_encryption_configuration

[google.cloud.bigquery.encryption_configuration.EncryptionConfiguration](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.encryption_configuration.EncryptionConfiguration): Custom encryption configuration for the destination table.

Custom encryption configuration (e.g., Cloud KMS keys) or :data:`None` if using default encryption.

See [destination_encryption_configuration](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJobConfig).

### ended

Datetime at which the job finished.

**Returns**  
---  
**Type** | **Description**  
`Optional[datetime.datetime]` | the end time (None until set from the server).  
  
### error_result

Output only. Final error result of the job.

If present, indicates that the job has completed and was unsuccessful.

See: <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatus.FIELDS.error_result>

**Returns**  
---  
**Type** | **Description**  
`Optional[Mapping]` | the error information (None until set from the server).  
  
### errors

Output only. The first errors encountered during the running of the job.

The final message includes the number of errors that caused the process to stop. Errors here do not necessarily mean that the job has not completed or was unsuccessful.

See: <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatus.FIELDS.errors>

**Returns**  
---  
**Type** | **Description**  
`Optional[List[Mapping]]` | the error information (None until set from the server).  
  
### etag

ETag for the job resource.

**Returns**  
---  
**Type** | **Description**  
`Optional[str]` | the ETag (None until set from the server).  
  
### job_id

str: ID of the job.

### job_type

Type of job.

**Returns**  
---  
**Type** | **Description**  
`str` | one of 'load', 'copy', 'extract', 'query'.  
  
### labels

Dict[str, str]: Labels for the job.

### location

str: Location where the job runs.

### num_child_jobs

The number of child jobs executed.

See: <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatistics.FIELDS.num_child_jobs>

### parent_job_id

Return the ID of the parent job.

See: <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatistics.FIELDS.parent_job_id>

**Returns**  
---  
**Type** | **Description**  
`Optional[str]` | parent job id.  
  
### path

URL path for the job's APIs.

**Returns**  
---  
**Type** | **Description**  
`str` | the path based on project and job ID.  
  
### project

Project bound to the job.

**Returns**  
---  
**Type** | **Description**  
`str` | the project (derived from the client).  
  
### reservation_id

str: Name of the primary reservation assigned to this job.

Note that this could be different than reservations reported in the reservation field if parent reservations were used to execute this job.

### reservation_usage

Job resource usage breakdown by reservation.

**Returns**  
---  
**Type** | **Description**  
`List[[google.cloud.bigquery.job.ReservationUsage](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.ReservationUsage)]` | Reservation usage stats. Can be empty if not set from the server.  
  
### script_statistics

Statistics for a child job of a script.

### self_link

URL for the job resource.

**Returns**  
---  
**Type** | **Description**  
`Optional[str]` | the URL (None until set from the server).  
  
### session_info

[Preview] Information of the session if this job is part of one.

.. versionadded:: 2.29.0

### sources

List[[google.cloud.bigquery.table.TableReference](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.TableReference)]): Table(s) from which data is to be loaded.

### started

Datetime at which the job was started.

**Returns**  
---  
**Type** | **Description**  
`Optional[datetime.datetime]` | the start time (None until set from the server).  
  
### state

Output only. Running state of the job.

Valid states include 'PENDING', 'RUNNING', and 'DONE'.

See: <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatus.FIELDS.state>

**Returns**  
---  
**Type** | **Description**  
`Optional[str]` | the state (None until set from the server).  
  
### transaction_info

Information of the multi-statement transaction if this job is part of one.

Since a scripting query job can execute multiple transactions, this property is only expected on child jobs. Use the [list_jobs](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client) method with the `parent_job` parameter to iterate over child jobs.

.. versionadded:: 2.24.0

### user_email

E-mail address of user who submitted the job.

**Returns**  
---  
**Type** | **Description**  
`Optional[str]` | the URL (None until set from the server).  
  
### write_disposition

See [write_disposition](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJobConfig).

## Methods 

### add_done_callback
    
    
    add_done_callback(fn)

Add a callback to be executed when the operation is complete.

If the operation is not already complete, this will start a helper thread to poll for the status of the operation in the background.

**Parameter**  
---  
**Name** | **Description**  
`fn` |  `Callable[Future]`   
The callback to execute when the operation is complete.  
  
### cancel
    
    
    cancel(
        client=None,
        retry: typing.Optional[
            google.api_core.retry.retry_unary.Retry
        ] = google.api_core.retry.retry_unary.Retry,
        timeout: typing.Optional[float] = None,
    ) -> bool

API call: cancel job via a POST request

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/cancel>

**Parameters**  
---  
**Name** | **Description**  
`client` |  `Optional[[google.cloud.bigquery.client.Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client)]`   
the client to use. If not passed, falls back to the `client` stored on the current dataset.  
`retry` |  `Optional[google.api_core.retry.Retry]`   
How to retry the RPC.  
`timeout` |  `Optional[float]`   
The number of seconds to wait for the underlying HTTP transport before using `retry`  
**Returns**  
---  
**Type** | **Description**  
`bool` | Boolean indicating that the cancel request was sent.  
  
### cancelled
    
    
    cancelled()

Check if the job has been cancelled.

This always returns False. It's not possible to check if a job was cancelled in the API. This method is here to satisfy the interface for `google.api_core.future.Future`.

**Returns**  
---  
**Type** | **Description**  
`bool` | False  
  
### done
    
    
    done(
        retry: google.api_core.retry.retry_unary.Retry = google.api_core.retry.retry_unary.Retry,
        timeout: typing.Optional[float] = 128,
        reload: bool = True,
    ) -> bool

Checks if the job is complete.

**Parameters**  
---  
**Name** | **Description**  
`timeout` |  `Optional[float]`   
The number of seconds to wait for the underlying HTTP transport before using `retry`.  
`reload` |  `Optional[bool]`   
If `True`, make an API call to refresh the job state of unfinished jobs before checking. Default `True`.  
`retry` |  `Optional[google.api_core.retry.Retry]`   
How to retry the RPC. If the job state is `DONE`, retrying is aborted early, as the job will not change anymore.  
**Returns**  
---  
**Type** | **Description**  
`bool` | True if the job is complete, False otherwise.  
  
### exception
    
    
    exception(timeout=object)

Get the exception from the operation, blocking if necessary.

See the documentation for the `result` method for details on how this method operates, as both `result` and this method rely on the exact same polling logic. The only difference is that this method does not accept `retry` and `polling` arguments but relies on the default ones instead.

**Parameter**  
---  
**Name** | **Description**  
`timeout` |  `int`   
How long to wait for the operation to complete.  
**Returns**  
---  
**Type** | **Description**  
`Optional[google.api_core.GoogleAPICallError]` | The operation's error.  
  
### exists
    
    
    exists(
        client=None,
        retry: google.api_core.retry.retry_unary.Retry = google.api_core.retry.retry_unary.Retry,
        timeout: typing.Optional[float] = None,
    ) -> bool

API call: test for the existence of the job via a GET request

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get>

**Parameters**  
---  
**Name** | **Description**  
`timeout` |  `Optional[float]`   
The number of seconds to wait for the underlying HTTP transport before using `retry`.  
`client` |  `Optional[[google.cloud.bigquery.client.Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client)]`   
the client to use. If not passed, falls back to the `client` stored on the current dataset.  
`retry` |  `Optional[google.api_core.retry.Retry]`   
How to retry the RPC.  
**Returns**  
---  
**Type** | **Description**  
`bool` | Boolean indicating existence of the job.  
  
### from_api_repr
    
    
    from_api_repr(resource, client)

Factory: construct a job given its API representation

**Note:** This method assumes that the project found in the resource matches the client's project. 

**Parameters**  
---  
**Name** | **Description**  
`resource` |  `Dict`   
dataset job representation returned from the API  
`client` |  `[google.cloud.bigquery.client.Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client)`   
Client which holds credentials and project configuration for the dataset.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.bigquery.job.CopyJob` | Job parsed from `resource`.  
  
### reload
    
    
    reload(
        client=None,
        retry: google.api_core.retry.retry_unary.Retry = google.api_core.retry.retry_unary.Retry,
        timeout: typing.Optional[float] = 128,
    )

API call: refresh job properties via a GET request.

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get>

**Parameters**  
---  
**Name** | **Description**  
`timeout` |  `Optional[float]`   
The number of seconds to wait for the underlying HTTP transport before using `retry`.  
`client` |  `Optional[[google.cloud.bigquery.client.Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client)]`   
the client to use. If not passed, falls back to the `client` stored on the current dataset.  
`retry` |  `Optional[google.api_core.retry.Retry]`   
How to retry the RPC.  
  
### result
    
    
    result(
        retry: typing.Optional[
            google.api_core.retry.retry_unary.Retry
        ] = google.api_core.retry.retry_unary.Retry,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.bigquery.job.base._AsyncJob

Start the job and wait for it to complete and get the result.

**Parameters**  
---  
**Name** | **Description**  
`retry` |  `Optional[google.api_core.retry.Retry]`   
How to retry the RPC. If the job state is `DONE`, retrying is aborted early, as the job will not change anymore.  
`timeout` |  `Optional[float]`   
The number of seconds to wait for the underlying HTTP transport before using `retry`. If multiple requests are made under the hood, `timeout` applies to each individual request.  
**Exceptions**  
---  
**Type** | **Description**  
`google.cloud.exceptions.GoogleAPICallError` | if the job failed.  
`concurrent.futures.TimeoutError` | if the job did not complete in the given timeout.  
**Returns**  
---  
**Type** | **Description**  
`_AsyncJob` | This instance.  
  
### running
    
    
    running()

True if the operation is currently running.

### set_exception
    
    
    set_exception(exception)

Set the Future's exception.

### set_result
    
    
    set_result(result)

Set the Future's result.

### to_api_repr
    
    
    to_api_repr()

Generate a resource for `_begin`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
