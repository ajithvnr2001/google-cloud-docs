---
url: https://docs.cloud.google.com/storage/docs/troubleshooting-insights/
title: Troubleshooting Storage Intelligence issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:38:35.431455+00:00
---

# Troubleshooting Storage Intelligence issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/troubleshooting-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Troubleshooting Storage Intelligence issues Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to troubleshoot common issues with [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview), [Storage Insights inventory reports](https://docs.cloud.google.com/storage/docs/insights/inventory-reports), [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets), [object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/overview) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), and [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

## Storage Intelligence configuration errors

The following sections describe errors you might encounter when [configuring or managing Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence) for a resource.

### 400: Invalid bucket name

**Issue** : The request returns `400 Bad Request` with the message `The specified bucket is not valid.`

**Solution** : The request is invalid. Ensure the request meets the following requirements:

  * Use `locations/global`. Storage Intelligence doesn't support other locations.
  * Ensure that bucket names or regular expressions in `bucket_id_regexes` are valid.



The following is an example of a valid request:
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
          "edition_config": "STANDARD",
          "filter": {
            "included_cloud_storage_buckets": {
              "bucket_id_regexes": [
                "my-bucket-name",
                "prod-data-.*"
              ]
            }
          }
        }' \
        "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/intelligenceConfig?updateMask=edition_config,filter"

### 400: Invalid argument - empty update mask

**Issue** : When you send a configuration or update request, the request returns `400 Bad Request` with the message `Empty UPDATE_MASK in the request.`

**Solution** : Provide a non-empty `UPDATE_MASK` in your request. `UPDATE_MASK` specifies a comma-separated list of [`FieldMask`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) fields in the [`IntelligenceConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig) resource to update (such as `updateMask=edition_config` or `updateMask=edition_config,filter`).

### 400: Invalid update mask path

**Issue** : When updating a configuration, the request returns `400 Bad Request` with the message `Invalid UPDATE_MASK paths.`

**Solution** : Verify that each field name in `UPDATE_MASK` matches a valid field in the [`IntelligenceConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig) resource.

### 400: Field is not editable

**Issue** : When updating a configuration, the request returns `400 Bad Request` with the message `Invalid UPDATE_MASK: UPDATE_TIME field is not editable.`

**Solution** : Remove uneditable system fields (such as `UPDATE_TIME`) from `UPDATE_MASK`. Only specify mutable fields defined in [`IntelligenceConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig).

### 400: Invalid value

**Issue** : The request returns `400 Bad Request` with the message `Invalid value at storage_intelligence.edition_config.`

**Solution** : Set [`edition_config`](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#edition-configuration) to a supported value: `INHERIT`, `STANDARD`, or `DISABLED`.

### 400: Non-empty filter

**Issue** : The request returns `400 Bad Request` with the message `Non-empty filter cannot be specified for INHERIT or DISABLED edition configuration.`

**Solution** : Remove [bucket filters](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#bucket-filters) from the request. Bucket filters aren't supported when [`edition_config`](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#edition-configuration) is set to `INHERIT` or `DISABLED`.

### 400: Empty location or bucket values in filter

**Issue** : The request returns `400 Bad Request` with the message `Empty location or bucket values in filter.`

**Solution** : Ensure that neither `location` nor `bucket` is an empty string in your [bucket filter](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#bucket-filters).

## Storage Insights common issues

This section describes how to resolve common issues with [inventory reports](https://docs.cloud.google.com/storage/docs/insights/inventory-reports) and [datasets](https://docs.cloud.google.com/storage/docs/insights/datasets).

### Multiple inventory reports generated daily

**Issue** : An inventory report configuration generates multiple report files each day.

**Solution** : Cloud Storage shards inventory reports for buckets with more than 1,000,000 objects, generating one shard per 1,000,000 objects. For example, a bucket with 3,500,000 objects generates four report shards and a [manifest file](https://docs.cloud.google.com/storage/docs/insights/inventory-reports#manifest-file) that lists each shard.

### Inventory reports not appearing in the destination bucket

**Issue** : Inventory reports don't appear in the destination bucket.

**Solution** : If reports aren't delivered to the destination bucket, verify the following:

  * Ensure the configured start date has passed. For more information, see [Create an inventory report configuration](https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports#create-report-config).

  * View your inventory report history to check for failures and their root causes. To see your inventory report history, complete the following steps:

    1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

    2. In the list of buckets, click the name of the source bucket that contains the inventory report configuration.

    3. On the **Bucket details** page, click the **Inventory reports** tab.

    4. In the list of inventory report configurations, click the UUID of the inventory report configuration that generated the reports you want to check.

    5. Check for failures in the **Inventory report history** section. You can hold the pointer over **Help** (help) to get details about why a failure occurred.

  * Make sure the project-level service agent is granted the IAM roles required for reading and writing inventory reports. For more information, see [Grant required roles to the service agent](https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports#grant-permissions-to-service-account).




### Inventory report delays

**Issue** : Inventory report generation is delayed.

**Solution** : Report generation times vary. Delays of up to 24 hours are normal.

### Datasets not getting populated

**Issue** : Storage Insights dataset tables remain empty.

**Solution** : In your linked BigQuery dataset, check `error_attributes_view` for error codes. For more information, see [Troubleshoot dataset errors](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#troubleshoot-error-codes).

### Null values in 'ref' column when querying datasets

**Issue** : When querying Storage Insights datasets in BigQuery, the `ref` column returns `null`.

**Solution** : For objects ending in `/`, the `ref` column in datasets is null.

If the `ref` column returns null values when you query Storage Insights datasets in BigQuery, verify that you have granted the required connection permissions and roles, including access to Cloud Storage resources, as described in [Analyze object data and metadata using BigQuery](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#analyze-object-data).

## Object enrichments errors

**Preview — Object enrichments**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This section describes how to resolve common issues when configuring, generating, or querying [object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/overview).

### Enrichments are missing for objects

**Issue** : Object enrichments don't appear on objects after you configure object enrichments.

**Solution** : Verify the following:

  * **Service agent permissions** : Ensure that you grant the object enrichments service agent the `roles/storage.annotationGeneratorService` role on the target bucket (or project) and the `roles/storage.bucketViewer` role on the project. For instructions, see [Grant permissions to the service agent](https://docs.cloud.google.com/storage/docs/object-enrichments/configure-object-enrichments#grant-permissions).
  * **Filter and scope configuration** : Ensure that your `FeatureConfig` resource explicitly includes the target bucket name. Cloud Storage doesn't automatically include buckets created after you create the `FeatureConfig` resource. Additionally, if you delete and recreate or [relocate](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) a bucket, you must update the `FeatureConfig` resource to re-include it.
  * **Model prerequisites and`Content-Type` metadata**: Verify that objects meet the content type and size limits for your enabled models. Cloud Storage uses the object's [`Content-Type`](https://docs.cloud.google.com/storage/docs/metadata#content-type) metadata field to determine eligibility (`BMP`, `GIF`, `ICO`, `JPEG`, `PNG`, `TIFF`, or `WEBP` for images; `application/pdf` for PDF classification). If the `Content-Type` metadata is missing or incorrect, Cloud Storage doesn't process the object until you update its metadata. Additionally, the object enrichments service skips objects larger than 20 MiB. For more information, see [Supported models and schemas](https://docs.cloud.google.com/storage/docs/object-enrichments/models).
  * **Processing latency** : Allow sufficient time for asynchronous processing. The object enrichments service processes objects asynchronously. Enrichments for newly uploaded objects typically appear within several hours. In contrast, backfilling existing objects in large buckets can take hours or days.



### Object enrichments aren't visible in BigQuery

**Issue** : Object enrichments appear in the API but don't appear in BigQuery.

**Solution** : Check the following:

  * **Storage Insights datasets configuration** : Verify that you have [configured Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) for the bucket.
  * **Daily report schedule** : Wait for the daily dataset update. Storage Insights datasets update every 24 hours. Therefore, newly generated enrichments might take up to 24 hours to appear in the `object_contexts_catalog_view` view in BigQuery.
  * **IAM permissions** : Ensure that you have permissions to run jobs and read data in BigQuery (such as `roles/bigquery.jobUser` and `roles/bigquery.dataViewer`). For query guidance, see [Analyze object enrichments in BigQuery](https://docs.cloud.google.com/storage/docs/object-enrichments/analyze-bigquery).



### Permission denied when retrieving extended object enrichments data

**Issue** : A permission error occurs when retrieving extended object enrichments data.

**Solution** : You must have the `storage.objects.viewFullContext` permission on the object or bucket to retrieve extended data, such as bounding box coordinates or category confidence scores. Roles such as Storage Object User (`roles/storage.objectUser`) and Storage Admin (`roles/storage.admin`) include this permission. For more information, see [Manage object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/manage-object-enrichments#required-roles).

### Permission denied when managing feature configurations

**Issue** : A permission error occurs when creating, updating, or deleting a [`FeatureConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs).

**Solution** : Verify that your account has the Storage Admin (`roles/storage.admin`) role or a custom role with the necessary permissions on the target project. These required permissions include `storage.featureConfigs.create`, `storage.featureConfigs.update`, or `storage.featureConfigs.delete`. For method-specific permissions, see [Configure object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/configure-object-enrichments#required-roles) and the [`featureConfigs` API resource](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs).

## Storage batch operations job validation errors

This section describes validation errors that occur when submitting a [batch operations job](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs) request to `storagebatchoperations.googleapis.com`.

### 400: Invalid job ID or resource name

**Issue** : The job creation request returns a `400 Bad Request` (`INVALID_ARGUMENT`) response with the reason `JOB_ID_INVALID` or `RESOURCE_NAME_TOO_LONG`.

**Solution** : Verify that the job ID consists of 1–63 lowercase alphanumeric characters or hyphens (`[a-z0-9]([-a-z0-9]*[a-z0-9])?`), and that the full job resource path (`projects/PROJECT_ID/locations/LOCATION/jobs/JOB_ID`) doesn't exceed 200 bytes. If the path exceeds 200 bytes, shorten the job ID. For more information, see [Job name](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-name).

### 400: Job description exceeds limit

**Issue** : The job creation request returns a `400 Bad Request` (`INVALID_ARGUMENT`) response with the reason `DESCRIPTION_TOO_LONG`.

**Solution** : Ensure the job description is 1,024 bytes or fewer. If it exceeds this limit, shorten the text. For more information, see [Job description](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-description).

### 400: Missing or invalid job source configurations

**Issue** : The job creation request returns a `400 Bad Request` (`INVALID_ARGUMENT`) response with any of the following reasons:

  * `SOURCE_NOT_SPECIFIED`
  * `BUCKET_LIST_EMPTY`
  * `TOO_MANY_BUCKETS`
  * `MULTI_BUCKET_NOT_SUPPORTED`
  * `BUCKET_NAME_REQUIRED`
  * `OBJECT_CONFIGURATION_REQUIRED`



**Solution** : Ensure that your job specifies a valid source configuration (`bucket_list` or `project_source`) and that each bucket defines an object selection method. For more information, see [Create and manage batch operations jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

### 400: Invalid bucket or object name

**Issue** : The job creation request returns a `400 Bad Request` (`INVALID_ARGUMENT`) response with the reason `BUCKET_NAME_INVALID` or `OBJECT_NAME_INVALID`.

**Solution** : Ensure that all bucket and object names comply with Cloud Storage naming requirements. For more information, see [Bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming) and [Object naming guidelines](https://docs.cloud.google.com/storage/docs/objects#naming).

### 400: Project source configuration errors

**Issue** : The job creation request returns a `400 Bad Request` (`INVALID_ARGUMENT`) response with any of the following reasons:

  * `PROJECT_SOURCE_PROJECT_INVALID`
  * `PROJECT_SOURCE_DRY_RUN_FIELDS_EXCLUSIVE`
  * `PROJECT_SOURCE_DRY_RUN_ID_INVALID`



**Solution** : Verify that your project source configuration meets formatting and field exclusivity requirements. If you specify a dry-run job ID, omit all other `project_source` parameters. For more information, see [Create a job using advanced filters](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#advanced-filters).

### 400: Conflicting or missing transformation parameters

**Issue** : The job creation request returns a `400 Bad Request` (`INVALID_ARGUMENT`) response with any of the following reasons:

  * `TRANSFORMATION_NOT_SPECIFIED`
  * `REWRITE_OBJECT_MISSING_PARAMETERS`
  * `PUT_OBJECT_HOLD_MISSING_PARAMETERS`
  * `PUT_METADATA_MISSING_PARAMETERS`



**Solution** : Specify exactly one transformation type with all required parameters. If configuring object retention, verify that [Object Lock](https://docs.cloud.google.com/storage/docs/object-lock) is enabled on the bucket and that timestamps use RFC 3339 UTC format. For more information about parameter requirements by transformation, see [Job type](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-type).

### 400: Overlapping or duplicate object prefixes

**Issue** : The job creation request returns a `400 Bad Request` (`INVALID_ARGUMENT`) response with the reason `OBJECT_PREFIX_OVERLAP` or `DUPLICATE_OBJECT_PREFIX`.

**Solution** : Remove duplicate prefixes and ensure that no prefix in `included_object_prefixes` is a prefix of another entry in the list. For more information, see [Object prefixes](https://docs.cloud.google.com/storage/docs/batch-operations/overview#object-prefixes).

### 400: Manifest file formatting and access issues

**Issue** : The job creation request returns a `400 Bad Request` (`INVALID_ARGUMENT`) response with the reason `MANIFEST_LOCATION_REQUIRED` or `MANIFEST_LOCATION_INVALID`, or the job can't read the manifest.

**Solution** : Verify that the manifest URI is a valid CSV path (`gs://<bucket_name>/<path>/<object_name>.csv`) and that the Storage batch operations service agent has the `roles/storage.objectViewer` role on the manifest bucket. For more information about CSV formatting and schema requirements, see [Manifest](https://docs.cloud.google.com/storage/docs/batch-operations/overview#manifest).

### 400: Storage Insights dataset discovery errors

**Issue** : Using an Storage Insights dataset for object discovery returns a `400 Bad Request` (`INVALID_ARGUMENT` or `FAILED_PRECONDITION`) response with any of the following reasons:

  * `BUCKET_DISCOVERY_SNAPSHOT_TOO_OLD`
  * `TARGET_LOCATIONS_REQUIRED_FOR_SNAPSHOT_TIME`
  * `BUCKET_DISCOVERY_TOO_MANY_BUCKETS`



**Solution** : Verify that `snapshot_time` is within the last 48 hours, specify `target_locations` for the buckets, and ensure the discovery query matches no more than 1,000 buckets. For more information, see [Create a manifest using Storage Insights datasets](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#create-manifest-using-insights-datasets).

### 400: Storage class transformation fails on Autoclass-enabled buckets

**Issue** : The job creation request returns a `400 Bad Request` (`FAILED_PRECONDITION`) response with the reason `AUTOCLASS_STORAGE_CLASS_TRANSFORMATION_UNSUPPORTED`.

**Solution** : You can't run storage class transformations on buckets with [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass#transitions) enabled. Either target a bucket without Autoclass or remove the storage class transformation. For more information, see [Autoclass restrictions](https://docs.cloud.google.com/storage/docs/autoclass#transitions).

### 400: Object ACL updates fail on uniform bucket-level access buckets

**Issue** : The job creation request returns a `400 Bad Request` (`FAILED_PRECONDITION`) response with the reason `UBLA_OBJECT_ACL_UPDATE_UNSUPPORTED`.

**Solution** : You can't update object ACLs on buckets with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access#enabled) enabled. Manage access using IAM roles at the bucket or project level instead. For more information, see [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access#enabled).

## Storage batch operations runtime and execution issues

This section describes issues that occur during the asynchronous execution of a batch operations job.

### 403: Permission errors during execution

**Issue** : A batch job fails during execution with `403 Forbidden` (`PERMISSION_DENIED`).

**Solution** : Grant the Storage batch operations service agent (`service-PROJECT_NUMBER@gcp-sa-storagebatchoperations.iam.gserviceaccount.com`) the required IAM roles for your transformation type. For more information, see [Grant permissions to the service agent](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

### CMEK encryption errors during object rewrite

**Issue** : Object rewrites fail with `400 Bad Request` or `403 Forbidden` due to Cloud KMS key status or permission errors.

**Solution** : Verify that the Cloud KMS key is `Enabled` and resides in the same region as the target bucket, and that the service agent has the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role. For more information, see [Job type: Rewrite object](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-type).

### High failure count in error_summaries

**Issue** : A batch job completes with a non-zero `counters.failed_object_count` and error codes in `error_summaries` (such as `404 NOT_FOUND`, `412 FAILED_PRECONDITION`, or `403 PERMISSION_DENIED`).

**Solution** : Run [`gcloud storage batch-operations jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/describe) with the `--location` flag (for example, `gcloud storage batch-operations jobs describe JOB_ID --location=LOCATION`) to view the aggregated error breakdown, and check Cloud Logging for per-object error logs. For more information, see [Get job details](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#get-batch-operation-jobs).

### Storage batch operations job fails due to a snapshot that's over two days old

**Issue** : When you create a CEL filter-based [storage batch operations job](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#advanced-filters), job creation fails. The error message states that the snapshot time is older than two days.

**Solution** : To prevent actions on outdated object states, storage batch operations automatically fails job creation. This failure occurs if the selected snapshot is older than two days. Select one of the following methods to resolve this issue:

  * **Use a manifest file** : Query your dataset manually in BigQuery. Export the results to a CSV manifest file, and upload the file to a Cloud Storage bucket. You can then [create the batch operations job using the manifest method](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#method-manifest) to avoid the two-day limit.
  * **Check dataset configurations** : Verify that your [dataset configurations](https://docs.cloud.google.com/storage/docs/insights/datasets) are active and not paused. Confirm that dataset snapshots run successfully. For information about how to verify your configurations, see [View a dataset configuration](https://docs.cloud.google.com/storage/docs/insights/manage-datasets#view).
  * **Use target location and snapshot time overrides** : Specify the `--target-snapshot-time` flag to bypass the two-day staleness failure by explicitly selecting a snapshot in RFC 3339 format. Specify the `--target-locations` flag to limit the operation to the locations where the snapshot exists. You can use these overrides to resolve synchronization delays that prevent the automated global snapshot from updating. Consequently, you can manually target a more recent regional snapshot. For the command syntax, see [Create a job using advanced filters](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#advanced-filters).

**Caution:** Providing a manual manifest file or overriding the snapshot age bypasses the safety checks designed to prevent actions on outdated object states. Under normal operations, Storage Insights updates dataset snapshots once every 24 hours. Before using these bypass methods, verify that targeting objects based on older metadata is safe for your workload. 

### CEL filter-based storage batch operations job fails on newly subscribed projects

**Issue** : Running a CEL filter-based storage batch operations job on a newly subscribed project fails because the system cannot find a valid snapshot.

**Solution** : After you enable the [Storage Intelligence](https://docs.cloud.google.com/storage/docs/insights/datasets) subscription, you must wait 24 hours before running CEL filter-based storage batch operations jobs. This delay lets the system perform the initial metadata snapshot and establish the starting snapshot time.

### CEL filter-based storage batch operations job fails with permissions errors or throws runtime errors

**Issue** : A CEL filter-based storage batch operations job fails during execution or returns runtime permissions errors.

**Solution** : storage batch operations uses your user credentials to process objects. The job fails if you don't have the necessary IAM reader or writer permissions on the targeted buckets and objects. This issue occurs when your CEL filters select resources that you don't have access to. Confirm that your account has the Storage Admin (`roles/storage.admin`), Storage Object Admin (`roles/storage.objectAdmin`), or equivalent roles for all buckets and objects in the scope of the job. For instructions on granting roles, see [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Monitoring and log analysis

For more information about inspecting per-object execution failures and error payloads in Cloud Logging, see [View storage batch operations logs](https://docs.cloud.google.com/storage/docs/batch-operations/configure-logs#view-logs).

## Storage Intelligence advisor issues

This section provides guidance on how to resolve commonly encountered issues when using [Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview).

### Storage Intelligence advisor permission denied errors

**Issue** : You receive a `Permission denied` error when you access Storage Intelligence advisor, and charts and metrics are empty or show permission errors.

**Solution** : This issue occurs if you don't have an IAM role with the required permissions to view Storage Intelligence advisor. Ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the project, folder, or organization that you want to view. For a list of required permissions, see [Required roles](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#required-roles).

### Insufficient permissions to view an affected project

**Issue** : When you view findings at the organization or folder level, the **Projects with findings detected** panel displays a warning indicator with the message `You've insufficient permission to access this project` next to a project.

**Solution** : This issue occurs if you have permissions to view Storage Intelligence advisor at the organization or folder level, but lack the required IAM permissions on that specific project. Ask the project administrator to grant you the Storage Admin (`roles/storage.admin`) role on the affected project.

### Storage Intelligence advisor is empty or data is missing

**Issue** : The Storage Intelligence advisor page loads, and the charts, metrics in the **At a glance** section (labeled **Project at a glance** , **Folder at a glance** , or **Organization at a glance** depending on the selected resource), or the **Top findings** section are empty or the data is outdated.

**Solution** : This issue can occur for the following reasons:

  * **Data processing latency** : Storage Intelligence metrics and findings rely on daily snapshots and analysis of storage usage. Data can take 24 to 48 hours to appear in Storage Intelligence advisor. Such delays typically occur after you create new buckets or when you view Storage Intelligence advisor for the first time. If you expect to see recent activity data, wait 48 hours and then check again.
  * **No storage resources** : If the selected project, folder, or organization doesn't contain any buckets or objects for the selected time period, Storage Intelligence advisor is empty. Choose a different project, folder, or organization that contains storage resources.
  * **Incorrect time filter** : The time filter is set to a range where no storage activity occurred. Adjust the time filter to a range that includes storage activity.



### Findings are not appearing in Storage Intelligence advisor

**Issue** : You expect to see findings in the **Top findings** section based on recent storage activity, but the section is empty.

**Solution** : This issue occurs if Storage Intelligence advisor generates no findings for the selected time period. A lack of findings can occur for the following reasons:

  * **No matching patterns** : The most recent analysis cycle detected no storage behavior that matches a finding pattern.
  * **Data processing delays** : Findings rely on storage metrics, which take 24 to 48 hours to process. Findings for events that occurred in the last 24 hours appear after the next processing cycle completes.



### Issues when using VPC Service Controls

**Issue** : You receive access denied or permission errors when you try to access Storage Intelligence advisor from a project inside a VPC Service Controls service perimeter.

**Solution** : This issue occurs if VPC Service Controls is not configured correctly to allow communication between your project, the Google Cloud console, and Storage Intelligence resources. To resolve this issue, review the following requirements:

  * **Restricted services** : Verify whether the service perimeter restricts the Cloud Storage API (`storage.googleapis.com`) and the Storage Insights (`storageinsights.googleapis.com`) API. For details, see [List and describe service parameters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#list-and-describe).
  * **Perimeter configuration** : Verify that the project that you are using to view Storage Intelligence advisor is in the same service perimeter as the projects you monitor. If they are in different perimeters, you must [configure ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) or [use perimeter bridges](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters).
  * **Access from outside the perimeter** : If you access the Google Cloud console from a network outside the perimeter, you must create an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) or an [access level](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels#create_an_access_level) that includes your user account and the public IP address range that you are using.
  * **Shared VPC** : If you use Shared VPC, verify that the project is in the same service perimeter as your service projects. For details, see [Shared VPC](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#shared_vpc).
  * **Audit logs** : Use the [violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer) to check for VPC Service Controls violations in your audit logs. The violation analyzer helps diagnose the violation and identify causes, such as a `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` error.



## What's next

  * [Overview of Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview)
  * [Configure and manage Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence)
  * [Overview of object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/overview)
  * [Create and manage batch operations jobs](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs)
  * [Analyze object data and metadata using BigQuery](https://docs.cloud.google.com/storage/docs/insights/configure-datasets#analyze-object-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
