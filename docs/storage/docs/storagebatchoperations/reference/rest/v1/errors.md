---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/errors/
title: Storage Batch Operations API Version v1: Error Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:39.374959+00:00
---

# Storage Batch Operations API Version v1: Error Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Storage Batch Operations API Version v1: Error Catalog Stay organized with collections  Save and categorize content based on your preferences. 

## Service: storagebatchoperations.googleapis.com

When facing errors, refer to this catalog alongside using our [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If you're using your own libraries, keep this guide handy for debugging and error resolution. To know more about the error response structure, visit [the error overview page](https://cloud.google.com/apis/design/errors).

## Error codes

The following table lists HTTP status codes and associated errors that you might encounter when interacting with our API. Each status code corresponds to one or more reasons and descriptions to help you troubleshoot and handle errors effectively in your application. Within the descriptions, variables denoted by curly braces (`{}`) represent placeholders for values that are specific to your request.

**Note:** This list contains some error messages related to its API, but is not a complete list of those messages.

Reason | HTTP Status Code | Description  
---|---|---  
`JOB_ID_INVALID` | `400` | The 'job_id' is invalid. The job ID must match the pattern `[a-z0-9]([-a-z0-9]*[a-z0-9])?`. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#invalid-job-id).  
`RESOURCE_NAME_TOO_LONG` | `400` | The resource name exceeds the maximum allowed length of {max_length} bytes. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#invalid-job-id).  
`DESCRIPTION_TOO_LONG` | `400` | The job 'description' exceeds the maximum allowed length of {max_length} bytes. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#description-too-long).  
`SOURCE_NOT_SPECIFIED` | `400` | A source ('bucket_list' or 'project_source') must be specified for the job. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#source-errors).  
`TRANSFORMATION_NOT_SPECIFIED` | `400` | A transformation must be specified for the job. Specify exactly one transformation: 'delete_object', 'put_object_hold', 'put_metadata', 'rewrite_object', 'update_object_custom_context', 'set_object_acls', or 'drop_object_google_context'. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`BUCKET_LIST_EMPTY` | `400` | The 'bucket_list' must not be empty. Specify at least one bucket configuration. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#source-errors).  
`TOO_MANY_BUCKETS` | `400` | The 'bucket_list' must not exceed {max_buckets} buckets. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#source-errors).  
`BUCKET_NAME_REQUIRED` | `400` | The 'bucket' field must be specified in the bucket configuration. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#source-errors).  
`OBJECT_CONFIGURATION_REQUIRED` | `400` | An object configuration ('prefix_list', 'manifest', or 'project_source') must be specified in the bucket operation. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#source-errors).  
`MANIFEST_LOCATION_REQUIRED` | `400` | The 'manifest_location' field must be specified. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#manifest-errors).  
`MANIFEST_LOCATION_INVALID` | `400` | The manifest location '{manifest_location}' is invalid. The location must follow the format `gs://<bucket_name>/<path>/<object_name>.csv` where `<path>` is optional and `<object_name>` is followed by `.csv` and contains at most one wildcard character ('*'). For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#manifest-errors).  
`BUCKET_NAME_INVALID` | `400` | The bucket name '{bucket_name}' does not conform to Cloud Storage bucket naming requirements. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#invalid-bucket-or-object-name).  
`OBJECT_NAME_INVALID` | `400` | The object name '{object_name}' does not conform to Cloud Storage object naming requirements. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#invalid-bucket-or-object-name).  
`OBJECT_PREFIX_INVALID_UTF8` | `400` | The object prefix contains invalid UTF-8 characters. Ensure that the prefix is valid UTF-8. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#prefix-errors).  
`OBJECT_PREFIX_TOO_LONG` | `400` | The object prefix exceeds the maximum allowed length of {max_length} bytes. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#prefix-errors).  
`OBJECT_PREFIX_INVALID_CHARACTER` | `400` | The object prefix contains an invalid newline or carriage return character. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#prefix-errors).  
`OBJECT_PREFIX_OVERLAP` | `400` | The object prefix '{prefix_1}' overlaps with '{prefix_2}'. Object prefixes must not be prefixes of other included prefixes. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#prefix-errors).  
`DUPLICATE_OBJECT_PREFIX` | `400` | Duplicate object prefix '{object_prefix}' found in 'included_object_prefixes'. Remove the duplicate entry. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#prefix-errors).  
`TOO_MANY_OBJECT_PREFIXES` | `400` | The 'prefix_list' must not exceed {max_prefixes} included object prefixes. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#prefix-errors).  
`PROJECT_SOURCE_DRY_RUN_ID_INVALID` | `400` | The 'dry_run_job_id' is invalid. The job ID must match the pattern `[a-z0-9]([-a-z0-9]*[a-z0-9])?`. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#project-source-errors).  
`PROJECT_SOURCE_DRY_RUN_FIELDS_EXCLUSIVE` | `400` | When 'dry_run_job_id' is specified, all other fields in 'ProjectSource' must be empty. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#project-source-errors).  
`PROJECT_SOURCE_PROJECT_INVALID` | `400` | The project '{project}' is invalid. The project must follow the format 'projects/{project_number}' or 'projects/{project_id}'. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#project-source-errors).  
`INSIGHTS_DATASET_CONFIG_INVALID` | `400` | The insights dataset configuration '{insights_dataset_config}' is invalid. The configuration resource name must follow the format 'projects/{project}/locations/{location}/datasetConfigs/{dataset_config}'. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#insights-discovery-errors).  
`TARGET_LOCATIONS_REQUIRED_FOR_SNAPSHOT_TIME` | `400` | The 'locations' field in 'target_locations' must be specified when 'snapshot_time' is provided. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#insights-discovery-errors).  
`TOO_MANY_TARGET_LOCATIONS` | `400` | The 'target_locations' list must not exceed {max_locations} locations. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#insights-discovery-errors).  
`CEL_EXPRESSION_TOO_LONG` | `400` | The filter expression must not exceed {max_length} bytes. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#insights-discovery-errors).  
`KMS_KEY_INVALID` | `400` | The KMS key is invalid. The key must follow the format 'projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}'. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#cmek-errors).  
`REWRITE_OBJECT_MISSING_PARAMETERS` | `400` | At least one of 'storage_class' or 'kms_key' must be specified for 'RewriteObject'. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`PUT_OBJECT_HOLD_MISSING_PARAMETERS` | `400` | At least one of 'temporary_hold' or 'event_based_hold' must be specified. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`PUT_METADATA_MISSING_PARAMETERS` | `400` | At least one field in 'PutMetadata' must be specified. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`RETAIN_UNTIL_TIME_REQUIRED` | `400` | The 'retain_until_time' field must be specified in RFC 3339 format when 'retention_mode' is set. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`RETENTION_MODE_REQUIRED` | `400` | The 'retention_mode' field must be set to 'LOCKED' or 'UNLOCKED'. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`RETAIN_UNTIL_TIME_INVALID_FORMAT` | `400` | The 'retain_until_time' field must be in RFC 3339 timestamp format (for example, '2026-12-31T23:59:59Z'). For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`CUSTOM_CONTEXT_KEY_CONFLICT` | `400` | The same key cannot be specified in both 'updates' and 'keys_to_clear'. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`UPDATE_OBJECT_CUSTOM_CONTEXT_MISSING_ACTION` | `400` | At least one action in 'UpdateObjectCustomContext' must be specified. If 'clear_all' is specified, it must be set to true. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`SET_OBJECT_ACLS_MISSING_ACTION` | `400` | At least one of 'grants' or 'remove_entities' must be specified in 'SetObjectAcls'. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`UNSUPPORTED_ACL_ENTITY` | `400` | The entity '{entity}' is unsupported. Only 'allUsers' and 'allAuthenticatedUsers' are supported. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`ACL_ENTITY_CONFLICT` | `400` | The same entity cannot be specified in both 'grants' and 'remove_entities'. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#transformation-errors).  
`AUTOCLASS_STORAGE_CLASS_TRANSFORMATION_UNSUPPORTED` | `400` | Storage class transformations cannot be performed on Autoclass-enabled buckets. Disable Autoclass on the bucket or remove the storage class transformation. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#autoclass-errors).  
`UBLA_OBJECT_ACL_UPDATE_UNSUPPORTED` | `400` | Cannot update access control lists (ACLs) for objects in a bucket with uniform bucket-level access enabled. Manage access using IAM permissions instead. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#ubla-errors).  
`BUCKET_DISCOVERY_INSIGHTS_DATASET_NOT_FOUND` | `404` | Failed to perform bucket discovery. The 'insights_dataset_config' cannot be found. Verify that the insights dataset exists and is accessible. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#insights-discovery-errors).  
`BUCKET_DISCOVERY_SNAPSHOT_TOO_OLD` | `400` | Failed to perform bucket discovery. The latest dataset snapshot time is older than two days. Verify that the dataset configuration is active and generating snapshots, specify 'snapshot_time' and 'target_locations' overrides, or use a CSV manifest instead. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#insights-discovery-errors).  
`BUCKET_DISCOVERY_TOO_MANY_BUCKETS` | `400` | Failed to perform bucket discovery. Too many buckets discovered. Only 1,000 buckets are supported. For more information, see our [Troubleshooting documentation](https://cloud.google.com/storage/docs/storage-intelligence/troubleshooting#insights-discovery-errors).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
