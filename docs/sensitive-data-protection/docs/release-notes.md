---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes/
title: Sensitive Data Protection release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:28.129626+00:00
---

# Sensitive Data Protection release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Resources ](https://docs.cloud.google.com/sensitive-data-protection/docs/resources)



Send feedback 

#  Sensitive Data Protection release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Sensitive Data Protection. You can periodically check this page for announcements about new or updated features, known issues, and deprecated functionality.

For a list of known issues for Sensitive Data Protection, see [Known issues](https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues).

**Current version: v2**

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/dlp-release-notes.xml) directly. 

## October 09, 2026

Change

If you set `[InfoType.version](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)` to `legacy` when including the `MEDICAL_ID` infoType in your `[InspectConfig](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`, Sensitive Data Protection now includes `MEDICAL_RECORD_NUMBER` findings as type `MEDICAL_ID` in the scan results.

## October 03, 2026

Change

A new version with an updated name dictionary is available for the `PERSON_NAME` [infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) detector. You can try it out by setting `[InfoType.version](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType#FIELDS.version)` to `latest` when including the `PERSON_NAME` infoType in your `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`.

You can still use the previous functionality by setting `[InfoType.version](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType#FIELDS.version)` to `stable` or leaving it unset when using the `PERSON_NAME` infoType. In 30 days, the new version will be promoted to `stable`.

## August 31, 2026

Feature

Sensitive Data Protection content policies are in [General Availability](https://cloud.google.com/products#product-launch-stages). You can use content policies to evaluate content and return an `ALLOW` or `BLOCK` verdict based on data sensitivity.

For more information about content policies, see the following:

  * [Overview of content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy)
  * [Create and manage content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies)



Sensitive Data Protection content policies are integrated with Gemini Enterprise. For more information, see the following:

  * [Protect sensitive data in sources](https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data)
  * [Protect sensitive data in Gemini Notebook Enterprise sources](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/protect-sensitive-data)



## August 20, 2026

Change

Image scanning is available in the following regions:

  * `europe-north1`
  * `us-central1`



For more information, see [Locations that support image scanning](https://docs.cloud.google.com/sensitive-data-protection/docs/locations#image-limitations).

## August 13, 2026

Feature

The `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, and `OPENAI_API_KEY` infoType detectors are available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## July 14, 2026

Feature

The `CRIME_STATUS` infoType detector is available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## July 13, 2026

Change

If you leave `[InfoType.version](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType#FIELDS.version)` unset or set it to `stable` when setting the `MEDICAL_ID` infoType in your `[InspectConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`, Sensitive Data Protection includes `MEDICAL_RECORD_NUMBER` findings as type `MEDICAL_ID` in the scan results.

You can still use the old functionality by setting `InfoType.version` to `legacy` for the next 90 days.

## July 09, 2026

Feature

The `SWITZERLAND_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## June 29, 2026

Feature

You can configure Sensitive Data Protection to detect specific file labels, which can represent Google Drive labels or Microsoft sensitivity labels. For more information, see [Create a custom metadata label detector](https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels).

## June 23, 2026

Feature

[Image safety classification infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#image-context) are now supported in `[ExcludeByImageFindings](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#excludebyimagefindings)` and `[AdjustByImageFindings](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#adjustbyimagefindings)` detection rules.

For information about configuring these rules, see [Modifying infoType detectors to refine scan results](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules).

## June 22, 2026

Change

Image scanning is available in the following cloud regions:

  * `asia-southeast1`
  * `us-east4`
  * `us-west1`



For more information, see [Locations that support image scanning](https://cloud.google.com/sensitive-data-protection/docs/locations#image-limitations).

Fixed

Between July 2025 and June 2026, some [table data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#table-data-profile) saved to BigQuery contained an incorrect `1970-01-01` timestamp instead of `NULL` in [`expiration_time`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles#TableDataProfile.FIELDS.expiration_time) for tables that don't expire. This issue has been fixed. New exports of table data profiles show the correct expiration timestamps.

## June 12, 2026

Feature

Added support for inspecting and de-identifying batched content. You can now include a `[BatchContentItem](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#BatchContentItem)` in your `[ContentItem](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem)` requests.

## June 08, 2026

Feature

The `OBJECT_TYPE/PERSON/SIGNATURE` infoType detector is available in `global` and the `asia`, `europe`, and `us` multi-regions. For more information about all infoTypes, see [InfoType detector reference](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## June 03, 2026

Feature

Added support for inspecting and de-identifying conversational content. You can now include a `[Conversation](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#Conversation)` in your `[ContentItem](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem)` requests.

## May 11, 2026

Change

If you set `[InfoType.version](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)` to `latest` when including the `MEDICAL_ID` infoType in your `[InspectConfig](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`, Sensitive Data Protection will now include `MEDICAL_RECORD_NUMBER` findings as type `MEDICAL_ID` in the scan results.

You can still use the old functionality by setting `InfoType.version` to `stable`. In 30 days, the new functionality will be promoted to `stable`.

## March 28, 2026

Feature

You can configure Sensitive Data Protection to detect specific client-provided metadata. For more information, see [Create a custom metadata label detector](https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels).

## March 13, 2026

Feature

The `USER_NAME` infoType detector is available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## March 11, 2026

Feature

The `CRIME_STATUS` infoType detector is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information about all infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## March 07, 2026

Feature

You can configure Sensitive Data Protection to detect specific metadata labels in your content. For more information, see [Create a custom metadata label detector](https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels).

## February 23, 2026

Feature

Sensitive Data Protection can discover and profile Vertex AI tuning jobs. For more information, see [Sensitive data discovery for Vertex AI](https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-vertex-ai).

Feature

The following features are in [General Availability](https://cloud.google.com/products#product-launch-stages):

  * [Adjustment rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules#adjustment-rules), which let you customize the likelihood of findings based on their context. Adjustment rules support text-based and image-based operations.
  * [Image-based exclusion rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules#exclusion-rules), which let you refine your image inspection results by excluding findings based on their spatial relationships with other findings.
  * [Enhanced rule ordering](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules#rule-order), which lets you chain rules based on the order you specify them in the ruleset.



For information about configuring these rules, see [Modifying infoType detectors to refine scan results](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules).

Feature

The `KOREA_BRN` infoType detector is available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## January 20, 2026

Feature

Sensitive Data Protection is available in the `asia-southeast3` (Bangkok) region. For more information, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations).

## January 16, 2026

Feature

The following infoType detectors are available in `global` and the `asia`, `europe`, and `us` multi-regions:

  * `IMAGE_TYPE/CONTEXT/VIOLENCE`
  * `IMAGE_TYPE/CONTEXT/SEXUALLY_EXPLICIT`
  * `IMAGE_TYPE/CONTEXT/SEXUALLY_SUGGESTIVE`



For more information about all infoTypes, see [InfoType detector reference](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## January 05, 2026

Feature

General infoType functionality and the following infoTypes are now available in all regions:

  * `CREDIT_CARD_DATA`
  * `DEMOGRAPHIC_DATA`
  * `DRIVERS_LICENSE_NUMBER`
  * `FINANCIAL_ID`
  * `GEOGRAPHIC_DATA`
  * `GOVERNMENT_ID`
  * `MEDICAL_DATA`
  * `MEDICAL_ID`
  * `SECURITY_DATA`
  * `TECHNICAL_ID`



For more information about all built-in infoTypes, see the [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## December 15, 2025

Feature

The `OBJECT_TYPE/PERSON/FACE` infoType detector is available in [Preview](https://cloud.google.com/products#product-launch-stages) in `global` and the `asia`, `europe`, and `us` multi-regions. For more information about all infoTypes, see [InfoType detector reference](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## November 23, 2025

Feature

The `KOREA_NHI_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## November 07, 2025

Feature

The following infoType detectors are available in `global` and the `europe` and `us` multi-regions:

  * `DOCUMENT_TYPE/CONTEXT/FINANCE`
  * `DOCUMENT_TYPE/CONTEXT/HEALTH`
  * `DOCUMENT_TYPE/CONTEXT/LEGAL`
  * `DOCUMENT_TYPE/CONTEXT/OBSCENE`
  * `DOCUMENT_TYPE/CONTEXT/OFFENSIVE`
  * `DOCUMENT_TYPE/CONTEXT/POLITICS`
  * `DOCUMENT_TYPE/CONTEXT/RELIGION`
  * `DOCUMENT_TYPE/CONTEXT/SEXUAL`



For more information about all infoTypes, see [InfoType detector reference](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## November 03, 2025

Feature

The `OBJECT_TYPE/PERSON/PASSPORT` and `OBJECT_TYPE/PERSON/PHOTO_ID_CARD` infoType detectors are available in `global` and the `asia`, `europe`, and `us` multi-regions. For more information about all infoTypes, see [InfoType detector reference](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## October 27, 2025

Feature

The `NEW_ZEALAND_DRIVERS_LICENSE_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## October 17, 2025

Feature

Customers with an organization-level activation of Security Command Center Premium have an organization-level discovery subscription at no charge from Sensitive Data Protection. For more information, see [Sensitive data discovery in Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery#sensitive-data-discovery-scc-premium).

## October 10, 2025

Feature

The `BRAZIL_RG_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## October 02, 2025

Breaking

This is an addition to the May 1 release note announcing the deprecation of the ability to send inspection and discovery results from Sensitive Data Protection to Data Catalog.

If you have workflows that create inspection jobs or job triggers and set the deprecated [`PublishFindingsToCloudDataCatalog`](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#publishfindingstoclouddatacatalog) action, you must update those workflows by January 30, 2026. On or after this date, new jobs and job triggers that are created by those workflows will fail.

## September 22, 2025

Feature

The `DOCUMENT_TYPE/FINANCE/INVOICE` and `DOCUMENT_TYPE/MEDICAL/RECORD` infoType detectors are available in `global` and the `asia`, `europe`, and `us` multi-regions. For more information about all infoTypes, see [InfoType detector reference](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## September 19, 2025

Feature

When you inspect a BigQuery table for sensitive data, you can send the inspection findings to Dataplex Universal Catalog. For more information, see [Send inspection results to Dataplex Universal Catalog as aspects](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job).

## September 08, 2025

Fixed

Fixed the issue preventing Sensitive Data Protection from detecting sensitive data in the headers and footers of certain rich document types.

## September 02, 2025

Feature

When configuring schedules for Cloud Storage data discovery, you can select data based on specific tags. For more information, see [Profile Cloud Storage data in an organization or folder](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-cloud-storage) or [Profile Cloud Storage data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-cloud-storage).

## August 29, 2025

Announcement

The August 25 release note announcing the release of the `DOCUMENT_TYPE/FINANCE/INVOICE` and `DOCUMENT_TYPE/MEDICAL/RECORD` infoType detectors was published in error. These infotypes are not available.

## August 25, 2025

Feature

The `DOCUMENT_TYPE/FINANCE/INVOICE` and `DOCUMENT_TYPE/MEDICAL/RECORD` infoType detectors are available in `global` and the `asia`, `europe`, and `us` multi-regions. For more information about all infoTypes, see [InfoType detector reference](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

## August 15, 2025

Feature

The `AUSTRIA_SOCIAL_SECURITY_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

Feature

During discovery operations, Sensitive Data Protection scans the contents of various archive files. For a list of supported file types, see [Supported file clusters in discovery operations](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#file_clusters).

## August 13, 2025

Feature

You can configure Sensitive Data Protection to save the findings from an inspection job to a Cloud Storage bucket or folder. For more information, see [Save findings to Cloud Storage](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions#save-findings-cloud-storage).

## August 04, 2025

Feature

Sensitive Data Protection provides recommendations to optimize your infoType selections. In the Google Cloud console, if you select a specific infoType that is covered by a general infoType, Sensitive Data Protection recommends general infoTypes that you can use instead.

For information about the benefits of using general infoTypes, see [General and specific infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes#general-specific-infotypes).

## August 01, 2025

Feature

The following infoType detectors are available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/C`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/CPP`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/CS`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/GO`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/HTML`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/JAVA`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/JAVASCRIPT`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/JSON`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/PHP`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/POWERSHELL`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/PYTHON`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/RUST`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/SHELL`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/SQL`
  * `DOCUMENT_TYPE/R&D/SOURCE_CODE/TYPESCRIPT`



## July 04, 2025

Feature

Sensitive Data Protection can detect and redact the following object infoTypes in images:

  * `OBJECT_TYPE/BARCODE`
  * `OBJECT_TYPE/LICENSE_PLATE`
  * `OBJECT_TYPE/PERSON`
  * `OBJECT_TYPE/WHITEBOARD`



For more information, see the following:

  * [Inspect an image for sensitive objects](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images#inspect_an_image_for_sensitive_objects)
  * [Object redaction](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images#object-redaction)



## June 25, 2025

Feature

The `CZECHIA_PERSONAL_ID_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## May 19, 2025

Change

The [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) was updated to include the designated categories (locations, industries, and types) and default sensitivity score of each infoType.

## May 14, 2025

Fixed

[Inspection jobs for XSLX files in Cloud Storage](https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage#inspecting-gcs) have improved performance. Sensitive Data Protection reads [large custom dictionary](https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes) source data only once for each sheet that has potential findings.

## May 12, 2025

Change

By default, scans for `MAC_ADDRESS` findings now include `MAC_ADDRESS_LOCAL` findings. Previously, you could only use this functionality if you set the `[InfoType.version](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)` of `MAC_ADDRESS` to `latest` in your `[InspectConfig](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`.

You can still use the old version of `MAC_ADDRESS` by setting its `[InfoType.version](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)` to `legacy` or by using the `MAC_ADDRESS_UNIVERSAL` infoType. In 90 days, the new functionality will be promoted to `legacy`.

## May 01, 2025

Deprecated

On or after September 30, 2025, you can no longer send inspection and discovery results from Sensitive Data Protection to Data Catalog. [Data Catalog is deprecated](https://docs.cloud.google.com/dataplex/docs/deprecations) and will be discontinued on January 30, 2026. For Sensitive Data Protection, no action is required from you. No inspection or discovery configuration will break. 

For discovery operations, we recommend that you [add Dataplex Catalog aspects based on insights from data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects) instead.

Feature

You can automatically attach aspects to Dataplex entries after profiling supported data resources. For more information, see [Add Dataplex Catalog aspects based on insights from data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects).

## April 28, 2025

Feature

The discovery service of Sensitive Data Protection now supports Azure Blob Storage. You can run discovery to generate data profiles of your Blob Storage containers. [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) provide metrics and insights about the sensitivity and risk levels of your data to help you plan your data protection and governance workflows.

This feature is available only to Security Command Center Enterprise customers. To use this feature, you need an Azure connector in Security Command Center that has permissions for Sensitive Data Protection discovery.

To get started on profiling Blob Storage data, see the following:

  * [Connect to Microsoft Azure for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure)
  * [Profile Azure Blob Storage data](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-azure-blob-storage)



## April 17, 2025

Change

The discovery findings that Sensitive Data Protection generates in Security Command Center include recommended next steps. This improvement applies to the finding categories listed in [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

## April 11, 2025

Change

If you set `[InfoType.version](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)` to `latest` when including the `MAC_ADDRESS` infoType in your `[InspectConfig](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`, Sensitive Data Protection will now include `MAC_ADDRESS_LOCAL` findings as type `MAC_ADDRESS` in the scan results.

You can still use the old functionality by setting `InfoType.version` to `stable`, by leaving `InfoType.version` unset when using the `MAC_ADDRESS` infoType, or by using the `MAC_ADDRESS_UNIVERSAL` infoType. In 30 days, the new functionality will be promoted to `stable`.

## April 02, 2025

Feature

The `MAC_ADDRESS_UNIVERSAL` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## March 19, 2025

Feature

The `CZECHIA_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## March 04, 2025

Feature

Sensitive Data Protection is available in the `europe-north2` region. For more information, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations).

## February 17, 2025

Feature

Data profiles that send findings to Security Command Center include the `INFO_TYPES` and `RELATED_RESOURCES` fields when available. These fields appear in the `sourceProperties` field of the finding in Security Command Center. The affected finding categories are `DATA_RISK`, `DATA_SENSITIVITY`, `PUBLIC_SENSITIVE_DATA`, `SECRETS_IN_STORAGE`, and `SENSITIVE_DATA_CMEK_DISABLED`.

## February 14, 2025

Feature

[Sensitive data discovery for Vertex AI](https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-vertex-ai) is in [General Availability](https://cloud.google.com/products#product-launch-stages). You can run discovery at the organization, folder, or project level to generate profiles of your Vertex AI training data. Data profiles provide metrics and insights about the sensitivity and risk levels of your data to help you plan your data governance workflows.

## February 11, 2025

Feature

The `JAPAN_CORPORATE_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## February 10, 2025

Change

The `RELIGIOUS_TERM` infoType detector is now generally available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## February 05, 2025

Change

The `CREDIT_CARD_EXPIRATION_DATE` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## February 04, 2025

Announcement

Regional endpoints for Sensitive Data Protection are available in the `eu` and `us` multi-regions. For more information, see [Global and regional endpoints for Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints).

## February 03, 2025

Feature

The `CVV_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## January 13, 2025

Feature

The `TAIWAN_ID_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

Feature

The `FRANCE_DRIVERS_LICENSE_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## December 06, 2024

Change

The current default `DATE_OF_BIRTH` [infoType](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference) detection model, which is available when [`InfoType.version`](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) is set to `latest` or `stable`, is now also used when [`InfoType.version`](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) is set to `legacy`. 

The old detection model that was previously available by setting [`InfoType.version`](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) to `legacy` is no longer available.

## November 25, 2024

Change

The `PHONE_NUMBER` [infoType](https://cloud.google.com/dlp/docs/infotypes-reference) functionality that was previously only available by setting [`InfoType.version`](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` or `stable` is now also used when [`InfoType.version`](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) is set to `legacy`. The new model includes `US_TOLLFREE_PHONE_NUMBER` findings as type `PHONE_NUMBER` in the scan results.

The old detection model that was previously available by setting [`InfoType.version`](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy` is no longer available.

## November 19, 2024

Announcement

The November 4 release note announcing the release of sample discovery findings was published in error. This feature is not available.

## November 15, 2024

Announcement

[Sensitive data discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) is now included in Security Command Center Enterprise. To enable discovery in the Security Command Center Enterprise tier, see [Enable sensitive data discovery in the Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery) in the Security Command Center documentation.

The Sensitive Data Protection discovery service remains available to Security Command Center Premium and Standard customers as a [separately priced feature](https://cloud.google.com/sensitive-data-protection/pricing#data_profiling_pricing). For more information, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

## November 14, 2024

Change

The current default `STREET_ADDRESS` [infoType](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference) detection model, which is available when [`InfoType.version`](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) is set to `latest` or `stable`, is now also used when [`InfoType.version`](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) is set to `legacy`. 

The old detection model that was previously available by setting [`InfoType.version`](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) to `legacy` is no longer available.

## November 11, 2024

Change

The current default `ORGANIZATION_NAME` [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detection model, which is available when [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) is set to `latest` or `stable`, is now also used when [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) is set to `legacy`. 

The old detection model that was previously available by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy` is no longer available.

The region restriction on the `ORGANIZATION_NAME` [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) has been lifted. It is now available in all regions.

## November 08, 2024

Feature

The `EMPLOYMENT_STATUS` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## November 04, 2024

Feature

You can configure discovery to save sample findings to a BigQuery table. This feature is useful if you want to evaluate whether your [inspection configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#inspection-template) is correctly matching the type of information that you want to flag as sensitive. To enable this feature, [create or edit the scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#create) for the data resource that you want to profile.

## October 28, 2024

Feature

The `ITALY_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## October 25, 2024

Feature

The `PARAGUAY_TAX_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

Feature

The sensitive data discovery service can now detect the presence of [secrets](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets), such as passwords and authentication tokens, in your Cloud Run service revision environment variables. Sensitive Data Protection sends any findings to Security Command Center as [vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#sdp-vulnerabilities). For more information, see [Report secrets in environment variables to Security Command Center](https://docs.cloud.google.com/dlp/docs/secrets-discovery).

## October 11, 2024

Feature

The `KOREA_DRIVERS_LICENSE_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## October 10, 2024

Feature

The `INDONESIA_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## October 01, 2024

Change

The current default `LOCATION` [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detection model, which is accessible when [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) is set to `latest` or `stable`, is now also used when [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) is set to `legacy`. 

The old detection model that was previously accessible by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy` is no longer accessible.

The region restriction on the `LOCATION` [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) has been lifted. It is now available in all regions.

## September 30, 2024

Feature

The ` FINLAND_BUSINESS_ID ` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## September 17, 2024

Feature

The `POLITICAL_TERM` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

Feature

The `NEW_ZEALAND_NHI_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## September 11, 2024

Feature

The discovery service of Sensitive Data Protection now supports Amazon S3. You can run discovery to generate data profiles of your S3 buckets. Data profiles provide metrics and insights about the sensitivity and risk levels of your data to help you plan your data governance workflows.

This feature is available only to Security Command Center Enterprise customers. To use this feature, you need an AWS connector in Security Command Center that has Sensitive Data Protection enabled.

To get started on profiling Amazon S3 data, see the following:

  * [Connect to AWS for vulnerability detection and risk assessment](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws)
  * [Sensitive data discovery for Amazon S3](https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-amazon-s3)
  * [Profile Amazon S3 data](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-amazon-s3)



For more information about sensitive data discovery, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## September 10, 2024

Feature

The `DOD_ID_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## September 06, 2024

Feature

The `SEXUAL_ORIENTATION` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## August 27, 2024

Feature

Regional endpoints are available for Sensitive Data Protection. Regional endpoints help you meet data residency requirements by keeping data at rest, in use, and in transit within your specified region. For more information, see [Global and regional endpoints for Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints). 

Regional endpoints for Sensitive Data Protection are available in the following regions:

  * `australia-southeast1`
  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `me-central1`
  * `me-central2`
  * `me-west1`
  * `southamerica-east1`
  * `southamerica-west1`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`



## August 15, 2024

Change

The `PHONE_NUMBER` [infoType](https://cloud.google.com/dlp/docs/infotypes-reference) functionality that was previously only accessible by setting [`InfoType.version`](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` has been promoted to be the default detection model for this infoType. The new model includes `US_TOLLFREE_PHONE_NUMBER` findings as type `PHONE_NUMBER` in the scan results.

To enable the new functionality, leave [`InfoType.version`](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) unset, or set it to `latest` or `stable`. To use the old functionality, set [`InfoType.version`](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy`. You can continue to use the legacy functionality for 90 days.

## August 05, 2024

Change

The `ORGANIZATION_NAME` [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detection model that was previously only accessible by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` has been promoted to be the default detection model for this infoType. The new model offers improved detection quality.

To use the new model, leave [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) unset, or set it to `latest` or `stable`. To use the old detection model, set [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy`. You can continue to use the legacy model for 90 days.

Change

The `STREET_ADDRESS` [infoType](https://cloud.google.com/dlp/docs/infotypes-reference) detection model that was previously only accessible by setting [`InfoType.version`](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` has been promoted to be the default detection model for this infoType. The new model offers improved detection quality.

To use the new model, leave [`InfoType.version`](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) unset, or set it to `latest` or `stable`. To use the old detection model, set [`InfoType.version`](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy`. You can continue to use the legacy model for 90 days.

## July 31, 2024

Change

The `DATE_OF_BIRTH` [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detection model that was previously only accessible by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` has been promoted to be the default detection model for this infoType. The new model offers improved detection quality.

To use the new model, leave [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) unset, or set it to `latest` or `stable`. To use the old detection model, set [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy`. You can continue to use the legacy model for 90 days.

## July 25, 2024

Feature

Sensitive Data Protection can now apply tags to your profiled resources based on their calculated data sensitivity. Using these tags, you can configure [IAM conditions](https://docs.cloud.google.com/iam/docs/tags-access-control) that automatically grant or deny IAM access to resources based on the sensitivity of the data in those resources.

For more information, see [Control IAM access to resources based on data sensitivity](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity).

## July 17, 2024

Feature

The `ARMENIA_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## July 01, 2024

Feature

The `BELARUS_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## June 28, 2024

Feature

**Terraform support**

You can now use Terraform to [create and manage scan configurations](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations). Terraform management of discovery scan configurations is supported for BigQuery data, Cloud SQL data, and secrets in Cloud Functions environment variables. For a detailed reference document about Terraform resources, see [data_loss_prevention_discovery_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/data_loss_prevention_discovery_config) in the Terraform documentation.

## June 27, 2024

Feature

The `INDIA_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

Change

If you set `[InfoType.version](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)` to `latest` when including the `PHONE_NUMBER` infoType in your `[InspectConfig](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`, Sensitive Data Protection will now include `US_TOLLFREE_PHONE_NUMBER` findings as type `PHONE_NUMBER` in the scan results.

You can still use the old functionality by setting `InfoType.version` to `stable` or leaving it unset when using the `PHONE_NUMBER` infoType. In 30 days, the new functionality will be promoted to `stable`.

## June 24, 2024

Feature

The `RELIGIOUS_TERM` infoType detector is available in [Preview](https://cloud.google.com/products#product-launch-stages) in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

Change

A new detection model is available for the `ORGANIZATION_NAME` [infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) detector. The new model offers improved detection quality. You can try it out by setting [`InfoType.version`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) to `latest` when including the `ORGANIZATION_NAME` infoType in your [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig).

You can still use the old model by setting [`InfoType.version`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) to `stable` or leaving it unset when using the `ORGANIZATION_NAME` infoType. In 30 days, the new model will be promoted to `stable`.

## June 21, 2024

Feature

The discovery service of Sensitive Data Protection now supports Cloud Storage. You can run discovery at the organization, folder, or project level to generate data profiles of your Cloud Storage buckets. Data profiles provide metrics and insights about the sensitivity and risk levels of your data to help you plan your data governance workflows.

To get started on profiling Cloud Storage data, see the following:

  * [Profile Cloud Storage data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-cloud-storage)
  * [Profile Cloud Storage data in an organization or folder](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-cloud-storage)



For more information about sensitive data discovery, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## June 14, 2024

Feature

The `AZERBAIJAN_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## June 10, 2024

Change

A new detection model is available for the `DATE_OF_BIRTH` infoType detector. The new model offers improved detection quality. You can try it out by setting `[InfoType.version](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)` to `latest` when including the `DATE_OF_BIRTH` infoType in your `[InspectConfig](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`.

You can still use the old model by setting `InfoType.version` to `stable` or leaving it unset when using the `DATE_OF_BIRTH` infoType. In 30 days, the new model will be promoted to `stable`.

## June 07, 2024

Fixed

From May 27 through June 7, 2024, a bug caused Sensitive Data Protection to sometimes inaccurately populate integer fields as null instead of zero for findings written to BigQuery. This bug is now resolved.

For more information about sensitive data inspection, see [Inspect Google Cloud storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage).

## June 06, 2024

Feature

The `KAZAKHSTAN_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## May 23, 2024

Feature

The `TRADE_UNION` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## May 17, 2024

Change

The `LOCATION` [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detection model that was previously only accessible by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` has been promoted to be the default detection model for this infoType. The new model offers improved detection quality.

To use the new model, leave [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) unset, or set it to `latest` or `stable`. To use the old detection model, set [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy`. You can continue to use the legacy model for 90 days.

## May 13, 2024

Feature

The `UKRAINE_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

Feature

The `RUSSIA_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

Feature

The `UZBEKISTAN_PASSPORT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

Feature

The `IMMIGRATION_STATUS` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## April 25, 2024

Change

A new detection model is available for the `STREET_ADDRESS` infoType detector. The new model offers improved detection quality. You can try it out by setting `[InfoType.version](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)` to `latest` when including the `STREET_ADDRESS` infoType in your `[InspectConfig](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig)`.

You can still use the old model by setting `InfoType.version` to `stable` or leaving it unset when using the `STREET_ADDRESS` infoType. In 30 days, the new model will be promoted to `stable`.

## April 02, 2024

Announcement

If you opted to publish your data profiles to Security Command Center, you can configure Security Command Center to prioritize resources automatically according to the sensitivity of the data that the resources contain. For more information, see [Set resource priority values automatically by data sensitivity](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity).

If your discovery scan configuration isn't set to publish data profiles to Security Command Center, see [Enable publishing to Security Command Center in an existing configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc#edit-config).

## March 28, 2024

Feature

The `SWITZERLAND_SOCIAL_SECURITY_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## March 25, 2024

Fixed

From February 12 through 27, 2024, a bug caused Sensitive Data Protection to inaccurately set the free-text scores of certain data profiles to 0, where they should have been higher. This bug is now resolved. All affected data profiles have been reprofiled.

For more information about the discovery service, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## March 22, 2024

Feature

The [discovery and inspection services](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview), which support BigQuery, now support tables that contain columns with `INTERVAL`, `RANGE<DATE>`, `RANGE<DATETIME>`, and `RANGE<TIMESTAMP>` data types.

For more information about sensitive data discovery, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

For more information about sensitive data inspection for BigQuery, see [Inspect a BigQuery table](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#inspect_a_table).

## March 07, 2024

Feature

The discovery service of Sensitive Data Protection now supports Cloud SQL. You can run discovery at the organization, folder, or project level to generate data profiles of your Cloud SQL tables. Data profiles provide metrics and insights about the sensitivity and risk levels of your data to help you plan your data governance workflows.

To get started on profiling Cloud SQL data, see the following:

  * [Profile Cloud SQL data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-cloud-sql)
  * [Profile Cloud SQL data in an organization or folder](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-cloud-sql)



For more information about sensitive data discovery, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## March 04, 2024

Change

A new detection model is available for the `LOCATION` [infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) detector. The new model offers improved detection quality. You can try it out by setting [`InfoType.version`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) to `latest` when including the `LOCATION` infoType in your [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig).

You can still use the old model by setting [`InfoType.version`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) to `stable` or leaving it unset when using the `LOCATION` infoType. In 30 days, the new model will be promoted to `stable`.

## February 27, 2024

Feature

An improvement was made in the way Sensitive Data Protection calculates the predicted infoType of the data that it profiles. The service now considers correlations between the detected infoTypes, where one infoType is a subset of another. For more information, see [Predicted infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#predicted-infotype).

For more information about data profiling, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## February 16, 2024

Feature

The `HTTP_USER_AGENT` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

## February 15, 2024

Feature

The `BLOOD_TYPE` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## February 01, 2024

Feature

You can now configure your discovery scans to reprofile data when the [inspection template](https://docs.cloud.google.com/dlp/docs/data-profiles#inspection-template) changes. By default, inspection template changes do not cause the affected data to be reprofiled. For more information, see [Frequency of data profile generation](https://docs.cloud.google.com/dlp/docs/data-profiles#scan-frequency).

## January 31, 2024

Feature

Sensitive Data Protection is now available in Johannesburg, South Africa (`africa-south1` region).

For more information, see [Sensitive Data Protection locations](https://docs.cloud.google.com/dlp/docs/locations).

## January 10, 2024

Feature

The `FINANCIAL_ACCOUNT_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

## November 21, 2023

Issue

For BigQuery inspection jobs, when you set a sampling limit based on a percentage of the total number of table rows ([`rowsLimitPercent`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#BigQueryOptions.FIELDS.rows_limit_percent)), Sensitive Data Protection can inspect more rows than expected. If you need to put a hard limit on the number of rows to scan, we recommend setting a maximum number of rows ([`rowsLimit`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#BigQueryOptions.FIELDS.rows_limit)) instead.

## November 17, 2023

Feature

The sensitive data discovery service can now detect the presence of [secrets](https://docs.cloud.google.com/dlp/docs/infotypes-reference#credentials_and_secrets), such as passwords and authentication tokens, in your Cloud Functions environment variables. Sensitive Data Protection sends any findings to Security Command Center as [vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#sdp-vulnerabilities). For more information, see [Report secrets in environment variables to Security Command Center](https://docs.cloud.google.com/dlp/docs/secrets-discovery).

## November 09, 2023

Change

The following changes were made to the `COUNTRY_DEMOGRAPHIC` infoType detector:

  * The sensitivity score was changed from `HIGH` to `MODERATE`.
  * The type category was changed from `PII` to `DEMOGRAPHIC`.



## September 19, 2023

Feature

Sensitive Data Protection is available in `me-central2` (Dammam). For more information, see [Sensitive Data Protection locations](https://docs.cloud.google.com/dlp/docs/locations).

## September 14, 2023

Fixed

Since August 12, 2023, there has been an increase in latency issues with inspection jobs and data profile generation. These latency issues have been resolved.

## July 31, 2023

Feature

You can enrich your manually curated metadata in [Dataplex](https://docs.cloud.google.com/dataplex) with insights gathered from Sensitive Data Protection [data profiles](https://docs.cloud.google.com/dlp/docs/data-profiles). When you export your data profiles to Dataplex, tags are automatically attached to the profiled BigQuery tables. The tags include the following insights:

  * Information types ([infoTypes](https://docs.cloud.google.com/dlp/docs/infotypes-reference)) detected in the columns of the table
  * Calculated sensitivity level of the table
  * Calculated data risk level of the table



For more information, see [Tag tables based on insights from data profiles](https://docs.cloud.google.com/dlp/docs/send-profiles-to-dataplex).

## July 14, 2023

Feature

The `PORTUGAL_SOCIAL_SECURITY_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

## June 28, 2023

Change

The `CROATIA_PERSONAL_ID_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

## June 14, 2023

Feature

The subscription pricing mode for the discovery service is now [generally available](https://cloud.google.com/products#product-launch-stages). This pricing mode offers predictable and consistent costs, regardless of your data growth. In subscription mode, you choose how much compute time (capacity) to reserve for profiling. There is no charge for bytes profiled in this pricing mode. For more information, see [Discovery pricing](https://cloud.google.com/sensitive-data-protection/pricing#data_profiling_pricing).

## May 22, 2023

Feature

The `COUNTRY_DEMOGRAPHIC` infoType detector, which identifies when countries are used for place of birth, residency, or citizenship, is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

## May 04, 2023

Feature

The discovery service can now generate the following observation finding types in [Security Command Center](https://docs.cloud.google.com/security-command-center):

  * `Data sensitivity`
  * `Data risk`



These findings provide the [calculated sensitivity and data risk levels](https://docs.cloud.google.com/dlp/docs/sensitivity-risk-calculation) of the BigQuery tables that you [profile](https://docs.cloud.google.com/dlp/docs/data-profiles). Use this information to inform your response plans when you investigate vulnerabilities and threats involving BigQuery tables.

For more information, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/dlp/docs/send-profiles-to-scc).

## April 21, 2023

Feature

The `MARITAL_STATUS` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

## April 17, 2023

Feature

You can assign a sensitivity level to a built-in or custom infoType. Cloud DLP uses the sensitivity levels of individual infoTypes to [calculate the sensitivity levels](https://docs.cloud.google.com/dlp/docs/sensitivity-risk-calculation) of tables that you [profile](https://docs.cloud.google.com/dlp/docs/data-profiles). For more information, see [Manage infoTypes through the Google Cloud console](https://docs.cloud.google.com/dlp/docs/manage-infotypes-console).

## April 07, 2023

Feature

To help you understand and test the discovery service, Cloud DLP has made it easier for you to test profiling on a single table. You can profile up to 25 tables at no additional charge, one at a time. Only tables that are less than or equal to 1 TB in size can be profiled for free. For more information, see [Profile a table in test mode](https://docs.cloud.google.com/dlp/docs/single-table-mode).

## March 29, 2023

Change

The `legacy` version of the `STREET_ADDRESS` [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detection model will stay available until further notice. Previously, this `legacy` model was scheduled to be removed on 19 June 2023.

## March 21, 2023

Change

The STREET_ADDRESS [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detection model that was previously only accessible by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` has been promoted to be the default detection model for this infoType. 

To use the new model, leave [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) unset, or set it to `latest` or `stable`. To use the old detection model, set [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy`. You can continue to use the legacy model until 19 June 2023 (90 days from the time of this change).

## February 23, 2023

Feature

[Data profiles](https://docs.cloud.google.com/dlp/docs/data-profiles) generated at the column level include the following metrics:

  * Estimated null proportion: an approximate proportion of null values in a column, categorized as high, medium, low, or very low. 
  * Estimated uniqueness: an estimate of how much of the data in a column is unique, categorized as high, medium, or low. 



For more information on these metrics, see the [Metrics reference](https://docs.cloud.google.com/dlp/docs/metrics-reference).

## February 15, 2023

Feature

The VAT_NUMBER infoType detector can identify Belgium VAT numbers.

For more information about VAT_NUMBER and other built-in infoType detectors, see [InfoType detector reference](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

## February 06, 2023

Feature

To better understand the size and shape of your BigQuery data that's in scope for data profiling, you can run an estimation. Each estimate provides the approximate table count, data size, and profiling cost. For more information on running an estimation, see the following:

  * [Estimate data profiling cost for an organization or folder](https://docs.cloud.google.com/dlp/docs/estimate-org-folder)
  * [Estimate data profiling cost for a single project](https://docs.cloud.google.com/dlp/docs/estimate-project)



For more information on data profiling, see [Data profiles for BigQuery data](https://docs.cloud.google.com/dlp/docs/data-profiles).

## February 02, 2023

Feature

The SSL_CERTIFICATE infoType detector is available in all regions.

## January 26, 2023

Feature

The PORTUGAL_NIB_NUMBER infoType detector is available in all regions. For more information about all built-in infoTypes, see [infoType detector reference](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

## January 09, 2023

Feature

The US_MEDICARE_BENEFICIARY_ID_NUMBER and MEDICAL_RECORD_NUMBER [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detectors are available in all regions.

## December 27, 2022

Change

The current default PERSON_NAME [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detection model, which is accessible when [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) is set to `latest` or `stable`, is now also used when [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) is set to `legacy`. 

The old detection model that was previously accessible by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy` is no longer accessible.

## December 14, 2022

Change

A new detection model is available for the STREET_ADDRESS [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detector. The new model offers improved detection quality. You can try it out by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` when including the STREET_ADDRESS infoType in your [`InspectConfig`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig).

You can still use the old model by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `stable` or leaving it unset when using the STREET_ADDRESS infoType. In 30 days, the new model will be promoted to `stable`.

## December 01, 2022

Feature

The VAT_NUMBER infoType detector is available in all regions. Currently, this detector identifies VAT numbers from France, Germany, Hungary, Indonesia, Italy, and the Netherlands.

For more information about all built-in infoTypes, see [InfoType detector reference](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

Feature

The NEW_ZEALAND_IRD_NUMBER infoType detector is available in all regions.

## November 07, 2022

Feature

The [`ExcludeByHotword`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#excludebyhotword) type was added as a type of [ExclusionRule](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#exclusionrule). With this new type, you can do the following:

  * Exclude a column from inspect findings if the column name matches a regular expression.
  * Exclude a finding from inspect findings if that finding is proximate to a string that matches a regular expression.



Previously, you could do these only by setting up a [hotword rule](https://docs.cloud.google.com/dlp/docs/creating-custom-infotypes-likelihood) that lowers the likelihood of the matching findings.

For more information on excluding findings, see [Exclusion rules](https://docs.cloud.google.com/dlp/docs/creating-custom-infotypes-rules#exclusion-rules).

## October 19, 2022

Feature

The OAUTH_CLIENT_SECRET infoType detector is available in all regions.

## October 13, 2022

Feature

For new [data profiles](https://docs.cloud.google.com/dlp/docs/data-profiles), infoTypes other than the [predicted infoType](https://docs.cloud.google.com/dlp/docs/metrics-reference#column-data-profile) will include the approximate percentage of non-null rows in which the infoType was detected.

## August 29, 2022

Change

The PERSON_NAME [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detection model that was previously only accessible by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` has been promoted to be the default detection model for this infoType. 

To use the new model, leave [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) unset, or set it to `latest` or `stable`. To use the old detection model, set [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `legacy`. You can continue to use the legacy model for 90 days.

## August 19, 2022

Feature

Cloud DLP can profile [BigLake tables](https://cloud.google.com/bigquery/docs/biglake-intro). For more information on using Cloud DLP to profile your data, see [Data profiles for BigQuery data](https://cloud.google.com/dlp/docs/data-profiles).

## August 01, 2022

Feature

Cloud DLP can de-identify sensitive data stored in Cloud Storage. This feature is in [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [De-identification of sensitive data in storage](https://docs.cloud.google.com/dlp/docs/concepts-deidentify-storage).

## July 19, 2022

Change

A new detection model is available for the PERSON_NAME [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detector. The new model offers improved detection quality. You can try it out by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `latest` when including the PERSON_NAME infoType in your [`InspectConfig`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig).

You can still use the old model by setting [`InfoType.version`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) to `stable` or leaving it unset when using the PERSON_NAME infoType. In 30 days, the new model will be promoted to `stable`.

## July 06, 2022

Feature

[InfoType categories](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/ListInfoTypesResponse#infotypecategory) were added to built-in infoTypes. 

To get a list of built-in infoTypes, call the [`infoTypes.list`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/infoTypes/list) method.

## June 08, 2022

Change

The LOCATION_COORDINATES [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detector is available in all regions.

## April 14, 2022

Feature

The data profiler for BigQuery is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). The data profiler is a fully-managed service that continuously scans data across your entire organization to give you general awareness of what data you have, and specific visibility into where sensitive data is stored and processed. For more information, see [Data profiles for BigQuery data](https://docs.cloud.google.com/dlp/docs/data-profiles).

## January 18, 2022

Change

The SOUTH_AFRICA_ID_NUMBER [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detector is available in all regions.

## December 13, 2021

Change

The ICCID_NUMBER [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detector is available in all regions.

## December 06, 2021

Feature

The [dictionary replacement](https://cloud.google.com/dlp/docs/transformations-reference#dictionary-replacement) PrimitiveTransformation is generally available. The replacement dictionary replaces each detected sensitive value with a random value selected from a provided word list.

## October 18, 2021

Change

The IMSI_ID [infoType](https://docs.cloud.google.com/dlp/docs/infotypes-reference) detector is available in all regions.

## October 12, 2021

Feature

The data profiler for BigQuery is available in Preview. For more information, see [Data profiles for BigQuery data](https://docs.cloud.google.com/dlp/docs/data-profiles).

## June 02, 2021

Change

MEDICAL_TERM [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference) is now available in all regions.

## January 06, 2021

Feature

[Hybrid Jobs](https://docs.cloud.google.com/dlp/docs/concepts-hybrid-jobs) are now available for inspecting external data sources.

## December 07, 2020

Feature

Added whole document classification support with the following [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * DOCUMENT_TYPE/FINANCE/REGULATORY 
  * DOCUMENT_TYPE/FINANCE/SEC_FILING 
  * DOCUMENT_TYPE/HR/RESUME 
  * DOCUMENT_TYPE/LEGAL/BLANK_FORM 
  * DOCUMENT_TYPE/LEGAL/BRIEF 
  * DOCUMENT_TYPE/LEGAL/COURT_ORDER 
  * DOCUMENT_TYPE/LEGAL/LAW 
  * DOCUMENT_TYPE/LEGAL/PLEADING 
  * DOCUMENT_TYPE/R&D/PATENT 
  * DOCUMENT_TYPE/R&D/SOURCE_CODE 
  * DOCUMENT_TYPE/R&D/SYSTEM_LOG 
  * DOCUMENT_TYPE/R&D/DATABASE_BACKUP



## November 11, 2020

Change

PERSON_NAME, FIRST_NAME, LAST_NAME, MALE_NAME and FEMALE_NAME [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference) are now available in all regions.

## October 28, 2020

Change

DATE and TIME [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference) are now available in all regions.

## September 08, 2020

Change

STREET_ADDRESS [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference) is now available in all regions.

## August 28, 2020

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * STORAGE_SIGNED_URL
  * STORAGE_SIGNED_POLICY_DOCUMENT



Feature

[Risk analysis job creation](https://docs.cloud.google.com/dlp/docs/compute-risk-analysis) is now available in the Cloud DLP UI in Cloud Console.

## July 15, 2020

Change

Added [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * ISRAEL_IDENTITY_CARD_NUMBER



## June 19, 2020

Feature

Added support for location-based processing. Learn more: 

  * [Cloud DLP locations](https://docs.cloud.google.com/dlp/docs/locations)
  * [Specifying processing locations](https://docs.cloud.google.com/dlp/docs/specifying-location)



## June 15, 2020

Feature

Added [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * VEHICLE_IDENTIFICATION_NUMBER



## May 21, 2020

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * IRELAND_DRIVING_LICENSE_NUMBER
  * IRELAND_EIRCODE



## May 16, 2020

Feature

Added [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

AWS_CREDENTIALS

## May 04, 2020

Change

We have made quality and performance enhancements to our name detectors. PERSON_NAME should be used in most scenarios as it will return the most comprehensive finding. MALE_NAME and FEMALE_NAME are now synonymous with FIRST_NAME with [`Likelihood`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#likelihood) now never being greater than `POSSIBLE`. These changes will be rolled out over the coming days.

## April 28, 2020

Feature

Added additional [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * JSON_WEB_TOKEN



## April 16, 2020

Feature

Added support for `PDF` and `WORD` [`FileTypes`](http://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#filetype) and `PDF` and `WORD_DOCUMENT` [`BytesTypes`](http://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#bytestype).

## April 13, 2020

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * IRELAND_PPSN
  * IRELAND_PASSPORT



## April 08, 2020

Feature

Added additional infoType detectors:

  * `AZURE_AUTH_TOKEN`
  * `GCP_API_KEY`



## March 16, 2020

Feature

Added support for streaming data from external sources for inspection using hybrid jobs and job triggers. Hybrid jobs and job triggers in Cloud DLP enable you to stream data from virtually any source, whether on- or off-cloud, inspect it using Cloud DLP, and then save the results of the inspection scan as part of a job resource within Cloud DLP or to BigQuery.

## March 01, 2020

Feature

[`Regex`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/Regex), [`WordList`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/Dictionary#wordlist), and small [`Dictionary`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/Dictionary) objects can now be loaded from metadata stored in Cloud Spanner using [`CustomInfoType.Regex`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#regex) or [`CustomInfoType.Dictionary`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#dictionary). Doing this can be useful when sharing regexes or dictionaries for custom infoType inspection across multiple requests.

## January 09, 2020

Feature

Added additional infoType detectors:

  * `GENERIC_ID`



## December 10, 2019

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `AUSTRALIA_DRIVERS_LICENSE_NUMBER`
  * `FRANCE_TAX_IDENTIFICATION_NUMBER`



## November 08, 2019

Feature

The summary of a `DlpJob` findings can be published to Stackdriver using the new action [`PublishToStackdriver`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#action). Metrics on bytes inspected and transformed are automatically published for monitoring usage. For more information, see [Monitoring with Stackdriver](https://docs.cloud.google.com/dlp/docs/monitoring).

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `AUTH_TOKEN`
  * `BASIC_AUTH_HEADER`
  * `ENCRYPTION_KEY`
  * `HTTP_COOKIE`
  * `PASSWORD`
  * `WEAK_PASSWORD_HASH`
  * `XSRF_TOKEN`



Change

The pricing model for content methods has changed from "units" to a simpler model based just on bytes. For more information, see [Pricing](https://cloud.google.com/dlp/pricing).

## October 10, 2019

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `ADVERTISING_ID`
  * `ORGANIZATION_NAME`
  * `SPAIN_DNI_NUMBER`



## September 13, 2019

Feature

Added additional [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `SCOTLAND_COMMUNITY_HEALTH_NUMBER`



## August 26, 2019

Feature

The [Cloud DLP user interface (UI)](https://docs.cloud.google.com/dlp/docs/dlp-ui) is now generally available (GA) in the [Google Cloud Platform Console](https://console.cloud.google.com/security/dlp;source=7).

## August 15, 2019

Feature

Added additional [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `MEDICAL_TERM`



## August 05, 2019

Feature

Added additional [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `SPAIN_SOCIAL_SECURITY_NUMBER`



## July 09, 2019

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `GERMANY_SCHUFA_ID`
  * `CREDIT_CARD_TRACK_NUMBER`
  * `ITALY_FISCAL_CODE`



## June 28, 2019

Feature

Added additional [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `STREET_ADDRESS`



## June 12, 2019

Feature

Support for structured scanning of Avro files, surfacing findings as rows and columns rather than byte offsets. Existing jobs will begin scanning Avro files as structured.

Change

New simplified SKU for scanning of data in storage. [Updated Pricing](https://cloud.google.com/dlp/pricing).

## May 31, 2019

Feature

Added support for [`CustomInfoTypes`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#custominfotype) and [`DetectionRules`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#detectionrule) to the [Cloud DLP Beta UI](https://console.cloud.google.com/security/dlp;source=7) in the Google Cloud Platform Console.

## April 18, 2019

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `GERMANY_DRIVERS_LICENSE_NUMBER`
  * `GERMANY_IDENTITY_CARD_NUMBER`
  * `HONG_KONG_ID_NUMBER`
  * `INDIA_AADHAAR_INDIVIDUAL`
  * `INDIA_GST_INDIVIDUAL`
  * `THAILAND_NATIONAL_ID_NUMBER`



## April 04, 2019

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `INDONESIA_NIK_NUMBER`
  * `AUSTRALIA_PASSPORT`
  * `BELGIUM_NATIONAL_ID_CARD_NUMBER`
  * `GERMANY_TAXPAYER_IDENTIFICATION_NUMBER`
  * `PASSPORT`
  * `SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER`
  * `SINGAPORE_PASSPORT`
  * `TAIWAN_PASSPORT`
  * `TURKEY_ID_NUMBER`



## March 29, 2019

Feature

Added new crypto-based tokenization method: [`CryptoDeterministicConfig`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#cryptodeterministicconfig). For more information, see [Transformations Reference](https://docs.cloud.google.com/dlp/docs/transformations-reference).

## March 08, 2019

Feature

Added new [Cloud DLP Beta UI](https://console.cloud.google.com/security/dlp;source=7) in the Google Cloud Platform Console.

## February 11, 2019

Change

Updated the default list of infotypes included in [`ALL_BASIC`](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

Fixed

Clarified the documentation as to what behavior users can expect for the [`ALL_BASIC`](https://docs.cloud.google.com/dlp/docs/infotypes-reference).

## December 12, 2018

Fixed

De-identification requests using [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#cryptoreplaceffxfpeconfig) now correctly validate the alphabet of the value being transformed to match the transformations alphabet, now correctly rejecting values with whitespace, when whitespace is not part of the alphabet. Invalid requests will return an error in the `TransformationSummary` with the message "CryptoReplaceFfxFpeConfig's 'alphabet' does not include all the characters in the value being transformed; the set of distinct characters in any given value being transformed by this transformation must be a subset of the set of characters comprising the 'alphabet'."

## October 25, 2018

Feature

Added an additional [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `NORWAY_NI_NUMBER`



## October 02, 2018

Feature

Added support to Cloud Storage [`FileSet`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#fileset) for using regular expression filters to specify which files to include or exclude from the scan. This is useful for cases where the set of files to scan cannot be concisely expressed with a path and wildcards, such as:

  * Scan all files, but skip some specific files or folders that you are confident have no sensitive data.
  * Scan only files whose endings are in some known set of file extensions - for example, only .txt, .csv, and .json files.
  * Scan only files whose endings aren't in some known set of extensions - for example, skip .pdf files.



## September 19, 2018

Feature

Added support for [augmenting existing infoType detectors](https://docs.cloud.google.com/dlp/docs/creating-custom-infotypes-rules) using exclusion rules and hotword rules.

## August 24, 2018

Feature

Added an additional [infoType detector](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `DENMARK_CPR_NUMBER`



## August 17, 2018

Feature

Added additional [infoType detectors](https://docs.cloud.google.com/dlp/docs/infotypes-reference):

  * `CANADA_DRIVERS_LICENSE_NUMBER`
  * `DATE`
  * `DATE_OF_BIRTH`
  * `FEMALE_NAME`
  * `FINLAND_NATIONAL_ID_NUMBER`
  * `GCP_CREDENTIALS`
  * `GENDER`
  * `JAPAN_BANK_ACCOUNT`
  * `JAPAN_DRIVERS_LICENSE_NUMBER`
  * `MALE_NAME`
  * `NETHERLANDS_PASSPORT`
  * `SPAIN_DRIVERS_LICENSE_NUMBER`
  * `SWEDEN_NATIONAL_ID_NUMBER`
  * `SWEDEN_PASSPORT`
  * `TIME`
  * `US_STATE`



## August 10, 2018

Feature

Added support for [large custom dictionaries](https://docs.cloud.google.com/dlp/docs/creating-stored-infotypes). Cloud DLP can now scan for dictionaries containing up to tens of millions of entries.

Feature

Added support to [`BigQueryOptions`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#bigqueryoptions) for limiting the number of rows to scan per file by percentage.

Feature

Added support to [`CloudStorageOptions`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#cloudstorageoptions) for limiting the number of bytes to scan per file by percentage.

## June 01, 2018

Feature

Added support for [delta-presence estimation](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#privacymetric), a risk metric used when membership in the dataset is itself a piece of sensitive information.

## May 18, 2018

Feature

Added `sample_method` flag to [`BigQueryOptions`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#bigqueryoptions) and [`CloudStorageOptions`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#cloudstorageoptions) for limiting scans to a sample of content. This is useful to more efficiently scan large datasets where the intent is to only determine whether sensitive data may be located there and the exhaustive list of findings is not necessary.

## April 25, 2018

Feature

Added `row_limit` flag to [`BigQueryOptions`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#bigqueryoptions) to allow for sampling tables instead of scanning all rows.

Feature

For customers using Cloud Security Command Center, the summary of a `DlpJob` can be published to Cloud SCC using the new action [`PublishSummaryToCscc`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#action).

Feature

Dictionaries can now be loaded from files stored in Cloud Storage that consist of newline-delimited lists of phrases using the `cloud_storage_path` parameter in [`CustomInfoType.Dictionary`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Dictionary). Useful when sharing dictionaries for custom inspection across multiple requests.

## March 21, 2018

Change

The [`Finding`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Finding) object has been expanded with a new [`ContentLocation`](https://docs.cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#contentlocation) to better report findings from various data types (including images, records, and documents).

Change

`InfoTypeStatistics` object has been renamed to [`InfoTypeStats`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs#infotypestats).

Deprecated

The v2beta1 and v2beta2 APIs are now deprecated.

Change

The [`jobs.create`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs/create) method has been added to replace `dataSource.analyze` and `dataSource.inspect`.

Feature

Launched the new [V2](https://docs.cloud.google.com/dlp/docs/reference/rest/v2) version of the API.

Feature

**Cloud Data Loss Prevention (DLP) General Availability (GA) Release**

Change

The [`ContentItem`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/ContentItem) object has been simplified with a [`BytesType`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/ByteContentItem#BytesType) enum to specify the type of data to inspect.

## February 16, 2018

Feature

Job completion notifications for both risk analysis and inspection can now be sent to Cloud Pub/Sub.

Feature

Added support for choosing a default [likelihood](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#likelihood) for [`CustomInfoType`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#custominfotype) detectors and for adjusting likelihood using a new [`DetectionRule`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#detectionrule), which looks for related content within the vicinity of a finding.

Feature

Newly added [`JobTriggers`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.jobTriggers#resource-jobtrigger) allow for scheduling regular scans of storage. Combined with the new [`TimespanConfig`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#TimespanConfig), scans can be limited to only re-scanning new or modified content in BigQuery and Cloud Storage.

Feature

Added support for regular expression-based custom detectors.

## December 14, 2017

Feature

Launched the new v2beta2 version of the API, which includes a number of new and improved features, including templates for persisting de-identification and inspect configurations, a simplified job API for inspecting storage and risk analysis, and more.

Tips for migrating:

  * [`Content`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.content) API methods now take a single `ContentItem`.
  * [`InspectConfig`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig) now has a default likelihood, so when left unset findings below `POSSIBLE` will be excluded automatically.
  * Findings from inspect storage are now always stored in your own BigQuery instance, giving you more control of where your sensitive data is stored.
  * `content.redact`, was deprecated in favor of using [`content.deidentify`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.content/deidentify), for redacting text, and [`image.redact`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.image/redact), for redacting images.
  * [`InspectConfig`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig) now requires at least one [`InfoType`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InfoType) or [`CustomInfoType`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#custominfotype).
  * Long running operations were replaced by [`DlpJob`](https://docs.cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs#resource-dlpjob) objects for risk analysis and storage inspection. `inspect.operations.create` was renamed to `dataSource.inspect`.



## November 22, 2017

Feature

Added a new risk analysis metric, _k_ -map estimation, to `dataSource.analyze`.

## October 20, 2017

Feature

Launched support for searching for words or phrases from a custom dictionary provided by the user with the addition of `CustomInfoType` to `InspectConfig`. This feature is enabled in `content.inspect`, `content.redact`, `content.deidentify`, and `inspect.operations.create`.

## September 15, 2017

Feature

Launched support to de-identify content with the addition of `content.deidentify`.

Feature

Launched support to conduct risk analysis on BigQuery with the addition of `dataSource.analyze`.

## August 17, 2017

Feature

Added support to limit the number of findings per `InfoType` with the addition of `InfoTypeLimit` in `InspectConfig`.

Feature

Added support to limit the number of findings per file, Cloud Datastore entity, or database row with the addition of `OperationConfig` to `inspect.operations.create`.

## August 10, 2017

Feature

Added support for scanning and redacting structured data in both `content.redact` and `content.inspect` by providing a `Table` in `ContentItem`.

## August 03, 2017

Feature

Results can now be stored to BigQuery when scanning BigQuery, Cloud Datastore, and Cloud Storage using `inspect.operations.create`.

Feature

BigQuery can now be scanned using `inspect.operations.create`.

## June 15, 2017

Feature

Added support for auto-redacting all text from images. You can now also choose custom colors when using `content.redact` to fill the bounding boxes during image redaction.

## May 11, 2017

Feature

Launched support to filter findings by infoType and likelihood when using `inspect.results.list`.

## May 01, 2017

Feature

You can now store results from scanning Cloud Datastore or Cloud Storage using `inspect.operations.create`. Results are stored in Cloud Storage.

## March 23, 2017

Feature

Added support for auto-redacting findings in images. You can now use `content.redact` to fill the bounding box of a finding with a solid color.

## March 09, 2017

Feature

Launch of Cloud DLP API to **Beta**. Cloud DLP API enables developers and data owners to better understand and manage sensitive data by providing a fast, scalable classification for sensitive elements. Scan small text streams and images or larger datasets in Cloud Storage and Cloud Datastore. The Cloud DLP API is currently available as a REST API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
