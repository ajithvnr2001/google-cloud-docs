---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-firewall/
title: Collect Azure Firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:42.301275+00:00
---

# Collect Azure Firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Azure Firewall logs

**Parser Version:** 16.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export Azure Firewall logs to Google Security Operations using Azure Storage Account. The parser first attempts to process the input as JSON, extracting data from the **Records** field. If the **Record** field is empty, the parser then uses a series of Grok patterns and conditional statements to extract relevant fields from the message, handling different formats and variations in the Azure Firewall logs. 

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



## How to configure Log Export for Azure Firewalls Logs

  1. Sign in to the **Azure Portal** using your privileged account.
  2. Go to **Firewalls** and select the required firewall.
  3. Select **Monitoring > Diagnostic Services**.
  4. Click **\+ Add diagnostic setting**. 
     * Enter a descriptive name for the diagnostic setting.
  5. Select **allLogs**.
  6. Select the **Archive to a storage account** checkbox as the destination. 
     * Specify the **Subscription** and **Storage Account**.
  7. Click **Save**.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the Azure firewall feed

  1. Click the **Azure Platform** pack.
  2. Locate the **Azure firewall** log type and click **Add new feed**. 
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

     * **Shared key** : The shared key (a 512-bit random string in base-64 encoding) used to access Azure resources.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : [Namespace associated with the feed](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion Labels** : Labels applied to all events from this feed.
  4. Click **Create feed**. 


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM Mapping

Log field | UDM mapping | Logic  
---|---|---  
@timestamp | metadata.event_timestamp | Converts the raw log field `@timestamp` to UDM Format.  
category | security_result.rule_type | Maps the raw log field `category` to UDM.  
operationName | metadata.product_event_type | Maps the raw log field `operationName` to UDM.  
properties.Action | security_result.action | Maps the raw log field `properties.Action` to UDM, converting `ALLOW` to `ALLOW`, `DENY` to `BLOCK`, and any other value to `UNKNOWN_ACTION`.  
properties.DestinationIp | target.ip | Maps the raw log field `properties.DestinationIp` to UDM.  
properties.DestinationPort | target.port | Maps the raw log field `properties.DestinationPort` to UDM.  
properties.DnssecOkBit | additional.fields.value.bool_value | Maps the raw log field `properties.DnssecOkBit` to UDM.  
properties.EDNS0BufferSize | additional.fields.value.number_value | Maps the raw log field `properties.EDNS0BufferSize` to UDM.  
properties.ErrorMessage | additional.fields.value.string_value | Maps the raw log field `properties.ErrorMessage` to UDM.  
properties.ErrorNumber | additional.fields.value.number_value | Maps the raw log field `properties.ErrorNumber` to UDM.  
properties.Policy | security_result.detection_fields.value | Maps the raw log field `properties.Policy` to UDM.  
properties.Protocol | network.ip_protocol | Maps the raw log field `properties.Protocol` to UDM if it's not `HTTPS` or `HTTP`.  
properties.Protocol | network.application_protocol | Maps the raw log field `properties.Protocol` to UDM if it's `HTTPS` or `HTTP`.  
properties.QueryClass | network.dns.questions.class | Maps the raw log field `properties.QueryClass` to UDM using a lookup table for mapping DNS query classes.  
properties.QueryId | network.dns.id | Maps the raw log field `properties.QueryId` to UDM.  
properties.QueryName | network.dns.questions.name | Maps the raw log field `properties.QueryName` to UDM.  
properties.QueryType | network.dns.questions.type | Maps the raw log field `properties.QueryType` to UDM using a lookup table for mapping DNS record types.  
properties.RequestSize | network.sent_bytes | Maps the raw log field `properties.RequestSize` to UDM.  
properties.ResponseCode | network.dns.response_code | Maps the raw log field `properties.ResponseCode` to UDM using a lookup table for mapping DNS response codes.  
properties.ResponseFlags | additional.fields.value.string_value | Maps the raw log field `properties.ResponseFlags` to UDM.  
properties.ResponseSize | network.received_bytes | Maps the raw log field `properties.ResponseSize` to UDM.  
properties.Rule | security_result.rule_name | Maps the raw log field `properties.Rule` to UDM.  
properties.RuleCollection | security_result.detection_fields.value | Maps the raw log field `properties.RuleCollection` to UDM.  
properties.RuleCollectionGroup | security_result.detection_fields.value | Maps the raw log field `properties.RuleCollectionGroup` to UDM.  
properties.SourceIp | principal.ip | Maps the raw log field `properties.SourceIp` to UDM.  
properties.SourcePort | principal.port | Maps the raw log field `properties.SourcePort` to UDM.  
properties.msg | security_result.description | Maps the raw log field `properties.msg` to UDM after extracting other fields from it.  
records.category | security_result.rule_type | Maps the raw log field `records.category` to UDM.  
records.operationName | metadata.product_event_type | Maps the raw log field `records.operationName` to UDM.  
records.properties.msg |  | This field is used for extracting multiple fields using Grok patterns and doesn't have a direct mapping to UDM.  
records.resourceId | metadata.product_log_id | Maps the raw log field `records.resourceId` to UDM.  
resourceId | metadata.product_log_id | Maps the raw log field `resourceId` to UDM.  
time | metadata.event_timestamp | Converts the raw log field `time` to UDM Format.  
| metadata.vendor_name | This field is populated by the parser with the value `Microsoft Inc.`.  
| metadata.product_name | This field is populated by the parser with the value `Azure Firewall Application Rule`.  
| metadata.log_type | This field is populated by the parser with the value `AZURE_FIREWALL`.  
| additional.fields.key | This field is populated by the parser with the key for the additional field.  
| security_result.detection_fields.key | This field is populated by the parser with the key for the detection field.  
| network.application_protocol | This field is populated by the parser with the value `DNS` for DNS logs.  
| metadata.event_type | This field is populated by the parser based on the log message. It can be `NETWORK_CONNECTION`, `GENERIC_EVENT`, `STATUS_UPDATE`, or `NETWORK_DNS`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
