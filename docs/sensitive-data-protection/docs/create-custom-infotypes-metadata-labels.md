---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels/
title: Create a custom metadata label detector \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:03.060461+00:00
---

# Create a custom metadata label detector  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Create a custom metadata label detector Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Sensitive Data Protection to detect specific metadata labels in your content.

In this document, _metadata labels_ are file labels that are embedded in supported files or metadata provided by your client application in the inspection request. If Sensitive Data Protection finds content that matches your metadata criteria, it generates a finding.

To scan for metadata labels, create a custom metadata label infoType. Then, configure your inspection or discovery scan to search for that infoType.

## Benefits and use cases

This feature lets you use your existing classification taxonomies for content inspection and policy enforcement. If you use a custom or third-party classification system that applies metadata labels to your documents, you can configure Sensitive Data Protection to detect these metadata labels during your inspection or discovery operations.

Example use cases include the following:

  * Scan files for the presence of [Google Drive labels](https://developers.google.com/workspace/drive/labels/guides/overview) or [Microsoft sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels) that contain specific metadata.
  * Combine metadata label detection with standard infoType detection for a multi-layered approach.
  * Scan metadata that your client application passes alongside the content, even if the metadata isn't embedded in the file. In this document, this type of metadata is called _client-provided metadata_.
  * Sanitize documents using Model Armor based on specific metadata labels. To use this feature with Model Armor—or services that use Model Armor like Gemini Enterprise—you must [create an advanced Sensitive Data Protection configuration in Model Armor](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#advanced_sdp_configuration) that references this custom metadata label detector.



## Supported metadata formats

This feature can detect the following types of metadata:

  * Google Drive labels
  * Microsoft sensitivity labels on the following file types:

    * DOCX
    * PDF
    * PPTX
    * XLSX
  * Client-provided metadata




## Unsupported configurations

Custom metadata label detectors aren't supported in the following:

  * [Inspection rule sets](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InspectionRuleSet)
  * [De-identification transformations](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#de-identification_transformations)



## Create a metadata label detector

To create a metadata label detector, define a [`CustomInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType) within an [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) object. Depending on the type of metadata that you want to scan, define one of the following:

  * To scan for Google Drive labels and Microsoft sensitivity labels, define a [`FileLabelInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FileLabelInfoType). For more information, see Create a metadata label detector to scan for file labels in this document.
  * To use regular expressions to scan for custom key-value pairs, define a [`MetadataKeyValueExpression`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#MetadataKeyValueExpression). This type is appropriate for client-provided metadata. For more information, see Create a metadata label detector to scan for key-value pairs in this document.



## Create a metadata label detector to scan for file labels

To scan for Google Drive labels or Microsoft sensitivity labels, define a [`CustomInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType) that has a [`FileLabelInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FileLabelInfoType):
    
    
    {
      "inspectConfig": {
        "customInfoTypes": [
          {
            "infoType": {
              "name": "CUSTOM_METADATA_LABEL_NAME"
            },
            "likelihood": "LIKELIHOOD",
            "sensitivityScore": {
              "score": "SENSITIVITY_SCORE"
            },
            "fileLabelInfoType": {
              "googleDriveLabel": {
                "labelId": "LABEL_ID",
                "labelFieldsToMatch": [
                  {
                    "id": "FIELD_ID",
                    "value": "FIELD_VALUE"
                  }
                ]
              },
              "sensitivityLabel": {
                "guid": "GUID"
              }
            }
          }
        ]
      }
    }
    

Replace the following:

  * `CUSTOM_METADATA_LABEL_NAME`: The name to assign to the custom infoType detector.
  * `LIKELIHOOD`: Optional. The [`Likelihood`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood) value to assign to all findings that match this custom infoType. If you omit this field, the default likelihood level is `VERY_LIKELY`.
  * `SENSITIVITY_SCORE`: Optional. The [`SensitivityScore`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore) to assign to all findings that match this custom infoType. If you omit this field, the default sensitivity score is `HIGH`.

Sensitivity scores are used in [data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles). When profiling your data, Sensitive Data Protection uses the sensitivity scores of the infoTypes to [calculate the sensitivity level](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

  * `LABEL_ID`: Optional. The ID of a [Google Drive label](https://developers.google.com/workspace/drive/api/guides/about-labels) to match. If you specify only a `LABEL_ID`, the detector matches any file that has that Google Drive label applied, regardless of its field values. To match specific field values within a label, include a `labelFieldsToMatch` object.

  * `FIELD_ID`: Required if you specify a `labelFieldsToMatch` object. The ID of a Google Drive label field to match.

  * `FIELD_VALUE`: Required if you specify a `labelFieldsToMatch` object. The value of a Google Drive label field to match.

  * `GUID`: Optional. The GUID of a [Microsoft sensitivity label](https://learn.microsoft.com/en-us/purview/sensitivity-labels) to match.




### Example detector for a Google Drive label

This `inspectConfig` example defines a custom infoType named `CUSTOM_GOOGLE_DRIVE_LABEL_CONFIDENTIAL`. This custom infoType detects a Google Drive label that has the following:

  * The label ID `mydrive-label-id`
  * Within that label, a field with the ID `sensitivity-field-id` and the value `confidential`.



If you don't specify a field ID and value in `labelFieldsToMatch`, this custom infoType detects the files that have the `mydrive-label-id` label, regardless of the presence of any label fields.
    
    
    {
      "inspectConfig": {
        "customInfoTypes": [
          {
            "infoType": {
              "name": "CUSTOM_GOOGLE_DRIVE_LABEL_CONFIDENTIAL"
            },
            "likelihood": "VERY_LIKELY",
            "fileLabelInfoType": {
              "googleDriveLabel": {
                "labelId": "mydrive-label-id",
                "labelFieldsToMatch": [
                  {
                    "id": "sensitivity-field-id",
                    "value": "confidential"
                  }
                ]
              }
            }
          }
        ],
        "minLikelihood": "POSSIBLE"
      }
    }
    

When you use this configuration in an inspection job, Sensitive Data Protection generates a `CUSTOM_GOOGLE_DRIVE_LABEL_CONFIDENTIAL` finding if it finds a match.

### Example detector for a Microsoft sensitivity label

This `inspectConfig` example defines a custom infoType named `CUSTOM_SENSITIVITY_LABEL_CONFIDENTIAL`. This custom infoType detects a Microsoft sensitivity label that contains the GUID `12345678-9012-3456-7890-123456789012`:
    
    
    {
      "inspectConfig": {
        "customInfoTypes": [
          {
            "infoType": {
              "name": "CUSTOM_SENSITIVITY_LABEL_CONFIDENTIAL"
            },
            "likelihood": "VERY_LIKELY",
            "fileLabelInfoType": {
              "sensitivityLabel": {
                "guid": "12345678-9012-3456-7890-123456789012"
              }
            }
          }
        ],
        "minLikelihood": "POSSIBLE"
      }
    }
    

When you use this configuration in an inspection job, Sensitive Data Protection generates a `CUSTOM_SENSITIVITY_LABEL_CONFIDENTIAL` finding if it finds a match.

## Create a metadata label detector to scan for custom key-value pairs

To use regular expressions to scan for custom key-value pairs in client-provided metadata, follow these steps:

  1. Define a [`CustomInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType) that has a [`MetadataKeyValueExpression`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#MetadataKeyValueExpression):
         
         {
           "inspectConfig": {
             "customInfoTypes": [
               {
                 "infoType": {
                   "name": "CUSTOM_METADATA_LABEL_NAME"
                 },
                 "likelihood": "LIKELIHOOD",
                 "sensitivityScore": {
                   "score": "SENSITIVITY_SCORE"
                 },
                 "metadataKeyValueExpression": {
                   "keyRegex": "KEY_REGULAR_EXPRESSION",
                   "valueRegex": "VALUE_REGULAR_EXPRESSION"
                 }
               }
             ]
           }
         }
         

Replace the following:

     * `CUSTOM_METADATA_LABEL_NAME`: The name to assign to the custom infoType detector.
     * `LIKELIHOOD`: Optional. The [`Likelihood`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood) value to assign to all findings that match this custom infoType. If you omit this field, the default likelihood level is `VERY_LIKELY`.
     * `SENSITIVITY_SCORE`: Optional. The [`SensitivityScore`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore) to assign to all findings that match this custom infoType. If you omit this field, the default sensitivity score is `HIGH`.

Sensitivity scores are used in [data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles). When profiling your data, Sensitive Data Protection uses the sensitivity scores of the infoTypes to [calculate the sensitivity level](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

     * `KEY_REGULAR_EXPRESSION`: A regular expression to search for in the keys of metadata labels.

     * `VALUE_REGULAR_EXPRESSION`: A regular expression to search for in the values of metadata labels.

  2. In your [`content.inspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect) request, specify the client-provided metadata in the [`ContentMetadata`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#ContentMetadata) field of the [`ContentItem`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem).




### Example request for scanning client-provided metadata

The following example shows a `content.inspect` request that includes both a PDF file and client-provided metadata. The request uses a custom infoType named `CUSTOM_METADATA_CLASSIFICATION` to scan for files that are marked as "Confidential" or "Internal Use".
    
    
    {
      "inspectConfig": {
        "customInfoTypes": [
          {
            "infoType": {
              "name": "CUSTOM_METADATA_CLASSIFICATION"
            },
            "likelihood": "VERY_LIKELY",
            "metadataKeyValueExpression": {
              "keyRegex": "classification",
              "valueRegex": "Confidential|Internal Use"
            }
          }
        ]
      },
      "item": {
        "byteItem": {
          "type": "PDF",
          "data": "BASE64_ENCODED_PDF"
        },
        "contentMetadata": {
          "properties": [
            {
              "key": "classification",
              "value": "Confidential"
            }
          ]
        }
      }
    }
    

Replace `BASE64_ENCODED_PDF` with a base64-encoded file to scan.

Sensitive Data Protection generates a finding if it finds a match in the content. The finding's [`MetadataType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#MetadataType) for [`MetadataLocation`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#MetadataLocation) is populated based on whether the match is embedded in the file (`CONTENT_METADATA`) or provided by the client (`CLIENT_PROVIDED_METADATA`).

## What's next

  * Create an [advanced Sensitive Data Protection configuration in Model Armor](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#advanced_sdp_configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
