---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging/
title: Viewing error logs in Cloud Logging \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:18.628497+00:00
---

# Viewing error logs in Cloud Logging  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Viewing error logs in Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view logs in Google Cloud Observability for supported request types.

## Logging

Errors triggered in each of the following requests are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs).

  * [DICOM de-identification](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/deidentify)
  * [DICOM export](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export)
  * [DICOM import](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import)
  * [Dataset de-identification](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/deidentify)
  * [FHIR de-identification](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/deidentify)
  * [FHIR export](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export)
  * [FHIR import](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import)
  * [HL7v2 export](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export)
  * [HL7v2 import](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/import)



Errors are also logged if a Pub/Sub message can't be published to Pub/Sub. See [Troubleshooting Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub#troubleshooting) for more information.

Logging is automatic and doesn't need to be enabled. To disable Cloud Logging for one or all monitored resources, see [Logs exclusions](https://docs.cloud.google.com/logging/docs/exclusions).

### Viewing logs

To view all logs, go to the [Logs Explorer](https://console.cloud.google.com/logs).

To view logs for operations with an error status, follow these steps:

  1. In the Google Cloud console, go to the Cloud Healthcare API browser.

[Go to the Cloud Healthcare API browser](https://console.cloud.google.com/healthcare/browser)

  2. Select a dataset.

  3. Click the **Operations** tab.

  4. In the list of operations, choose **View details in Cloud Logging** from the **Actions** list to view the details of an erroneous operation.




### Filtering logs

You can filter logs by data store type, region, and dataset.

For example, to view logs for FHIR stores, click **Healthcare FHIR Store** in the first list under **Filter by label or text search**. You can also search by resource type. For example, searching for `healthcare_dicom_store` displays all logs generated for operations with `resource.type` set to `healthcare_dicom_store`.

[UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding is enforced for log fields. Characters that aren't UTF-8 characters are replaced with question marks.

For detailed information about the Logs Explorer, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Using Cloud Logging to find error events

You can also use Cloud Logging to find the audit log of an event causing an error. To find a error event in the audit logs, do the following:

  1. Search Cloud Logging for the operation that caused.

  2. Using the operation's log details, re-run the specific command.

  3. View the audit logs for the corresponding event. For more information on audit logs, see [Viewing Cloud Audit Logs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging).




### What is logged

Cloud Healthcare API log entries contain the following types of information for debugging requests:

  * General information, such as severity, project ID, project number, and timestamp.
  * `jsonPayload` contains the actual body of the entry. This field contains the error code, the error message, and the name of the source file whose import triggered the error.
  * `operation` contains the type and ID of the operation that produced the error.
  * `resource` contains the location, dataset, and data store involved in the error.



If the number of errors exceeds a threshold, a limited number of errors appears in Cloud Logging. The threshold is dynamically calculated based on the size of the input.

### Where logs are stored

Google Cloud Observability isn't a regionalized product. Logs written to Google Cloud Observability could be stored in a different region from the data stores.

### Sample DICOM import log entry

The following sample log entry shows an `empty DICOM instance found` error that occurred while attempting to import `gs://DICOM_FILENAME.dcm` to `projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID`.
    
    
     jsonPayload: {
      @type:  "type.googleapis.com/google.cloud.healthcare.logging.ImportDicomLogEntry"
      error: {
       code:  3
       message:  "empty DICOM instance found"
      }
      source:  "gs://DICOM_FILENAME.dcm"
     }
     logName:  "projects/PROJECT_ID/logs/healthcare.googleapis.com%2Foperations"
     operation: {
      id:  "PROJECT_ID"
      producer:  "import_dicom"
     }
     receiveTimestamp:  "TIMESTAMP"
     resource: {
      labels: {
       dataset_id:  "DATASET_ID"
       dicom_store_id:  "DICOM_STORE_ID"
       location:  "LOCATION"
       project_id:  "PROJECT_ID"
      }
      type:  "healthcare_dicom_store"
     }
     severity:  "ERROR"
     timestamp:  "TIMESTAMP"
    

### Sample FHIR import log entry

The following sample log entry shows a `cannot import resource` error that occurred while attempting to import `gs://FHIR_FILENAME.ndjson` to `projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStore/FHIR_STORE_ID`.
    
    
     jsonPayload: {
      @type:  "type.googleapis.com/google.cloud.healthcare.logging.ImportFhirLogEntry"
      error: {
       code:  3
       message:  "cannot import resource Patient/PATIENT_ID, conflicting resource already exists"
      }
      source:  "gs://FHIR_FILENAME.ndjson"
     }
     logName:  "projects/PROJECT_ID/logs/healthcare.googleapis.com%2Foperations"
     operation: {
      id:  "PROJECT_ID"
      producer:  "import_fhir"
     }
     receiveTimestamp:  "TIMESTAMP"
     resource: {
      labels: {
       dataset_id:  "DATASET_ID"
       fhir_store_id:  "FHIR_STORE_ID"
       location:  "LOCATION"
       project_id:  "PROJECT_ID"
      }
      type:  "healthcare_fhir_store"
     }
     severity:  "ERROR"
     timestamp:  "TIMESTAMP"
    

### Sample DICOM de-identify log entry

The following sample log entry shows a `cannot de-identify dicom instance` error that occurred while trying to de-identify DICOM instance INSTANCE_ID in dataset `projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID`.
    
    
     jsonPayload: {
      @type:  "type.googleapis.com/google.cloud.healthcare.logging.DeidentifyLogEntry"
      error: {
       code:  2
       message:  "Failed to process instance INSTANCE_ID"
      }
      resourceName:  "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID"
     }
     logName:  "projects/PROJECT_ID/logs/healthcare.googleapis.com%2Fdeidentify_dataset"
     operation: {
      id:  "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
      producer:  "healthcare.googleapis.com/DeidentifyDataset"
     }
     receiveTimestamp:  "TIMESTAMP"
     resource: {
      labels: {
       dataset_id:  "DATASET_ID"
       location:  "LOCATION"
       project_id:  "PROJECT_ID"
      }
      type:  "healthcare_dataset"
     }
     severity:  "ERROR"
     timestamp:  "TIMESTAMP"
    

## What's next

  * Review the [conceptual information about Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/concepts/introduction)
  * Review the [conceptual information about Cloud Logging](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
