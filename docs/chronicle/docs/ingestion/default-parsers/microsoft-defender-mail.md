---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-mail/
title: Collect Microsoft Defender for Office 365 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:31.243419+00:00
---

# Collect Microsoft Defender for Office 365 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Defender for Office 365 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect Microsoft Defender for Office 365 logs by setting up a Google Security Operations feed using Microsoft Azure Blob Storage V2.

Microsoft Defender for Office 365 is an email security solution that protects organizations against advanced threats such as phishing, business email compromise, and malware attacks. Email event data from Defender for Office 365 is available through the Microsoft Defender XDR Streaming API, which streams Advanced Hunting events to an Azure Storage account. Google SecOps reads the streamed events directly from the storage account, so no intermediate collector is required.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Microsoft Azure** portal with permissions to: 
    * Create Storage Accounts in the same tenant as Microsoft Defender XDR
    * Register resource providers on the subscription
    * Manage access keys
    * The **Contributor** role on the storage account (required by the Streaming API configuration)
  * Access to the **Microsoft Defender portal** with at least the **Security Administrator** role
  * Microsoft Defender for Office 365 deployed in your tenant: the Email* and UrlClickEvents Advanced Hunting tables are populated by records from Defender for Office 365 and stay empty without it

**Note:** If you restrict access to your Azure resources using an Azure Storage firewall, you must add the IP ranges used by Storage Transfer Service (STS) workers to your list of allowed IPs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting).



## Configure an Azure Storage Account

### Register the Microsoft.Insights resource provider

The Streaming API requires the **Microsoft.Insights** resource provider on the subscription that holds the storage account:

  1. Sign in to the **Azure portal**.
  2. Go to **Subscriptions > Your subscription > Resource providers**.
  3. Search for **Microsoft.Insights**.
  4. Click **Register**.



### Create a Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription (same tenant as Microsoft Defender XDR)  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `defenderemaillogs`)  
**Region** | Select the region (for example, `East US`)  
**Performance** | Standard (recommended)  
**Redundancy** | GRS (Geo-redundant storage) or LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Review the overview of the account and click **Create**.

  6. Wait for the deployment to complete.




### Allow trusted Microsoft services

  1. Go to the **Storage Account** you just created.
  2. Select **Networking** under **Security + networking**.
  3. On the **Firewalls and virtual networks** tab, under **Exceptions** , ensure **Allow Azure services on the trusted services list to access this storage account** is selected.
  4. Click **Save**.



### Get the Storage Account credentials

  1. In the same Storage Account, select **Access keys** under **Security + networking**.
  2. Click **Show keys**.
  3. Copy and save the following for later use: 
     * **Storage account name** : The name entered during creation (for example, `defenderemaillogs`)
     * **Key 1** or **Key 2** : The shared access key



### Get the Storage Account Resource ID

  1. In the same Storage Account, on the **Overview** page, click **JSON View**.
  2. Copy and save the **Resource ID**. It has the following format:
         
         /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Storage/storageAccounts/<STORAGE_ACCOUNT_NAME>
         




## Configure the Microsoft Defender XDR Streaming API

  1. Sign in to the [Microsoft Defender portal](https://security.microsoft.com) using an account with at least **Security Administrator** permissions.
  2. Go to **Settings > Microsoft Defender XDR > Streaming API**.
  3. Click **Add**.
  4. In the **Add new Streaming API settings** flyout, provide the following configuration details: 
     * **Name** : Enter a name for the settings (for example, `secops-email-events`).
     * Select **Forward events to Azure Storage**.
     * **Storage Account Resource ID** : Paste the Resource ID saved earlier.
  5. Select the following **Event types** : 
     * **EmailEvents**
     * **EmailAttachmentInfo**
     * **EmailUrlInfo**
     * **EmailPostDeliveryEvents**
     * **UrlClickEvents**
  6. Click **Submit**.



After streaming starts, a blob container is created in the storage account for each selected event type (documented by Microsoft). The container names follow the `insights-logs-advancedhunting-<event type>` pattern (for example, `insights-logs-advancedhunting-emailevents`). Microsoft's documentation shows the pattern for other tables, so always take the exact names from your storage account. Each blob row carries the event as JSON with `time`, `tenantId`, `category` (the table name with the `AdvancedHunting-` prefix), and the event fields inside a `properties` object.

**Note:** Copy the exact container names from the storage account (**Data storage > Containers**) once they appear. You need one name per event type for the feed configuration.

## Configure feeds in Google SecOps to ingest Microsoft Defender for Office 365 logs

Create one feed per event type container:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Defender for Office 365 - EmailEvents`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft Defender for Office 365** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
    
    https://<STORAGE_ACCOUNT_NAME>.blob.core.windows.net/insights-logs-advancedhunting-emailevents/
    

Replace the following:

     * `<STORAGE_ACCOUNT_NAME>`: Your Azure storage account name.
     * The container segment: the exact container name copied from the storage account.

**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source.
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
**Note:** If you select a deletion option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * From the authentication drop-down (defaults to **Access/Shared key**), select the method you want to use and provide the corresponding credential:

       * **Access/Shared key** : In the **Key** field, paste a storage account access key (**Key 1** or **Key 2**) captured earlier.
       * **SAS token** : In the **Token** field, paste a shared access signature (SAS) token issued for the container.
       * **Azure V2 Workload Identity Federation** : Enter the Microsoft Entra application **Client ID** and **Tenant ID**. Copy the read-only **Subject ID** that the feed displays and grant the matching identity access to the storage account on the Azure side.
**Note:** The service account shown on the right side of the feed is read-only. When you use **Azure V2 Workload Identity Federation** , configure your Microsoft Entra federated credential to trust this service account.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

  11. Repeat the steps for each remaining container (`insights-logs-advancedhunting-emailattachmentinfo`, `insights-logs-advancedhunting-emailurlinfo`, `insights-logs-advancedhunting-emailpostdeliveryevents`, `insights-logs-advancedhunting-urlclickevents`), using the same **Log type** and a distinct **Feed name**.




## Configure Azure Storage firewall (if enabled)

If your Azure Storage Account uses a firewall, you must add Google SecOps IP ranges.

  1. In the **Azure portal** , go to your **Storage Account**.
  2. Select **Networking** under **Security + networking**.
  3. Under **Firewalls and virtual networks** , select **Enabled from selected virtual networks and IP addresses**.
  4. In the **Firewall** section, under **Address range** , click **\+ Add IP range**.
  5. Add each Google SecOps IP range in CIDR notation.



To get the current IP ranges:

  * See [IP Allowlisting documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting)
  * Or retrieve them programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api)


  1. Click **Save**.

**Note:** This feed source uses the Storage Transfer Service (STS) to transfer data from Azure storage to Google SecOps. Before using this feed source, you may need to add the IP ranges used by STS workers to your list of allowed IPs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`CompAuth_label` | `additional.fields` | Merged  
`DKIM_label` | `additional.fields` | Merged  
`DMARC_label` | `additional.fields` | Merged  
`SPF_label` | `additional.fields` | Merged  
`additional_email_cluster_id` | `additional.fields` | Merged  
`additional_fields_label` | `additional.fields` | Merged  
`additional_replyto` | `additional.fields` | Merged  
`attachment_cnt_label` | `additional.fields` | Merged  
`attachment_count_label` | `additional.fields` | Merged  
`bulk_complaint_level_label` | `additional.fields` | Merged  
`clicked_label` | `additional.fields` | Merged  
`confidence_level_label` | `additional.fields` | Merged  
`connectors_label` | `additional.fields` | Merged  
`delivery_action_label` | `additional.fields` | Merged  
`delivery_location_label` | `additional.fields` | Merged  
`detection_methods_label` | `additional.fields` | Merged  
`email_action_label` | `additional.fields` | Merged  
`email_action_policy_guid_label` | `additional.fields` | Merged  
`email_action_policy_label` | `additional.fields` | Merged  
`email_cluster_id_label` | `additional.fields` | Merged  
`email_direction_label` | `additional.fields` | Merged  
`email_language_label` | `additional.fields` | Merged  
`exchange_transport_rule_label` | `additional.fields` | Merged  
`is_first_contact_label` | `additional.fields` | Merged  
`org_level_action_label` | `additional.fields` | Merged  
`org_level_policy_label` | `additional.fields` | Merged  
`phishData_label` | `additional.fields` | Merged  
`sender_from_address_label` | `additional.fields` | Merged  
`sender_mail_label` | `additional.fields` | Merged  
`spamData_label` | `additional.fields` | Merged  
`threat_names_label` | `additional.fields` | Merged  
`threat_types_label` | `additional.fields` | Merged  
`url_chain_list` | `additional.fields` | Merged  
`url_count_label` | `additional.fields` | Merged  
`url_loc_label` | `additional.fields` | Merged  
`url_location_label` | `additional.fields` | Merged  
`urlcount_label` | `additional.fields` | Merged  
`user_level_action_label` | `additional.fields` | Merged  
`user_level_policy_label` | `additional.fields` | Merged  
`workload_label` | `additional.fields` | Merged  
`_time` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSSSSSZ`  
`event_type` | `metadata.event_type` | Directly mapped  
`_raw.category` | `metadata.product_event_type` | Directly mapped  
`operationName` | `metadata.product_event_type` | Directly mapped  
`_raw.properties.ReportId` | `metadata.product_log_id` | Directly mapped  
`_raw.properties.SenderFromAddress` | `network.email.from` | Directly mapped  
`_raw.properties.InternetMessageId` | `network.email.mail_id` | Directly mapped  
`_raw.properties.Subject` | `network.email.subject` | Merged  
`properties.Subject` | `network.email.subject` | Merged  
`_raw.properties.RecipientEmailAddress` | `network.email.to` | Merged  
`email` | `network.email.to` | Mapped: `^.+@.+$` → `email`  
`properties.EmailSize` | `network.received_bytes` | Renamed/mapped  
`_raw.properties.NetworkMessageId` | `network.session_id` | Directly mapped  
`_raw.properties.SenderFromDomain` | `principal.administrative_domain` | Directly mapped  
`_raw.properties.SenderMailFromDomain` | `principal.administrative_domain` | Directly mapped  
`properties.SenderMailFromDomain` | `principal.administrative_domain` | Directly mapped  
`_raw.properties.UrlDomain` | `principal.asset.hostname` | Directly mapped  
`properties.SenderFromDomain` | `principal.asset.hostname` | Directly mapped  
`properties.UrlDomain` | `principal.asset.hostname` | Directly mapped  
`_raw.properties.SenderIPv4` | `principal.asset.ip` | Merged  
`_raw.properties.SenderIPv6` | `principal.asset.ip` | Merged  
`sender_ip` | `principal.asset.ip` | Merged  
`_raw.properties.SenderMailFromAddress` | `principal.email` | Directly mapped  
`target.SHA256` | `principal.file.sha256` | Directly mapped  
`_raw.properties.UrlDomain` | `principal.hostname` | Directly mapped  
`properties.SenderFromDomain` | `principal.hostname` | Directly mapped  
`properties.UrlDomain` | `principal.hostname` | Directly mapped  
`_raw.properties.SenderIPv4` | `principal.ip` | Merged  
`_raw.properties.SenderIPv6` | `principal.ip` | Merged  
`sender_ip` | `principal.ip` | Merged  
`_raw.properties.Url` | `principal.url` | Directly mapped  
`properties.Url` | `principal.url` | Directly mapped  
`_raw.properties.SenderObjectId` | `principal.user.product_object_id` | Directly mapped  
`tenantId` | `principal.user.product_object_id` | Directly mapped  
`_raw.properties.SenderDisplayName` | `principal.user.user_display_name` | Directly mapped  
`properties.SenderDisplayName` | `principal.user.user_display_name` | Directly mapped  
`action` | `security_result.action` | Merged  
`properties.Action` | `security_result.action_details` | Directly mapped  
`security_result_category` | `security_result.category` | Merged  
`category` | `security_result.category_details` | Merged  
`Phish_level` | `security_result.confidence` | Mapped: `high` → `HIGH_CONFIDENCE`, `medium` → `MEDIUM_CONFIDENCE`, `low` → `LOW_CONFIDENCE`  
`properties.ActionResult` | `security_result.description` | Directly mapped  
`action_type_label` | `security_result.detection_fields` | Merged  
`cribl_pipe_label` | `security_result.detection_fields` | Merged  
`email_action_label` | `security_result.detection_fields` | Merged  
`email_action_policy_label` | `security_result.detection_fields` | Merged  
`email_language_label` | `security_result.detection_fields` | Merged  
`emailactpol_guid_label` | `security_result.detection_fields` | Merged  
`internet_message_id_label` | `security_result.detection_fields` | Merged  
`network_message_id_label` | `security_result.detection_fields` | Merged  
`operation_name_label` | `security_result.detection_fields` | Merged  
`phish_level_label` | `security_result.detection_fields` | Merged  
`recipient_id_label` | `security_result.detection_fields` | Merged  
`report_id_label` | `security_result.detection_fields` | Merged  
`sender_id_label` | `security_result.detection_fields` | Merged  
`tenant_label` | `security_result.detection_fields` | Merged  
`transport_rule_guid_label` | `security_result.detection_fields` | Merged  
`trigger_label` | `security_result.detection_fields` | Merged  
`properties.DeliveryLocation` | `security_result.summary` | Directly mapped  
`properties.ThreatNames` | `security_result.threat_name` | Directly mapped  
`properties.AccountUpn` | `target.email` | Directly mapped  
`_raw.properties.FileName` | `target.file.full_path` | Directly mapped  
`_raw.properties.FileType` | `target.file.mime_type` | Directly mapped  
`properties.FileType` | `target.file.mime_type` | Directly mapped  
`properties.FileName` | `target.file.names` | Merged  
`_raw.properties.FileSize` | `target.file.size` | Renamed/mapped  
`properties.FileSize` | `target.file.size` | Renamed/mapped  
`properties.RecipientDomain` | `target.hostname` | Directly mapped  
`_raw.tenantId` | `target.resource.id` | Directly mapped  
`_raw.properties.RecipientObjectId` | `target.user.product_object_id` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `MICROSOFT_DEFENDER_MAIL`  
N/A | `metadata.vendor_name` | Constant: `MICROSOFT_DEFENDER_MAIL`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `security_result.confidence` | Constant: `HIGH_CONFIDENCE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-mail-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
