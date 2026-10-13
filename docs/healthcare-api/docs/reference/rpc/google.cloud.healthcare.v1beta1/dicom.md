---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom/
title: Package google.cloud.healthcare.v1beta1.dicom \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:22.148012+00:00
---

# Package google.cloud.healthcare.v1beta1.dicom  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Package google.cloud.healthcare.v1beta1.dicom Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[DicomService](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomService)` (interface)
  * `[BigQueryDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.BigQueryDestination)` (message)
  * `[BigQueryDestination.WriteDisposition](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.BigQueryDestination.WriteDisposition)` (enum)
  * `[CreateDicomStoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.CreateDicomStoreRequest)` (message)
  * `[DeleteDicomStoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DeleteDicomStoreRequest)` (message)
  * `[DicomStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStore)` (message)
  * `[DicomStore.StreamConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStore.StreamConfig)` (message)
  * `[DicomStoreMetrics](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStoreMetrics)` (message)
  * `[ExportDicomDataRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ExportDicomDataRequest)` (message)
  * `[ExportDicomDataResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ExportDicomDataResponse)` (message)
  * `[GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.GcsDestination)` (message)
  * `[GcsSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.GcsSource)` (message)
  * `[GetDicomStoreMetricsRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.GetDicomStoreMetricsRequest)` (message)
  * `[GetDicomStoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.GetDicomStoreRequest)` (message)
  * `[ImportDicomDataRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ImportDicomDataRequest)` (message)
  * `[ImportDicomDataResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ImportDicomDataResponse)` (message)
  * `[ListDicomStoresRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ListDicomStoresRequest)` (message)
  * `[ListDicomStoresResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ListDicomStoresResponse)` (message)
  * `[UpdateDicomStoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.UpdateDicomStoreRequest)` (message)



## DicomService

A service for handling collections of medical images in DICOM format.

CreateDicomStore  
---  
` rpc CreateDicomStore(`[CreateDicomStoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.CreateDicomStoreRequest)`) returns (`[DicomStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStore)`) ` Creates a new DICOM store within the parent dataset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteDicomStore  
---  
` rpc DeleteDicomStore(`[DeleteDicomStoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DeleteDicomStoreRequest)`) returns (`[Empty](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Empty)`) ` Deletes the specified DICOM store and removes all images that are contained within it.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ExportDicomData  
---  
` rpc ExportDicomData(`[ExportDicomDataRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ExportDicomDataRequest)`) returns (`[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports data to the specified destination by copying it from the DICOM store. Errors are also logged to Cloud Logging. For more information, see [Viewing errors in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). The `[metadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.metadata)` field type is `[OperationMetadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1#google.cloud.healthcare.v1beta1.OperationMetadata)`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetDicomStore  
---  
` rpc GetDicomStore(`[GetDicomStoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.GetDicomStoreRequest)`) returns (`[DicomStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStore)`) ` Gets the specified DICOM store.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetDicomStoreMetrics  
---  
` rpc GetDicomStoreMetrics(`[GetDicomStoreMetricsRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.GetDicomStoreMetricsRequest)`) returns (`[DicomStoreMetrics](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStoreMetrics)`) ` Gets metrics associated with the DICOM store.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ImportDicomData  
---  
` rpc ImportDicomData(`[ImportDicomDataRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ImportDicomDataRequest)`) returns (`[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Imports data into the DICOM store by copying it from the specified source. Errors are logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). The `[metadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.metadata)` field type is `[OperationMetadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1#google.cloud.healthcare.v1beta1.OperationMetadata)`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListDicomStores  
---  
` rpc ListDicomStores(`[ListDicomStoresRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ListDicomStoresRequest)`) returns (`[ListDicomStoresResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.ListDicomStoresResponse)`) ` Lists the DICOM stores in the given dataset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateDicomStore  
---  
` rpc UpdateDicomStore(`[UpdateDicomStoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.UpdateDicomStoreRequest)`) returns (`[DicomStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStore)`) ` Updates the specified DICOM store.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## BigQueryDestination

The BigQuery table where the server writes output.

Fields  
---  
`table_uri` |  `string` BigQuery URI to a table, up to 2000 characters long, in the format `bq://projectId.bqDatasetId.tableId`  
`force` |  `bool` Use `write_disposition` instead. If `write_disposition` is specified, this parameter is ignored. force=false is equivalent to write_disposition=WRITE_EMPTY and force=true is equivalent to write_disposition=WRITE_TRUNCATE.  
`write_disposition` |  ``[WriteDisposition](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.BigQueryDestination.WriteDisposition)`` Determines whether the existing table in the destination is to be overwritten or appended to. If a write_disposition is specified, the `force` parameter is ignored.  
  
## WriteDisposition

The BigQuery WriteDisposition used by the export operation.

Enums  
---  
`WRITE_DISPOSITION_UNSPECIFIED` | Default behavior is the same as WRITE_EMPTY.  
`WRITE_EMPTY` | Only export data if the destination table is empty.  
`WRITE_TRUNCATE` | Erase all existing data in the destination table before writing the instances.  
`WRITE_APPEND` | Append data to the destination table.  
  
## CreateDicomStoreRequest

Creates a new DICOM store.

Fields  
---  
`parent` |  `string` Required. The name of the dataset this DICOM store belongs to. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.dicomStores.create`

  
`dicom_store_id` |  `string` Required. The ID of the DICOM store that is being created. Any string value up to 256 characters in length.  
`dicom_store` |  ``[DicomStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStore)`` The DICOM store to create.  
  
## DeleteDicomStoreRequest

Deletes the specified DICOM store and removes all images that are contained within it.

Fields  
---  
`name` |  `string` Required. The resource name of the DICOM store to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.dicomStores.delete`

  
  
## DicomStore

Represents a DICOM store.

Fields  
---  
`name` |  `string` Identifier. Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`.  
`notification_config` |  ``[NotificationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1#google.cloud.healthcare.v1beta1.NotificationConfig)`` Notification destination for new DICOM instances. Supplied by the client.  
`labels` |  `map<string, string>` User-supplied key-value pairs used to organize DICOM stores.Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}No more than 64 labels can be associated with a given store.  
`stream_configs[]` |  ``[StreamConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStore.StreamConfig)`` Optional. A list of streaming configs used to configure the destination of streaming exports for every DICOM instance insertion in this DICOM store. After a new config is added to `stream_configs`, DICOM instance insertions are streamed to the new destination. When a config is removed from `stream_configs`, the server stops streaming to that destination. Each config must contain a unique destination.  
  
## StreamConfig

StreamConfig specifies configuration for a streaming DICOM export.

Fields  
---  
Union field `destination`. Required. `destination` can be only one of the following:  
`bigquery_destination` |  ``[BigQueryDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.BigQueryDestination)`` Results are appended to this table. The server creates a new table in the given BigQuery dataset if the specified table does not exist. To enable the Cloud Healthcare API to write to your BigQuery table, you must give the Cloud Healthcare API service account the bigquery.dataEditor role. The service account is: `service-{PROJECT_NUMBER}@gcp-sa-healthcare.iam.gserviceaccount.com`. The PROJECT_NUMBER identifies the project that the DICOM store resides in. To get the project number, go to the Cloud Console Dashboard. It is recommended to not have a custom schema in the destination table which could conflict with the schema created by the Cloud Healthcare API. Instance deletions are not applied to the destination table.The destination's table schema will be automatically updated in case a new instance's data is incompatible with the current schema. The schema should not be updated manually as this can cause incompatibilies that cannot be resolved automatically. One resolution in this case is to delete the incompatible table and let the server recreate one, though the newly created table only contains data after the table recreation.BigQuery imposes a 1 MB limit on streaming insert row size, therefore any instance that generates more than 1 MB of BigQuery data will not be streamed.If an instance cannot be streamed to BigQuery, errors will be logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)).  
  
## DicomStoreMetrics

DicomStoreMetrics contains metrics describing a DICOM store.

Fields  
---  
`name` |  `string` Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`.  
`study_count` |  `int64` Number of studies in the store.  
`series_count` |  `int64` Number of series in the store.  
`instance_count` |  `int64` Number of instances in the store.  
`structured_storage_size_bytes` |  `int64` Total structured storage bytes for all instances in the store.  
`blob_storage_size_bytes` |  `int64` Total blob storage bytes for all instances in the store.  
  
## ExportDicomDataRequest

Exports data from the specified DICOM store. If a given resource, such as a DICOM object with the same SOPInstance UID, already exists in the output, it is overwritten with the version in the source dataset. Exported DICOM data persists when the DICOM store from which it was exported is deleted.

Fields  
---  
`name` |  `string` Required. The DICOM store resource name from which to export the data. For example, `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.dicomStores.export`

  
`filter_config` |  ``[DicomFilterConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1#google.cloud.healthcare.v1beta1.DicomFilterConfig)`` Specifies the filter configuration.  
Union field `destination`. Specifies the destination of the output.To enable the Cloud Healthcare API to write to resources in your project, such as Cloud Storage buckets, you must give the Cloud Healthcare API service account the proper permissions. The service account is: `service-{PROJECT_NUMBER}@gcp-sa-healthcare.iam.gserviceaccount.com`. The PROJECT_NUMBER identifies the project that the DICOM store resides in. To get the project number, go to the Cloud Console Dashboard. `destination` can be only one of the following:  
`gcs_destination` |  ``[GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.GcsDestination)`` The Cloud Storage output destination.The Cloud Healthcare Service Agent requires the `roles/storage.objectAdmin` Cloud IAM roles on the Cloud Storage location.  
`bigquery_destination` |  ``[BigQueryDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.BigQueryDestination)`` The BigQuery output destination.You can only export to a BigQuery dataset that's in the same project as the DICOM store you're exporting from.The Cloud Healthcare Service Agent requires two IAM roles on the BigQuery location: `roles/bigquery.dataEditor` and `roles/bigquery.jobUser`.  
  
## ExportDicomDataResponse

This type has no fields.

Returns additional information in regards to a completed DICOM store export.

## GcsDestination

The Cloud Storage location where the server writes the output and the export configuration.

Fields  
---  
`uri_prefix` |  `string` The Cloud Storage destination to export to.URI for a Cloud Storage directory where the server writes the result files, in the format `gs://{bucket-id}/{path/to/destination/dir}`). If there is no trailing slash, the service appends one when composing the object path. The user is responsible for creating the Cloud Storage bucket referenced in `uri_prefix`.  
`mime_type` |  `string` MIME types supported by DICOM spec. Each file is written in the following format: `.../{study_id}/{series_id}/{instance_id}[/{frame_number}].{extension}` The frame_number component exists only for multi-frame instances.Supported MIME types are consistent with supported formats in DICOMweb: <https://cloud.google.com/healthcare/docs/dicom#retrieve_transaction>. Specifically, the following are supported:

  * application/dicom; transfer-syntax=1.2.840.10008.1.2.1 (uncompressed DICOM)
  * application/dicom; transfer-syntax=1.2.840.10008.1.2.4.50 (DICOM with embedded JPEG Baseline)
  * application/dicom; transfer-syntax=1.2.840.10008.1.2.4.90 (DICOM with embedded JPEG 2000 Lossless Only)
  * application/dicom; transfer-syntax=1.2.840.10008.1.2.4.91 (DICOM with embedded JPEG 2000)h
  * application/dicom; transfer-syntax=* (DICOM with no transcoding)
  * application/octet-stream; transfer-syntax=1.2.840.10008.1.2.1 (raw uncompressed PixelData)
  * application/octet-stream; transfer-syntax=* (raw PixelData in whatever format it was uploaded in)
  * image/jpeg; transfer-syntax=1.2.840.10008.1.2.4.50 (Consumer JPEG)
  * image/png

The following extensions are used for output files:

  * application/dicom -> .dcm
  * image/jpeg -> .jpg
  * image/png -> .png
  * application/octet-stream -> no extension

If unspecified, the instances are exported in the original DICOM format they were uploaded in.  
  
## GcsSource

Specifies the configuration for importing data from Cloud Storage.

Fields  
---  
`uri` |  `string` Points to a Cloud Storage URI containing file(s) with content only.The URI must be in the following format: `gs://{bucket_id}/{object_id}`. The URI can include wildcards in `object_id` and thus identify multiple files. Supported wildcards:

  * '*' to match 0 or more non-separator characters
  * '**' to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a file extension (such as .dcm), which imports all files with the extension in the specified directory and its sub-directories. For example, `gs://my-bucket/my-directory/**.dcm` imports all files with .dcm extensions in `my-directory/` and its sub-directories.
  * '?' to match 1 character.

All other URI formats are invalid. Files matching the wildcard are expected to contain content only, no metadata.  
  
## GetDicomStoreMetricsRequest

GetDicomStoreMetricsRequest specifices the DICOM store to get metrics for.

Fields  
---  
`name` |  `string` Required. The resource name of the DICOM store to get metrics for. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.dicomStores.get`

  
  
## GetDicomStoreRequest

Gets the specified DICOM store.

Fields  
---  
`name` |  `string` Required. The resource name of the DICOM store to get. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.dicomStores.get`

  
  
## ImportDicomDataRequest

Imports data into the specified DICOM store. Returns an error if any of the files to import are not DICOM files. This API accepts duplicate DICOM instances by ignoring the newly-pushed instance. It does not overwrite.

Fields  
---  
`name` |  `string` Required. The name of the DICOM store resource into which the data is imported. For example, `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.dicomStores.import`

  
`blob_storage_settings` |  ``[BlobStorageSettings](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/storageinfo#google.cloud.healthcare.v1beta1.storageinfo.BlobStorageSettings)`` Optional. The blob storage settings for the data imported by this operation.  
Union field `source`. Specifies the source data location and import configuration.To enable the Cloud Healthcare API to read from resources in your project such as Cloud Storage, you must give the Cloud Healthcare API service account the proper permissions. The service account is: `service-{PROJECT_NUMBER}@gcp-sa-healthcare.iam.gserviceaccount.com`. The PROJECT_NUMBER identifies the project that the DICOM store resides in. To get the project number, go to the Cloud Console Dashboard. `source` can be only one of the following:  
`gcs_source` |  ``[GcsSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.GcsSource)`` Cloud Storage source data location and import configuration.The Cloud Healthcare Service Agent requires the `roles/storage.objectViewer` Cloud IAM roles on the Cloud Storage location.  
  
## ImportDicomDataResponse

This type has no fields.

Returns additional information in regards to a completed DICOM store import.

## ListDicomStoresRequest

Lists the DICOM stores in the given dataset.

Fields  
---  
`parent` |  `string` Required. Name of the dataset. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.dicomStores.list`

  
`page_size` |  `int32` Limit on the number of DICOM stores to return in a single response. If not specified, 100 is used. May not be larger than 1000.  
`page_token` |  `string` The next_page_token value returned from the previous List request, if any.  
`filter` |  `string` Restricts stores returned to those matching a filter. The following syntax is available:

  * A string field value can be written as text inside quotation marks, for example `"query text"`. The only valid relational operation for text fields is equality (`=`), where text is searched within the field, rather than having the field be equal to the text. For example, `"Comment = great"` returns messages with `great` in the comment field.
  * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (`=`), along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * A date field value must be written in `yyyy-mm-dd` form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (`=`) , along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * Multiple field query expressions can be combined in one query by adding `AND` or `OR` operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it's just another part of the character string to be matched. You can prepend the `NOT` operator to an expression to negate it.

Only filtering on labels is supported. For example, `labels.key=value`.  
  
## ListDicomStoresResponse

Lists the DICOM stores in the given dataset.

Fields  
---  
`dicom_stores[]` |  ``[DicomStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStore)`` The returned DICOM stores. Won't be more DICOM stores than the value of page_size in the request.  
`next_page_token` |  `string` Token to retrieve the next page of results or empty if there are no more results in the list.  
  
## UpdateDicomStoreRequest

Updates the DICOM store.

Fields  
---  
`dicom_store` |  ``[DicomStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/dicom#google.cloud.healthcare.v1beta1.dicom.DicomStore)`` The DICOM store resource that updates the resource on the server. Only the fields listed in `update_mask` are applied. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `dicomStore`:

  * `healthcare.dicomStores.update`

  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
