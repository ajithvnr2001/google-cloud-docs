---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs/
title: Analyze regional secrets with Cloud Asset Inventory \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:58.567412+00:00
---

# Analyze regional secrets with Cloud Asset Inventory  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Analyze regional secrets with Cloud Asset Inventory Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Cloud Asset Inventory to monitor your secrets, export data for analysis, and run powerful queries to get the insights that you require.

## Overview

Cloud Asset Inventory analyzes your Google Cloud environment and records any changes to your cloud resources, such as virtual machines, databases, storage buckets, and in this context, your Secret Manager secrets. The integration between Secret Manager and Cloud Asset Inventory helps you do the following:

  * **Run queries** : Search for specific secrets or identify patterns across your secrets.

  * **Set up alerts** : Configure Cloud Asset Inventory to send notifications to Pub/Sub when specific events occur, such as when secrets are created, modified, or deleted.

  * **Export data** : Export your secret inventory to BigQuery for in-depth analysis and reporting.

  * **Manage and analyze your secrets** : See all your secrets in one place (across projects and your entire organization) and identify secrets that might be misconfigured or violate your organization's security policies. For example, you can find secrets that are not rotated regularly or lack proper access controls.




This is an advanced task for Secret Manager users. Before reading this page, we recommend that you read the following:

  * [Secret Manager overview](https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs) to understand the key concepts and features of Secret Manager

  * [Cloud Asset Inventory overview](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) to understand Cloud Asset Inventory and to see its comprehensive asset management features




### Querying Secret Manager

To analyze your secrets with SQL-like queries, we recommend that you [export](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-bigquery) your secret and secret versions to BigQuery. Secret Manager isn't integrated with [Asset Search](https://docs.cloud.google.com/asset-inventory/docs/searching-resources) or [Policy Analyzer](https://docs.cloud.google.com/asset-inventory/docs/searching-iam-policies). These queries use the Google Cloud CLI and BigQuery to search your assets.

### Limitations

Using Cloud Asset Inventory to analyze Secret Manager resources has the following limitation:

  * Cloud Asset Inventory supports exporting and listing snapshots for only the past five weeks.
  * Secret Manager data is synchronized with Cloud Asset Inventory every 7 hours. If a sync fails, freshness is delayed until the next successful sync. For use cases requiring real-time information, query the Secret Manager API instead. 



## Monitor asset changes

Cloud Asset Inventory tracks updates and supports [monitoring these changes](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes). You can [configure feeds](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes#creating_a_feed) to send notifications to a set of configured Pub/Sub topics each time there's a modification to your resources. Additionally, Cloud Asset Inventory supports [configuring conditions on your feeds](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes-with-condition), so that you can monitor specific changes for certain asset types. To learn how to trigger workflows on asset changes, see the [Pub/Sub documentation](https://docs.cloud.google.com/pubsub/docs).

## Export assets to BigQuery

Exporting your secrets and secret versions to BigQuery lets you run SQL-like queries over large amounts of data and produce meaningful insights about your assets. Before you export your assets, ensure that your [dataset and service accounts are configured correctly](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-bigquery#prepare-bigquery).

To export your assets, run the following command:

### gcloud

Before using any of the command data below, make the following replacements: 

  * CONTENT_TYPE: the asset content type (`RESOURCE`).
  * PROJECT_ID: the ID of the project containing the secrets to be analyzed.
  * SNAPSHOT_TIME: the [time](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) at which to snapshot resources. This may be between the current time and 5 weeks in the past.
  * BIGQUERY_PROJECT_ID: the ID of the project that the BigQuery table is in.
  * DATASET_ID: the ID of the BigQuery dataset.
  * TABLE_NAME: the table you're exporting your metadata to. If it doesn't exist, it's created.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset export \
      --content-type=CONTENT_TYPE \
      --project=PROJECT_ID \
      --snapshot-time=SNAPSHOT_TIME \
      --bigquery-table=projects/BIGQUERY_PROJECT_ID/datasets/DATASET_ID/tables/TABLE_NAME \
      --output-bigquery-force

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset export `
      --content-type=CONTENT_TYPE `
      --project=PROJECT_ID `
      --snapshot-time=SNAPSHOT_TIME `
      --bigquery-table=projects/BIGQUERY_PROJECT_ID/datasets/DATASET_ID/tables/TABLE_NAME `
      --output-bigquery-force

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset export ^
      --content-type=CONTENT_TYPE ^
      --project=PROJECT_ID ^
      --snapshot-time=SNAPSHOT_TIME ^
      --bigquery-table=projects/BIGQUERY_PROJECT_ID/datasets/DATASET_ID/tables/TABLE_NAME ^
      --output-bigquery-force

**Note:** Cloud Asset Inventory doesn't support appending data to an existing table. Data must be sent to a new table, or overwrite an existing table. 

For more information, see [Exporting to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-bigquery).

## Sample queries

Use these sample queries to find secrets and secret versions with specific properties.

### Regional secrets created in the last two weeks

Find secrets (and their properties) that were added to your organization in the past two weeks.

### BigQuery
    
    
      SELECT name, FROM BIGQUERY_TABLE
      WHERE asset_type='secretmanager.googleapis.com/Secret' AND
        resource.location <> "global" AND
        DATE(JSON_VALUE(resource.data, '$.createTime')) > DATE_SUB(CURRENT_DATE(), INTERVAL 2 WEEK);
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
        NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
        gcloud asset list --project=PROJECT_ID \
            --asset-types='secretmanager.googleapis.com/Secret' \
            --snapshot-time=$NOW \
            --content-type='resource' \
            --filter="resource.location != global AND resource.data.createTime>-P2W"
      

Replace PROJECT_ID with the ID of the project containing the secrets to be analyzed.

### Regional secrets in a specific location

Find all secrets stored in a specific location, such as `us-central1`.

### BigQuery
    
    
        SELECT * FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/Secret' AND
          resource.location = "us-central1";
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
        NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
        gcloud asset list --project=PROJECT_ID \
           --asset-types='secretmanager.googleapis.com/Secret' \
           --snapshot-time=$NOW \
           --content-type='resource' \
           --filter="resource.location = LOCATION AND resource.data.createTime>-P2W"
      

Replace the following:

  * PROJECT_ID: the ID of the project containing the secrets to be analyzed
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secrets



### Regional secret versions created over 180 days ago

List all secret versions that were created more than 180 days ago.

### BigQuery
    
    
        SELECT * FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/SecretVersion'
          resource.location <> "global" AND
          DATE(JSON_VALUE(resource.data, '$.createTime')) < DATE_SUB(CURRENT_DATE(), INTERVAL 180 DAY) AND
          JSON_VALUE(resource.data, '$.state') = "ENABLED";
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
        NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
        gcloud asset list --project=PROJECT_ID \
            --asset-types='secretmanager.googleapis.com/SecretVersion' \
            --snapshot-time=$NOW \
            --content-type='resource' \
            --filter="resource.location != global AND resource.data.createTime < P6M AND resource.data.state = ENABLED"
      

Replace PROJECT_ID with the ID of the project containing the secrets to be analyzed.

### Regional secrets without CMEK configured

List all secrets that are _not_ encrypted with customer-manager encryption keys (CMEK):

### BigQuery
    
    
        SELECT * FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/Secret'
          resource.location <> "global" AND
          JSON_VALUE(resource.data, "$.customerManagedEncryption.kmsKeyName") IS NOT NULL;
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
        NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
        gcloud asset list --project=PROJECT_ID \
            --asset-types='secretmanager.googleapis.com/SecretVersion' \
            --snapshot-time=$NOW \
            --content-type='resource' \
            --filter="(resource.location != global AND resource.data.customerManagedEncryption.kmsKeyVersionName = NULL) AND resource.data.state=ENABLED"
      

Replace PROJECT_ID with the ID of the project containing the secrets to be analyzed.

### Regional secrets with CMEK configured

List all secrets that are encrypted with CMEK.

### BigQuery
    
    
        SELECT * FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/Secret'
          resource.location <> "global" AND
          JSON_VALUE(resource.data, "$.customerManagedEncryption.kmsKeyName") IS NOT NULL;
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
        NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
        gcloud asset list --project=PROJECT_ID \
            --asset-types='secretmanager.googleapis.com/Secret' \
            --snapshot-time=$NOW \
            --content-type='resource' \
            --filter="resource.location != global AND resource.data.customerManagedEncryption != NULL"
      

Replace PROJECT_ID with the ID of the project containing the secrets to be analyzed.

### Regional secrets encrypted with a specific CMEK

Find secrets that are encrypted with a specific CMEK.

### BigQuery
    
    
        SELECT * FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/Secret'
          resource.location <> "global" AND
          JSON_VALUE(resource.data, "$.customerManagedEncryption.kmsKeyName") = KMS_KEY_NAME;
      

Replace the following:

  * BIGQUERY_TABLE: the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

  * KMS_KEY_NAME: the ID of the key or fully qualified identifier for the key




### gcloud
    
    
        NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
        gcloud beta asset list --project=PROJECT_ID \
            --asset-types='secretmanager.googleapis.com/Secret' \
            --snapshot-time=$NOW \
            --content-type='resource' \
            --filter="resource.location != global AND resource.data.customerManagedEncryption.kmsKeyName=KMS_KEY_NAME"
      

Replace the following:

  * PROJECT_ID: the ID of the project containing the secrets to be analyzed
  * KMS_KEY_NAME: the ID of the key or fully qualified identifier for the key



### Regional secret versions without CMEK configured

Find all enabled secret versions that are not encrypted with CMEK.

### BigQuery
    
    
        SELECT * FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/SecretVersion'
          resource.location <> "global" AND
          JSON_VALUE(resource.data, "$.customerManagedEncryption.kmsKeyVersionName") IS NULL AND
          JSON_VALUE(resource.data, "$.state") = "ENABLED";
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
        NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
        gcloud asset list --project=PROJECT_ID \
            --asset-types='secretmanager.googleapis.com/SecretVersion' \
            --snapshot-time=$NOW \
            --content-type='resource' \
            --filter="(resource.location != global AND resource.data.customerManagedEncryption.kmsKeyVersionName = NULL) AND resource.data.state=ENABLED"
      

Replace PROJECT_ID with the ID of the project containing the secrets to be analyzed.

### Regional secret versions encrypted with a specific CMEK

List all enabled secret versions encrypted with a specific CMEK version.

### BigQuery
    
    
        SELECT * FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/SecretVersion'
          resource.location <> "global" AND
          JSON_VALUE(resource.data, "$.customerManagedEncryption.kmsKeyVersionName") = KMS_KEY_VERSION_NAME AND
          JSON_VALUE(resource.data, "$.state") = "ENABLED";
      

Replace the following:

  * BIGQUERY_TABLE: the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

  * KMS_KEY_VERSION_NAME: the Cloud Key Management Service key version number




### gcloud
    
    
        NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
        gcloud asset list --project=PROJECT_ID \
            --asset-types='secretmanager.googleapis.com/SecretVersion' \
            --snapshot-time=$NOW \
            --content-type='resource' \
            --filter="(resource.location != global AND resource.data.customerManagedEncryption.kmsKeyVersionName = KMS_KEY_VERSION_NAME) AND resource.data.state=ENABLED"
      

Replace the following:

  * PROJECT_ID: the ID of the project containing the secrets to be analyzed
  * KMS_KEY_VERSION_NAME: the ID of the key version



### Regional secrets without rotation configured

Find all secrets that don't have a rotation schedule.

### BigQuery
    
    
        SELECT name FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/Secret' AND
          resource.location <> "global" AND
          JSON_EXTRACT(resource.data, '$.rotation') IS NULL;
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
      NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
      gcloud asset list --project=PROJECT_ID \
          --asset-types='secretmanager.googleapis.com/Secret' \
          --snapshot-time=$NOW \
          --content-type='resource' \
          --filter="resource.location != global AND resource.data.rotation = NULL"
      

Replace PROJECT_ID with the ID of the project containing the secrets to be analyzed.

### Regional secrets with a specific rotation period

Find all secrets scheduled to be rotated less than once every 90 days:

### BigQuery
    
    
        SELECT *
        FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/Secret' AND
          resource.location <> "global" AND
          CAST(
            TRIM(
              JSON_VALUE(JSON_EXTRACT(resource.data, "$.rotation.rotationPeriod")),"s")
            AS INT64)
        < 86400 * 90 #Rotation period in seconds (86400s in 1 day * 90 days)
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
      NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
      ROTATION_PERIOD_SECONDS=$((90 * 24 * 60 * 60))
      gcloud asset list --project=PROJECT_ID \
          --asset-types='secretmanager.googleapis.com/Secret' \
          --snapshot-time=$NOW \
          --content-type='resource' \
          --filter="resource.location != global AND resource.data.rotation != null AND resource.data.rotation.rotationPeriod <= ${ROTATION_PERIOD_SECONDS}s"
      

Replace PROJECT_ID with the ID of the project containing the secrets to be analyzed.

### Regional secrets that will expire in the next 30 days

List secrets that will expire in the next 30 days.

### BigQuery
    
    
        SELECT * FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/Secret' AND
          resource.location <> "global" AND
          DATE(JSON_VALUE(resource.data, '$.expireTime')) < DATE_ADD(CURRENT_DATE(), INTERVAL 30 DAY);
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
      NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
      gcloud asset list --project=PROJECT_ID \
          --asset-types='secretmanager.googleapis.com/Secret' \
          --snapshot-time=$NOW \
          --content-type='resource' \
          --filter="resource.location != global AND resource.data.expireTime < PD30"
      

Replace PROJECT_ID with the ID of the project containing the secrets to be analyzed.

### Regional secrets with a Pub/Sub topic configured

List all secrets that have at least one Pub/Sub topic configured.

### BigQuery
    
    
        SELECT name, ARRAY_LENGTH(JSON_EXTRACT_ARRAY(resource.data, '$.topics')) AS topics_count,
        FROM BIGQUERY_TABLE
        WHERE asset_type='secretmanager.googleapis.com/Secret' AND
          resource.location <> "global" AND
          ARRAY_LENGTH(JSON_EXTRACT_ARRAY(resource.data, '$.topics')) > 0
      

Replace BIGQUERY_TABLE with the full path to the BigQuery table that you have exported all the assets to in the [Export assets to BigQuery](https://docs.cloud.google.com/secret-manager/regional-secrets/analyze-resources-rs#export-assets-to-bigquery) section of this document.

### gcloud
    
    
      NOW=$(TZ=GMT date +"%Y-%m-%dT%H:%M:%SZ")
      gcloud asset list --project=PROJECT_ID \
          --asset-types='secretmanager.googleapis.com/Secret' \
          --snapshot-time=$NOW \
          --content-type='resource' \
          --filter="resource.location != global AND resource.data.topics != NULL"
      

Replace PROJECT_ID with the ID of the project containing the secrets to be analyzed.

## What's next

  * Learn about [best practices](https://docs.cloud.google.com/secret-manager/regional-secrets/best-practices-rs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
