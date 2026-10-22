---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune-context/
title: Collect Microsoft Intune Context logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:12.412081+00:00
---

# Collect Microsoft Intune Context logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-mdm-intune-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Intune Context logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Microsoft Intune logs by setting up a Google Security Operations feed using Microsoft Azure Blob Storage V2.

Microsoft Intune is a cloud-based endpoint management solution that manages user access to organizational resources and simplifies app and device management across devices including mobile devices, desktop computers, and virtual endpoints.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **Microsoft Azure** portal with permissions to: 
    * Create Storage Accounts
    * Configure Diagnostic Settings for Microsoft Intune
    * Manage access keys
  * A user with the **Intune Administrator** or **Global Administrator** Microsoft Entra role for the Intune tenant
  * An Azure subscription to set up the storage account

**Note:** If you restrict access to your Azure resources using an Azure Storage firewall, you must add the IP ranges used by Storage Transfer Service (STS) workers to your list of allowed IPs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip-allow-lists).

## Configure an Azure Storage Account

### Create the Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `intunelogsstorage`)  
**Region** | Select the region (for example, `East US`)  
**Performance** | Standard (recommended)  
**Redundancy** | GRS (Geo-redundant storage) or LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Review the overview of the account and click **Create**.

  6. Wait for the deployment to complete.




### Get Storage Account credentials

  1. Go to the **Storage Account** you just created.
  2. In the left navigation, select **Access keys** under **Security + networking**.
  3. Click **Show keys**.
  4. Copy and save the following for later use: 
     * **Storage account name** : The name you provided during creation
     * **Key 1** or **Key 2** : The shared access key (a 512-bit random string in base-64 encoding)



### Get the Blob service endpoint

  1. In the same Storage Account, select **Endpoints** from the left navigation.
  2. Copy and save the **Blob service** endpoint URL. 
     * Example: `https://intunelogsstorage.blob.core.windows.net/`



## Configure Microsoft Intune Diagnostic settings

  1. Sign in to the **Microsoft Intune admin center**.
  2. Go to **Reports > Diagnostic settings**.

     * If you don't already have diagnostic settings set up, you'll be prompted to turn them on. Once you've done that, continue with step 3.
     * If you already have diagnostic settings set up, continue to Step 3.
  3. Click **Add diagnostic setting**.

  4. Provide the following configuration details:

     * **Diagnostic setting name** : Enter a descriptive name (for example, `export-to-secops`).
     * In the **Logs** section, select **AuditLogs**.
     * In the **Destination details** section, select **Archive to a storage account** checkbox.
     * **Subscription** : Select the subscription containing your storage account.
     * **Storage account** : Select the storage account you created earlier.
  5. Click **Save**.




After configuration, logs will automatically be exported to the storage account. Audit Logs show a record of activities that generate a change in Intune. Operational Logs show details on users and devices that successfully (or failed) to enroll, and details on noncompliant devices. Device Compliance Organizational Logs show an organizational report for device compliance in Intune, and details on noncompliant devices. IntuneDevices show device inventory and status information for Intune enrolled and managed devices.

The Intune Audit Logs and Operational Logs are sent immediately from Intune to Azure Monitor services. The Intune Device Compliance Organizational Logs and IntuneDevices report data is sent from Intune to Azure Monitor services once every 24 hours. So, it can take up to 24 hours to get the logs in the Azure Monitor services. Once the data is sent from Intune, then it typically shows in the Azure Monitor service within 30 minutes.

**Note:** Azure diagnostic settings create containers in the storage account based on the log category. The container names follow the pattern `insights-logs-{categoryname}`. You can verify the actual container names in your storage account after enabling diagnostic settings.

## Configure a feed in Google SecOps to ingest Microsoft Intune logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft Intune Logs`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft Intune** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path. Since Intune creates multiple containers for different log categories, you will need to create separate feeds for each container. Use the following format:

     * For Audit Logs:
           
           https://intunelogsstorage.blob.core.windows.net/insights-logs-auditlogs/
           

     * For Operational Logs:
           
           https://intunelogsstorage.blob.core.windows.net/insights-logs-operationallogs/
           

     * For Device Compliance Organizational Logs:
           
           https://intunelogsstorage.blob.core.windows.net/insights-logs-devicecomplianceorg/
           

     * For Devices:
           
           https://intunelogsstorage.blob.core.windows.net/insights-logs-devices/
           

     * Replace `intunelogsstorage` with your Azure storage account name.

**Note:** Include the trailing slash (/) at the end of the URI. Verify the actual container names in your Azure Storage account, as they are created automatically by Azure diagnostic settings.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Shared key** : Enter the shared key value (access key) you captured from the Storage Account.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

  11. Repeat steps 1-10 to create additional feeds for each Intune log category container.




## Configure Azure Storage firewall (if enabled)

If your Azure Storage Account uses a firewall, you must add Google SecOps IP ranges.

  1. In the **Azure portal** , go to your **Storage Account**.
  2. Select **Networking** under **Security + networking**.
  3. Under **Firewalls and virtual networks** , select **Enabled from selected virtual networks and IP addresses**.
  4. In the **Firewall** section, under **Address range** , click **\+ Add IP range**.
  5. Add each Google SecOps IP range in CIDR notation.

     * To get the current IP ranges:

       * See [IP Allowlisting documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip-allow-lists)
       * Or retrieve them programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api)
  6. Click **Save**.

**Note:** This feed source uses the Storage Transfer Service (STS) to transfer data from Azure storage to Google SecOps. Before using this feed source, you must configure the Azure Storage firewall to allow access from the STS IP ranges.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`TargetDisplayNames_list` | `additional.fields` | Merged  
`TargetObjectIds_list` | `additional.fields` | Merged  
`UserPermissions_list` | `additional.fields` | Merged  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`operationName` | `metadata.product_event_type` | Directly mapped  
`properties.AuditEventId` | `metadata.product_log_id` | Directly mapped  
`correlationId` | `network.session_id` | Directly mapped  
`properties.Actor.Application` | `principal.application` | Directly mapped  
`properties.Actor.ApplicationName` | `principal.resource.name` | Directly mapped  
`PartnerTenantId_label` | `principal.user.attribute.labels` | Merged  
`isDelegatedAdmin_label` | `principal.user.attribute.labels` | Merged  
`category` | `security_result.category_details` | Merged  
`resultDescription` | `security_result.description` | Directly mapped  
`ActivityDate_label` | `security_result.detection_fields` | Merged  
`ActivityResultStatus_label` | `security_result.detection_fields` | Merged  
`ActivityType_label` | `security_result.detection_fields` | Merged  
`ActorType_label` | `security_result.detection_fields` | Merged  
`Category_label` | `security_result.detection_fields` | Merged  
`Name_label` | `security_result.detection_fields` | Merged  
`New_label` | `security_result.detection_fields` | Merged  
`Old_label` | `security_result.detection_fields` | Merged  
`identity_label` | `security_result.detection_fields` | Merged  
`resultType` | `security_result.summary` | Directly mapped  
`tenantId` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `Microsoft Intune Context`  
N/A | `metadata.vendor_name` | Constant: `Microsoft`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-mdm-intune-context-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
