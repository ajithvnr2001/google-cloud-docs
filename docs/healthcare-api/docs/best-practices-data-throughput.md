---
url: https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput/
title: Data ingestion throughput best practices \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:45.468614+00:00
---

# Data ingestion throughput best practices  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Data ingestion throughput best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for optimizing data throughput when ingesting data into the Cloud Healthcare API. These recommendations are for technical practitioners with experience in managing data throughput for large-scale systems.

## Data throughput

_Data throughput_ is the amount of resources, such as FHIR resources or DICOM instances, or bytes that the Cloud Healthcare API ingests each second.

## Data throughput constraints

The following list describes reasons why data throughput might be constrained:

  * You didn't plan for large volume requests that cause traffic spikes.
  * Bandwidth constraints slow the ingestion of large data volumes sent in a short amount of time.
  * Multiple concurrent transactions change the same Cloud Healthcare API resource which causes data contention.
  * Too many small requests are being made. For more information, see [Avoid small import and export requests](https://docs.cloud.google.com/healthcare-api/docs/best-practices-lros#avoid-small).
  * Too many long-running operations (LROs) run concurrently and bandwidth is limited.
  * Too many LROs are scheduled at the same time which leads to failures.



## Retry failed requests

If a client quickly and repeatedly retries requests after failures, it can exceed Cloud Healthcare API quotas. The following sections describe how to efficiently retry failed requests.

### Use exponential backoff with jitter and persistent retry queues

[Exponential backoff](https://wikipedia.org/wiki/Exponential_backoff) with introduced [jitter](https://wikipedia.org/wiki/Jitter) is a standard error-handling strategy for network applications. A client periodically retries failed requests with exponentially increasing delays between retries and a small, random delay.

Ensure your exponential backoff implementation is [idempotent](https://en.wikipedia.org/wiki/Idempotence) for each retry, especially if you're using custom logic to bypass failure conditions. See [9.2.2 Idempotent Methods](https://httpwg.org/specs/rfc9110.html#idempotent.methods) in the HTTP specification for more information.

Most programming languages offer libraries to simplify implementing exponential backoff and similar retry strategies. For long-term or multi-process retries, implement a _persistent retry queue_. This queue can reset the retry mechanism if you exceed the maximum backoff time.

Use exponential backoff when retrying these requests:

  * Operations that modify a FHIR resource or bundle of FHIR resources.
  * Synchronous LRO requests. Retry if there's an error when the LRO starts or if the LRO fails.

LROs have unique errors that might require you to implement the following retry strategies:

    * Use a separate bundle to store data that failed an import or create operation.
    * Use synchronous requests for data that failed to process.



### Example exponential backoff algorithm

An exponential backoff algorithm retries requests exponentially, increasing the waiting time between retries up to a maximum backoff time. The following algorithm implements [truncated exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff#Truncated_exponential_backoff) with jitter:

  1. Send a request to the Cloud Healthcare API.

  2. If the request fails, wait 1 + `random-fraction` seconds, then retry the request.

  3. If the request fails, wait 2 + `random-fraction` seconds, then retry the request.

  4. If the request fails, wait 4 + `random-fraction` seconds, then retry the request.

  5. Continue this pattern, waiting 2n \+ `random-fraction` seconds after each retry, up to a `maximum-backoff` time.

  6. After `deadline` seconds, stop retrying the request.




Use the following values as you implement the algorithm:

  * Before each retry, the wait time is `min((2n + random-fraction), maximum-backoff)`, with `n` starting at 0 and incremented by 1 for each retry.

  * Replace `random-fraction` with a random fractional value less than or equal to 1. Use a different value for each retry. Adding this random value prevents clients from becoming synchronized and sending many retries at the same time.

  * Replace `maximum-backoff` with the maximum amount of time, in seconds, to wait between retries. Typical values are 32 or 64 (25 or 26) seconds. Choose the value that works best for your use case.

  * Replace `deadline` with the maximum number of seconds to keep sending retries. Choose a value that reflects your use case.




The client can retry after reaching the `maximum-backoff` time using the same value as the backoff. For example, if the `maximum-backoff` time is 64 seconds, retry every 64 seconds. Ensure that the client doesn't retry indefinitely.

## Implement client-side rate limiting with traffic shaping

Rate limiting protects large-scale systems by preventing them from being overwhelmed by excessive requests. If client-side rate limiting isn't sufficient, the Cloud Healthcare API quota system might restrict data throughput. For more information, see [Best practices for quota management](https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management).

If you have additional requirements, like guaranteed delivery across retries, the strategies in Retry failed requests might be insufficient. [Traffic shaping](https://en.wikipedia.org/wiki/Traffic_shaping) is a rate-limiting technique that keeps the rate of client-side requests within bandwidth constraints. This spreads load spikes across hours or minutes which improves throughput. When quota is constrained, traffic shaping can achieve higher throughput than using retries alone because it avoids pushback and tracks worker units.

You can implement traffic shaping for synchronous create, delete, update, and delete (CRUD) operations, including [`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle).

### Traffic shaping requirements

To implement traffic shaping, your system must implement the following:

  * A storage-backed processing queue with redundancy to avoid disk failure.
  * Coordinated workers to pull from the processing queue.
  * Overall use detection to adjust the number of workers and their processing speed based on quota limits.
  * Disaster recovery for the storage-backed processing queue. If there's a disaster, your system must be able to purge or recover the queue.
  * Reduced LROs during peak hours. For more information, see Plan and use quota efficiently and [Queue and manage LROs](https://docs.cloud.google.com/healthcare-api/docs/best-practices-lros#queueing-and).



In the following cases, traffic shaping might only be required for a single pipeline stage:

  * Limiting the number of workers pulling from a previous pipeline step.
  * Limiting each worker individually.
  * Using a worker pool coordinator to adjust the rate at which individual units of work, such as queries per second (QPS) or ingested bytes per second, are processed.



### Implement rate limiting in other areas of your system

You can use existing programming languages and frameworks to implement traffic shaping. Consider the following open source projects and prebuilt solutions:

  * [Client-side throttling in Apache Beam](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/apachebeam-throttling). See [Horizontal autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling) for information on how to control throttling using the `numWorkers` and `maxNumWorkers` flags.

  * The Java [`RateLimiter`](https://guava.dev/releases/19.0/api/docs/index.html?com/google/common/util/concurrent/RateLimiter.html) class from the Google Guava set of core Java libraries.

  * The Python [`ratelimiter`](https://pypi.org/project/ratelimiter/) module.




For flow control, use the [high-level Pub/Sub client library](https://docs.cloud.google.com/pubsub/docs/pull#high_client_library).

#### Choose between asynchronous and synchronous processing

A client-side proxy layer that wraps requests to the Cloud Healthcare API, shown in [Handle errors at multiple layers](https://docs.cloud.google.com/healthcare-api/docs/best-practices-latency-error-handling#handle_errors_at_multiple_layers), can also control throttling across services that use the Cloud Healthcare API. Depending on the type of traffic shaping required, use one of these options:

Asynchronous
    Use asynchronous processing to queue requests and control workers. A proxy layer writes incoming requests to the queue and returns `200 OK` responses after each request is queued. This works best for write requests, but can be used for read requests in an LRO framework if clients can receive read results.
Synchronous
    

Synchronous processing provides a simple feedback mechanism if a unit of work depends on a previous unit finishing. A proxy layer delays outbound requests based on QPS or byte throughput limits, and the client blocks and waits for the proxy layer's response.

The proxy layer can adjust its rate limiting based on the number of instances, or it can coordinate with a controller process that adjusts the rate limit every few seconds. For the proxy layer to track the number of instances and their rate limits, each proxy instance can regularly read a file or make a remote procedure call (RPC) with the rate limits encoded.

Synchronous processing sometimes has the following disadvantages:

  * Resources in the client and proxy layers are unavailable while the client blocks and waits for a response. This can lead to errors, timeouts, and lowered data throughput, making it harder to scale.

  * If the client and proxy layer disconnect, more work is required to ensure data was modified as requested.




#### Use Cloud Tasks

Use [Cloud Tasks](https://docs.cloud.google.com/tasks/docs/dual-overview) to offload requests to a queue. Cloud Tasks automatically sets and monitors the following Google Cloud quotas:

  * Max burst size and max request concurrency using the [`RateLimits`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#ratelimits) object
  * Retry limits using the [`RetryConfig`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#retryconfig) object



See [Create queues](https://docs.cloud.google.com/tasks/docs/creating-queues) to create queues in Cloud Tasks. The [`Queue`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues) resource shows the options you can set on a queue. For example, you can use the [`RetryConfig`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues#RetryConfig) object to implement exponential backoff. See [Cloud Tasks client libraries](https://docs.cloud.google.com/tasks/docs/reference/libraries) for language-specific libraries.

When using Cloud Tasks, consider the following:

  * Cloud Tasks doesn't guarantee exactly once delivery. In exactly once delivery, any requests containing duplicated data are recognized as duplicates and ignored by the server. For more information, see [After Lambda: exactly once processing in Dataflow, Part 1](https://cloud.google.com/blog/products/data-analytics/after-lambda-exactly-once-processing-in-google-cloud-dataflow-part-1).
  * The maximum task size might be much smaller than the maximum FHIR bundle size in the Cloud Healthcare API. For more information, see [Cloud Tasks quotas and limits](https://docs.cloud.google.com/tasks/docs/quotas) and [Cloud Healthcare API quotas and limits](https://docs.cloud.google.com/healthcare-api/quotas).
  * Cloud Tasks has [issues and limitations](https://docs.cloud.google.com/tasks/docs/common-pitfalls).



#### Combine FHIR bundles with rate limiters

Retrying FHIR bundles with exponential backoff and rate limiters helps to maintain high data throughput and manage load spikes.

A client can send batch and transaction FHIR bundles to Cloud Tasks, which sends the requests in the bundle to the Cloud Healthcare API. If the rate limiter is full or over quota because it reached its maximum queue size and ran out of disk space, the client can implement exponential backoff to queue the bundles.

Prevent the rate limiter queue from becoming full by monitoring these resources:

  * FHIR operation quotas in the Cloud Healthcare API
  * Rate limiter quotas
  * Rate limiter errors



If the rate limiter queue becomes full, your system must alert a human and stop the client from sending requests.

## Use HTTP persistent (reusable keep-alive) connections

By default, the Cloud Healthcare API opens a new TCP connection for each CRUD request. This requires a [TCP handshake](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Protocol_operation), which can cause overhead and degrade performance. To improve performance, use [HTTP keep-alive](https://en.wikipedia.org/wiki/HTTP_persistent_connection) to keep the TCP connection open for multiple requests.

To use HTTP keep-alive in HTTP/1.1, set the `Connection` header to `keep-alive`:
    
    
    Connection: keep-alive
    

HTTP/2 uses one TCP connection for sequential and concurrent requests, which avoids the overhead automatically.

The Python [`requests`](https://requests.readthedocs.io/en/latest/user/advanced.html#keep-alive) library uses HTTP keep-alive by default. If you're using Node.js, set [`keepAlive`](https://nodejs.org/api/http.html#new-agentoptions) to `true` when you create an `http.Agent` object, and then pass the object in your request.

## Use a testing framework

A testing framework ensures your code works and helps you do the following:

  * Prepare for sudden traffic spikes in an application or pipeline.
  * Test whether exponential backoff and client-side rate limiting improve performance. Tests can show if these implementations create a backlog of tasks that must be handled separately.
  * Separate and control high-priority traffic. For example, if a user is waiting for a response, the workload on background processing tasks can be reduced to ensure the user experience isn't degraded.
  * Test synchronous and asynchronous queueing strategies for regulating traffic flow, or test if the proxy layer handles pushback.
  * Plan for disaster recovery. This typically requires resetting incoming traffic or using queues to resume traffic after the disaster ends.



## Use Cloud Monitoring

Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to monitor your test and production environments. Follow these recommendations:

  * Integrate Cloud Tasks with other Google Cloud logging and monitoring services, such as [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).
  * [Create custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics) with the Cloud Monitoring API to track key metrics like retries, queue sizes, and queue age.
  * [Create service-level objectives (SLOs)](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo) and service-level indicators (SLIs) for your environments. See [Introduction to SLIs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/overview#introduction_to_slis) for recommendations.
  * Create alerting policies using [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert). Alerting policies notify you of issues like if your system is under stress or requires human intervention.
  * Create [operational playbooks](https://sre.google/workbook/on-call/) so that system administrators know what to do if an alerting policy sends a notification.
  * Use the operational playbooks in a staging environment to respond to the following scenarios:

    * Backlogs caused by rate limiting
    * Pushback caused by exceeding quota limits
    * Incoming traffic spikes



## Prevent `429 Resource Exhausted operation_too_costly` errors

Making thousands of parallel updates each day to a FHIR resource can cause lock contention, latency, and prevents transactions from completing. Transactions that can't complete can create a backlog of `429 Resource Exhausted operation_too_costly` errors:
    
    
    HTTP/1.1 429 Too many requests
    ...
    
    {
      "issue": [
        {
          "code": "too-costly",
          "details": {
            "text": "operation_too_costly"
          },
          "diagnostics": "aborted due to lock contention while executing transactional bundle. Resource type: FHIR_RESOURCE_TYPE",
          "severity": "error"
        }
      ],
      "resourceType": "OperationOutcome"
    }
    

In the error, "cost" refers to resource usage and data throughput, not billing costs.

A `429 Too Many Requests` error doesn't always indicate a quota issue. The error can occur when the Cloud Healthcare API FHIR server detects excessive lock contention on database records. This can happen due to many operations in a FHIR bundle or a combination of CRUD operations.

Consider the following scenario:

  1. A FHIR transaction bundle that updates a Patient resource and other FHIR resources locks the Patient resource until the transaction finishes.
  2. Multiple FHIR bundles try to update the Patient resource in parallel, and lock contention occurs. Error responses include a `diagnostics` field with the text `Resource type: PATIENT`.

You can retry updating the Patient resource with exponential backoff, but long lock contention periods can lead to timeouts, reduced throughput, and increased resource usage.

  3. The Cloud Healthcare API FHIR server eventually detects a backlog of transactions and load-sheds by returning `operation_too_costly` errors. This limits traffic and prevents further errors. 

The `operation_too_costly` errors throttle all FHIR CRUD operations in your Google Cloud project, which affects all applications connected to your project.




### Troubleshoot `429 Too Many Requests` errors

To troubleshoot `429 Too Many Requests` errors, search Cloud Logging. Errors containing `operation_too_costly` indicate lock contention. If the errors are caused by resource exhaustion, check for quota issues.

If throttling occurs, transaction bundles might fail due to high levels of lock contention and produce the following error:
    
    
    HTTP/1.1 429 Too many requests
    ...
    
    {
      "issue": [
        {
          "code": "too-costly",
          "details": {
            "text": "operation_too_costly"
          },
          "diagnostics": "aborted due to cumulative heavy load or lock contention in this project while executing transactional bundle, please see https://cloud.google.com/healthcare-api/docs/troubleshooting#fhir_transaction_bundle_heavy_load for more information",
          "severity": "error"
        }
      ],
      "resourceType": "OperationOutcome"
    }
    

To troubleshoot the error, go to the [FHIR transactional bundle aborted due to cumulative heavy load](https://docs.cloud.google.com/healthcare-api/docs/troubleshooting#fhir_transaction_bundle_heavy_load) link in the `diagnostics` field.

### Avoid large bundles

The `429 Too Many Requests` error is more likely with large transaction bundles. Bundles of any size can create throughput bottlenecks. Test different bundles to find the optimal size.

Large bundles with retries can have diminishing performance returns and are more susceptible to having multiple failures. Clients should implement additional logic to manage the subset of FHIR resources that failed in a transaction.

Batch bundles can encounter `429 Too Many Requests` and `413 Request Entity Too Large` errors and throughput bottlenecks if they're large or have high QPS.

Avoid using large bundles with thousands of transactions. Instead, do the following:

  * Use smaller transaction bundles that support data consistency. If FHIR resources don't depend on each other, update them separately. For example, a FHIR resource might not depend on the specific version of another resource in the same bundle.
  * Use some batching in bundles and avoid individual requests. Batching can improve performance, but large batches can cause errors and degrade data throughput. Similar-sized batch bundles have less contention because they don't hold locks across FHIR resource updates.



Small transaction bundles avoid contention because they only hold a few locks at a time and finish quickly. This helps prevent a backlog of stacked transactions.

## LRO throughput

See [LRO data throughput](https://docs.cloud.google.com/healthcare-api/docs/best-practices-lros#data-throughput).

## FHIR data storage options

If your FHIR data volume is small to moderate, use [`fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/create) to store data. To store large volumes of FHIR resources, use `fhir.executeBundle` or [`fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import). For information on each method, see [FHIR import options](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-import).

### Import FHIR resources

Consider the following when deciding whether to use FHIR import:

  * FHIR import doesn't limit the total size of the data it imports. If a FHIR bundle exceeds [50 MB](https://docs.cloud.google.com/healthcare-api/quotas#resource_limits), you can upload the FHIR resources to Cloud Storage and import them. Avoid concurrent high-latency or large imports, or data throughput might be limited.

  * FHIR import has less complexity than using FHIR bundles. For example, you don't have to do the following:

    * Partition large bundles into smaller ones
    * Manage schedules
    * Retry transient errors at the resource or bundle level
  * FHIR import doesn't enforce referential integrity. For more information, see [FHIR referential integrity](https://docs.cloud.google.com/healthcare-api/docs/best-practices-lros#fhir-referential).

  * Don't use FHIR import when data freshness is a high priority. Imports can be fast, but could be delayed for hours or days.

  * FHIR imports perform better when there are few LROs in your Google Cloud project.

  * FHIR import can achieve high data throughput if your application can handle bulk errors and failures on a subset of resources.




### Use FHIR bundles

Use FHIR bundles instead of FHIR import in the following cases:

  * It's too expensive, in either billing costs or network bandwidth, to build a pipeline to store data in Cloud Storage and import it.

  * Referential integrity must be enforced.

  * [FHIR profile validation](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-profiles) must be enforced.

  * You need to send [Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub) when FHIR resources are stored. FHIR import doesn't support Pub/Sub notifications.

  * Data freshness is a priority and data must be ingested in seconds or minutes. However, even in a well-architected system, data throughput can be constrained by the following:

    * Upstream delays in processing pipelines. Pipelines might need more time to prepare data before the data can be ingested.
    * Backoffs, retries, and traffic shaping proxy layers.



FHIR bundles have the following limitations:

  * Quota and billing are applied to each operation in the bundle as if each operation was executed independently. For example, if a bundle has 10 `POST` operations, 5 `GET` operations, and 1 `DELETE` operation, the quota and billing applied to the bundle is the same as if those operations were executed independently.

  * Large transaction bundles are more likely to have transaction conflicts that lead to lock contention. For more information, see Prevent `429 Resource Exhausted operation_too_costly` errors.

  * Batch bundles can improve data throughput, but don't have transactional consistency capabilities like referential integrity.

  * Large batch bundles can have reduced throughput. For more information, see Avoid large bundles.




## DICOM data storage options

You can use the following methods to achieve high data throughput when sending data from a Picture Archiving and Communication System (PACS) to the Cloud Healthcare API:

The open source [Cloud Healthcare API DICOM adapter](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs) using the [DICOM message service element (DIMSE)](https://dicom.nema.org/dicom/2013/output/chtml/part07/sect_3.10.html) protocol
    

The adapter optimizes data throughput when you sync a PACS with the Cloud Healthcare API. Before syncing, run performance tests and verify that the adapter can sustain peak data throughput.

Use this adapter if you can't upload DICOM files to Cloud Storage using [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) or another transfer option. For example, you might be unable to meet these Storage Transfer Service requirements:

  * Mounting a file system to every machine that hosts agents in your [agent pool](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools) to retrieve source data.
  * If you transfer data at a regular interval instead of a one-time batch load, you must measure changes to the data's size over time to determine what's changed.
  * [Maximizing agent transfer performance](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices#sizing-agents).
  * Paying for and allocating Cloud Storage storage.
  * Validating data transfers to Cloud Storage.
  * Removing Cloud Storage resources after you import data to the Cloud Healthcare API and fix any import errors.
  * Scheduling batch ingestion intervals based on a clinical system's network and storage capacity.



We recommend you use Storage Transfer Service for a single batch load to populate a DICOM store. Using Storage Transfer Service regularly requires additional work, like a synchronous import pipeline. For more information, see [Storage Transfer Service file system transfer details](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#file_system_transfer_details).

[`dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import)
    

Use this method to store large volumes of DICOM data.

DICOMweb [Store Transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#store_transaction)
    

Use this method to store DICOM data programmatically.

## Manage quota to optimize data throughput

The following sections describe how to manage and plan quota to optimize data throughput. For general best practices on quota management, see [Quota management best practices](https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management).

### Plan quota for predictable traffic

Plan your quota requirements by first analyzing your client application's typical daily traffic. Even if traffic is predictable, plan for more quota than you need on average. This helps you avoid errors and provides a safety margin against traffic spikes or occasional increases in daily use.

The following diagram shows requests to the Cloud Healthcare API that are consistent in size and sent in predictable patterns:

![Comparison of quota usage between peak and typical hours.](https://docs.cloud.google.com/static/healthcare-api/images/predictable-peak-usage.svg)**Figure 1.** The aggregate hourly API load across datasets and data stores in a Google Cloud project.

### Plan quota for large volume requests

Avoid scheduling large batch jobs during peak hours. For more information, see [Favor low-volume transactions on a consistent basis](https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management#favor_low-volume_transactions_on_a_consistent_basis).

The following diagram shows a predictable traffic pattern. However, a large volume batch request during a peak traffic period exceeds the available quota. This can cause `429 Resource Exhausted` errors for all requests in your project.

![Comparison of quota usage between peak and typical hours with a
          higher peak.](https://docs.cloud.google.com/static/healthcare-api/images/new-peak-usage.svg)**Figure 2.** An irregular distribution of resource usage caused by a large batch job during peak hours.

If your system has additional flexibility quota, small traffic spikes won't cause errors or cause predictable peak loads to encounter errors. The small spikes must be distributed among many data stores, applications, and other clients producing load within the Google Cloud project.

To prevent a single large batch job from causing traffic spikes, see Avoid large bundles.

### Request additional quota

To maintain high data throughput and avoid `429 Resource Exhausted` errors, see the best practices on this page, especially Manage quota to optimize data throughput. These best practices ensure that your client application is robust and can scale with changes in request volume. Requesting additional quota without implementing the best practices is unlikely to prevent errors over the long term.

If you implement the best practices and still need more quota, see [Best practices for requesting additional quota](https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management#request-quota).

## Data ingestion throughput resources

For more information about data ingestion throughput, see [Manage traffic and load for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/traffic-load).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
