---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okera-dap/
title: Collect Okera Dynamic Access Platform (ODAP) audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:35.608678+00:00
---

# Collect Okera Dynamic Access Platform (ODAP) audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okera-dap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Okera Dynamic Access Platform (ODAP) audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Okera Dynamic Access Platform (ODAP) audit logs to Google Security Operations using cloud storage (Amazon S3, Google Cloud Storage, or Azure Blob Storage).

Okera Dynamic Access Platform (ODAP) is a data access control and governance platform that provides fine-grained access control, automated data discovery and classification, and comprehensive audit logging for data lakes and analytics platforms. The platform generates JSON-formatted audit logs that capture all data access events, policy changes, and administrative actions.

**Note:** Okera was acquired by Databricks in May 2023, and the product has been integrated into Databricks Unity Catalog. For existing Okera ODAP deployments still in use, this guide provides instructions for exporting audit logs to cloud storage for ingestion into Google SecOps. For new deployments, consider using Databricks Unity Catalog audit logs instead.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * An active Okera ODAP deployment (version 2.0 or later)
  * Administrative access to Okera cluster configuration (Helm chart or configuration YAML)
  * Privileged access to one of the following cloud platforms: 
    * **AWS** (S3, IAM) for Amazon S3 storage
    * **GCP** (Cloud Storage, IAM) for Google Cloud Storage
    * **Azure** (Storage Accounts) for Azure Data Lake Storage Gen2
  * Okera cluster must have write access to the cloud storage location



## Configure Okera ODAP audit log export

Okera ODAP audit logs are configured through the cluster configuration YAML file and deployed using the Okera Helm chart. The audit logs are written in JSON format to a shared cloud storage location.

### Determine your cloud storage platform

Choose one of the following cloud storage platforms based on your Okera deployment:

  * **Amazon S3** : For Okera clusters running on AWS
  * **Google Cloud Storage** : For Okera clusters running on GCP
  * **Azure Data Lake Storage Gen2** : For Okera clusters running on Azure



### Configure audit log storage location

  1. Access your Okera cluster configuration YAML file.
  2. Locate the audit log configuration section.
  3. Configure the audit log destination based on your cloud platform:

     * **For Amazon S3:**
           
           WATCHER_LOG_DST_DIR: "s3://your-company/okera/ops/"
           WATCHER_AUDIT_LOG_DST_DIR: "s3://your-company/okera/audit/"
           WATCHER_S3_REGION: "us-east-1"
           WATCHER_S3_ENCRYPT: "true"
           WATCHER_AUDIT_UPLOAD_INTERVAL_SEC: "15"
           

Replace the following:

       * `your-company`: Your S3 bucket name
       * `us-east-1`: Your AWS region
     * **For Google Cloud Storage:**
           
           WATCHER_LOG_DST_DIR: "gs://your-company/okera/ops/"
           WATCHER_AUDIT_LOG_DST_DIR: "gs://your-company/okera/audit/"
           WATCHER_AUDIT_UPLOAD_INTERVAL_SEC: "15"
           

Replace the following:

       * `your-company`: Your GCS bucket name
     * **For Azure Data Lake Storage Gen2:**
           
           WATCHER_LOG_DST_DIR: "abfs://okera-ops@yourstorageaccount.dfs.core.windows.net/"
           WATCHER_AUDIT_LOG_DST_DIR: "abfs://okera-audit@yourstorageaccount.dfs.core.windows.net/"
           WATCHER_AUDIT_UPLOAD_INTERVAL_SEC: "15"
           

Replace the following:

       * `yourstorageaccount`: Your Azure storage account name
       * `okera-ops` and `okera-audit`: Your container names
  4. Save the configuration file.

  5. Update the Okera cluster using the Helm chart:
         
         helm upgrade okera okera/okera -f your-config.yaml
         

  6. Verify that the audit logs are being written to the configured location:

     * **For S3:**
           
           aws s3 ls s3://your-company/okera/audit/
           

     * **For GCS:**
           
           gsutil ls gs://your-company/okera/audit/
           

     * **For Azure:**
           
           az storage blob list --account-name yourstorageaccount --container-name okera-audit
           


**Note:** The audit logs are written as JSON text files partitioned by date. Each file contains newline-delimited JSON records for audit events.

### Audit log format

Okera audit logs are written in JSON format with the following characteristics:

  * Each file contains multiple JSON records, one per line (NDJSON format)
  * Records include all data access events, policy changes, and administrative actions
  * Files are organized by date in the storage location
  * The `okera_system.audit_logs` dataset provides a queryable view of the audit data



## Configure cloud storage access for Google SecOps

Follow the appropriate guide below based on your cloud storage platform:

### For Amazon S3

  1. Create an IAM user with read access to the S3 bucket containing Okera audit logs.
  2. Follow the steps in the [AWS S3 configuration guide](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudtrail) to: 
     * Create an IAM user
     * Generate access keys
     * Grant `AmazonS3ReadOnlyAccess` or a custom policy with `s3:GetObject` and `s3:ListBucket` permissions



### For Google Cloud Storage

  1. Retrieve the Google SecOps service account email:

     1. Go to **SIEM Settings > Feeds**.
     2. Click **Add New Feed**.
     3. Click **Configure a single feed**.
     4. Enter a name for the feed (for example, `okera-audit-logs`).
     5. Select **Google Cloud Storage V2** as the **Source type**.
     6. Select **Okera DAP** as the **Log type**.
     7. Click **Get Service Account**.
     8. Copy the service account email displayed.
  2. Grant the service account access to your GCS bucket:

     1. Go to **Cloud Storage > Buckets** in the GCP Console.
     2. Click on the bucket containing Okera audit logs.
     3. Go to the **Permissions** tab.
     4. Click **Grant access**.
     5. In **Add principals** , paste the Google SecOps service account email.
     6. In **Assign roles** , select **Storage Object Viewer**.
     7. Click **Save**.



### For Azure Blob Storage

  1. Retrieve the storage account access key:

     1. In the Azure portal, go to your **Storage Account**.
     2. Select **Access keys** under **Security + networking**.
     3. Click **Show keys**.
     4. Copy **Key 1** or **Key 2**.
  2. Note the Blob service endpoint:

     * Format: `https://yourstorageaccount.blob.core.windows.net/`



## Configure a feed in Google SecOps to ingest Okera ODAP audit logs

### For Amazon S3

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. Enter a unique name for the **Feed name** (for example, `okera-audit-s3`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Okera DAP** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://your-company/okera/audit/`
     * **Source deletion option** : Select **Never** (recommended to preserve audit logs)
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : IAM user access key with read access to the S3 bucket
     * **Secret Access Key** : IAM user secret key
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next** and then click **Submit**.




### For Google Cloud Storage

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. Enter a unique name for the **Feed name** (for example, `okera-audit-gcs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Okera DAP** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following fields:

     * **Storage bucket URL** : `gs://your-company/okera/audit/`
     * **Source deletion option** : Select **Never** (recommended to preserve audit logs)
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next** and then click **Submit**.




### For Azure Blob Storage

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. Enter a unique name for the **Feed name** (for example, `okera-audit-azure`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Okera DAP** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following fields:

     * **Azure URI** : `https://yourstorageaccount.blob.core.windows.net/okera-audit/`
     * **Source deletion option** : Select **Never** (recommended to preserve audit logs)
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Shared key** : The storage account access key
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next** and then click **Submit**.




## Verify audit log ingestion

  1. Wait 10-15 minutes for the initial ingestion to complete.
  2. Go to **Search** in Google SecOps.
  3. Run a search query to verify Okera audit logs are being ingested:
         
         metadata.vendor_name = "Okera"
         

  4. Verify that events are appearing with recent timestamps.

  5. Check the feed status:

     1. Go to **SIEM Settings > Feeds**.
     2. Locate your Okera audit feed.
     3. Verify the **Status** shows **Active**.
     4. Check **Last successful ingestion** timestamp.



## Troubleshooting

### No logs appearing in Google SecOps

  * Verify that Okera is writing audit logs to the configured cloud storage location
  * Check that the storage path in the feed configuration matches the `WATCHER_AUDIT_LOG_DST_DIR` setting
  * Verify cloud storage permissions are correctly configured
  * Check the feed status for error messages



### Permission errors

  * **S3** : Verify the IAM user has `s3:GetObject` and `s3:ListBucket` permissions
  * **GCS** : Verify the Google SecOps service account has **Storage Object Viewer** role
  * **Azure** : Verify the storage account access key is correct and not expired



### Okera not writing audit logs

  * Verify the `WATCHER_AUDIT_LOG_DST_DIR` configuration is set correctly
  * Check that the Okera cluster has write permissions to the cloud storage location
  * Verify the Helm chart update was applied successfully
  * Check Okera cluster logs for errors related to audit log uploads



## Migration to Databricks Unity Catalog

If you are planning to migrate from Okera ODAP to Databricks Unity Catalog:

  1. Review the [Databricks Unity Catalog audit logs documentation](https://docs.databricks.com/data-governance/unity-catalog/audit.html)
  2. Configure Unity Catalog audit log delivery to cloud storage
  3. Create a new Google SecOps feed for Unity Catalog audit logs
  4. Maintain both feeds during the migration period
  5. Decommission the Okera feed after migration is complete



For assistance with Okera ODAP or migration to Unity Catalog, contact Databricks support.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
extensions.auth.type | extensions.auth.type | Authentication type  
json_entry.request_time | metadata.event_timestamp | Timestamp when the event occurred  
metadata.event_type | metadata.event_type | Type of event  
json_entry.statement_type | metadata.product_event_type | Product-specific event type  
metadata.product_name | metadata.product_name | Product name  
metadata.vendor_name | metadata.vendor_name | Vendor/company name  
json_entry.session_id | network.session_id | Session identifier  
json_entry.connected_user | principal.user.userid | User identifier  
json_entry.auth_failure | security_result.action | Action taken  
json_entry.status | security_result.summary | Summary of the security result  
json_entry.client_application | target.application | Application name  
json_entry.client_network_address | target.ip | IP address  
json_entry.client_network_address | target.port | Port number  
json_entry.request_id | target.resource.attribute.labels | Key-value pairs of attributes for the resource  
json_entry.num_results_read | target.resource.attribute.labels |   
json_entry.num_results_returned | target.resource.attribute.labels |   
json_entry.peak_memory_usage | target.resource.attribute.labels |   
json_entry.statement | target.resource.attribute.labels |   
json_entry.bytes_scanned | target.resource.attribute.labels |   
json_entry.for_reporting | target.resource.attribute.labels |   
json_entry.auth_failure | target.resource.attribute.labels |   
json_entry.default_db | target.resource.name | Name of the resource  
target.resource.resource_type | target.resource.resource_type | Type of resource  
json_entry.user | target.user.userid | User identifier  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okera-dap-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
