---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-identity-context/
title: Collect Google Cloud Identity Context logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:42:02.726815+00:00
---

# Collect Google Cloud Identity Context logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-identity-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Google Cloud Identity Context logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Google Cloud Identity Context logs to Google Security Operations using Google Cloud Storage V2.

Cloud Identity Context provides user and device information for identity-aware access decisions, including device posture, user attributes, and group memberships used for security context enrichment.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * A Google Workspace or Cloud Identity environment with users and devices
  * IAM permissions to create logging sinks in the GCP project
  * A logging Admin role (`roles/logging.admin`) or equivalent permissions



## Create a Google Cloud Storage bucket

### Using Google Cloud Console

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cloud-identity-context-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Using the gcloud command-line tool

  * Alternatively, create a bucket using the `gcloud` command:
        
        gcloud storage buckets create gs://cloud-identity-context-logs \
            --location=us-central1 \
            --default-storage-class=STANDARD
        

    * Replace: `cloud-identity-context-logs` with your bucket name (globally unique).
    * Replace: `us-central1` with your preferred region (e.g., `us-central1`, `europe-west1`).



## Export Cloud Identity Context logs to GCS

Cloud Identity Context logs are collected in Cloud Logging. To export them to GCS, create a Cloud Logging sink:

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project.
  3. Go to **Logging > Log Router**.
  4. Click **Create sink**.
  5. Enter the following details:

     * **Sink name** : `cloud-identity-context-sink`
     * **Sink description** : Optional description
     * Click **Next**
  6. In the **Select sink service** section:

     * Choose **Cloud Storage bucket** as the sink service
     * Select the bucket you created earlier
     * Click **Next**
  7. In the **Choose logs to include in sink** section, use the following filter:
         
         resource.type="audited_resource"
             protoPayload.serviceName="cloudidentity.googleapis.com"
         

  8. Click **Next**

  9. Review your sink configuration and click **Create sink**.

  10. Copy the service account displayed in the confirmation message (e.g., `service-PROJECT_NUMBER@gcp-sa-logging.iam.gserviceaccount.com`).

  11. Go to **Cloud Storage > Buckets**.

  12. Select your bucket.

  13. Go to the **Permissions** tab.

  14. Click **Grant access**.

  15. Paste the service account email from step 9.

  16. Assign the **Storage Object Creator** role.

  17. Click **Save**.




## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Select **Google Cloud Storage V2** as the **Source type**.
  4. Click **Get Service Account**.
  5. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  6. Copy this email address. You will use it in the next step.


**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.

## Grant IAM permissions to the Google SecOps service account

### Using Google Cloud Console

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.



### Using the gcloud command-line tool

  * Use the following command:
        
        gcloud storage buckets add-iam-policy-binding gs://cloud-identity-context-logs \
            --member="serviceAccount:<SECOPS_SERVICE_ACCOUNT_EMAIL>" \
            --role="roles/storage.objectViewer"
        

Replace:

    * `cloud-identity-context-logs`: With your bucket name.
    * `<SECOPS_SERVICE_ACCOUNT_EMAIL>`: With the Google SecOps service account email.



## Configure a feed in Google SecOps to ingest Cloud Identity Context logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cloud Identity Context Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Google Cloud Identity Context** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URI** : Enter the GCS bucket URI:
           
           gs://cloud-identity-context-logs/
           

     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never deletes any files after transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select deletion on success, the service account must have **Storage Object Admin** role instead of Storage Object Viewer.
     * **Maximum File Age (Days)** : Include files modified within the last number of days. Default is 180.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : Labels applied to all events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




For more information about Google Security Operations feeds, see [Google Security Operations feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type).

If you encounter issues when you create feeds, [contact Google Security Operations support](https://docs.cloud.google.com/chronicle/docs/getting-support).

## Field mapping reference

The Cloud Identity Context parser extracts user and device identity information from Google Cloud Identity, including user attributes, email addresses, group memberships, organizational unit paths, and device posture data. It maps these fields to the UDM `entity` model with entity type `USER`.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`product_object_id` | `entity.asset.product_object_id` | Directly mapped  
`data.protoPayload.requestMetadata.callerIp` | `entity.ip` | Merged  
`authorizationInfodata_granted_label` | `entity.labels` | Merged  
`authorizationInfodata_permission_label` | `entity.labels` | Merged  
`authorizationInfodata_resource_label` | `entity.labels` | Merged  
`data_logname_label` | `entity.labels` | Merged  
`field_` | `entity.labels` | Merged  
`referencedTables_datasetId_label` | `entity.labels` | Merged  
`referencedTables_projectId_label` | `entity.labels` | Merged  
`referencedTables_tableId_label` | `entity.labels` | Merged  
`referencedViews_datasetId_label` | `entity.labels` | Merged  
`referencedViews_projectId_label` | `entity.labels` | Merged  
`referencedViews_tableId_label` | `entity.labels` | Merged  
`value` | `entity.location.country_or_region` | Directly mapped  
`data.protoPayload.resourceName` | `entity.resource.name` | Directly mapped  
`company_name` | `entity.user.company_name` | Renamed/mapped  
`depart` | `entity.user.department` | Merged  
`organisation` | `entity.user.department` | Merged  
`alias` | `entity.user.email_addresses` | Merged  
`data.protoPayload.authenticationInfo.principalEmail` | `entity.user.email_addresses` | Merged  
`email` | `entity.user.email_addresses` | Merged  
`emails` | `entity.user.email_addresses` | Merged  
`primaryEmail` | `entity.user.email_addresses` | Merged  
`employeeId` | `entity.user.employee_id` | Directly mapped  
`employee_id` | `entity.user.employee_id` | Directly mapped  
`ext.value` | `entity.user.employee_id` | Directly mapped  
`first_name` | `entity.user.first_name` | Directly mapped  
`givenName` | `entity.user.first_name` | Directly mapped  
`name.givenName` | `entity.user.first_name` | Directly mapped  
`orgUnitPath` | `entity.user.group_identifiers` | Merged  
`familyName` | `entity.user.last_name` | Directly mapped  
`last_name` | `entity.user.last_name` | Directly mapped  
`name.familyName` | `entity.user.last_name` | Directly mapped  
`office_address.country_or_region` | `entity.user.office_address.country_or_region` | Directly mapped  
`office_address.state` | `entity.user.office_address.state` | Directly mapped  
`number` | `entity.user.phone_numbers` | Merged  
`data.insertId` | `entity.user.product_object_id` | Directly mapped  
`id` | `entity.user.product_object_id` | Directly mapped  
`title` | `entity.user.title` | Directly mapped  
`familyName` | `entity.user.user_display_name` | Directly mapped  
`givenName` | `entity.user.user_display_name` | Directly mapped  
`name.fullName` | `entity.user.user_display_name` | Directly mapped  
`user_display_name` | `entity.user.user_display_name` | Directly mapped  
`data.insertId` | `entity.user.userid` | Directly mapped  
`userid` | `entity.user.userid` | Directly mapped  
`windows_sid` | `entity.user.windows_sid` | Directly mapped  
`value` | `metadata.event_timestamp` | Parsed as `ISO8601`  
N/A | `metadata.description` | Constant: `From BigQuery`  
N/A | `metadata.entity_type` | Constant: `USER`  
N/A | `metadata.product_entity_id` | Constant: `unknown`  
N/A | `metadata.product_name` | Constant: `Cloud Identity`  
N/A | `metadata.vendor_name` | Constant: `Google`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloud-identity-context-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
