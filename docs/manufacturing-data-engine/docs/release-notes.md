---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/release-notes/
title: Manufacturing Data Engine release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:36.795660+00:00
---

# Manufacturing Data Engine release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/manufacturing-data-engine/docs/release-notes)



Send feedback 

#  Manufacturing Data Engine release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Manufacturing Data Engine. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

Versions covered in this change log:

Version | Supported for new deployments | Archived | Critical update | API compatible MC versions  
---|---|---|---|---  
`v1.5.2` | done | No | Yes | 2.22 - 2.26  
`v1.5.1` | done | No | Yes | 2.22 - 2.26  
`v1.5.0` | done | No | No | 2.22 - 2.26  
`v1.4.2` | done | No | Yes | 2.22 - 2.26  
`v1.4.1` | done | No | No | 2.22 - 2.26  
`v1.4.0` | done | No | No | 2.22 - 2.26  
`v1.3.8` | done | No | No | 2.15 - 2.22  
`v1.3.7` | close | No | No | 2.15 - 2.22  
`v1.3.6` | close | No | No | 2.15 - 2.22  
`v1.3.5` | close | No | Yes | 2.15 - 2.22  
`v1.3.4` | close | No | No | 2.15 - 2.22  
`v1.3.3` | close | No | No | 2.15 - 2.22  
`v1.3.2` | close | No | Yes | 2.15 - 2.22  
`v1.3.1` | close | Yes | Yes | 2.15 - 2.22  
`v1.3.0` | close | Yes | Yes | 2.15  
  
You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/manufacturing-data-engine-release-notes.xml) directly. 

## December 10, 2025

Fixed

  * **Fix (423567127):** Fixed a bug that prevented numeric values to be correctly processed when using file ingestion.
  * **Fix (441294785):** Fixed a bug that prevented the deletion of a message class if the related parser had been deleted beforehand.
  * **Fix (443710570)** : Fixed a bug that could use an old version of a parser script when uploading a new configuration package that had the same parser name.



Libraries

**Release signature**
    
    
    6e178bd
    1.5.2
    9ee64699a1bdf1cf690e7930d968f002
    

Security

  * **Improvement (448853115)** : Added the ability to enable and configure VPC flow logging from Terraform. Collecting VPC flow logs is recommended to detect potential intrusions or anomalies.
  * **Improvement (450530585)** : Updated container images and dependencies to address known security vulnerabilities.
  * **Improvement (448854007):** Adjusted IAM roles used by some MDE service accounts following the least-privilege approach.
  * **Improvement (448148987)** : Switched to DNS-based endpoint with AIM access control for GKE control plane, following security best practices.
  * **Improvement (448148673)** : Enabled SSL required mode on the Cloud SQL instance for additional security enforcement.
  * **Improvement (448148275)** : Enabled in-transit encryption and token authentication for Redis.



Change

  * **Improvement (441727217)** : Introduced an option to enable parsers after types activation when you upload a new configuration package.
  * **Improvement (333321871)** : Refactored scripts to collect additional information for the MDE team when you open a support ticket to help faster troubleshooting.
  * **Improvement (441660844)** : Added `typesMetadataBuckets` and `typesTransformations` JSON arrays as responses to the Tags API implementation.
  * **Improvement (435358499)** : Enabled Streaming Engine for Dataflow in all MDE deployment sizes for optimized consumption, saving resources.



Announcement

### Release 1.5.2

This release is a **critical update** if you have an existing deployment of MDE version 1.5.0. This release introduces a new configuration package upload option that allows users to automatically enable and activate all entities created following the upload. It also includes other minor improvements and bug fixes.

Follow the [Upgrade guide](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/upgrade-guide) in the MDE documentation for detailed instructions. Note that instructions are different depending on the MDE version you are upgrading from.

## August 29, 2025

Announcement

### Release 1.5.1

This release is a **critical update** if you have an existing deployment of MDE version 1.5.0. This release resolves a bug regarding materialization of metadata instances created prior to MDE 1.5.0. This release also includes other minor improvements and bug fixes.

Change

  * **Improvement (407009198)** : Improved the error handling when `upload` and `parsing` configuration packages.
  * **Improvement (423531705):** Improved MDE logging for BigQuery sink related operations. 
  * **Improvement (423530033):** Improved manifest validation on configuration package uploads.
  * **Improvement (423554635)** : Added `CreatedAt` column with default sorting on the MDE UI configuration packages page.
  * **Improvement (430962108):** Added more sorting options on the MDE UI _Configurations_ and _Metadata Instances_ pages.
  * **Improvement (423531714)** : Various improvements on Helm charts, including image tag management, and k8s secrets/configmaps.
  * **Improvement (407037164)** : More descriptive message added to MDE UI to confirm Type deletion.



Security

  * **Improvement (427447932)** : Brought Docker images to versions without vulnerabilities reported at the time of the release.
  * **Improvement (361290775)** : Modified Terraform deployment scripts to enforce TLS v1.2 for an external MDE UI Load Balancer.



Fixed

  * **Fix (417666631):** Fixed an issue with metadata materialization for metadata instances that had been created prior to migrating to MDE 1.5.0.
  * **Fix (420921890):** Fixed an error when attempting to update an instance tag metadata and saved it for instances that had been created prior to migrating to MDE 1.5.0.
  * **Fix (423535516)** : Fixed inconsistent API response codes when trying to delete non-existing entities. 
  * **Fix (383519276)** : Fixed missing fields in MDE logging and added more details to make troubleshooting easier.
  * **Fix (424077359)** : Fixed instance bucket creation through API. It now adds default `createdTime` as the time when the API call was received.
  * **Fix (422991109 and 424084607)** : Fixed `ghost` deletion of Types and Metadata Buckets after removing a configuration package.
  * **Fix (423859259)** : Fixed removal of BigQuery views when a Type is manually deleted.
  * **Fix (406803212)** : Fixed wrong version materialization on MDE system tables.
  * **Fix (407015039)** : Fixed `Delete` button in MDE UI when the system is in PROD mode (Production mode).
  * **Fix (435653743)** : Fixed missing Grafana Terraform module.



Libraries

**Release signature**
    
    
    b0fc163
    1.5.1
    ffb87d39d343c20abebd2f52df74a2d3
    

## March 31, 2025

Announcement

### Release 1.5.0

This release is **not a critical update** , unless you are directly impacted by the bug fixes, you don't need to update, and you can wait for future releases before updating.

Feature

  * **Configuration Packages** : Introduces a file-based configuration package system for atomic deployments and GitOps integration. For more information, see [Upload configuration package](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/upload-config-package) and [File content](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/configuration/content).
  * **Development Mode** : Adds a "Development Mode" to allow deletion of MDE entities and configuration packages, use with caution. For more information, see [Development mode](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/development-mode).



Change

  * **Metadata Versioning** : To enhance the query readability of the metadata instances, MDE v1.5.0 introduced a new field called `validFrom` that designates the time when a particular metadata instance is effective. MDE uses this field to check which metadata instance picks based on the source message event time, not processing time, enabling accurate historical data representation. For more information, see [Versioning metadata buckets](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#versioning_metadata_buckets).



## December 13, 2024

Announcement

### Release 1.4.2

This release is a **critical update** if you have an existing deployment of MDE version 1.4.0 or 1.4.1. This release resolves a bug regarding the raw messages writing, where the Cloud Storage Avro files were not being written.

Fixed

  * **Fix (381418590)** : Fixing an issue of the generated BigQuery views for the types when one of the bucket or data field schemas contains arrays.
  * **Fix (382189410)** : Fixing issue of the Cloud Storage Writer not writing the raw messages to the Cloud Storage bucket.



Change

**Important:** If you are upgrading from 1.4.0 or 1.4.1 make sure that you manually drain the `Cloud Storage writer` dataflow job, which forces the raw message files to be written to Cloud Storage before shutting down the job.

Libraries

**Release signature**
    
    
    57c3062
    1.4.2
    ccc9f5b6c30a1c1a42eae04c995f783b
    

## November 07, 2024

Announcement

### Release 1.4.1

This release is **not a critical update** , unless you are directly impacted by the bug fixes, you don't need to update, and you can wait for future releases before upgrading.

Change

  * **Improvement (376024419)** : Enable automatic reconciliation of the missing infrastructure elements and for MDE types. When the user creates a new type, multiple infrastructure components are created in the background. To accommodate cases like type activation or upgrade issues, MDE now checks for missing infrastructure components in the startup of the `bigquery-sink` service and makes sure that it is aligned with the types configurations in MDE.



Libraries

**Release signature**
    
    
    0b539af
    1.4.1
    0e06a47adf3c1f7efedfcb182235b490
    

Change

**Helm charts** \- MDE services containers image tag: `3f285a5`. \- MDE UI image tag: `2.22.0-dev.0.123.4`.

Fixed

  * **Fix (375367674)** : Fixing issue when the edge messages contained fields named `event` or `headers` which was colliding with the MDE `event`, and `headers` attribute that are used during the message-class resolution. The MDE message headers are now reserved in a new keyword called `mdeHeaders`.
  * **Fix (371176757)** : Fixing issue of losing the monitoring metrics after upgrading from 1.3.x to 1.4.0. parsers.
  * **Fix (377694402)** : Upgrading the Apache Beam runtime to the latest version of `2.60.0`.
  * **Fix (377672812)** : Upgrading Terraform runtime and the required Google Cloud provider versions to solve multiple deployment bugs.



Change

**Important:** This release requires different runtime versions for Terraform to use the latest Terraform Google Cloud providers and solve multiple deployment bugs. For more information, see the [deployment guide](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/guide).

## September 05, 2024

Announcement

### Version 1.4.0

This release is **not a critical update** , unless you are directly impacted by the bug fixes, you don't need to update, and you can wait for future releases before upgrading.

**Important:** This releases a new automatic deletion of metadata instances versions that exceeds a predefined threshold (default is 200 instance). This protects the platform from performance degradation that is caused by configuration errors. For best practices on how to use the MDE metadata system, see the [metadata concept page](https://cloud.google.com/manufacturing-data-engine/docs/concepts/metadata).

**Note** : If you are upgrading from older releases, the Terraform may not be able to perform an in-place upgrade for the `Cloud Storage Writer` dataflow job. In that case, you need to stop it manually, before starting the upgrade.

Change

  * **Improvement (330297418)** : Enable the three-projects topology for bigquery-sink: the service to be deployed in a project, the Pub/Sub in another project, and the BigQuery datasets in a third project. Find these as dedicated properties in the BigQuery sink helm chart.
  * **Improvement (320427338)** : Creating automatic BigQuery views based on the type buckets schema. This provides a stable column-based schema for accessing the types as well as its metadata in a single view. For more information, see [Analyticis view](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/analytics-view).
  * **Improvement (320427684)** : Types data field schema validation. The non-numeric types can have a JSON schema that governs the data field of its records, and this schema is now enforced during the processing. For more information, see [Data field](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/type#data_field).
  * **Improvement (320427624)** : New real-time stats service for the ingested tags. For more information, see [Real-Time service](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/real-time-service).
  * **Improvement (324029584)** : Automatic deletion for excessive metadata instances to prevent the system performance degradation. For more information, see [Metadata automatic deletion](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#metadata_automatic_deletion).
  * **Improvement (353244779)** : New [Notification API](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/notification-api) endpoint to display time-sensitive messages to the user such as the metadata instances approach the maximum size limit.
  * **Improvement (353247809)** : New [API](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/stream-processing-operations) to stop and start the processing of messages.



Libraries

**Release signature**
    
    
    7176648
    1.4.0
    cf0b7439bf9862b06aedcea13dd783fe
    

Change

**Helm charts**

  * MDE services containers image tag: `a04af0d`.
  * MDE UI image tag: `2.22.0-dev.0.123.4`.



Fixed

  * **Fix (324563314)** : Enabling the Dataflow Streaming Engine for the Cloud Storage flows.
  * **Fix (327369559)** : Listing the parsers endpoint does not return the disabled parsers.
  * **Fix (320427422)** : Upgrading the Spring stack to 3.x.
  * **Fix (353240181)** : Security and performance fixes.



Security

The vulnerability scanner may flag a critical CVE related to the zlib libraries in the base OS of the container images. The binary of this impacted library is not built in the MDE container images, and it is not impacted by this vulnerability. Nonetheless, once a new Debian OS patch is available, MDE will release an updated container images so that the vulnerability scanner does not flag this issue. For more information about the vulnerability, see the [Debian tracker](https://security-tracker.debian.org/tracker/CVE-2023-45853).

## February 29, 2024

Announcement

### Version 1.3.8

This release is **not a critical update** , unless you are directly impacted by the bug fixes, you don't need to update, and you can wait for future releases before upgrading.

**Important:** This release introduces a limitation on the execution time of parsers. If the parser execution time exceeds seven seconds, it will be preempted and an error message will be produced in the operations log. If the parser needs more than seven seconds, we recommend to break it into multiple parsers and attach it to the same message class.

Change

  * **Improvement (324563314)** : Enabling the Dataflow Streaming Engine for the Cloud Storage Flows to improve the scalability behaviour of the Cloud Storage jobs.



Libraries

**Release signature**
    
    
    a94aa0e
    1.3.8
    e74afda073cd5d52a591763c5ea7cbe1
    

Fixed

  * **Fix (324540732)** : Adding JVM initialization flags to increase the memory utilisation per pod.
  * **Fix (324040010)** : Configuration Manager running out of memory when running a misconfigured parser that impacts the CPU and memory allocations.
  * **Fix (321911849)** : Message Mapper running out of memory when running a misconfigured parser that impacts the CPU and memory allocations.
  * **Fix (322148462)** : Fixing web interface error when interacting with items in a paginated response with size of more than 100 items.
  * **Fix (327323565)** : Cloud Storage Writer out of memory error when ingesting large number of items.
  * **Fix (328190564)** : Cloud Storage Reader out of memory error when reading a large number of files.
  * **Fix (327369559)** : Listing parsers in the web interface does not show the disabled parsers.



Change

**Helm charts**

  * MDE services containers image tag: `09497d7`.
  * MDE UI image tag: `2.15.0.0.109.2`.



## January 17, 2024

Announcement

### Version 1.3.7

This release is **not a critical update** , unless you are directly impacted by the bug fixes, you don't need to update, and you can wait for future releases before upgrading.

Libraries

**Library updates**

  * Updated Apache Beam SDK to version 2.53.0.



Libraries

**Release signature**
    
    
    7460a29
    1.3.7
    3ed1b9c3886f123e0d839126a1577c63
    

Change

  * **Improvement (320427011)** : All the services now use full names for Pub/Sub subscriptions and topics (For example: projects/PROJECT_ID/subscriptions/configuration-processing-subscription). This allows having the topics or subscriptions in a different project that the one the services are deployed to.
  * **Improvement (320443808)** : All dataflow jobs now use private IP by default. For more information, see [Routes Firewall](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall).



Change

**Helm charts**

  * MDE services containers image tag: `4b79010`.
  * MDE UI image tag: `2.15.0.0.109.2`.



Breaking

The following Dataflow jobs need to be manually stopped before upgrading:

  * eventchange-dataflow-flex-job
  * gcs-writer-dataflow-flex-job
  * window-dataflow-flex-job
  * bigtable-writer-dataflow-flex-job
  * gcs-reader-dataflow-flex-job



## December 19, 2023

Announcement

### Version 1.3.6

This release is **not a critical update** , unless you are directly impacted by the bug fixes, you don't need to update, and you can wait for future releases before upgrading.

Breaking

The following Dataflow jobs need to be manually stopped before upgrading:

  * eventchange-dataflow-flex-job
  * gcs-writer-dataflow-flex-job
  * window-dataflow-flex-job
  * bigtable-writer-dataflow-flex-job
  * gcs-reader-dataflow-flex-job



Change

  * **Improvement (311599436)** : Added a new field to the output of the [Group Event Change Transformation](https://cloud.google.com/manufacturing-data-engine/docs/concepts/transformation) to include the message that triggered the change in the transformation
  * **Improvement (316554360)** : When parsing a message, add the output of the headers field to the Pub/Sub headers and preserve through the entire pipeline.



Fixed

  * **Fix (315935780)** : Pub/Sub attributes on input-messages are filtered and can't be used in the source message class or parser.



Change

**Helm charts**

  * MDE services containers image tag: `8199764`.
  * MDE UI image tag: `2.15.0.0.109.2`.



Libraries

**Release signature**
    
    
    1b11952
    1.3.6
    bfaaf15fad73e78565006891342dbd08
    

## November 09, 2023

Announcement

### Version 1.3.5

This release is **not a critical update** , unless you are directly impacted by the bug fixes, you don't need to update, and you can wait for future releases before upgrading.

Libraries

**Release signature**
    
    
    8584357
    1.3.5
    db04eff8fb5f0d2267d1653498480ec7
    

Change

**Helm charts**

  * MDE services containers image tag: `7a994ee`.
  * MDE UI image tag: `2.15.0.0.109.2`.



Change

The following Dataflow jobs need to be stopped before upgrading:

  * eventchange-dataflow-flex-job
  * gcs-writer-dataflow-flex-job
  * window-dataflow-flex-job



Fixed

  * **Fix (309074623)** : Updates to different libraries, particularly Redis ones.
  * **Fix (308779353)** : Cloud Storage Writer configuration manager connection should use gRPC.
  * **Fix (307925709)** : When a message class has multiple parsers and one fails the others fail as well.
  * **Fix (300928888)** : Whistle parser shouldn't fail when it doesn't produce any records.
  * **Fix (307925851)** : Event change transformation is not working for discrete boolean output.
  * **Fix (308551795)** : Upgrade Apache Beam to 2.51.0.
  * **Fix (309078367)** : Pub/Sub subscriptions have a 30 days expiration date.



## September 29, 2023

Announcement

### Version 1.3.4

This release is **not a critical update** , unless you are directly impacted by the bug fixes, you don't need to update, and you can wait for future releases before upgrading.

Change

**Helm charts**

  * MDE services containers image tag: `e29b2aa`.
  * MDE UI image tag: `"2.15.0.0.104.0-noauth`.



Change

**Infrastructure changes** : MDE version variable `mde_version` updated from 1.3.3 to 1.3.4:
    
    
        tf
        variable "mde_version" {
          type    = string
          default = "1.3.4"
        }
    

Fixed

  * **Fix (301210983)** : Materialize Metadata flag on the sinks only works when the BigQuery sink Materialize Metadata flag is enabled.
  * **Fix (295150919)** : Multiple security vulnerabilities fixes.
  * **Fix (294996056)** : Better service logging and removing unnecessary errors to enhance the troubleshooting experience.
  * **Fix (300863283)** : Added missing `sid` header in the Federation API data fields.



Change

  * **Improvement (301217870)** : Improved validation messages in the parser test API to better indicate how the input messages timestamps and extra fields are handled.
  * **Improvement (300220191)** : Enabling more special characters in the tag name to allow `.`, `$`, `!`, and `*`.
  * **Improvement (302490275)** : The `mde::sanitizeTagName()` Whistle function is now supporting the allowed special characters in the tag name.
  * Multiple documentation updates including specifying the recommended number of types for the small size deployments.



**Note** : Only GKE services are affected by this release.

Libraries

**Release signature**
    
    
    3374a74
    1.3.4
    e7ea042c2381ab7275d681e66a8c0f8a
    

## September 15, 2023

Announcement

### Version 1.3.3

This release is **not a critical update** , unless you are directly impacted by the bug fixes, you don't need to update, and you can wait for future releases before upgrading.

Change

  * **Fix (300404657)** : Malformed input to ops-log not stored in BigQuery due serialization issues.
  * **Fix (300030725)** : Bucket references and instances should be optional when parsing messages.



**Note** : Only GKE services are affected by this release.

Issue

  * **Issue (294526878)** : When updating metadata instances in the UI on a Tag it is not possible to add empty string `""` as a value.
  * **Workaround** : Use the API if you need to insert an empty string as a value for a metadata instance attribute.



Libraries

**Release signature**
    
    
    832ef19
    1.3.3
    48234a49942b0c6031acd67c236ea022
    

Change

**Infrastructure changes** : MDE version variable `mde_version` updated from 1.3.2 to 1.3.3.
    
    
        tf
        variable "mde_version" {
          type    = string
          default = "1.3.3"
        }
    

Change

**Helm charts**

  * MDE services containers image tag: `cdcb206`.
  * MDE UI image tag: `2.13.2.0.99.7-noauth` (same as 1.3.2).



## September 11, 2023

Announcement

### Version 1.3.2

This release is **a critical update**.

Feature

  * MDE UI can now test for a matching message class on the whole list of message classes (like in v1.2) rather than just the individual message class.



Change

  * **Fix (296532636)** : Pub/Sub Sink did not set a data field for numeric records.
  * **Fix (297851980)** : Some parsers failed to save when using specific MDE Whistle functions.
  * **Fix (298031330)** : Cloud Storage Reader was deployed with incorrect input subscription.
  * **Fix (296385152)** : Additional documentation guidance regarding MDE naming limitations.
  * **Fix (298579836)** : Cloud Storage ingestion specs mismatch between cols in spec and CSV file could cause endless retries.
  * **Fix (299418960)** : Documentation [deployment guide](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/guide) added.
  * **Fix (298907994)** : Pub/Sub topics not used for 30 days would expire and cause issues if needed later. Expiration removed on all topics.
  * **Fix (299275899)** : MC and MDE web interface unable to create new types if system had not config added using API first.
  * **Fix (299229076, 298609054, 298609075)** : Ingestion pipeline retry logic updated to better handle misconfigurations.



**Note** : All changes are either in Dataflow jobs or GKE services.

Change

**Infrastructure changes**

  * You must update the file: `deployment/terraform/modules/deployment/dataflow-gcs-reader.tf` if you have modified the Terraform. The specific change is related to the `inputSubscription`.
  * MDE version variable `mde_version` updated from 1.3.1 to 1.3.2.
  * All Pub/Sub topics no longer have any expiration time set See the Terraform for details. If you have your own Terraform you should also remove the expiration from all relevant topics.
  * As a result of `Fix (298907994)` you may see Terraform plan report that a number of Pub/Sub topics would be created. This only happens if they have expired.



Change

**Helm charts**

  * MDE services containers image tag: `3bf1635`.
  * MDE UI image tag: `2.13.2.0.99.7-noauth`.



Issue

  * **Issue (294526878)** : When updating metadata instances in the UI on a Tag it is not possible to add empty string `""` as a value. 
    * **Workaround** : Use the API if you need to insert an empty string as a value for a metadata instance attribute.



## August 23, 2023

Announcement

### Version 1.3.1

This release is **a critical update**.

Issue

  * **Issue (294526878)** : When updating metadata instances in the web interface on a Tag it is not possible to add empty string `""` as a value. 
    * **Workaround:** Use the API if you need to insert an empty string as a value for a metadata instance attribute.
  * **Issue (296532636)** : Pub/Sub Sink doesn't set data for numeric records.
  * **Issue (297851980)** : Parsers that use MDE whistle functions, pass an input parameter instead of a String fail to be saved. 
    * **Workaround** : Add null check and return empty string if null for example `var santizedTagName: if $root.tagName? then mde::sanitizeTagName($root.tagName) else "";`.



Breaking

  * **Fix (294809257, 294995452, 295141703)** : Introduces breaking changes where the Pub/Sub topics and subscriptions **must** be destroyed and recreated by Terraform.



**Warning** : This fix is very important for the stability of MDE and should be applied to all system as soon as possible.

This could cause data loss for any messages that are "in flight" in the processing pipeline. Data already process and stored will **not** be affected.

Change

**Helm charts**

  * Containers image tag: `456bde9`.



Change

  * **Fix (294525580)** : Disable message class doesn't actually disable the message class in the system.
  * **Fix (294809257, 294995452, 295141703)** : Missing bucket or natural key references can cause Metadata Manager service to spam the Operations Log tables in BigQuery and potentially overload the ingestion pipeline.
  * **Fix (294819318)** : When cloning LookML repository, it could fail.
  * **Fix (294981315)** : Helm chart for adding LB to MC update to use the correct resource label.
  * **Fix (295163432)** : When deploying MDE in some Google Cloud project, the deployment with terraform apply would recreate the GKE cluster with each apply.
  * **Fix (295548129)** : Old validation script from v.1.2.0 removed from package.
  * **Fix (294807712)** : MDE web interface had a wrong name in the title.



Change

**Infrastructure changes**

  * Terraform IDs are use for reference not the actual names of the resources. For the full set of changes make sure the review the complete terraform code in the package.
  * MDE version variable `mde_version` updated from 1.3.0 to 1.3.1.
  * Dead letter topic added to the following subscriptions and topics.
  * Pub/Sub subscriptions mentioned earlier have dead letter policy applied.
  * GKE lifecycle has the following ignore changes added.



## August 03, 2023

Announcement

### Version 1.3.0

This release is **a critical update**.

Change

  * Refined the metadata bucket configuration entity by distinguishing between Tag and Record buckets and allow for data contextualization at different aggregation levels.
  * Improved query experience and performance in BigQuery by normalizing metadata, allowing efficient retrieval of metadata without needing to unnest records, and enabling new query patterns.
  * Improved support for Bigtable sink, allowing all archetypes to be stored in Bigtable.
  * Improved query performance by associating each type with a dedicated table in BigQuery to better take advantage of table partitioning.
  * Tag names are now global, and parsers targeting different types can emit records referencing the same tag name.
  * Improved Federation API surface that enables new data access patterns for all archetypes.
  * The number of required fields in a parser has been reduced.
  * Improved logging and introduced the ability to set logging levels.
  * Improved observability and monitoring by exposing new Cloud Monitoring metrics.
  * Internal performance improvements.
  * Improved documentation, deployment and configuration guides, as well as improved access and distribution to documentation content.
  * Reduced the cost by 20% for smaller instances of MDE by migrating key data processing workloads from Dataflow to GKE.
  * Improved the default configuration package by providing better integration with MCe and enabling the ingestion of any data stream with minimal structural requirements. The configuration package now supports the ingestion of data arrays and complex value objects from MCe.
  * Upgraded to Whistle v1.4.0.
  * Improved transformation model: added the capability to apply several versions of the same transformation to the same Type.



Issue

  * **Issue (294526878)** : When updating metadata instances in the web interface on a Tag it is not possible to add empty string `""` as a value. 
    * **Workaround** : Use the API if you need to insert an empty string as a value for a metadata instance attribute.
  * **Issue (294525580)** : Disable message class does not actually disable the message class in the system. 
    * **Workaround** : Delete the message class instead using the API.
  * **Issue (294809257)** : Missing bucket or natural key references can cause Metadata Manager service to spam the Operations Log tables in BigQuery. 
    * Take great care when working with parsers to create the bucket beforehand and double check log for any errors when having deployed a new parser.



Feature

**New features**

  * Added a standalone UI for Manufacturing Data Engine for deployment without Manufacturing Connect.
  * Introduced a new archetype family - clustered - to enable user-defined data clustering logic in BigQuery and row-key generation in Bigtable for the Federation API.
  * Introduced a Pub/Sub sink to allow for extensibility and custom integration. Support for messages in both JSON and ProtoBuf.
  * Extended the BigQuery schema with new fields to simplify and better support analytics use-cases. See the schema changes in the v1.3 [BigQuery Schemas documentation](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/bigquery-schemas).
  * Introduced new datasets in BigQuery: `mde_data`, `mde_dimension`, and `mde_system` to improve data table governance.
  * Configuration data is now exported to dedicated tables in the `mde_system` dataset.
  * Introduced type versioning.
  * Introduced Lookup buckets to enable retrieving reference data in the parser.
  * Introduced type - metadata bucket associations and improved metadata validation by providing the ability to require record contextualization with specific bucket metadata.
  * Added a new identifier (natural key) to metadata instances to enable retrieval of instances by a business-friendly key, such as the tag name, allowing users to manage shared instances centrally.
  * Introduced new custom Whistle functions to look up metadata instances in parsers by natural key.
  * Introduced shared cache using Redis.
  * Introduced more granular deployment sizes to support varied deployment scenarios.
  * Created a MDE LookML library to distribute common MDE LookML components and configuration packages.



Change

  * Metadata buckets support only a single schema and the schema is a property of the bucket.
  * Configuration Manager API has been refactored into configuration and Metadata management API, and the API surface has been simplified to align with Google API design and general REST API best practices.
  * BigQuery schema changes: 
    * Removed default archetype tables.
    * Removed `sfp_data dataset`.
    * Improved storage footprint by removing fields from abstract base schemas of types (archetype schemas). See the schema changes in the v1.3 reference.
    * Changed field naming style from camel case to snakecase.
    * Configuration model concepts have been refined and renamed.
    * Simplified proto record schemas by removing redundant fields
    * AVRO files containing processed data stored in the Cloud Storage data sink are stored by type.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
