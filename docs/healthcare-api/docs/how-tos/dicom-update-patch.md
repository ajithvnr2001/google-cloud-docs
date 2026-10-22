---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-update-patch/
title: Update and patch DICOM studies, series, and instances \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:32.825524+00:00
---

# Update and patch DICOM studies, series, and instances  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-update-patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Update and patch DICOM studies, series, and instances Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how DICOM studies, series, and instances in the Cloud Healthcare API can be updated and patched in-place. For information on how to populate stores in the Cloud Healthcare API with DICOM data, see [Using the DICOMweb standard](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb).

## Updating DICOM instances

DICOM instances can be replaced by uploading a new version of the `.dcm` file. Similar to [`storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#store-dicom), a multipart file may also be used to update multiple instances at once (often for updating a study or series with multiple instances). After updating, the original instance will be fully replaced.

Unlike [`storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#store-dicom), updating a full instance cannot be done with JSON metadata. For partial updates with JSON, see Patching DICOM metadata.

Updating an instance will be treated as an "upsert". If the instance exists, then it will be updated. If the instance does not exist, then the instance will be created and inserted into the store.

When inserting a new instance, the `SOP_CLASS_UID`, `SOP_INSTANCE_UID`, `STUDY_INSTANCE_UID`, and `SERIES_INSTANCE_UID` values are gathered from the provided metadata. UIDs must meet these requirements:

  * Contain only numeric values separated by periods.
  * Contain no protected health information (PHI).



The following example shows how to update an instance in a DICOM store. For more information, see [`projects.locations.datasets.dicomStores.updateInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores/updateInstances).

### curl

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `DICOM_INSTANCE_FILE`: the path to a DICOM instance file on your local machine ending in the `.dcm` suffix



The following sample shows a `PUT` request using `curl`.
    
    
    curl -X PUT \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/dicom" \
        --data-binary @DICOM_INSTANCE_FILE \
        "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies"

The output is the following XML response:

#### Response
    
    
    <NativeDicomModel>
      <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
        <Value number="1">https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID</Value>
      </DicomAttribute>
      <DicomAttribute tag="00081199" vr="SQ" keyword="ReferencedSOPSequence">
        <Item number="1">
          <DicomAttribute tag="00081150" vr="UI" keyword="ReferencedSOPClassUID">
            <Value number="1">SOP_CLASS_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081155" vr="UI" keyword="ReferencedSOPInstanceUID">
            <Value number="1">SOP_INSTANCE_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
            <Value number="1">https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID</Value>
          </DicomAttribute>
        </Item>
      </DicomAttribute>
    </NativeDicomModel>
    

### Updating multiple instances at once

The following example shows how to update a DICOM study or series, consisting of multiple instances, using a multipart message.

### curl

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `MULTIPART_FILE`: the path to a multipart file on your local machine. The file contains multiple DICOM instances, with each separated by a boundary.
  * `BOUNDARY`: the boundary used to separate the DICOM instances in the multipart file



The following sample shows a `PUT` request using `curl`.
    
    
    curl -X PUT \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: multipart/related; type=application/dicom; boundary=BOUNDARY" \
        --data-binary @MULTIPART_FILE \
        "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies"

The output is the following XML response:

#### Response
    
    
    <NativeDicomModel>
      <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
        <Value number="1">https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID</Value>
      </DicomAttribute>
      <DicomAttribute tag="00081199" vr="SQ" keyword="ReferencedSOPSequence">
        <Item number="1">
          <DicomAttribute tag="00081150" vr="UI" keyword="ReferencedSOPClassUID">
            <Value number="1">SOP_CLASS_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081155" vr="UI" keyword="ReferencedSOPInstanceUID">
            <Value number="1">SOP_INSTANCE_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
            <Value number="1">https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID</Value>
          </DicomAttribute>
        </Item>
      </DicomAttribute>
    </NativeDicomModel>
    

## Patching DICOM metadata

You can add, remove, or edit a DICOM tag at the study, series, or instance level. The behavior for each of the levels is as follows:

  * If you edit a study-level tag using [`projects.locations.datasets.dicomStores.studies.updateMetadata`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores.studies/updateMetadata), the edit applies to all of the instances in the study. A long-running operation will be returned
  * If you edit a series-level tag using [`projects.locations.datasets.dicomStores.studies.series.updateMetadata`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores.studies.series/updateMetadata), the edit applies to all of the instances in the series. A long-running operation will be returned
  * If you edit an instance-level tag using [`projects.locations.datasets.dicomStores.studies.series.instances.updateMetadata`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores.studies.series.instances/updateMetadata), the edit applies only to the instance you specified. The edit will happen synchronously and JSON metadata about the edited instance will be returned



For patches that return a long-running operation, any failures to apply the patch to an instance will be logged in [Cloud Logging](https://docs.cloud.google.com/logging/docs). The number of failed instances is returned in the operation metadata, along with a link to the associated logs.

### JSON Patch

The syntax for tag editing follows the [JSON Patch standard](https://tools.ietf.org/html/rfc6902). Only the operations `add`, `replace`, and `remove` are supported. You can specify a tag using its public keyword (if the tag is public), or by an 8 digit hexadecimal identifier. Note that all tag paths must be prefixed with `/`. When you `add` or `replace` a tag, you must specify a VR and a value for the tag along with the tag identifier. When you `remove` a tag, you only need to specify the tag identifier.

Editing tags within a sequence is supported, as well as sequence replacement. See patch limitations for what is not supported using patch. To specify a tag within a sequence, separate the sequence and child tag with the item index and backslashes. Here is an example which `add`s the tag `InstanceCreationDate` to the 2nd item of `ReferencedInstanceSequence` (note that sequence items are 0-indexed):
    
    
    [
      {
        "op": "add",
        "path": "/ReferencedInstanceSequence/1/InstanceCreationDate",
        "value": {
          "vr": "DA",
          "Value": [ "20240501" ]
        }
      }
    ]
    

For adding a full sequence (or replacing a full sequence), the `value` field of the JSON Patch entry must be the DICOM JSON representation of a sequence. Here is an example of adding the `OtherPatientIDs` sequence with 2 elements to an instance:
    
    
    [
      {
        "op": "add",
        "path": "/OtherPatientIDs",
        "value": {
          "vr": "SQ",
          "Value": [
            {
              "00100020": {
                "vr": "LO",
                "Value": [ "54321" ]
              },
              "00100021": {
                "vr": "LO",
                "Value": [ "Hospital B" ]
              }
            },
            {
              "00100020": {
                "vr": "LO",
                "Value": [ "24680" ]
              },
              "00100021": {
                "vr": "LO",
                "Value": [ "Hospital C" ]
              }
            }
          ]
        }
      }
    ]
    

### Patching a single instance

### curl

To edit DICOM tags for a single instance, make a `PATCH` request and specify the following information:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `STUDY_UID`: the study UID of the DICOM instance
  * `SERIES_UID`: the series UID of the DICOM instance
  * `INSTANCE_UID`: the instance UID of the DICOM instance



The following sample shows a `PATCH` request using `curl`.
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data '[
          {
            "op": "add",
            "path": "/ProductName",
            "value": {
              "vr": "LO",
              "Value": [
                "My Product"
              ]
            }
          },
          {
            "op": "replace",
            "path": "/PatientName",
            "value": {
              "vr": "PN",
              "Value": [
                "New Patient Name"
              ]
            }
          },
          {
            "op": "remove",
            "path": "/Manufacturer"
          }
        ]' \
        "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_UID/series/SERIES_UID/instances/INSTANCE_UID/metadata"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "studyUID": "STUDY_UID",
      "seriesUID": "SERIES_UID",
      "instanceUID": "INSTANCE_UID",
      "createTimestamp": "CREATE_TIMESTAMP",
      "metadata": {
        // Full DICOM JSON metadata for the instance after edits applied
      }
    }
    
    

### Patching a study or series

### curl

To edit DICOM tags for all instances in a given study, make a `PATCH` request and specify the following information:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `STUDY_UID`: the study UID of the DICOM study



The following sample shows a `PATCH` request using `curl`.
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data '[
          {
            "op": "add",
            "path": "/ProductName",
            "value": {
              "vr": "LO",
              "Value": [
                "My Product"
              ]
            }
          },
          {
            "op": "replace",
            "path": "/PatientName",
            "value": {
              "vr": "PN",
              "Value": [
                "New Patient Name"
              ]
            }
          },
          {
            "op": "remove",
            "path": "/Manufacturer"
          }
        ]' \
        "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_UID/metadata"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation ID. To track the status of the operation and view more details, use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/private/docs/reference/rest/v1beta1/projects.locations.datasets.operations/get):
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.dicom.DicomWebService.UpdateStudyMetadata",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "CLOUD_LOGGING_URL",
        "counter": {
          "success": "1" // Number of instances updated in the study
        }
      },
      "done": true,
      "response": {
        "@type": "..."
      }
    }
    

### Limitations

The following limitations and additional behavior apply when editing DICOM tags:

  * You cannot edit the following tags: 
    * `SOPInstanceUID (0008,0018)`
    * `SeriesInstanceUID (0020,000E)`
    * `StudyInstanceUID (0020,000D)`
    * `Modality (0008,0060)`
    * `ModalitiesInStudy (0008,0061)`
    * `SpecificCharacterSet (0008,0005)`
    * Any tag with a Group Number less than "0008"
    * Any tag considered bulkdata (see [bulkdata definition](https://docs.cloud.google.com/healthcare-api/docs/dicom#bulkdata-definition))
    * In addition to the preceding definition, any tag with a VR of OD, OF, OL, OV, SV, or UV cannot be added using `patch` (either `add` or `replace` operations), regardless of length
  * A sequence that contains a tag considered bulkdata cannot be edited 
    * This means that `replace` or `remove` operations on a sequence tag will fail if any of the tags contained in the original sequence are considered bulkdata
    * In addition, any `replace` or `add` operations on a sequence tag will fail if any of the tags contained in the new sequence are considered bulkdata
  * If you try to `replace` or `remove` a tag that doesn't exist, the Cloud Healthcare API returns an error and the edit fails
  * If you try to `add` a tag that already exists, the edit operation behaves the same way as if you had called a replace operation. The replace operation replaces the existing value of the tag with the new value specified in the operation
  * While sequences may be added/replaced/removed (and tags within items in a sequence may be edited as well), individual items in a sequence may not be added/replaced/removed 
    * In practice, this means any edit with a tag path ending in an index will be rejected (for example, `/ReferencedSeriesSequence/0`)
    * If changes to an individual item in a sequence are necessary, replace the entire parent sequence with a copy that has the changes applied



## Updating using DICOM Studio

**Note:** Before you begin, it is important to read Patching DICOM metadata to understand the high level semantics of DICOM patching.

You can use DICOM Studio to update DICOM metadata for a study, series, or instance.

To update DICOM metadata using DICOM Studio:

  1. [Search for the study, series, or instance](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#search-dicom-studio) that you want to update.
  2. In the search results, click the item to navigate to its details page.
  3. Click the **Metadata** tab.
  4. Select the checkbox for one or more tags you want to edit, and then click **Edit**.
  5. In the edit panel, expand the tag you want to modify.
  6. Edit the tag's keyword, VR, or value.
  7. Click **Save**.



All limitations still apply to the user interface. In addition, the user interface has the following limitations:

  1. The tag editing interface does not support editing tags with a Value Multiplicity (VM) greater than 1.
  2. The tag editing interface does not provide any guidance or validation on the expected VR or value types.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
