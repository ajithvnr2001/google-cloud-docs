---
url: https://docs.cloud.google.com/healthcare-api/docs/best-practices-lros/
title: Long-running operations best practices \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:57:45.779919+00:00
---

# Long-running operations best practices  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/best-practices-lros/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Long-running operations best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for running and managing long-running operations (LROs) in the Cloud Healthcare API. For an overview of LROs in the Cloud Healthcare API, see [Managing long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations).

## LRO properties

The following sections apply to the methods listed in [Methods that return an LRO](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#methods_that_return_an_lro).

### Quota impact

LROs don't share quota with Cloud Healthcare API create, read, update, and delete (CRUD) methods that consume the following types of quota:

  * [`fhir_read_ops`](https://docs.cloud.google.com/healthcare-api/quotas#fhir_read_ops)
  * [`fhir_write_ops`](https://docs.cloud.google.com/healthcare-api/quotas#fhir_write_ops)
  * [`fhir_search_ops`](https://docs.cloud.google.com/healthcare-api/quotas#fhir_search_ops)
  * [`fhir_store_ops`](https://docs.cloud.google.com/healthcare-api/quotas#fhir_store_ops)
  * [`dicom_web_ops`](https://docs.cloud.google.com/healthcare-api/quotas#dicomweb_ops)
  * [`dicom_ops`](https://docs.cloud.google.com/healthcare-api/quotas#dicom_ops)



LRO quota is calculated using the [`fhir_store_lro_ops`](https://docs.cloud.google.com/healthcare-api/quotas#fhir_store_lro_ops) and [`dicom_store_lro_ops`](https://docs.cloud.google.com/healthcare-api/quotas#dicom_store_lro_ops) metrics.

The Cloud Healthcare API limits the number of LROs that can run concurrently in a Google Cloud project. For more information, see Limits on the number of LROs.

### Data throughput

LRO methods typically achieve higher data throughput than equivalent CRUD methods. For example, importing DICOM instances with [`dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import) typically outperforms storing the instances individually with [`dicomStores.storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/storeInstances).

Running multiple LROs concurrently might not increase data throughput due to the following constraints, especially when processing large data volumes:

  * Quota limitations
  * Resource contention
  * Other traffic that your Google Cloud project sends to the Cloud Healthcare API while an LRO runs



For maximum data throughput when running LROs, consider the following:

  * Small import and export batches typically have low throughput because of overhead.
  * LROs run and consume quota separately from other Cloud Healthcare API operations.
  * Each LRO has a maximum throughput.
  * Concurrent LROs on the same resource can cause lock contention.
  * The Cloud Healthcare API limits the number of LROs that can run concurrently in a Google Cloud project. For more information, see Limits on the number of LROs.



Plan for the number of LROs your use case requires. If you have to partition large data batches across multiple LROs, try to keep the number of partitions low.

### FHIR referential integrity

The [`fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import) method doesn't consider the [`disableReferentialIntegrity`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.disable_referential_integrity) setting. This lets you import data with arbitrary interdependencies that don't require ordering or grouping, which increases data throughput. If the input data contains invalid references or if some FHIR resources fail to import, the FHIR store's state might violate [referential integrity](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-referential-integrity).

To use `fhirStores.import`, your client application needs to ensure FHIR resource references are valid by verifying the following:

  * FHIR resource data and formatting are correct
  * Any errors that occur during the import are managed



To enforce referential integrity, use [`fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/create) or [`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle) instead of `fhirStores.import`. For more information, see [Importing FHIR data versus executing bundles](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#importing_fhir_data_versus_executing_bundles).

### Pub/Sub notifications

Some Cloud Healthcare API methods send Pub/Sub notifications for clinical events, such as the creation or deletion of a healthcare resource. For a list of methods that send Pub/Sub notifications, see [Configuring Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub).

The following import methods don't send Pub/Sub notifications:

  * [`dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import)
  * [`fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import)



If parts of your application require a notification when an import finishes, use another notification method that can list the data in the import.

### Error handling limits

The Cloud Healthcare API might not log all errors in an LRO, especially if the LRO processes large data volumes and produces many errors. Implement a way to track LRO processing and errors separately. For more information, see Resource error handling.

### Data and search indexing

Delays in search results can occur due to asynchronous search indexing. If an LRO creates or updates a FHIR resource, it might take additional time before the changes are available in search results.

For example, a search for Patient resources in a FHIR store might not return all results immediately after a FHIR import operation.

### Order of execution

LROs are scheduled based on Google Cloud resource availability. The order in which LROs execute and finish might not match the order in which they were requested.

## Avoid small import and export requests

This section describes LRO limitations when processing small data volumes.

LROs returned from import and export operations help scale data throughput by processing large amounts of data quickly and avoiding load spikes. To store small amounts of data, use another technique in [Best practices for storing data](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#best_practices_for_storing_data).

### Limits on the number of LROs

The Cloud Healthcare API limits the number of LROs that can run concurrently in a Google Cloud project. The limit is based on the following:

  * The type of LRO.
  * The amount of Google Cloud resources allocated to the LRO. This is based on the size of the input data.



If you run too many LROs, the Cloud Healthcare API rate limits, produces errors, and might reduce LRO throughput. The Cloud Healthcare API automatically conserves Google Cloud resources so that the number of LROs remains within the resource limits.

LROs are background processes, so if the load from LROs interferes with higher-priority processes, such CRUD operations, the Cloud Healthcare API can reduce LRO throughput. This ensures that the higher-priority processes are available.

### Resource allocation and cleanup overhead

When an LRO starts, the Cloud Healthcare API allocates resources. This can take several minutes because the Cloud Healthcare API has to do the following:

  1. Start a controller process.
  2. Allocate workers from a worker pool.
  3. Determine the size of the input data.
  4. Start allocating work at scale.



Stopping and cleaning up an LRO can also take several minutes.

Because of the overhead, an LRO that processes a small amount of data might spend most of its time allocating worker pools and cleaning up resources.

If you have many of these LROs, you might encounter lower data throughput because you're more likely to meet your Google Cloud project quota limits.

### Limits on requesting LRO quota

Before requesting more LRO quota, implement the [Best practices for quota management](https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management). If you still need more quota, contact [Google Cloud Customer Care](https://docs.cloud.google.com/support). To make a request, see [Best practices for requesting additional quota](https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management#request-quota).

You might need additional quota if your input data is large, for example:

  * You're importing DICOM instances that are multiple petabytes (PB) in size.
  * You're importing tens of billions of FHIR resources.



## LRO status and failure states

When you start an LRO, the response contains a unique ID. You can view an LRO's status by polling its ID. After the LRO finishes, it has one of the following states:

  * Successfully finished without errors
  * Successfully finished with some errors
  * Failed to finish, but possibly produced a partial output before failing



The following JSON example describes the response returned when an LRO finishes:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "METADATA_TYPE",
        "apiMethodName": "API_METHOD_NAME",
        "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "endTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "logsUrl": "https://console.cloud.google.com/CLOUD_LOGGING_URL"
        "counter": {
          "success": "SUCCESS_COUNT",
          // If there were any failures, they display in the `failure` field.
          "failure": "FAILURE_COUNT"
        }
      },
      "done": true,
      // The `response` field only displays if there were no errors.
      "response": {
        "@type": 
        
      },
      // If there were any errors, an `error` field displays instead of a `response` field.
      // See [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting) for a list of response codes.
      "error": {
        "code": ERROR_CODE,
        "message": "DESCRIPTION",
        "details": [
          {
            "@type": "...",
            FIELD1: ...,
            ...
          }
        ]
      }
    }
    

To get the status of an LRO, list LROs, and cancel LROs, see [Managing long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations).

### Manage LRO status and failure states

To manage LRO status and failure states, follow these best practices:

  * Poll LROs to get their status and verify when they're finished. To poll an LRO, repeatedly call the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method until the operation finishes. Use a backoff between each poll request, such as 10 seconds. When the response contains `"done": true`, the LRO has finished.
  * After an LRO finishes, check whether the response contains an `error` field. If it does, determine whether to retry the operation based on the following:

    * The error code. See [Troubleshooting LROs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting) for error codes and recommended actions.
    * The number of retries that already occurred.
    * The time between when the LRO began and when the error occurred. For example, if an LRO that normally takes several hours takes several days and hasn't returned a failure status, you might want a human to intervene. For more information about when human intervention might be required, see [Plan for final error states](https://docs.cloud.google.com/healthcare-api/docs/best-practices-latency-error-handling#plan_for_final_error_states).

See Queue an LRO for information on how to retry an LRO.

  * If you're not retrying the LRO, view the [`metadata.counter.failure`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations#Operation.FIELDS.metadata) field to see if errors occurred on specific resources. You might be able to process the resources individually. For more information, see Handling resource errors.




## Handle resource errors

An LRO can finish with errors. Errors in the LRO response follow the [Google Cloud error model](https://docs.cloud.google.com/apis/design/errors#error_model). The LRO response includes a link to Cloud Logging for more information.

### LRO error details

LRO errors in Cloud Logging have the following properties:

  * The Cloud Logging error log doesn't contain the LRO ID. Use the `operation.id` and `operation.producer` fields to find the LRO's status and errors. For example, LROs invoked from the [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import) method contain `import_fhir` in the `operation.producer` field.

If multiple LROs have the same `operation.id` and `operation.producer`, use the `createTime` and `endTime` timestamps to identify the correct LRO.

  * Not all LRO errors are available in Cloud Logging. The `metadata.counter.failure` field might exceed the number of actual errors logged due to the following:

    * Cloud Logging quota limitations
    * Cloud Logging service availability
    * LRO log limits

For example, if an LRO imports 10 million FHIR resources, and 50% of them have formatting errors, only a few hundred or a few thousand errors might be logged due to rate limiting and Cloud Logging quotas.

The number of errors logged also varies depending on how long the LRO runs while encountering high error rates. If the LRO runs slowly, it might show more errors in Cloud Logging because the errors were spread out over a long time and weren't subject to rate-limiting.




### Effects of retrying an LRO

If an LRO encounters an error and a client application automatically retries the operation using the same data, the retry might cause more errors.

Consider a scenario where a `fhirStores.import` LRO finishes with errors because some of the FHIR resources it tried to import were invalid. Automatically retrying the import with the same data might generate many `409 ALREADY_EXISTS` errors because some FHIR resources were imported in the original operation. If you query an LRO and find a failed create operation, don't automatically retry. A human should review `409 ALREADY_EXISTS` errors.

If a retry succeeds, the `metadata.counter.failure` field doesn't include errors from previous operations. This might causes an incorrect error count because the response from the successful retry doesn't include errors from previous attempts.

### Retry an LRO

If you have a a client-side processing pipeline that detects LRO errors, don't use Cloud Logging. As shown in LRO error details, the Cloud Logging error logs for LROs are unreliable and incomplete. Use the techniques in the following sections instead.

#### Retry import operations

To detect data that failed to import, compare imported data in Cloud Healthcare API to its source data in Cloud Storage. You can import data using the following methods:

  * [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import)
  * [`projects.locations.datasets.dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import)
  * [`projects.locations.datasets.hl7V2Stores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/import)



Use a unique identifier, such as a medical record number (MRN) for a FHIR Patient resource, to compare the data.

See Effects of retrying an LRO for steps to take when retrying an import operation.

Re-running an import might recreate resources that you previously deleted. Consider the following scenario:

  1. You try importing 1,000,000 FHIR resources. 50,000 resources fail due to formatting errors.
  2. You spend several days fixing the formatting errors. During that time, a patient requests that you remove their records.
  3. If you re-run the import, you risk recreating the patient's data that you deleted.



#### Retry export operations

To detect data that failed to export to BigQuery, write a script to compare unique IDs in the source data to the exported data.

You can export data to BigQuery using the following methods:

  * [`projects.locations.datasets.fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export)
  * [`projects.locations.datasets.dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export)
  * [`projects.locations.datasets.hl7V2Stores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export)



## Queue and manage LROs

If you run LROs that process large data volumes for onboarding or on a regular schedule, implement the following LRO queueing techniques:

  * Limit concurrent LROs to a small number, like `5`. You can adjust this limit depending on the size and types of LROs you run.
  * Monitor LRO completion. If errors occur, reschedule the LRO or resolve the errors separately in your processing pipeline.
  * Automatically resolve the errors in Handling resource errors when possible.

    * Understand the use case for FHIR imports to determine whether to ignore `409 ALREADY_EXISTS` errors or perform separate CRUD operations to resolve the errors. As shown in LRO error details, some `409 ALREADY_EXISTS` errors might not be logged to Cloud Logging. If your application relies on error logs, use one of the techniques in Retry an LRO.

    * To resolve a few errors, queue a smaller LRO for the data that encountered the errors or perform separate CRUD operations.

    * To resolve many errors, rerunning the LRO might be the simplest option to ensure consistency. See Retry import operations for the risks of rerunning an import on deleted data.

  * Automatically detect whether human intervention is required to address errors. You should have tools and [operational playbooks](https://sre.google/workbook/on-call/) for system administrators. Tasks to address errors might include the following:

    * Reschedule an LRO.
    * Reschedule a subset of data from a previous LRO.
    * Examine errors and address individual data elements that encountered errors. This task is only possible if you can determine that all errors in the LRO were logged.
  * Determine LRO schedules. You might schedule LROs to avoid running at peak hours when many CRUD operations are running. For more information, see [Manage quota to maximize data throughput](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#manage-quota).




## Monitor and receive alerts

Create and maintain procedures for monitoring LROs and resolving alerts. Alerts are primarily caused by LRO statuses and queueing issues. Procedures should address the following situations:

  * LROs that unsuccessfully retry more times than they're configured to.
  * Issues that require human intervention to resolve a subset of errors. For example, if an LRO fails, and the client can't resolve the errors, human intervention is likely required. See Queue and managing LROs for more information on how to resolve issues that require human intervention.
  * Queues that exceed a length or grow too quickly.
  * Policy requirements not being met, such as a a permissions issue or a misconfiguration.
  * Consistency checks that show systemic problems across multiple LROs. You might have several de-identification LROs that expect the source dataset and destination dataset to have the same number of FHIR resources. If there's a discrepancy that's growing over time, it might indicate unprocessed data.
  * LRO quota issues. For more information, see [Manage quota to maximize data throughput](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#manage-quota) and [Best practices for quota management](https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
