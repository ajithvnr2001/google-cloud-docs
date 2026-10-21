---
url: https://docs.cloud.google.com/chronicle/docs/reports/export-rawLogs-to-self-managed-gcs-bucket/
title: Export raw logs to a self-managed Google Cloud Storage bucket \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:34:08.683732+00:00
---

# Export raw logs to a self-managed Google Cloud Storage bucket  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/export-rawLogs-to-self-managed-gcs-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Export raw logs to a self-managed Google Cloud Storage bucket

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

The Data Export API facilitates the bulk export of your security data from Google Security Operations to a Google Cloud Storage bucket that you control. This capability supports critical, long-term data retention, and supports historical forensic analysis, and strict compliance requirements (such as SOX and GDPR).

For the detailed API reference information, see [Data Export API (enhanced)](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced).

The Data Export API provides a scalable and reliable solution for point-in-time data exports and handles requests of up to 100 TB. 

As a managed pipeline, it offers essential enterprise-grade features, including:

  * Automated retries on transient errors
  * Comprehensive job status monitoring
  * A full audit trail for each export job



The API logically partitions the exported data by date and time within your Google Cloud Storage bucket.

This feature lets you build large-scale data offloading workflows. Google SecOps manages the export process complexity to provide stability and performance.

## Key benefits

The Data Export API provides a resilient and auditable solution for managing the lifecycle of your security data, with the following key benefits:

  * **Reliability** : the service handles large-scale data transfers. The system uses an exponential backoff strategy to automatically retry export jobs that encounter transient issues (for example, temporary network problems), making it resilient. If your export job fails due to a transient error, it automatically retries several times. If a job fails permanently after all retries, the system updates its status to `FINISHED_FAILURE`, and the API response for that job contains a detailed error message that explains the cause. 
  * **Comprehensive auditability** : to meet strict compliance and security standards, the system captures every action related to an export job in an immutable audit trail. This trail includes the creation, start, success, or failure of every job, along with the user who initiated the action, a timestamp, and the job parameters.

**Note:** The API doesn't have a built-in scheduler to set up a daily export for compliance. To set up a recurring daily export, you must create your own automation.
  * **Optimized for performance and scale** : the API uses a robust job management system. This system includes queuing and prioritization to provide platform stability and prevent any single tenant from monopolizing resources.

  * **Enhanced data integrity and accessibility** : the system automatically organizes data into a logical directory structure within your Google Cloud Storage bucket, which helps you locate and query specific time windows for historical analysis.

  * **Security** : the API is designed to be fully compliant with customer-managed encryption keys (CMEK) (zero-trust security) and data RBAC (least-privilege access). Export jobs inherit the data visibility scope of the user triggering the request to prevent unauthorized data extraction. The export pipeline is also fully integrated with Google Cloud Key Management Service, and data remains encrypted at rest in your Google Cloud Storage bucket using your own keys.




## Key terms and concepts

  * **Export job** : a single, asynchronous operation to export a specific time range of log data to a Google Cloud Storage bucket. The system tracks each job with a unique `dataExportId`.
  * **Job status** : the current state of an export job in its lifecycle (for example, `IN_QUEUE`, `PROCESSING`, `FINISHED_SUCCESS`).
  * **Google Cloud Storage bucket** : a user-owned Google Cloud Storage bucket that serves as the destination for the exported data. 
  * **Log types** : the specific categories of logs that you can export (for example, `NIX_SYSTEM`, `WINDOWS_DNS`, `CB_EDR`). For more details, see the [list of all supported log types](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods#listlogtypes).



## Understand the exported data structure

When a job completes successfully, the system writes the data to your Google Cloud Storage bucket. It uses a specific, partitioned directory structure to simplify data access and querying.

**Directory path structure:** `gs://GCS_BUCKET_NAME/ EXPORT_JOB_NAME/LOGTYPE/EVENT_TIME_BUCKET/EPOCH_EXECUTION_TIME/FILE_SHARD_NAME.csv`

Where:

  * GCS_BUCKET_NAME: refers to the name of your Google Cloud Storage bucket.
  * EXPORT_JOB_NAME: refers to the unique name of your export job.
  * LOGTYPE: refers to the name of the log type for the exported data.
  * EVENT_TIME_BUCKET: refers to the hour range of the event timestamps of exported logs. The format is a UTC timestamp: `year/month/day/UTC-timestamp`—where `UTC-timestamp` is `hour/minute/second`. For example, `2025/08/25/01/00/00` refers to `UTC 01:00:00 AM, August 25, 2025`.
  * EPOCH_EXECUTION_TIME: refers to the Unix epoch time value, indicating when the export job began.
  * FILE_SHARD_NAME: refers to the name of the sharded files containing raw logs. Each file shard has an upper file size limit of 100 MB.



## Performance and limitations

The service has the following specific limits to ensure platform stability and fair resource allocation:

  * **Maximum data volume per job** : each individual export job can request up to 100 TB of data. For larger datasets, Google recommends breaking the export into multiple jobs with smaller time ranges.
  * **Concurrent jobs** : each customer tenant can run or queue a maximum of three export jobs concurrently. The system rejects any new job creation request that exceeds this limit.
  * **Job completion times** : the volume of exported data determines job completion times. A single job can take up to 18 hours.
  * **Export format and data scope** : the API supports bulk, point-in-time exports, with the following limitations and features: 
    * **Raw logs only** : you can only export raw logs, (not UDM logs, UDM events, or detections). To learn how to export UDM data, see [Export to a self-managed BigQuery project](https://docs.cloud.google.com/chronicle/docs/reports/export-to-customer-managed-project).
    * **Data compression** : the API exports data as uncompressed text.



## Prerequisites and architecture

This section outlines the system architecture and necessary requirements for using the Data Export API and details the system architecture. Use this information to verify that your environment is correctly configured.

**Important:** Users with global access can see all data within the permissions granted by their roles, and are not subject to data RBAC scope restrictions ([learn more](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles)).

Before using the Data Export API, complete the following prerequisite steps to set up your Google Cloud Storage destination and grant the necessary permissions:

  1. **Grant permissions to the user**. To use the Data Export API, you need the following permissions in the BYOP Google Cloud project linked to your Google SecOps tenant:

     * [chronicle.dataExports.fetchServiceAccountForDataExport](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.dataExports.fetchServiceAccountForDataExport)
     * [chronicle.dataExports.create](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.dataExports.create)
     * [chronicle.dataExports.cancel](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.dataExports.cancel)
     * [chronicle.dataExports.get](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.dataExports.get)
     * [chronicle.dataExports.list](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.dataExports.list)

These permissions form part of the following predefined IAM roles:

     * [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin): grants full permissions to create, update, cancel, and view export jobs using the API. This role confers global access.
     * [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer): grants read-only access to view job configurations and history using the API. Without the `restrictedDataAccess` role, a user with this role can view all data (see the **\+ Add Another Role** step and add a condition). 
  2. **Apply data RBAC scopes to a user**. Do the following to restrict a user to specific data access scopes:

     1. Ensure the data RBAC scopes that you want to apply are already created within the Google SecOps UI under **Settings > SIEM Settings > Data Access > Scopes**. Note the full name of each scope you intend to assign to the user. 
     2. Create an Identity and Access Management (IAM) custom role for data export management. Because predefined roles might grant too much access, or not have the specific combination of permissions, do the following to create a custom role tailored for managing data exports within a scoped context:

        1. In the Google Cloud console, go to **IAM & Admin > Roles**.
        2. Click **\+ Create Role**.
        3. Enter a title (for example, `SecOps Scoped Data Export User`).
        4. Enter an ID (for example, `secopsScopedDataExportUser`).
        5. Click **\+ Add Permissions**.
        6. Filter for Chronicle permissions and add the relevant permissions listed in the first step (**Grant permissions to the API user**).
        7. Click **Create**.
  3. **Grant IAM roles to the user**. On the IAM page, do the following to assign the necessary roles to your user:

     1. Go to **IAM & Admin > IAM**.
     2. Click **\+ Grant Access**.
     3. For **New principals** , enter the email address of the user.
     4. Do the following to assign roles:

        1. Add the custom role you created (for example, `SecOps Scoped Data Export User`).
        2. Click **\+ Add Another Role** and add the [Chronicle API Restricted Data Access](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccess) (`restrictedDataAccess`) role. This role is critical for marking the user as subject to data scopes.
  4. **Add an IAM condition to the`Chronicle API Restricted Data Access` role binding**. Do the following to link the user to specific data scopes:

     1. Click **Add IAM Condition**.
     2. Use either the Condition builder or Condition editor to define the allowed scopes, using the scope name created in the first step as the Resource name. For example, to use a scope named `scope_test`, set the condition `resource.name.endsWith("/dataAccessScopes/scope_test")`.

To learn more about how data RBAC is implemented for the Data Export API, see How data RBAC applies to the Data Export API.

  5. **Create a Google Cloud Storage bucket**. In your Google Cloud project, create a new Google Cloud Storage bucket (the destination for your exported data) in the same region as your Google SecOps tenant. Make it private, to prevent unauthorized access. For details, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  6. **Grant permissions to the Service Account**. Do the following to grant the Google SecOps Service Account, which is linked to your Google SecOps tenant, the necessary IAM roles to write data to your bucket:

     1. Call the `FetchServiceAccountForDataExport` API endpoint to identify your Google SecOps instance's unique Service Account. The API returns the Service Account email.

Example request:
            
            {
              "parent": "projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
            }
            

Example response:
            
            {
              "service_account_email": "service-1234@gcp-sa-chronicle.iam.gserviceaccount.com"
            }
            

     2. Grant the Google SecOps Service Account principal the following IAM roles for the destination Google Cloud Storage bucket, which let the Google SecOps service write exported data files to your Google Cloud Storage bucket:

        * `Storage object administrator (roles/storage.objectAdmin)`
        * `Legacy bucket reader (roles/storage.legacyBucketReader)`

For details, see [Grant access to the Google SecOps Service Account](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#grant-sa-access).

  7. **Complete the authentication**. The Data Export API authenticates your calls. To set up this authentication, follow the instructions in the following sections:

     1. [Authentication methods for Google Cloud services](https://docs.cloud.google.com/docs/authentication#authorization-gcp)
     2. [Application default credentials](https://docs.cloud.google.com/docs/authentication#adc)



## Key use cases and core workflow

The Data Export API provides a suite of endpoints to create data export jobs and manage the entire lifecycle of bulk data export. You perform all interactions using API calls.

The following use cases describe how to create, monitor, and manage data export jobs.

### Create a new data export job

The system stores data export job specifications on the _parent resource_ Google SecOps instance. This instance is the source of the log data for the export job.

  * To learn how to identify the unique Service Account for your Google SecOps instance, see [FetchServiceAccountForDataExports](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced#fetchserviceaccountfordataexports).

  * To start a new export, send a `POST` request to the `dataExports.create` endpoint. For details, see [`CreateDataExport` endpoint](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced#createdataexport). 




### Monitor data export job status

You can view data export job details and status for a specific export job, or configure a filter to view certain types of jobs.

  * To learn how to view a specific export job, see [GetDataExport](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced#getdataexport).

  * To learn how to list certain types of data export jobs using a filter, see [ListDataExport](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced#listdataexport).




### Cancel queued jobs

You can cancel a job when its status is `IN_QUEUE`.

To learn how to cancel a queued job, see [CancelDataExport](https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced#canceldataexport).

## How data RBAC applies to the Data Export API

Export jobs inherit the data RBAC scope of users creating an export job, which prevents unauthorized data extraction. 

If you attempt to export data that's beyond what your data access scope permits, the API automatically excludes such data at the time of executing the export job. The value of the `dataRbacFiltered` field in the metadata of completed jobs (that is, jobs with the status `FINISHED_SUCCESS`) indicates whether data was excluded. If `dataRbacFiltered` is `true`, some or all data selected for the export job was excluded because they fell outside the data RBAC scopes applicable to the job creator. If `dataRbacFiltered` is `false`, the export job was not impacted by data RBAC scope restrictions, and all data included as part of the job was successfully exported.

The API applies the data RBAC scopes that are applicable to the creator at the time of the job creation. Any changes in data RBAC scopes don't apply retroactively to jobs that have been already created. 

**Note:** The estimated volume indicated at the time of job creation does not account for possible data exclusions due to data RBAC scope restrictions. This might result in cases where the actual exported volume is lower than the estimated volume.

To learn more about data RBAC, see [Data RBAC overview](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

## Troubleshoot common issues

The API provides detailed error messages to help diagnose problems.

Canonical code | Error message  
---|---  
`INVALID_ARGUMENT` | `INVALID_REQUEST: Invalid request parameter PARAMETER_1, PARAMETER_2, ... PARAMETER_N. Please fix the request parameters and try again.`  
`PERMISSION_DENIED` | `INSUFFICIENT_PERMISSIONS: Unable to validate request with the current CMEK key. Please fix the CMEK key and try again`  
`NOT_FOUND` | `BUCKET_NOT_FOUND: The destination Google Cloud Storage bucket BUCKET_NAME does not exist. Please create the destination Google Cloud Storage bucket and try again.`  
`NOT_FOUND` | `REQUEST_NOT_FOUND: The dataExportId:DATA_EXPORT_ID does not exist. Please add a valid dataExportId and try again.`  
`FAILED_PRECONDITION` | `BUCKET_INVALID_REGION: The Google Cloud Storage bucket BUCKET_ID's region:REGION_1 is not the same region as the SecOps tenant region:REGION_2. Please create the Google Cloud Storage bucket in the same region as SecOps tenant and try again.`  
`FAILED_PRECONDITION` | `INSUFFICIENT_PERMISSIONS: The Service Account P4SA does not have storage.objects.create, storage.objects.get and storage.buckets.get permissions on the destination Google Cloud Storage bucket BUCKET_NAME. Please provide the required access to the Service Account and try again.`  
`FAILED_PRECONDITION` | `INVALID_CANCELLATION: The request status is in the STATUS stage and can't be cancelled. You can only cancel the request if the status is in the IN_QUEUE stage.`  
`RESOURCE_EXHAUSTED` | `CONCURRENT_REQUEST_LIMIT_EXCEEDED: Maximum concurrent requests limit LIMIT reached for the request size SIZE_LIMIT. Please wait for the existing requests to complete and try again.`  
`RESOURCE_EXHAUSTED` | `REQUEST_SIZE_LIMIT_EXCEEDED: The estimated export volume: ESTIMATED_VOLUME for the request is greater than maximum allowed export volume: ALLOWED_VOLUME per request. Please try again with a request within the allowed export volume limit.`  
`INTERNAL` | `INTERNAL_ERROR: An Internal error occurred. Please try again.`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
