---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-vpn/
title: Collect Azure VPN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:50.064125+00:00
---

# Collect Azure VPN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-vpn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Azure VPN logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how to export Azure VPN logs to Google Security Operations using an Azure Storage Account. The parser extracts fields from JSON-formatted Azure VPN logs and then uses Grok patterns to extract further details from the **properties.message** field. Finally, it maps the extracted information to the standardized fields of the Unified Data Model (UDM). 

## Before you begin

Ensure you have the following prerequisites:

  * Google SecOps instance
  * An active Azure tenant
  * Privileged access to Azure



## Configure Azure Storage Account

  1. In the Azure console, search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Specify values for the following input parameters: 
     * **Subscription** : Select the subscription.
     * **Resource Group** : Select the resource group.
     * **Region** : Select the region.
     * **Performance** : Select the performance (Standard recommended).
     * **Redundancy** : Select the redundancy (GRS or LRS recommended).
     * **Storage account name** : Enter a name for the new storage account.
  4. Click **Review + create**.
  5. Review the overview of the account and click **Create**.
  6. From the **Storage Account Overview** page, select the **Access keys** submenu in **Security + networking**.
  7. Click **Show** next to **key1** or **key2**.
  8. Click **Copy to clipboard** to copy the key.
  9. Save the key in a secure location for later use.
  10. From the **Storage Account Overview** page, select the **Endpoints** submenu in **Settings**.
  11. Click **Copy to clipboard** to copy the **Blob service** endpoint URL; for example, `https://<storageaccountname>.blob.core.windows.net`.
  12. Save the endpoint URL in a secure location for later use.



## How to configure Log Export for Azure VPN Gateway Logs

  1. Sign in to the **Azure Portal** using your privileged account.
  2. Select the **Subscription** being monitored. 
  3. In the resource list of that subscription, locate the VPN gateway (this should typically be of the Resource Type, Virtual Network Gateway).
  4. Click the Gateway.
  5. Select **Monitoring > Diagnostic Services**.
  6. Click **\+ Add diagnostic setting**. 
     * Enter a descriptive name for the diagnostic setting.
  7. Select **allLogs**.
  8. Select the **Archive to a storage account** checkbox as the destination. 
     * Specify the **Subscription** and **Storage Account**.
  9. Click **Save**.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the Azure VPN feed

  1. Click the **Azure Platform** pack.
  2. Locate the **Azure VPN** log type and click **Add new feed**.
  3. Specify values for the following fields:

     * **Source Type** : Microsoft Azure Blob Storage V2.
     * **Azure URI** : The blob endpoint URL. 
       * `ENDPOINT_URL/BLOB_NAME`
         * Replace the following: 
           * `ENDPOINT_URL`: The blob endpoint URL (`https://<storageaccountname>.blob.core.windows.net`)
           * `BLOB_NAME`: The name of the blob (such as, `<logname>-logs`)
     * **Source deletion options** : Select the deletion option according to your ingestion preferences.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.

     * **Shared key** : The access key to the Azure Blob Storage.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : [Namespace associated with the feed](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion Labels** : Labels applied to all events from this feed.
  4. Click **Create feed**. 


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
category | security_result.category_details | Directly mapped from the `category` field in the raw log.  
IV_PLAT | security_result.detection_fields.value | Directly mapped from the `IV_PLAT` field in the raw log. Part of a key-value pair within the detection_fields array, where the key is `IV_PLAT`.  
IV_PLAT_VER | security_result.detection_fields.value | Directly mapped from the `IV_PLAT_VER` field in the raw log. Part of a key-value pair within the detection_fields array, where the key is `IV_PLAT_VER`.  
IV_PROTO | security_result.detection_fields.value | Directly mapped from the `IV_PROTO` field in the raw log. Part of a key-value pair within the detection_fields array, where the key is `IV_PROTO`.  
IV_VER | security_result.detection_fields.value | Directly mapped from the `IV_VER` field in the raw log. Part of a key-value pair within the detection_fields array, where the key is `IV_VER`.  
level | security_result.severity | Mapped from the `level` field in the raw log. If `level` is `Informational`, the `severity` is set to `INFORMATIONAL`.  
local_ip | target.ip | Extracted from the `properties.message` field using grok patterns and mapped to the target IP address.  
local_port | target.port | Extracted from the `properties.message` field using grok patterns and mapped to the target port number. Converted to integer type.  
operationName | metadata.product_event_type | Directly mapped from the `operationName` field in the raw log.  
properties.message | metadata.description | Extracted from the `properties.message` field using grok patterns. Depending on the message format, the description might include additional details extracted from `desc2` field.  
remote_ip | principal.ip | Extracted from the `properties.message` field using grok patterns and mapped to the principal IP address.  
remote_port | principal.port | Extracted from the `properties.message` field using grok patterns and mapped to the principal port number. Converted to integer type.  
resourceid | target.resource.product_object_id | Directly mapped from the `resourceid` field in the raw log.  
time | timestamp, metadata.event_timestamp | Parsed from the `time` field in the raw log using the RFC 3339 format and mapped to both the event timestamp and the UDM timestamp.  
| metadata.log_type | Hardcoded to `AZURE_VPN`.  
| metadata.vendor_name | Hardcoded to `AZURE`.  
| metadata.product_name | Hardcoded to `VPN`.  
| metadata.event_type | Dynamically set based on the presence of IP addresses. If both `remote_ip` and `local_ip` are present, it's set to `NETWORK_CONNECTION`, otherwise `USER_RESOURCE_ACCESS`.  
| extensions.auth.type | Hardcoded to `VPN`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-vpn-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
