---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-annotation/
title: Write de-identify operation metadata to a FHIR store \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:50.439154+00:00
---

# Write de-identify operation metadata to a FHIR store  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-annotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Write de-identify operation metadata to a FHIR store Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**  
  
This page describes Preview features that are subject to change and may have limited support. Changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see [Pre-GA Offering Terms for Cloud Healthcare API](https://cloud.google.com/healthcare-api/docs/pre-ga-terms#pre-ga_offering_terms_for) and the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

This page explains how to de-identify DICOM data and write metadata about the de-identify operation and what was de-identified to a FHIR store. The metadata is stored in FHIR [Provenance](https://www.hl7.org/fhir/provenance.html) resources in the FHIR store. You can then query the data using [FHIR custom searches](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-custom-search) to answer questions like the following:

  * What was de-identified?
  * How and why was the data de-identified?
  * When did the de-identify operation occur, and how long did it take?



## Before you begin

  * [De-identifying DICOM data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-deidentify)



## Using FHIR instead of annotations

The Cloud Healthcare API offers an annotations API which you can use to [annotate de-identified data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/annotations-deidentify).

Writing de-identify operation metadata to a FHIR store works similarly, and has the following advantages:

  * You don't need to use the annotations API, which is a separate API.
  * You don't need to create and manage annotation stores and annotation records.
  * You can continue to work with the FHIR standard and the Cloud Healthcare API FHIR API.
  * You can [export the FHIR resources to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery) for exploration and analysis. The generated data is only compatible with the `LOSSLESS` or `ANALYTICS_V2` [`SchemaType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores#SchemaType). 
    * You can [stream FHIR resource changes to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bigquery-streaming) to synchronize the data in a FHIR store with a BigQuery dataset in near real time.
  * More information is provided about the de-identify operation metadata.



## Requirements

The FHIR store that holds the de-identify operation metadata must meet the following requirements:

  * Must already exist.
  * Must be a version [R4](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#Version) FHIR store.
  * Must have [`enableUpdateCreate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.enable_update_create) set to `true`.



## Provenance resources in the operation metadata FHIR store

When you run a DICOM de-identify operation, the following Provenance resources are written to the operation metadata FHIR store:

  * A Provenance resource that summarizes the de-identify operation, such as the name of the long-running operation, when the operation occurred, and what configuration was used. For a list of fields in this Provenance resource, see De-identify operation metadata in a Provenance resource.

  * A Provenance resource for each DICOM instance that was de-identified. For a list of fields in this Provenance resource, see DICOM de-identification metadata in a Provenance resource.

    * The resource contains information about what was de-identified, such as a DICOM tag or the portion of a DICOM image, and the actions that were taken, such as whether the information was redacted, transformed, or ignored.
    * The resource might contain de-identified data processed by optical character recognition (OCR) that falls within the scope of protected health information (PHI).

The de-identified text, or `quote`, is accompanied with its information type, or `infoType` and the likelihood of finding the information, or `confidence`. For example, if a DICOM image containing the burnt-in text `John Doe` is de-identified, the Provenance resource will contain `quote` set to `John Doe`, `infoType` set to `PERSON_NAME`, and a `confidence` value between 0 and 1.

The DICOM de-identification metadata is only generated if the [`dicomStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores/deidentify) method is called with [`ImageConfig.textRedactionMode`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores#TextRedactionMode) set to `REDACT_SENSITIVE_TEXT` or `REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS`. If you set `REDACT_ALL_TEXT`, the method generates de-identified text as a single string in the `extracted-text` field. The string contains no segmentation. Tokens are separated by spaces.

**Note:** When the operation metadata contains PHI, we recommend that you control access to the data stores such that no single principal has access to both the destination DICOM store and the operation metadata FHIR store. For more information on controlling access, see [Controlling access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/controlling-access).



### De-identify operation metadata in a Provenance resource

The following table shows a description of the metadata in the de-identify operation and the corresponding field in the metadata where it can be found in the Provenance resource. The "Provenance resource field" cells contain sample values which are for demonstration purposes.

Metadata description | Provenance resource field  
---|---  
Provenance resource ID | `Provenance.id`  
When the de-identify operation began | `Provenance.occurredDateTime`  
Provenance resource creation timestamp | `Provenance.recorded`  
Name of de-identification long-running operation | 
    
    
        Provenance.agent.who: {
          "identifier": {
            "system": "https://g.co/healthcare/operation"
            "value": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
          }
        }
          
  
Source DICOM store | 
    
    
        Provenance.entity.role: "SOURCE"
        Provenance.entity.what.identifier.value: "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/SOURCE_DICOM_STORE_ID"
          
  
Destination DICOM store | `Provenance.target.type.value`  
[`DeidentifyConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/DeidentifyConfig) value used | 
    
    
        Provenance.entity.extension: [{
          url: 'https://g.co/deidentify-config',
          valueString: 'DEIDENTIFY_CONFIG' // Can be either a JSON configuration or a path to a Cloud Storage URI and timestamp if the configuration was provided using Cloud Storage
        }]
          
  
### DICOM de-identification metadata in a Provenance resource

The following table shows a description of the metadata in the DICOM instance that was de-identified and the metadata's corresponding field in a Provenance resource. The "Provenance resource field" cells contain sample values which are for demonstration purposes.

Metadata description | Provenance resource field  
---|---  
Link to the de-identify operation resource | `Provenance.agent.who: {reference: "Provenance/PROVENANCE_RESOURCE_ID"}`  
Provenance resource creation timestamp | `Provenance.recorded`  
Source DICOM instance REST path | 
    
    
        Provenance.entity.role: SOURCE
        Provenance.entity.what.identifier.value
          
  
Destination DICOM instance REST path | `Provenance.target.type.value`  
DICOM image size | 
    
    
        Provenance.entity.extension: [
          {
            url: 'https://g.co/WIDTH',
            valueDecimal: WIDTH
          },
            url: 'https://g.co/HEIGHT',
            valueDecimal: HEIGHT
          }
        ]
          
  
Structured size | 
    
    
        Provenance.entity.extension: [{
          url: 'https://g.co/DICOM_STRUCTURED_SIZE',
          valueDecimal: VALUE,
        }]
          
  
DICOM image annotation | 
    
    
        Provenance.entity.extension: [{
          url: 'https://g.co/DICOM_IMAGES',
          extension: [
            { FRAME_0
            },
            { FRAME_1
            },
            ...
          ]
        }]
          
  
DICOM frame annotation | 
    
    
        Provenance.entity.extension['https://g.co/dicom-images'].extension: [
          {
            url: 'frame-index',
            valueDecimal: 0,
            extension: [
              {
                url: 'left',
                valueDecimal: LEFT_VALUE
              },
              {
                url: 'right',
                valueDecimal: RIGHT_VALUE
              },
              {
                url: 'top',
                valueDecimal: TOP_VALUE
              },
              {
                url: 'bottom',
                valueDecimal: BOTTOM_VALUE
              },
              {
                url: 'relative-left',
                valueDecimal: RELATIVE_LEFT_VALUE / WIDTH
              },
              {
                url: 'relative-right',
                valueDecimal: RELATIVE_RIGHT_VALUE / HEIGHT
              },
              {
                url: 'relative-top',
                valueDecimal: RELATIVE_TOP_VALUE / WIDTH
              },
              {
                url: 'relative-bottom',
                valueDecimal: RELATIVE_BOTTOM / HEIGHT
              }
            ]
          }
        ]
          
  
DICOM frame annotation | 
    
    
        // Only available if the text redaction mode is REDACT_SENSITIVE_TEXT or
        // REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS
        Provenance.entity.extension: [
           {
            "url": "quote", // The PHI text de-identified
            "valueString": "John Doe"
           },
          {
            "url": "infoType", // The type of the de-identified text
            "valueString": "PERSON_NAME"
           },
          {
            "url": "confidence", // The likelihood of finding this quote and its infoType
            "valueDecimal": 0.7
           }
        ]
          
  
DICOM frame annotation | 
    
    
        // Only available if the text redaction mode is REDACT_ALL_TEXT
        Provenance.entity.extension: [
           {
            "url": "extracted-text", // The entire PHI text de-identified
            "valueString": "John Doe 27-Jan-1999 Sex:M"
           }
        ]
          
  
All DICOM tags annotation | 
    
    
        Provenance.entity.extension: [{
          url: 'https://g.co/dicom-tags',
          extension: [
            { // tag (0002,0000)
            },
            { // tag (0002,0001)
            },
            ...
          ]
        }]
          
  
DICOM individual tag notation | 
    
    
        Provenance.entity.extension['https://g.co/dicom-tags'].extension: [
          {
            url: 'tag-id',
            valueString: '00080012',
            extension: [
              {
                url: 'byte-start',
                valueDecimal: 10
              },
              {
                url: 'byte-end',
                valueDecimal: 18
              },
              {
                url: 'finding-infotype',
                valueString: 'PERSON_NAME'
              },
              {
                url: 'text-original',
                valueString: 'John Doe'
              },
              {
                url: 'text-replaced',
                valueString: 'PERSON_NAME'
              },
              {
                url: 'deidentify-action',
                valueString: 'REMOVED'
                // Possible values are "REMOVED", "DELETED", "REGENERATED UID",
                // "RESET", "CLEANED", and "RECURSED"
              },
              {
                url: 'deidentify-reason',
                valueString: 'Matched VALUE'
                // Possible values include "ID", "VR", or "Expression",
                // for example "Matched ID: DICOM_TAG_ID"
              }
            ]
          }
        ]
          
  
## Examples

### Before you begin

Ensure that you have the [`roles/healthcare.fhirResourceEditor`](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirResourceEditor) role on the operation metadata FHIR store before running any of the following examples. You need this role to write to the operation metadata FHIR store.

### De-identify DICOM data, write to a FHIR store, and search Provenance resources

Before running this example, complete the following steps:

  1. Create a [source dataset](https://docs.cloud.google.com/healthcare-api/docs/how-tos/datasets#create-dataset) containing a [DICOM store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom#creating_a_dicom_store) with at least one DICOM instance to be de-identified.
  2. Create a destination dataset containing an empty DICOM store and an empty [FHIR store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir#creating_a_fhir_store). The FHIR store must meet the requirements.



This example expands on [Combining tag de-identification and burnt-in text redaction](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-deidentify#combining_tag_de-identification_and_burnt-in_text_redaction). In this example, the de-identification occurs on a single DICOM store and the de-identified data is written to a new DICOM store. The operation metadata FHIR store is in the same dataset as the new DICOM store.

This example uses two DICOM instances. The instances are not provided for you, so the sample responses will not align exactly with your de-identified data.

  1. De-identify the DICOM data.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the dataset containing the source DICOM store
     * SOURCE_DATASET_ID: the source DICOM store's parent dataset
     * SOURCE_DICOM_STORE_ID: the ID of the DICOM store containing data that you are de-identifying
     * DESTINATION_DATASET_ID: an existing dataset that contains the metadata operation FHIR store, and where the de-identified DICOM store will be created
     * DESTINATION_DICOM_STORE_ID: the DICOM store where de-identified data from the source DICOM store will be written
     * OPERATION_METADATA_FHIR_STORE_ID: the FHIR store where de-identification operation metadata will be written

Request JSON body: 
    
    {
      "destinationStore": "projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/dicomStores/DESTINATION_DICOM_STORE_ID",
      "config": {
        "dicom": {
          "filterProfile": "DEIDENTIFY_TAG_CONTENTS"
        },
        "image": {
          "textRedactionMode": "REDACT_ALL_TEXT"
        },
        "operationMetadata": {
          "fhirOutput": {
            "fhirStore": "projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE"
          }
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "destinationStore": "projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/dicomStores/DESTINATION_DICOM_STORE_ID",
      "config": {
        "dicom": {
          "filterProfile": "DEIDENTIFY_TAG_CONTENTS"
        },
        "image": {
          "textRedactionMode": "REDACT_ALL_TEXT"
        },
        "operationMetadata": {
          "fhirOutput": {
            "fhirStore": "projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE"
          }
        }
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/dicomStores/SOURCE_DICOM_STORE_ID:deidentify"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "destinationStore": "projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/dicomStores/DESTINATION_DICOM_STORE_ID",
      "config": {
        "dicom": {
          "filterProfile": "DEIDENTIFY_TAG_CONTENTS"
        },
        "image": {
          "textRedactionMode": "REDACT_ALL_TEXT"
        },
        "operationMetadata": {
          "fhirOutput": {
            "fhirStore": "projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE"
          }
        }
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/dicomStores/SOURCE_DICOM_STORE_ID:deidentify" | Select-Object -Expand Content

The response is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations). Long-running operations are returned when method calls might take a substantial amount of time to complete. Note the value of OPERATION_ID. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

  2. Get the status of the operation.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the dataset
     * SOURCE_DATASET_ID: the dataset where the de-identify operation is running
     * OPERATION_ID: the ID of the de-identify operation 

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.deidentify.DeidentifyService.DeidentifyDicomStore",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer?advancedFilter=operation.id%3Dprojects%2FPROJECT_ID%2Flocations%2FLOCATION%2Fdatasets%2FDATASET_ID%2Foperations%2FOPERATION_IDTIMESTAMP&project=PROJECT_ID&interval=NO_LIMIT",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.deidentify.DeidentifyDicomStoreSummary"
      }
    }
    

  3. After successfully de-identifying DICOM data and writing the operation metadata to a FHIR store, you can view the Provenance resources in the FHIR store.

To view the Provenance resources, use the [`fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/search) method.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * OPERATION_METADATA_FHIR_STORE_ID: the ID of the FHIR store containing the metadata

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance" | Select-Object -Expand Content

The following response was a result of de-identifying two DICOM instances. The de-identify operation resulted in the following three Provenance resources being created: 
     * One Provenance resource for each of the two DICOM instances
     * One Provenance resource for the de-identify operation

#### Response
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/PROVENANCE_RESOURCE_ID",
          "resource": {
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/PROVENANCE_RESOURCE_ID"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/dicomStores/SOURCE_DICOM_STORE"
                  }
                }
              }
            ],
            "id": "PROVENANCE_RESOURCE_ID",
            "meta": {
              "lastUpdated": "LAST_UPDATED",
              "versionId": "MTY0NjMzNDU4ODg3NDcwMTAwMA"
            },
            "occurredDateTime": "OCCURRED_DAY_TIME",
            "recorded": "2010-11-08T08:30:24-04:00",
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/dicomStores/DESTINATION_DICOM_STORE"
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/8408902d-3e33-4af6-8c2c-5c7314c30c34",
          "resource": {
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/PROVENANCE_RESOURCE_ID"
                  }
                }
              }
            ],
            "entity": [
              {
                "extension": [
                  {
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0
                      },
                      {
                        "url": "frame-index",
                        "valueDecimal": 1
                      }
                    ],
                    "url": "https://g.co/dicom-images"
                  },
                  {
                    "extension": [
                      {
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "AGE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "30"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "AGE"
                          }
                        ],
                        "url": "tag-id",
                        "valueString": "00101010"
                      },
                      {
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 4
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "GENERIC_ID"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1234"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "GENERIC_ID"
                          }
                        ],
                        "url": "tag-id",
                        "valueString": "00100020"
                      }
                    ],
                    "url": "https://g.co/dicom-tags"
                  }
                ],
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/dicomStores/SOURCE_DICOM_STORE/dicomWeb/studies/1/series/2/instances/4"
                  }
                }
              }
            ],
            "id": "8408902d-3e33-4af6-8c2c-5c7314c30c34",
            "meta": {
              "lastUpdated": "LAST_UPDATED",
              "versionId": "MTY0NjMzNDU4ODg3NDcwMTAwMA"
            },
            "recorded": "2010-11-08T08:39:25-04:00",
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/dicomStores/DESTINATION_DICOM_STORE/dicomWeb/studies/1/series/2/instances/4"
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/PROVENANCE_RESOURCE_ID",
          "resource": {
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/PROVENANCE_RESOURCE_ID"
                  }
                }
              }
            ],
            "entity": [
              {
                "extension": [
                  {
                    "extension": [
                      {
                        "extension": [
                          {
                            "url": "bottom",
                            "valueDecimal": 100
                          },
                          {
                            "url": "left",
                            "valueDecimal": 100
                          },
                          {
                            "url": "right",
                            "valueDecimal": 200
                          },
                          {
                            "url": "top",
                            "valueDecimal": 200
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "bottom",
                            "valueDecimal": 900
                          },
                          {
                            "url": "left",
                            "valueDecimal": 900
                          },
                          {
                            "url": "right",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "top",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.5
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.5
                          }
                        ],
                        "url": "frame-index",
                        "valueDecimal": 0
                      }
                    ],
                    "url": "https://g.co/dicom-images"
                  },
                  {
                    "extension": [
                      {
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 10
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 18
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "text-original",
                            "valueString": "John Doe"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "byte-start",
                            "valueDecimal": 25
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 35
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "DATE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1900-12-31"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "DATE"
                          }
                        ],
                        "url": "tag-id",
                        "valueString": "00100021"
                      },
                      {
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "LOCATION"
                          },
                          {
                            "url": "text-original",
                            "valueString": "US"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "LOCATION"
                          }
                        ],
                        "url": "tag-id",
                        "valueString": "00102150"
                      }
                    ],
                    "url": "https://g.co/dicom-tags"
                  }
                ],
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/dicomStores/SOURCE_DICOM_STORE/dicomWeb/studies/1/series/2/instances/3"
                  }
                }
              }
            ],
            "id": "PROVENANCE_RESOURCE_ID",
            "meta": {
              "lastUpdated": "LAST_UPDATED",
              "versionId": "MTY0NjMzNDU4ODg3NDcwMTAwMA"
            },
            "recorded": "2010-11-08T08:39:24-04:00",
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/dicomStores/DESTINATION_DICOM_STORE/dicomWeb/studies/1/series/2/instances/3"
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/?"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/?"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/?"
        }
      ],
      "resourceType": "Bundle",
      "total": 3,
      "type": "searchset"
    }
    




### Store sample data, create a relative x coordinate custom FHIR search, and query

Before running this example, create a destination dataset containing an empty DICOM store and an empty FHIR store. The FHIR store must meet the requirements.

The following example shows how you can store the three Provenance resources created in De-identify DICOM data, write to a FHIR store, and search Provenance resources and then create a custom search. The custom search queries the `relative-x-coordinate-bottom-left` in one of the de-identified DICOM instances.

  1. Store the Provenance resources.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * OPERATION_METADATA_FHIR_STORE_ID: the ID of the FHIR store containing the metadata

Request JSON body: 
    
    {
      "resourceType": "Bundle",
      "type": "transaction",
      "entry": [
        {
          "request": {"method": "PUT", "url": "Provenance/operation-123"},
          "resource": {
            "resourceType": "Provenance",
            "id": "operation-123",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store"
                }
              }
            ],
            "occurredDateTime": "2010-11-08T08:30:00-04:00",
            "recorded": "2010-11-08T08:30:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "system": "https://g.co/healthcare/operation",
                    "value": "projects/my-project/locations/us-central1/datasets/my-dataset/operations/123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store"
                  }
                }
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0,
                        "extension": [
                          {
                            "url": "bottom",
                            "valueDecimal": 100
                          },
                          {
                            "url": "left",
                            "valueDecimal": 100
                          },
                          {
                            "url": "right",
                            "valueDecimal": 200
                          },
                          {
                            "url": "top",
                            "valueDecimal": 200
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "bottom",
                            "valueDecimal": 900
                          },
                          {
                            "url": "left",
                            "valueDecimal": 900
                          },
                          {
                            "url": "right",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "top",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.5
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.5
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00100021",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 10
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 18
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "text-original",
                            "valueString": "John Doe"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "byte-start",
                            "valueDecimal": 25
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 35
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "DATE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1900-12-31"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "DATE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00102150",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "LOCATION"
                          },
                          {
                            "url": "text-original",
                            "valueString": "US"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "LOCATION"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:25-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0
                      },
                      {
                        "url": "frame-index",
                        "valueDecimal": 1,
                        "extension": [
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00101010",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "AGE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "30"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "AGE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00100020",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 4
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "GENERIC_ID"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1234"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "GENERIC_ID"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "resourceType": "Bundle",
      "type": "transaction",
      "entry": [
        {
          "request": {"method": "PUT", "url": "Provenance/operation-123"},
          "resource": {
            "resourceType": "Provenance",
            "id": "operation-123",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store"
                }
              }
            ],
            "occurredDateTime": "2010-11-08T08:30:00-04:00",
            "recorded": "2010-11-08T08:30:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "system": "https://g.co/healthcare/operation",
                    "value": "projects/my-project/locations/us-central1/datasets/my-dataset/operations/123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store"
                  }
                }
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0,
                        "extension": [
                          {
                            "url": "bottom",
                            "valueDecimal": 100
                          },
                          {
                            "url": "left",
                            "valueDecimal": 100
                          },
                          {
                            "url": "right",
                            "valueDecimal": 200
                          },
                          {
                            "url": "top",
                            "valueDecimal": 200
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "bottom",
                            "valueDecimal": 900
                          },
                          {
                            "url": "left",
                            "valueDecimal": 900
                          },
                          {
                            "url": "right",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "top",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.5
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.5
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00100021",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 10
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 18
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "text-original",
                            "valueString": "John Doe"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "byte-start",
                            "valueDecimal": 25
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 35
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "DATE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1900-12-31"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "DATE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00102150",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "LOCATION"
                          },
                          {
                            "url": "text-original",
                            "valueString": "US"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "LOCATION"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:25-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0
                      },
                      {
                        "url": "frame-index",
                        "valueDecimal": 1,
                        "extension": [
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00101010",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "AGE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "30"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "AGE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00100020",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 4
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "GENERIC_ID"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1234"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "GENERIC_ID"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "resourceType": "Bundle",
      "type": "transaction",
      "entry": [
        {
          "request": {"method": "PUT", "url": "Provenance/operation-123"},
          "resource": {
            "resourceType": "Provenance",
            "id": "operation-123",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store"
                }
              }
            ],
            "occurredDateTime": "2010-11-08T08:30:00-04:00",
            "recorded": "2010-11-08T08:30:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "system": "https://g.co/healthcare/operation",
                    "value": "projects/my-project/locations/us-central1/datasets/my-dataset/operations/123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store"
                  }
                }
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0,
                        "extension": [
                          {
                            "url": "bottom",
                            "valueDecimal": 100
                          },
                          {
                            "url": "left",
                            "valueDecimal": 100
                          },
                          {
                            "url": "right",
                            "valueDecimal": 200
                          },
                          {
                            "url": "top",
                            "valueDecimal": 200
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "bottom",
                            "valueDecimal": 900
                          },
                          {
                            "url": "left",
                            "valueDecimal": 900
                          },
                          {
                            "url": "right",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "top",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.5
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.5
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00100021",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 10
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 18
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "text-original",
                            "valueString": "John Doe"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "byte-start",
                            "valueDecimal": 25
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 35
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "DATE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1900-12-31"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "DATE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00102150",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "LOCATION"
                          },
                          {
                            "url": "text-original",
                            "valueString": "US"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "LOCATION"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:25-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0
                      },
                      {
                        "url": "frame-index",
                        "valueDecimal": 1,
                        "extension": [
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00101010",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "AGE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "30"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "AGE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00100020",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 4
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "GENERIC_ID"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1234"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "GENERIC_ID"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        }
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "entry": [
        {
          "response": {
            "etag": "W/\"MTY0NjY4Mzk2NDk3NDc5NzAwMA\"",
            "lastModified": "LAST_MODIFIED",
            "location": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/operation-123/_history/MTY0NjY4Mzk2NDk3NDc5NzAwMA",
            "status": "200 OK"
          }
        },
        {
          "response": {
            "etag": "W/\"MTY0NjY4Mzk2NDk3NDc5NzAwMA\"",
            "lastModified": "LAST_MODIFIED",
            "location": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/b7346cbf-3741-450c-940e-bca88cb30d82/_history/MTY0NjY4Mzk2NDk3NDc5NzAwMA",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "W/\"MTY0NjY4Mzk2NDk3NDc5NzAwMA\"",
            "lastModified": "LAST_MODIFIED",
            "location": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/abafcb5c-7bc4-4f39-a222-5320560242c1/_history/MTY0NjY4Mzk2NDk3NDc5NzAwMA",
            "status": "201 Created"
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "transaction-response"
    }
    

  2. Create a SearchParameter resource on the DICOM image's relative x coordinate.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * OPERATION_METADATA_FHIR_STORE_ID: the ID of the FHIR store containing the metadata

Request JSON body: 
    
    {
      "resourceType": "SearchParameter",
      "url": "relative-x-coordinate-bottom-left",
      "base": ["Provenance"],
      "code": "relative-x-coordinate-bottom-left",
      "name": "relative x-coordinate of the bottom left corner of the bounding box",
      "type": "number",
      "expression": "Provenance.entity.extension('https://g.co/dicom-images').extension('frame-index').extension('relative-bottom').value.as(Decimal)",
      "status": "active",
      "description": "A search on bottom left relative x-coordinate of annotations generated from de-identification of a DICOM file"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "resourceType": "SearchParameter",
      "url": "relative-x-coordinate-bottom-left",
      "base": ["Provenance"],
      "code": "relative-x-coordinate-bottom-left",
      "name": "relative x-coordinate of the bottom left corner of the bounding box",
      "type": "number",
      "expression": "Provenance.entity.extension('https://g.co/dicom-images').extension('frame-index').extension('relative-bottom').value.as(Decimal)",
      "status": "active",
      "description": "A search on bottom left relative x-coordinate of annotations generated from de-identification of a DICOM file"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/SearchParameter"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "resourceType": "SearchParameter",
      "url": "relative-x-coordinate-bottom-left",
      "base": ["Provenance"],
      "code": "relative-x-coordinate-bottom-left",
      "name": "relative x-coordinate of the bottom left corner of the bounding box",
      "type": "number",
      "expression": "Provenance.entity.extension('https://g.co/dicom-images').extension('frame-index').extension('relative-bottom').value.as(Decimal)",
      "status": "active",
      "description": "A search on bottom left relative x-coordinate of annotations generated from de-identification of a DICOM file"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/SearchParameter" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "base": [
        "Provenance"
      ],
      "code": "relative-x-coordinate-bottom-left",
      "description": "A search on bottom left relative x-coordinate of annotations generated from de-identification of a DICOM file",
      "expression": "Provenance.entity.extension('https://g.co/dicom-images').extension('frame-index').extension('relative-bottom').value.as(Decimal)",
      "id": "f4b2ba96-4014-45db-82d5-3bc7cda0995c",
      "meta": {
        "lastUpdated": "LAST_UPDATED",
        "versionId": "MTY0NjQzNTQzODQzNzE1MDAwMA"
      },
      "name": "relative x-coordinate of the bottom left corner of the bounding box",
      "resourceType": "SearchParameter",
      "status": "active",
      "type": "number",
      "url": "relative-x-coordinate-bottom-left"
    }
    

  3. Enable the custom SearchParameter resource on the FHIR store.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * OPERATION_METADATA_FHIR_STORE_ID: the ID of the FHIR store containing the metadata

Request JSON body: 
    
    {
      "canonicalUrls": [
        "relative-x-coordinate-bottom-left"
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "canonicalUrls": [
        "relative-x-coordinate-bottom-left"
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID:configureSearch"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "canonicalUrls": [
        "relative-x-coordinate-bottom-left"
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID:configureSearch" | Select-Object -Expand Content

The response is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations). Long-running operations are returned when method calls might take a substantial amount of time to complete. Note the value of OPERATION_ID. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

  4. Get the status of the operation.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the dataset
     * DATASET_ID: the dataset where the custom search operation is running
     * OPERATION_ID: the ID of the custom search operation 

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ConfigureSearch",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer?advancedFilter=operation.id%3Dprojects%2FPROJECT_ID%2Flocations%2FLOCATION%2Fdatasets%2FDATASET_ID%2Foperations%2FOPERATION_IDTIMESTAMP&project=PROJECT_ID&interval=NO_LIMIT",
        "counter": {
          "success": "3"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    

  5. Query the Provenance resource using the relative x coordinate search parameter:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * OPERATION_METADATA_FHIR_STORE_ID: the ID of the FHIR store containing the metadata

To send your request, choose one of these options:

#### curl

  
The following sample uses the `relative-x-coordinate-bottom-left=le0.05` query, which searches for an x coordinate within 5% of the edge of the image. 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance?relative-x-coordinate-bottom-left=le0.05"

#### PowerShell

  
The following sample uses the `relative-x-coordinate-bottom-left=le0.05` query, which searches for an x coordinate within 5% of the edge of the image. 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance?relative-x-coordinate-bottom-left=le0.05" | Select-Object -Expand Content

The response shows that one DICOM instance that satisfies the search query is returned: 
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/90062087-8ac2-499c-b952-a04999578bd0",
          "resource": {
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "extension": [
                  {
                    "extension": [
                      {
                        "extension": [
                          {
                            "url": "bottom",
                            "valueDecimal": 100
                          },
                          {
                            "url": "left",
                            "valueDecimal": 100
                          },
                          {
                            "url": "right",
                            "valueDecimal": 200
                          },
                          {
                            "url": "top",
                            "valueDecimal": 200
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "bottom",
                            "valueDecimal": 900
                          },
                          {
                            "url": "left",
                            "valueDecimal": 900
                          },
                          {
                            "url": "right",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "top",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.5
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.5
                          }
                        ],
                        "url": "frame-index",
                        "valueDecimal": 0
                      }
                    ],
                    "url": "https://g.co/dicom-images"
                  },
                  {
                    "extension": [
                      {
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 10
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 18
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "text-original",
                            "valueString": "John Doe"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "byte-start",
                            "valueDecimal": 25
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 35
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "DATE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1900-12-31"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "DATE"
                          }
                        ],
                        "url": "tag-id",
                        "valueString": "00100021"
                      },
                      {
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "LOCATION"
                          },
                          {
                            "url": "text-original",
                            "valueString": "US"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "LOCATION"
                          }
                        ],
                        "url": "tag-id",
                        "valueString": "00102150"
                      }
                    ],
                    "url": "https://g.co/dicom-tags"
                  }
                ],
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                  }
                }
              }
            ],
            "id": "90062087-8ac2-499c-b952-a04999578bd0",
            "meta": {
              "lastUpdated": "LAST_UPDATED",
              "versionId": "MTY0NjY4NDg4Nzk3MDM2MTAwMA"
            },
            "recorded": "2010-11-08T08:39:24-04:00",
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/?relative-x-coordinate-bottom-left=le0.05"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/?relative-x-coordinate-bottom-left=le0.05"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/?relative-x-coordinate-bottom-left=le0.05"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    




### Store sample data, create a source DICOM custom FHIR search, and query

Before running this example, create a destination dataset containing an empty DICOM store and an empty FHIR store. The FHIR store must meet the requirements.

The following example shows how you can store the three Provenance resources created in De-identify DICOM data, write to a FHIR store, and search Provenance resources and then create a custom search. The custom search queries for information about one of the two source DICOM images.

  1. Store the Provenance resources.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * OPERATION_METADATA_FHIR_STORE_ID: the ID of the FHIR store containing the metadata

Request JSON body: 
    
    {
      "resourceType": "Bundle",
      "type": "transaction",
      "entry": [
        {
          "request": {"method": "PUT", "url": "Provenance/operation-123"},
          "resource": {
            "resourceType": "Provenance",
            "id": "operation-123",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store"
                }
              }
            ],
            "occurredDateTime": "2010-11-08T08:30:00-04:00",
            "recorded": "2010-11-08T08:30:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "system": "https://g.co/healthcare/operation",
                    "value": "projects/my-project/locations/us-central1/datasets/my-dataset/operations/123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store"
                  }
                }
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0,
                        "extension": [
                          {
                            "url": "bottom",
                            "valueDecimal": 100
                          },
                          {
                            "url": "left",
                            "valueDecimal": 100
                          },
                          {
                            "url": "right",
                            "valueDecimal": 200
                          },
                          {
                            "url": "top",
                            "valueDecimal": 200
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "bottom",
                            "valueDecimal": 900
                          },
                          {
                            "url": "left",
                            "valueDecimal": 900
                          },
                          {
                            "url": "right",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "top",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.5
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.5
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00100021",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 10
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 18
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "text-original",
                            "valueString": "John Doe"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "byte-start",
                            "valueDecimal": 25
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 35
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "DATE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1900-12-31"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "DATE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00102150",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "LOCATION"
                          },
                          {
                            "url": "text-original",
                            "valueString": "US"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "LOCATION"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:25-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0
                      },
                      {
                        "url": "frame-index",
                        "valueDecimal": 1,
                        "extension": [
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00101010",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "AGE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "30"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "AGE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00100020",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 4
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "GENERIC_ID"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1234"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "GENERIC_ID"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "resourceType": "Bundle",
      "type": "transaction",
      "entry": [
        {
          "request": {"method": "PUT", "url": "Provenance/operation-123"},
          "resource": {
            "resourceType": "Provenance",
            "id": "operation-123",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store"
                }
              }
            ],
            "occurredDateTime": "2010-11-08T08:30:00-04:00",
            "recorded": "2010-11-08T08:30:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "system": "https://g.co/healthcare/operation",
                    "value": "projects/my-project/locations/us-central1/datasets/my-dataset/operations/123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store"
                  }
                }
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0,
                        "extension": [
                          {
                            "url": "bottom",
                            "valueDecimal": 100
                          },
                          {
                            "url": "left",
                            "valueDecimal": 100
                          },
                          {
                            "url": "right",
                            "valueDecimal": 200
                          },
                          {
                            "url": "top",
                            "valueDecimal": 200
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "bottom",
                            "valueDecimal": 900
                          },
                          {
                            "url": "left",
                            "valueDecimal": 900
                          },
                          {
                            "url": "right",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "top",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.5
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.5
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00100021",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 10
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 18
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "text-original",
                            "valueString": "John Doe"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "byte-start",
                            "valueDecimal": 25
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 35
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "DATE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1900-12-31"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "DATE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00102150",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "LOCATION"
                          },
                          {
                            "url": "text-original",
                            "valueString": "US"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "LOCATION"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:25-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0
                      },
                      {
                        "url": "frame-index",
                        "valueDecimal": 1,
                        "extension": [
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00101010",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "AGE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "30"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "AGE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00100020",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 4
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "GENERIC_ID"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1234"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "GENERIC_ID"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "resourceType": "Bundle",
      "type": "transaction",
      "entry": [
        {
          "request": {"method": "PUT", "url": "Provenance/operation-123"},
          "resource": {
            "resourceType": "Provenance",
            "id": "operation-123",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store"
                }
              }
            ],
            "occurredDateTime": "2010-11-08T08:30:00-04:00",
            "recorded": "2010-11-08T08:30:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "system": "https://g.co/healthcare/operation",
                    "value": "projects/my-project/locations/us-central1/datasets/my-dataset/operations/123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store"
                  }
                }
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:24-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/3"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0,
                        "extension": [
                          {
                            "url": "bottom",
                            "valueDecimal": 100
                          },
                          {
                            "url": "left",
                            "valueDecimal": 100
                          },
                          {
                            "url": "right",
                            "valueDecimal": 200
                          },
                          {
                            "url": "top",
                            "valueDecimal": 200
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.05
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.1
                          },
                          {
                            "url": "bottom",
                            "valueDecimal": 900
                          },
                          {
                            "url": "left",
                            "valueDecimal": 900
                          },
                          {
                            "url": "right",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "top",
                            "valueDecimal": 1000
                          },
                          {
                            "url": "relative-bottom",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-left",
                            "valueDecimal": 0.45
                          },
                          {
                            "url": "relative-right",
                            "valueDecimal": 0.5
                          },
                          {
                            "url": "relative-top",
                            "valueDecimal": 0.5
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00100021",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 10
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 18
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "text-original",
                            "valueString": "John Doe"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "PERSON_NAME"
                          },
                          {
                            "url": "byte-start",
                            "valueDecimal": 25
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 35
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "DATE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1900-12-31"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "DATE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00102150",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "LOCATION"
                          },
                          {
                            "url": "text-original",
                            "valueString": "US"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "LOCATION"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        },
        {
          "request": {"method": "POST", "url": "Provenance"},
          "resource": {
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                }
              }
            ],
            "recorded": "2010-11-08T08:39:25-04:00",
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                  }
                },
                "extension": [
                  {
                    "url": "https://g.co/dicom-images",
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0
                      },
                      {
                        "url": "frame-index",
                        "valueDecimal": 1,
                        "extension": [
                        ]
                      }
                    ]
                  },
                  {
                    "url": "https://g.co/dicom-tags",
                    "extension": [
                      {
                        "url": "tag-id",
                        "valueString": "00101010",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "AGE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "30"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "AGE"
                          }
                        ]
                      },
                      {
                        "url": "tag-id",
                        "valueString": "00100020",
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 4
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "GENERIC_ID"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1234"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "GENERIC_ID"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        }
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "entry": [
        {
          "response": {
            "etag": "W/\"MTY0NjY4Mzk2NDk3NDc5NzAwMA\"",
            "lastModified": "LAST_MODIFIED",
            "location": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/operation-123/_history/MTY0NjY4Mzk2NDk3NDc5NzAwMA",
            "status": "200 OK"
          }
        },
        {
          "response": {
            "etag": "W/\"MTY0NjY4Mzk2NDk3NDc5NzAwMA\"",
            "lastModified": "LAST_MODIFIED",
            "location": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/b7346cbf-3741-450c-940e-bca88cb30d82/_history/MTY0NjY4Mzk2NDk3NDc5NzAwMA",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "W/\"MTY0NjY4Mzk2NDk3NDc5NzAwMA\"",
            "lastModified": "LAST_MODIFIED",
            "location": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/abafcb5c-7bc4-4f39-a222-5320560242c1/_history/MTY0NjY4Mzk2NDk3NDc5NzAwMA",
            "status": "201 Created"
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "transaction-response"
    }
    

  2. Create a SearchParameter resource on the source DICOM image.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * OPERATION_METADATA_FHIR_STORE_ID: the ID of the FHIR store containing the metadata

Request JSON body: 
    
    {
      "resourceType": "SearchParameter",
      "url": "lookup-source-instance",
      "base": ["Provenance"],
      "code": "lookup-source-instance",
      "name": "look up the source DICOM instance",
      "type": "string",
      "expression": "Provenance.entity.what.identifier.value",
      "status": "active",
      "description": "A search on the source DICOM instance"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "resourceType": "SearchParameter",
      "url": "lookup-source-instance",
      "base": ["Provenance"],
      "code": "lookup-source-instance",
      "name": "look up the source DICOM instance",
      "type": "string",
      "expression": "Provenance.entity.what.identifier.value",
      "status": "active",
      "description": "A search on the source DICOM instance"
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/SearchParameter"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "resourceType": "SearchParameter",
      "url": "lookup-source-instance",
      "base": ["Provenance"],
      "code": "lookup-source-instance",
      "name": "look up the source DICOM instance",
      "type": "string",
      "expression": "Provenance.entity.what.identifier.value",
      "status": "active",
      "description": "A search on the source DICOM instance"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/SearchParameter" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "base": [
        "Provenance"
      ],
      "code": "lookup-source-instance",
      "description": "A search on the source DICOM instance",
      "expression": "Provenance.entity.what.identifier.value",
      "id": "f4b2ba96-4014-45db-82d5-3bc7cda0995c",
      "meta": {
        "lastUpdated": "LAST_UPDATED",
        "versionId": "MTY0NjY4ODAzODY3NDAxODAwMA"
      },
      "name": "look up the source DICOM instance",
      "resourceType": "SearchParameter",
      "status": "active",
      "type": "string",
      "url": "lookup-source-instance"
    }
    

  3. Enable the custom SearchParameter resource on the FHIR store.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * OPERATION_METADATA_FHIR_STORE_ID: the ID of the FHIR store containing the metadata

Request JSON body: 
    
    {
      "canonicalUrls": [
        "lookup-source-instance"
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "canonicalUrls": [
        "lookup-source-instance"
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID:configureSearch"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "canonicalUrls": [
        "lookup-source-instance"
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID:configureSearch" | Select-Object -Expand Content

The response is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations). Long-running operations are returned when method calls might take a substantial amount of time to complete. Note the value of OPERATION_ID. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

  4. Get the status of the operation.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the dataset
     * DATASET_ID: the dataset where the custom search operation is running
     * OPERATION_ID: the ID of the custom search operation 

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ConfigureSearch",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer?advancedFilter=operation.id%3Dprojects%2FPROJECT_ID%2Flocations%2FLOCATION%2Fdatasets%2FDATASET_ID%2Foperations%2FOPERATION_IDTIMESTAMP&project=PROJECT_ID&interval=NO_LIMIT",
        "counter": {
          "success": "3"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    

  5. Query the Provenance resource using the source DICOM image search parameter.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: your Google Cloud project ID
     * LOCATION: the location of the parent dataset
     * DATASET_ID: the FHIR store's parent dataset
     * OPERATION_METADATA_FHIR_STORE_ID: the ID of the FHIR store containing the metadata

To send your request, choose one of these options:

#### curl

  
The following sample uses the `lookup-source-instance:contains=studies/1/series/2/instances/4` query, which returns information about the instance that contains `studies/1/series/2/instances/4` in its identifier. 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance?lookup-source-instance:contains=studies/1/series/2/instances/4"

#### PowerShell

  
The following sample uses the `lookup-source-instance:contains=studies/1/series/2/instances/4` query, which returns information about the instance that contains `studies/1/series/2/instances/4` in its identifier. 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance?lookup-source-instance:contains=studies/1/series/2/instances/4" | Select-Object -Expand Content

The response shows that one DICOM instance that satisfies the search query is returned: 
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/d82007a1-6481-4793-b17c-ae152051ee9f",
          "resource": {
            "agent": [
              {
                "who": {
                  "identifier": {
                    "value": "projects/test-project/locations/us-central1/datasets/test-dataset/fhirStores/test-fhir-store/fhir/Provenance/operation-123"
                  }
                }
              }
            ],
            "entity": [
              {
                "extension": [
                  {
                    "extension": [
                      {
                        "url": "frame-index",
                        "valueDecimal": 0
                      },
                      {
                        "url": "frame-index",
                        "valueDecimal": 1
                      }
                    ],
                    "url": "https://g.co/dicom-images"
                  },
                  {
                    "extension": [
                      {
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 2
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "AGE"
                          },
                          {
                            "url": "text-original",
                            "valueString": "30"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "AGE"
                          }
                        ],
                        "url": "tag-id",
                        "valueString": "00101010"
                      },
                      {
                        "extension": [
                          {
                            "url": "byte-start",
                            "valueDecimal": 0
                          },
                          {
                            "url": "byte-end",
                            "valueDecimal": 4
                          },
                          {
                            "url": "finding-infotype",
                            "valueString": "GENERIC_ID"
                          },
                          {
                            "url": "text-original",
                            "valueString": "1234"
                          },
                          {
                            "url": "text-replaced",
                            "valueString": "GENERIC_ID"
                          }
                        ],
                        "url": "tag-id",
                        "valueString": "00100020"
                      }
                    ],
                    "url": "https://g.co/dicom-tags"
                  }
                ],
                "role": "source",
                "what": {
                  "identifier": {
                    "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/test-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                  }
                }
              }
            ],
            "id": "d82007a1-6481-4793-b17c-ae152051ee9f",
            "meta": {
              "lastUpdated": "2022-03-07T20:28:07.970361+00:00",
              "versionId": "MTY0NjY4NDg4Nzk3MDM2MTAwMA"
            },
            "recorded": "2010-11-08T08:39:25-04:00",
            "resourceType": "Provenance",
            "target": [
              {
                "identifier": {
                  "value": "https://healthcare.googleapis.com/projects/test-project/locations/us-central1/datasets/test-dataset/dicomStores/deid-dicom-store/dicomWeb/studies/1/series/2/instances/4"
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "relation": "search",
          "url": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/?lookup-source-instance%3Acontains=studies%2F1%2Fseries%2F2%2Finstances%2F4"
        },
        {
          "relation": "first",
          "url": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/?lookup-source-instance%3Acontains=studies%2F1%2Fseries%2F2%2Finstances%2F4"
        },
        {
          "relation": "self",
          "url": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/OPERATION_METADATA_FHIR_STORE_ID/fhir/Provenance/?lookup-source-instance%3Acontains=studies%2F1%2Fseries%2F2%2Finstances%2F4"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    




### Export and query the operation metadata FHIR store

The following example shows how you can export the de-identify operation metadata in the FHIR store to BigQuery and query the exported data for PHI data processed by OCR. The generated data is only compatible with the `LOSSLESS` or `ANALYTICS_V2` [`SchemaType`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores#SchemaType).

  1. [Export the metadata in the FHIR store to a BigQuery dataset](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery).

The metadata is exported to a table named `Provenance` in the selected BigQuery dataset.

  2. Go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  3. In the **Explorer** pane, complete these steps:

     1. Select your Google Cloud project.
     2. Select the BigQuery dataset where you exported the DICOM metadata.
     3. Select the **Provenance** table.
  4. Click add_box **Compose new query**.

  5. Run the following query:
         
         SELECT
           what.identifier.value AS Source,
           target[OFFSET(0)].identifier.value AS Destination,
           `left` AS `Left`,
           `right` AS `Right`,
           top AS Top,
           bottom AS Bottom,
           quote AS Quote,
           infoType AS InfoType,
           confidence AS Confidence
         FROM
           `PROJECT_ID.BIGQUERY_DATASET.Provenance`, UNNEST(entity), UNNEST(dicom_images), UNNEST(frame_index)
         LIMIT
           10
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project
     * BIGQUERY_DATASET: the BigQuery dataset where you exported the metadata from the FHIR store
  6. Click play_circle **Run**.

The query results show the metadata for the de-identified PHI data in a tabular format. If you don't specify a destination table, the query job writes the output to a temporary (cache) table.




## Quota

Writing de-identify operation metadata to a FHIR store consumes `fhir_write_ops` quotas in the project where the operation metadata is written. One FHIR resource is created for each DICOM instance, so the throughput of the de-identify operation cannot be greater than what your FHIR quota allows.

## Billing

Each Provenance resource created in the operation metadata FHIR store incurs a charge for calling [`fhir.update`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/update). The number of API calls to `fhir.update` can be calculated as: `Total number of DICOM instances de-identified + 1`.

## What's next

  * Learn how to [export the FHIR resources to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery) for exploration and analysis.
  * Learn how to [stream FHIR resource changes to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bigquery-streaming) to synchronize the data in a FHIR store with a BigQuery dataset in near real time.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
