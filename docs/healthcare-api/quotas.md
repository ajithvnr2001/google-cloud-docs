---
url: https://docs.cloud.google.com/healthcare-api/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:56.568987+00:00
---

# Quotas and limits  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Resources ](https://docs.cloud.google.com/healthcare-api/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Healthcare API enforces limits on resource usage for a variety of reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Google Cloud also offers [free trial quotas](https://cloud.google.com/free/docs/free-trial-quotas) that provide limited access for users that are exploring Google Cloud, including Cloud Healthcare API.

Quotas for Cloud Healthcare API are enforced by project on either a per-region or multi-region basis. Quota exhaustion in a single region doesn't affect your usage of Cloud Healthcare API in other regions.

## Checking your quotas and usage

Quotas are limits on storage (also called ingress limits) and operations.

To check the available quota for resources in your project, go to the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in Google Cloud console.

To display only Cloud Healthcare API quotas, in the **Filter table** drop-down list, select **Service** and then select **Cloud Healthcare API**.

Not all projects have the same quotas. As your use of Cloud Healthcare API expands over time, your quotas can increase accordingly. If you expect a notable upcoming increase in usage, you can proactively request quota adjustments from the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in Google Cloud console. There is no charge for requesting an increase in quota. Your costs increase only if you use more resources.

## Resource limits

Cloud Healthcare API limits the size of the content of a request, such as the size of an X-ray image in a DICOM request. You cannot request a change to a resource limit; however, in some situations you can use an import operation to import content that is larger than a resource limit.

The following resource limits apply and are subject to change.

Modality | Request size limit  
---|---  
DICOM | 

  * [Store transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#store_transaction): Unlimited. All other methods 10 MB.
  * Store transaction or [retrieve transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#retrieve_transaction): Timeout occurs if the operation exceeds 30 minutes.
  * [Search transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#search_transaction) methods have a maximum offset of 1,000,000 and maximum limit of 5,000 for studies/series and 50,000 for instances.
  * [De-identification](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-deidentify): De-identification cannot process DICOM files larger than 1 GB if pixel redaction is involved. If the Pixel Data is compressed, its uncompressed size cannot exceed 2 GB. The uncompressed size can be calculated using DICOM tags as follows: `NumberOfFrames * Rows * Columns * SamplesPerPixel * BitsAllocated / 8`.
  * Ingested DICOM files have a limit of 4 GB per tag. This limit does not apply for values with undefined length.
  * When transcoding DICOM data, the maximum file size is 1 GB and the maximum frame size is 150 MB.
  * When applying the [`viewport`](https://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_8.3.5.html#sect_8.3.5.1.3) query parameter on rendered resources, the maximum frame size is 50 MB, and the maximum dimension (width or height) is 10,000 pixels.
  * [`dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores/import): Maximum file size is 100 GB.

  
FHIR | 

  * [`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle): 50 MB. You might encounter limitations based on the number of entries in a bundle. For more information, see FHIR `executeBundle` size limits.
  * [`fhir.Binary-create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Binary-create): 1 GB
  * [`fhir.Binary-update`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Binary-update): 1 GB
  * All other methods: 10 MB. This limit applies to the internal representation of the resource, not the size of the JSON payload you send. A resource that meets this limit might have a JSON payload larger than 10 MB.

  
HL7v2 | Size of the base64-encoded `data` field: 10 MB  
  
If you attempt to process content larger than the associated resource limit, an error occurs.

### FHIR executeBundle size limits

You can use the [`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle) method to perform multiple FHIR operations in a single API request. The number of operations depends on the number of entries in a batch or transaction bundle. This approach is more efficient than making individual API calls for each operation.

Processing times for `fhir.executeBundle` requests increase with the number of entries in the bundle. Factors like resource contention (for example, updating the same resource as part of many transaction bundles in parallel) can also impact performance. For examples of when resource contention can occur and how to prevent it from causing errors, see [Data throughput best practices](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput). Large bundles, especially those exceeding 1,000 entries, might time out and fail to complete.

To ensure successful and timely processing, consider these limits when sending your `fhir.executeBundle` requests:

  * Transaction bundles: Bundles exceeding 4,500 entries are immediately rejected to prevent timeouts. Transaction bundles require all operations to succeed.
  * Batch bundles: No specific entry limit exists, but larger bundles increase the risk of timeouts. Timeouts might result in partial success, with only some entries processed.



## Using import operations for content that exceeds resource limits

Import operations permit you to process content that is larger than the associated resource limit. The content size in an import operation is limited only by the Google Cloud maximum storage size of 5 TB for individual objects. Import operations are subject to storage quotas that determine how long an import operation takes. You might want to use an import operation, for example, if you want to store many DICOM instances in a DICOM store and don't want to be subject to the request size limit. Rather than uploading the instances using the available [Store Transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#store_transaction) methods, you could instead upload the instances into a Cloud Storage bucket and then import them into the DICOM store.

For detailed steps to import DICOM data using an import operation, see [Importing and exporting DICOM data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export).

For detailed steps to import FHIR resources using an import operation, see [Importing and exporting FHIR Resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export).

For detailed steps to import HL7v2 messages using an import operation, see [Import HL7v2 messages from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/hl7v2-storage-import).

## Request a change to quota

To request a change to a quota, you must have `serviceusage.quotas.update` permission. This permission is included by default for the following [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles): Owner, Editor, and Quota Administrator.

  1. Go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the **Quotas** page, select the quotas that you want to change. If you want to display only Cloud Healthcare API quotas, select **Service** from the **Filter table** drop-down list and then select **Cloud Healthcare API**.

  3. Check the boxes of the quotas that you want to edit.

  4. Click the **Edit Quotas** button at the top of the page.

  5. Fill out the form and then click **Next**.

  6. Enter the limits that you are requesting and then click **Next**.

  7. Click **Submit request**.




A request to decrease quota is rejected by default. If you want to reduce your quota, reply to the support email with an explanation of your requirements. A support representative will respond to your request.

You will receive a response from the Cloud Healthcare API team within 24 to 48 hours of your request.

Plan to request additional resources at least a few days in advance to make sure that there is enough time to fulfill your request.

## Location quota requests

You can request a quota increase for the Cloud Healthcare API in a specific [region](https://docs.cloud.google.com/healthcare-api/docs/regions), or in a [multi-region location](https://docs.cloud.google.com/healthcare-api/docs/regions#multi-regional_locations).

To request a quota increase in a single region: In your quota increase request, specify the region.

To request a quota increase in a multi-region location:

  * For a quota increase in the `us` multi-region, state in your request that the quota is for "US meta region."
  * For a quota increase in the `eu` multi-region, state in your request that the quota is for "EU meta region."



## Quota limits

The following sections describe the quotas associated with Cloud Healthcare API data stores and operations.

### DICOM quotas

The following table describes the Cloud Healthcare API quotas associated with DICOM stores and DICOM operations.

Metric name | Display name | Description | `dicomweb_ops` | Number of DICOMweb operations per minute per region | Includes the following methods: 

  * All `projects.locations.datasets.dicomStores.studies` methods in [v1beta1](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores.studies) and [v1](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies)
  * All `projects.locations.datasets.dicomStores.studies.series` methods in [v1beta1](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores.studies.series) and [v1](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series)
  * All `projects.locations.datasets.dicomStores.studies.series.instances` methods in [v1beta1](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores.studies.series.instances) and [v1](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances)
  * All `projects.locations.datasets.dicomStores.studies.series.instances.frames` methods in [v1beta1](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores.studies.series.instances.frames) and [v1](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances.frames)

  
---|---|---  
`dicom_structured_storage_bytes` | Structured DICOM storage ingress in bytes per minute per region | Structured bytes, in the form of DICOM tags and related metadata, sent to the Cloud Healthcare API while processing `dicomweb_ops` operations.  
`dicom_store_ops` | Number of DICOM store operations per minute per region | Operations on the DICOM store, not DICOM data. Includes the following methods:  


  * [`dicomStores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/create)
  * [`dicomStores.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/delete)
  * [`dicomStores.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/get)
  * [`dicomStores.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/list)
  * [`dicomStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/patch)

  
`dicom_store_lro_ops` | Number of DICOM store long-running operations per minute per region | Operations on the DICOM store, not DICOM data, that return a long-running operation. Includes the following methods:  


  * [`dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export)
  * [`dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import)
  * [`dicomStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/deidentify)

  
`dicom_structured_storage_operations_bytes` | Structured DICOM storage ingress for long-running operations in bytes per minute per region | Structured bytes, in the form of DICOM tags and related metadata, sent to the Cloud Healthcare API while processing `dicom_store_lro_ops` operations.  
  
### FHIR quotas

The following table describes the Cloud Healthcare API quotas associated with FHIR stores and FHIR operations.

Metric name | Display name | Description | `fhir_read_ops` | Number of FHIR read operations per minute per region | Measured in units, where one unit is one read request on an individual FHIR resource.  
  
Includes the following methods:  
**v1beta1:**

  * [`fhirStores.fhir.ConceptMap-translate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/ConceptMap-translate)
  * [`fhirStores.fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/executeBundle)
  * [`fhirStores.fhir.capabilities`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/capabilities)
  * [`fhirStores.fhir.read`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/read)
  * [`fhirStores.fhir.vread`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/vread)
  * [`fhirStores.fhir.history`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/history)
  * [`fhirStores.fhir.Resource-validate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Resource-validate)
  * [`fhirStores.fhir.Consent-enforcement-status`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Consent-enforcement-status)

**v1:**

  * [`fhirStores.fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle)
  * [`fhirStores.fhir.capabilities`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/capabilities)
  * [`fhirStores.fhir.read`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/read)
  * [`fhirStores.fhir.vread`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/vread)
  * [`fhirStores.fhir.history`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/history)
  * [`fhirStores.fhir.Resource-validate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Resource-validate)

  
---|---|---  
`fhir_write_ops` | Number of FHIR write operations per minute per region | Measured in units, where one unit is one create, update, or delete request on an individual FHIR resource.  
  
Includes the following methods:  
**v1beta1:**

  * [`fhirStores.fhir.conditionalDelete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/conditionalDelete)
  * [`fhirStores.fhir.conditionalPatch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/conditionalPatch)
  * [`fhirStores.fhir.conditionalUpdate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/conditionalUpdate)
  * [`fhirStores.fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/create)
  * [`fhirStores.fhir.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/delete)
  * [`fhirStores.fhir.Resource-purge`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Resource-purge)
  * [`fhirStores.fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/executeBundle)
  * [`fhirStores.fhir.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/patch)
  * [`fhirStores.fhir.update`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/update)

**v1:**

  * [`fhirStores.fhir.conditionalDelete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalDelete)
  * [`fhirStores.fhir.conditionalPatch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalPatch)
  * [`fhirStores.fhir.conditionalUpdate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalUpdate)
  * [`fhirStores.fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/create)
  * [`fhirStores.fhir.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/delete)
  * [`fhirStores.fhir.Resource-purge`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Resource-purge)
  * [`fhirStores.fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle)
  * [`fhirStores.fhir.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/patch)
  * [`fhirStores.fhir.update`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/update)

  
`fhir_search_ops` | Number of FHIR search operations per minute per region | Measured in units, where one unit is a search request on a FHIR resource type where the search doesn't require resolving references, except when `_include` is used. For example, a `Observation?subject:Patient.identifier=system|value` search consumes two `fhir_search_ops` quota units because it requires two searches, one on the Observation resource and one on the Patient resource, using the `subject` as a reference.  
  
Includes the following methods:  
**v1beta1:**

  * [`fhirStores.fhir.Patient-consent-enforcement-status`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Patient-consent-enforcement-status)
  * [`fhirStores.fhir.ConceptMap-search-translate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/ConceptMap-search-translate)
  * [`fhirStores.fhir.conditionalDelete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/conditionalDelete)
  * [`fhirStores.fhir.conditionalPatch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/conditionalPatch)
  * [`fhirStores.fhir.conditionalUpdate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/conditionalUpdate)
  * [`fhirStores.fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/executeBundle)
  * [`fhirStores.fhir.Resource-incoming-references`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Resource-incoming-references)
  * [`fhirStores.fhir.Observation-lastn`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Observation-lastn)
  * [`fhirStores.fhir.Patient-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Patient-everything)
  * [`fhirStores.fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/search)
  * [`fhirStores.fhir.search-type`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/search-type)

**v1:**

  * [`fhirStores.fhir.conditionalDelete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalDelete)
  * [`fhirStores.fhir.conditionalPatch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalPatch)
  * [`fhirStores.fhir.conditionalUpdate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalUpdate)
  * [`fhirStores.fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle)
  * [`fhirStores.fhir.Patient-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Patient-everything)
  * [`fhirStores.fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search)
  * [`fhirStores.fhir.search-type`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search-type)

  
`fhir_storage_egress_bytes` | FHIR storage egress in bytes per minute per region | Measured in units, where one unit is one byte the Cloud Healthcare API reads from storage while processing `fhir_read_ops`, `fhir_write_ops`, and `fhir_search_ops` operations.  
`fhir_storage_bytes` | FHIR storage ingress in bytes per minute per region | Bytes sent to the Cloud Healthcare API while processing `fhir_write_ops` operations.  
`fhir_store_ops` | Number of FHIR store operations per minute per region | Operations on the FHIR store, not FHIR data.  
  
Includes the following methods:  


  * [`fhirStores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/create)
  * [`fhirStores.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/delete)
  * [`fhirStores.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/get)
  * [`fhirStores.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/list)
  * [`fhirStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch)

  
`fhir_store_lro_ops` | Number of FHIR store long-running operations per minute per region | Operations on the FHIR store, not FHIR data, that return a long-running operation.  
  
Includes the following methods:  


  * [`fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export)
  * [`fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import)
  * [`fhirStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/deidentify)

  
`fhir_storage_operations_bytes` | FHIR storage ingress for long-running operations in bytes per minute per region | Bytes sent to the Cloud Healthcare API while processing `fhir_store_lro_ops` operations.  
  
#### Multi-operation searches

A single request can consume multiple quota units. For example, a `GET` search request using `Observation?subject:Patient.identifier=system|value` as the search parameter consumes two `fhir_search_ops` quota units. Two search operations are performed, one on the Observation resource and one on the Patient resource, using the `subject` as a reference.

If a conditional delete request using `Observation?status=canceled` as the search criteria searches for and deletes six Observation resources, the following quota units are consumed:

  * One `fhir_search_ops` quota unit, because the `GET` search request is only performed on one type of FHIR resource, the Observation resource. The request returns all Observation resources matching the search criteria.
  * Six `fhir_write_ops` quota units, because there are a total of six `DELETE` operations on the deleted Observation resources.



#### Execute bundle quota consumption

To send an [execute bundle](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bundles) request, regardless of the quota the request consumes, your Google Cloud project must have at least one unit available for each of the following quotas:

  * `fhir_read_ops`
  * `fhir_write_ops`
  * `fhir_search_ops`



If these quotas aren't available, the execute bundle request fails.

For example, if you send a [`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle) request with a transaction bundle containing 100 `POST` operations, each of which creates a FHIR resource, the Cloud Healthcare API first verifies that at least one quota unit is available for `fhir_read_ops`, `fhir_write_ops`, and `fhir_search_ops`. If the verification succeeds, the Cloud Healthcare API executes the bundle and creates the FHIR resources, which consume a total of 100 `fhir_write_ops` quota units.

Consider the following transaction bundle, which uses a conditional reference to create an Observation resource if the `reference` exists:
    
    
    {
      "resourceType": "Bundle",
      "type": "transaction",
      "entry": [
        {
          "request": {
            "method": "POST",
            "url": "Observation"
          },
          "resource": {
            "resourceType": "Observation",
            "subject": {
              "reference": "Patient?identifier=a1b2c3d4e5"
            }
          }
        }
      ]
    }
    

When you execute the bundle, the Cloud Healthcare API first verifies that at least one quota unit is available for `fhir_read_ops`, `fhir_write_ops`, and `fhir_search_ops`. If the verification succeeds, the Cloud Healthcare API executes the bundle. The following quota units are consumed:

  * One `fhir_write_ops` to create the new Observation resource.
  * One `fhir_search_ops`, because a single search operation is performed on the `Patient?identifier=a1b2c3d4e5` reference.



## Best practices

For best practices on managing Cloud Healthcare API quota, see [Quota management best practices](https://docs.cloud.google.com/healthcare-api/docs/best-practices-quota-management).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
